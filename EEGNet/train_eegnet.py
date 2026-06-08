import argparse
import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split, LeaveOneGroupOut
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# This is the EEGNet we use, from github repo: 
# https://github.com/vlawhern/arl-eegmodels

from EEGModels import EEGNet

CLASSES = ['no_stimulation', 'intermediate_intensity', 'max_intensity']
N_CLASSES = 3

# EEGNet hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)

F1, D, F2 = 8, 2, 16
DROPOUT_WITHIN = 0.5
DROPOUT_CROSS  = 0.25

# Training hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)

EPOCHS = 500
BATCH_SIZE = 32
PATIENCE_EARLY_STOP = 50
PATIENCE_LR_REDUCE  = 20

# Random seed for reproducibility

SEED = 42


'''Model Builder:
This function builds the EEGNet using the repo linked above. We use and
train this EEGNet to perform a 3-way classification of pain tolerance.'''

def model_builder(n_channels, n_samples, s_freq, dropout_rate):
    kernel_length = s_freq // 2 # Divide by smaller number for recognition among lower frequencies
    print(f"Building EEGNet: C={n_channels}, T={n_samples}, kernLength={kernel_length}")
    model = EEGNet(
        nb_classes = N_CLASSES,
        Chans = n_channels,
        Samples = n_samples,
        dropoutRate = dropout_rate,
        kernLength = kernel_length,
        F1 = F1, D = D, F2 = F2,
        dropoutType = 'Dropout'
    )
    model.compile(
        loss='categorical_crossentropy',
        optimizer=tf.keras.optimizers.Adam(),
        metrics=['accuracy']
    )
    return model


