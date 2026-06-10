The results here were from the hyperparams as follows:
  Data range: [-0.2,+1.5]
  CLASSES = ['no_stimulation', 'min_intensity', 'medium_intensity', 'max_intensity']
  N_CLASSES = 4
  # EEGNet hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)
  F1, D, F2 = 8, 2, 16
  DROPOUT_WITHIN = 0.5
  DROPOUT_CROSS  = 0.25
  # Training hyperparams (Lawhern et al. 2016, EEGNet-8,2 variant)
  EPOCHS = 500
  BATCH_SIZE = 32
  PATIENCE_EARLY_STOP = 15
  PATIENCE_LR_REDUCE  = 20
  # Random seed for reproducibility
  SEED = 42
  np.random.seed(SEED)
  tf.random.set_seed(SEED)

############################################################
# Subject 1/31: EMS0001
############################################################
Loaded EMS0001 from /kaggle/input/datasets/akablawi/ems-4class/EMS0001.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.61e-04, 5.25e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.39e-06, 1.25e-06]
  Per-channel std range:  [5.19e-06, 8.96e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2232 - loss: 1.4872 - val_accuracy: 0.3333 - val_loss: 1.3806 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3125 - loss: 1.3535 - val_accuracy: 0.3750 - val_loss: 1.3753 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.3393 - loss: 1.3344 - val_accuracy: 0.3333 - val_loss: 1.3711 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.3839 - loss: 1.3021 - val_accuracy: 0.3750 - val_loss: 1.3674 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4911 - loss: 1.2433 - val_accuracy: 0.4167 - val_loss: 1.3634 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.4464 - loss: 1.2264 - val_accuracy: 0.3750 - val_loss: 1.3589 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5714 - loss: 1.1896 - val_accuracy: 0.3750 - val_loss: 1.3537 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.1685 - val_accuracy: 0.3750 - val_loss: 1.3481 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.1494 - val_accuracy: 0.3750 - val_loss: 1.3410 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.5982 - loss: 1.1328 - val_accuracy: 0.3750 - val_loss: 1.3334 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 1.0736 - val_accuracy: 0.3750 - val_loss: 1.3246 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.0580 - val_accuracy: 0.4167 - val_loss: 1.3161 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 1.0275 - val_accuracy: 0.4583 - val_loss: 1.3087 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 1.0073 - val_accuracy: 0.4583 - val_loss: 1.2999 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9907 - val_accuracy: 0.4583 - val_loss: 1.2893 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6339 - loss: 0.9733 - val_accuracy: 0.5417 - val_loss: 1.2799 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9578 - val_accuracy: 0.5000 - val_loss: 1.2709 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 0.9613 - val_accuracy: 0.5000 - val_loss: 1.2617 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.7321 - loss: 0.9206 - val_accuracy: 0.5833 - val_loss: 1.2522 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8853 - val_accuracy: 0.5833 - val_loss: 1.2422 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 62ms/step - accuracy: 0.7232 - loss: 0.8848 - val_accuracy: 0.5417 - val_loss: 1.2337 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 57ms/step - accuracy: 0.7500 - loss: 0.8794 - val_accuracy: 0.5833 - val_loss: 1.2286 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8501 - val_accuracy: 0.5833 - val_loss: 1.2219 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.8353 - val_accuracy: 0.5000 - val_loss: 1.2120 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8066 - val_accuracy: 0.5000 - val_loss: 1.2066 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 61ms/step - accuracy: 0.7768 - loss: 0.8176 - val_accuracy: 0.5000 - val_loss: 1.1943 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 63ms/step - accuracy: 0.7946 - loss: 0.8072 - val_accuracy: 0.5000 - val_loss: 1.1741 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 60ms/step - accuracy: 0.7946 - loss: 0.7799 - val_accuracy: 0.5000 - val_loss: 1.1616 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 60ms/step - accuracy: 0.7946 - loss: 0.7736 - val_accuracy: 0.5000 - val_loss: 1.1591 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.7705 - val_accuracy: 0.5000 - val_loss: 1.1623 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7673 - val_accuracy: 0.5000 - val_loss: 1.1581 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.7224 - val_accuracy: 0.5000 - val_loss: 1.1575 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7431 - val_accuracy: 0.4583 - val_loss: 1.1482 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.7263 - val_accuracy: 0.5000 - val_loss: 1.1275 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7313 - val_accuracy: 0.4583 - val_loss: 1.1188 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.7013 - val_accuracy: 0.5000 - val_loss: 1.1315 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6793 - val_accuracy: 0.4583 - val_loss: 1.1203 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.6981 - val_accuracy: 0.4583 - val_loss: 1.1111 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.7007 - val_accuracy: 0.4583 - val_loss: 1.1068 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.6685 - val_accuracy: 0.4167 - val_loss: 1.1026 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6703 - val_accuracy: 0.5417 - val_loss: 1.0896 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6510 - val_accuracy: 0.5417 - val_loss: 1.0784 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.6328 - val_accuracy: 0.5000 - val_loss: 1.0821 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 44ms/step - accuracy: 0.8661 - loss: 0.6522 - val_accuracy: 0.5000 - val_loss: 1.0810 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 57ms/step - accuracy: 0.9018 - loss: 0.6432 - val_accuracy: 0.5000 - val_loss: 1.0673 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6272 - val_accuracy: 0.5000 - val_loss: 1.0667 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5932 - val_accuracy: 0.4583 - val_loss: 1.0819 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6125 - val_accuracy: 0.5000 - val_loss: 1.0733 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6296 - val_accuracy: 0.5417 - val_loss: 1.0670 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 57ms/step - accuracy: 0.8571 - loss: 0.6073 - val_accuracy: 0.5000 - val_loss: 1.0455 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.5977 - val_accuracy: 0.4583 - val_loss: 1.0341 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5708 - val_accuracy: 0.4583 - val_loss: 1.0591 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5586 - val_accuracy: 0.5417 - val_loss: 1.0593 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5740 - val_accuracy: 0.5417 - val_loss: 1.0577 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5835 - val_accuracy: 0.5417 - val_loss: 1.0546 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5814 - val_accuracy: 0.5833 - val_loss: 1.0404 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5671 - val_accuracy: 0.5000 - val_loss: 1.0587 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5615 - val_accuracy: 0.4167 - val_loss: 1.0724 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5503 - val_accuracy: 0.4167 - val_loss: 1.0764 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.5441 - val_accuracy: 0.5000 - val_loss: 1.0587 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5590 - val_accuracy: 0.5417 - val_loss: 1.0403 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 41ms/step - accuracy: 0.8929 - loss: 0.5482 - val_accuracy: 0.4583 - val_loss: 1.0352 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.5206 - val_accuracy: 0.4583 - val_loss: 1.0349 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.5163 - val_accuracy: 0.5000 - val_loss: 1.0319 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 56ms/step - accuracy: 0.9375 - loss: 0.5355 - val_accuracy: 0.5000 - val_loss: 1.0315 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5333 - val_accuracy: 0.5833 - val_loss: 1.0338 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.5196 - val_accuracy: 0.5417 - val_loss: 1.0328 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 56ms/step - accuracy: 0.9375 - loss: 0.5040 - val_accuracy: 0.5417 - val_loss: 1.0268 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5045 - val_accuracy: 0.5417 - val_loss: 1.0356 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.4902 - val_accuracy: 0.4583 - val_loss: 1.0489 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5110 - val_accuracy: 0.4583 - val_loss: 1.0446 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5042 - val_accuracy: 0.4583 - val_loss: 1.0338 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.4738 - val_accuracy: 0.4583 - val_loss: 1.0356 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4773 - val_accuracy: 0.5000 - val_loss: 1.0464 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5030 - val_accuracy: 0.5000 - val_loss: 1.0471 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.4552 - val_accuracy: 0.5000 - val_loss: 1.0277 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 60ms/step - accuracy: 0.9196 - loss: 0.4857 - val_accuracy: 0.5417 - val_loss: 1.0071 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 62ms/step - accuracy: 0.9286 - loss: 0.4809 - val_accuracy: 0.5000 - val_loss: 0.9913 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4744 - val_accuracy: 0.5000 - val_loss: 1.0066 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.4674 - val_accuracy: 0.5417 - val_loss: 1.0152 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4592 - val_accuracy: 0.5000 - val_loss: 1.0126 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4516 - val_accuracy: 0.5417 - val_loss: 1.0168 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4438 - val_accuracy: 0.5417 - val_loss: 1.0377 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.4608 - val_accuracy: 0.5417 - val_loss: 1.0107 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.4472 - val_accuracy: 0.5417 - val_loss: 0.9886 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4383 - val_accuracy: 0.5000 - val_loss: 0.9909 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.4135 - val_accuracy: 0.5833 - val_loss: 0.9993 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4591 - val_accuracy: 0.5833 - val_loss: 0.9887 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4633 - val_accuracy: 0.7083 - val_loss: 1.0099 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4247 - val_accuracy: 0.6667 - val_loss: 1.0097 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4576 - val_accuracy: 0.6250 - val_loss: 1.0022 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4378 - val_accuracy: 0.5833 - val_loss: 1.0059 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4394 - val_accuracy: 0.5833 - val_loss: 0.9955 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.4088 - val_accuracy: 0.5000 - val_loss: 0.9808 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.4155 - val_accuracy: 0.5833 - val_loss: 0.9607 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4337 - val_accuracy: 0.6250 - val_loss: 0.9724 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 58ms/step - accuracy: 0.9286 - loss: 0.4145 - val_accuracy: 0.6667 - val_loss: 0.9585 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.4254 - val_accuracy: 0.5833 - val_loss: 0.9445 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 59ms/step - accuracy: 0.9643 - loss: 0.3896 - val_accuracy: 0.5833 - val_loss: 0.9377 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4091 - val_accuracy: 0.6667 - val_loss: 0.9636 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 45ms/step - accuracy: 0.9286 - loss: 0.4255 - val_accuracy: 0.5833 - val_loss: 0.9982 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3989 - val_accuracy: 0.6250 - val_loss: 0.9787 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3987 - val_accuracy: 0.6250 - val_loss: 0.9776 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3848 - val_accuracy: 0.5833 - val_loss: 0.9903 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3762 - val_accuracy: 0.6250 - val_loss: 0.9840 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3761 - val_accuracy: 0.6250 - val_loss: 0.9424 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 58ms/step - accuracy: 0.9286 - loss: 0.4133 - val_accuracy: 0.6250 - val_loss: 0.9362 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3757 - val_accuracy: 0.6250 - val_loss: 0.9669 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3828 - val_accuracy: 0.6250 - val_loss: 0.9805 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.3967 - val_accuracy: 0.6250 - val_loss: 0.9264 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.3939 - val_accuracy: 0.6667 - val_loss: 0.8972 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3403 - val_accuracy: 0.6250 - val_loss: 0.9345 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3540 - val_accuracy: 0.5833 - val_loss: 0.9322 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.3574 - val_accuracy: 0.5833 - val_loss: 0.9673 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.3835 - val_accuracy: 0.5833 - val_loss: 0.9769 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3476 - val_accuracy: 0.6250 - val_loss: 0.9760 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.3610 - val_accuracy: 0.6250 - val_loss: 1.0003 - learning_rate: 0.0010
Epoch 118/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3707 - val_accuracy: 0.5833 - val_loss: 0.9931 - learning_rate: 0.0010
Epoch 119/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.3439 - val_accuracy: 0.5417 - val_loss: 0.9816 - learning_rate: 0.0010
Epoch 120/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.3407 - val_accuracy: 0.5417 - val_loss: 0.9329 - learning_rate: 0.0010
Epoch 121/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3754 - val_accuracy: 0.5833 - val_loss: 0.9143 - learning_rate: 0.0010
Epoch 122/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3455 - val_accuracy: 0.5833 - val_loss: 0.9371 - learning_rate: 0.0010
Epoch 123/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3606 - val_accuracy: 0.6250 - val_loss: 0.9224 - learning_rate: 0.0010
Epoch 124/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.3355 - val_accuracy: 0.5833 - val_loss: 0.9304 - learning_rate: 0.0010
Epoch 125/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3400 - val_accuracy: 0.5417 - val_loss: 0.9557 - learning_rate: 0.0010
Epoch 126/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3570 - val_accuracy: 0.5833 - val_loss: 0.9804 - learning_rate: 0.0010
Epoch 126: early stopping
Restoring model weights from the end of the best epoch: 111.
Training complete. Best epoch: 111 of 126. Best val_loss: 0.8972, val_accuracy: 0.6667

========== Evaluation: within-subject test / EMS0001 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         0         2         0
  min_intens         2         4         0         0
  medium_int         1         0         5         0
  max_intens         0         0         1         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.571     0.667     0.615         6
   min_intensity      1.000     0.667     0.800         6
medium_intensity      0.625     0.833     0.714         6
   max_intensity      1.000     0.833     0.909         6

        accuracy                          0.750        24
       macro avg      0.799     0.750     0.760        24
    weighted avg      0.799     0.750     0.760        24

Overall accuracy: 0.7500

Artifacts saved to /kaggle/working/within_all/EMS0001/

############################################################
# Subject 2/31: EMS0002
############################################################
Loaded EMS0002 from /kaggle/input/datasets/akablawi/ems-4class/EMS0002.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.43e-04, 1.62e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-4.76e-07, 4.19e-07]
  Per-channel std range:  [3.54e-06, 1.84e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2679 - loss: 1.4777 - val_accuracy: 0.2917 - val_loss: 1.3841 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.3750 - loss: 1.3587 - val_accuracy: 0.2917 - val_loss: 1.3815 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 61ms/step - accuracy: 0.3125 - loss: 1.3442 - val_accuracy: 0.3333 - val_loss: 1.3779 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 61ms/step - accuracy: 0.5179 - loss: 1.2993 - val_accuracy: 0.5417 - val_loss: 1.3732 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.5536 - loss: 1.2597 - val_accuracy: 0.5000 - val_loss: 1.3674 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.2145 - val_accuracy: 0.4583 - val_loss: 1.3601 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.2019 - val_accuracy: 0.5417 - val_loss: 1.3511 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1667 - val_accuracy: 0.5417 - val_loss: 1.3412 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.1241 - val_accuracy: 0.5000 - val_loss: 1.3302 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5893 - loss: 1.1171 - val_accuracy: 0.5417 - val_loss: 1.3174 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.6071 - loss: 1.0777 - val_accuracy: 0.5417 - val_loss: 1.3040 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 1.0405 - val_accuracy: 0.5417 - val_loss: 1.2895 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 60ms/step - accuracy: 0.6607 - loss: 1.0391 - val_accuracy: 0.5417 - val_loss: 1.2731 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 60ms/step - accuracy: 0.7589 - loss: 0.9752 - val_accuracy: 0.5833 - val_loss: 1.2578 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9872 - val_accuracy: 0.5833 - val_loss: 1.2429 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9703 - val_accuracy: 0.5833 - val_loss: 1.2281 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9484 - val_accuracy: 0.5833 - val_loss: 1.2112 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9073 - val_accuracy: 0.5833 - val_loss: 1.1963 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8857 - val_accuracy: 0.6250 - val_loss: 1.1835 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 61ms/step - accuracy: 0.7232 - loss: 0.8823 - val_accuracy: 0.6250 - val_loss: 1.1718 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8618 - val_accuracy: 0.6667 - val_loss: 1.1625 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8574 - val_accuracy: 0.6667 - val_loss: 1.1525 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8395 - val_accuracy: 0.6667 - val_loss: 1.1439 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 57ms/step - accuracy: 0.7143 - loss: 0.8131 - val_accuracy: 0.6667 - val_loss: 1.1330 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8253 - val_accuracy: 0.6667 - val_loss: 1.1179 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8150 - val_accuracy: 0.7083 - val_loss: 1.1046 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.7693 - val_accuracy: 0.7500 - val_loss: 1.0976 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.7866 - val_accuracy: 0.7917 - val_loss: 1.0860 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.7768 - loss: 0.7778 - val_accuracy: 0.7917 - val_loss: 1.0700 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.7725 - val_accuracy: 0.7500 - val_loss: 1.0560 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.7661 - val_accuracy: 0.7083 - val_loss: 1.0490 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.7301 - val_accuracy: 0.7083 - val_loss: 1.0440 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.7366 - val_accuracy: 0.7083 - val_loss: 1.0369 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.7247 - val_accuracy: 0.6667 - val_loss: 1.0287 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7156 - val_accuracy: 0.7083 - val_loss: 1.0269 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.6995 - val_accuracy: 0.7083 - val_loss: 1.0193 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.7150 - val_accuracy: 0.7083 - val_loss: 1.0101 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7039 - val_accuracy: 0.7083 - val_loss: 1.0017 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.6750 - val_accuracy: 0.7083 - val_loss: 0.9931 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.7078 - val_accuracy: 0.7083 - val_loss: 0.9831 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6629 - val_accuracy: 0.6667 - val_loss: 0.9848 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.6339 - val_accuracy: 0.6667 - val_loss: 0.9826 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.6738 - val_accuracy: 0.7083 - val_loss: 0.9757 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 60ms/step - accuracy: 0.8661 - loss: 0.6561 - val_accuracy: 0.7083 - val_loss: 0.9699 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 61ms/step - accuracy: 0.8750 - loss: 0.6505 - val_accuracy: 0.7083 - val_loss: 0.9662 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 47ms/step - accuracy: 0.8304 - loss: 0.6612 - val_accuracy: 0.6667 - val_loss: 0.9673 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6386 - val_accuracy: 0.6250 - val_loss: 0.9631 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 60ms/step - accuracy: 0.8750 - loss: 0.6225 - val_accuracy: 0.6667 - val_loss: 0.9567 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.6142 - val_accuracy: 0.7500 - val_loss: 0.9418 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.6104 - val_accuracy: 0.6667 - val_loss: 0.9424 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 44ms/step - accuracy: 0.8661 - loss: 0.6245 - val_accuracy: 0.6667 - val_loss: 0.9446 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.5994 - val_accuracy: 0.6250 - val_loss: 0.9366 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.6071 - val_accuracy: 0.6667 - val_loss: 0.9357 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5924 - val_accuracy: 0.6250 - val_loss: 0.9425 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.5722 - val_accuracy: 0.6250 - val_loss: 0.9544 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6064 - val_accuracy: 0.6667 - val_loss: 0.9492 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5776 - val_accuracy: 0.7083 - val_loss: 0.9469 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5812 - val_accuracy: 0.6250 - val_loss: 0.9524 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.5534 - val_accuracy: 0.6250 - val_loss: 0.9416 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 57ms/step - accuracy: 0.9107 - loss: 0.5368 - val_accuracy: 0.5833 - val_loss: 0.9292 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.5371 - val_accuracy: 0.6250 - val_loss: 0.9094 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5493 - val_accuracy: 0.6667 - val_loss: 0.9033 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5365 - val_accuracy: 0.6667 - val_loss: 0.9084 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5335 - val_accuracy: 0.6667 - val_loss: 0.9036 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5405 - val_accuracy: 0.7083 - val_loss: 0.9291 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5382 - val_accuracy: 0.6250 - val_loss: 0.9353 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 59ms/step - accuracy: 0.9286 - loss: 0.5401 - val_accuracy: 0.5833 - val_loss: 0.9023 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.5509 - val_accuracy: 0.6250 - val_loss: 0.8972 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5028 - val_accuracy: 0.6667 - val_loss: 0.9035 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.5211 - val_accuracy: 0.5833 - val_loss: 0.9016 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.5175 - val_accuracy: 0.6250 - val_loss: 0.9169 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 41ms/step - accuracy: 0.9196 - loss: 0.5236 - val_accuracy: 0.6250 - val_loss: 0.9279 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5113 - val_accuracy: 0.6250 - val_loss: 0.9123 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4988 - val_accuracy: 0.6250 - val_loss: 0.9095 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4798 - val_accuracy: 0.6250 - val_loss: 0.9182 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5030 - val_accuracy: 0.6250 - val_loss: 0.9227 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.5027 - val_accuracy: 0.6250 - val_loss: 0.9263 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.4654 - val_accuracy: 0.6250 - val_loss: 0.9261 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4854 - val_accuracy: 0.6250 - val_loss: 0.9150 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.4307 - val_accuracy: 0.6250 - val_loss: 0.9012 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 55ms/step - accuracy: 0.9554 - loss: 0.4503 - val_accuracy: 0.6250 - val_loss: 0.8967 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 57ms/step - accuracy: 0.9643 - loss: 0.4735 - val_accuracy: 0.6250 - val_loss: 0.8887 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 56ms/step - accuracy: 0.9107 - loss: 0.4649 - val_accuracy: 0.6250 - val_loss: 0.8759 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.4426 - val_accuracy: 0.6250 - val_loss: 0.8810 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4596 - val_accuracy: 0.6250 - val_loss: 0.8925 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4631 - val_accuracy: 0.6250 - val_loss: 0.9153 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.4406 - val_accuracy: 0.6250 - val_loss: 0.9144 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.4118 - val_accuracy: 0.6250 - val_loss: 0.9155 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 40ms/step - accuracy: 0.9375 - loss: 0.4724 - val_accuracy: 0.6250 - val_loss: 0.9309 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.4276 - val_accuracy: 0.6250 - val_loss: 0.9188 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 40ms/step - accuracy: 0.9464 - loss: 0.4327 - val_accuracy: 0.6250 - val_loss: 0.9030 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.4107 - val_accuracy: 0.6250 - val_loss: 0.8888 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.4115 - val_accuracy: 0.6250 - val_loss: 0.8891 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 41ms/step - accuracy: 0.9911 - loss: 0.4186 - val_accuracy: 0.6250 - val_loss: 0.8934 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4323 - val_accuracy: 0.6250 - val_loss: 0.9103 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.4349 - val_accuracy: 0.6250 - val_loss: 0.9019 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.4091 - val_accuracy: 0.6250 - val_loss: 0.8991 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4351 - val_accuracy: 0.6250 - val_loss: 0.9072 - learning_rate: 0.0010
Epoch 98: early stopping
Restoring model weights from the end of the best epoch: 83.
Training complete. Best epoch: 83 of 98. Best val_loss: 0.8759, val_accuracy: 0.6250

========== Evaluation: within-subject test / EMS0002 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         1         1         1
  min_intens         1         2         2         1
  medium_int         0         1         2         3
  max_intens         0         0         0         6

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.750     0.500     0.600         6
   min_intensity      0.500     0.333     0.400         6
medium_intensity      0.400     0.333     0.364         6
   max_intensity      0.545     1.000     0.706         6

        accuracy                          0.542        24
       macro avg      0.549     0.542     0.517        24
    weighted avg      0.549     0.542     0.517        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0002/

############################################################
# Subject 3/31: EMS0003
############################################################
Loaded EMS0003 from /kaggle/input/datasets/akablawi/ems-4class/EMS0003.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.87e-04, 1.79e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-8.79e-07, 1.24e-06]
  Per-channel std range:  [4.86e-06, 2.91e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2143 - loss: 1.5079 - val_accuracy: 0.3750 - val_loss: 1.3832 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.3304 - loss: 1.3389 - val_accuracy: 0.2917 - val_loss: 1.3811 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4107 - loss: 1.3099 - val_accuracy: 0.2500 - val_loss: 1.3785 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2608 - val_accuracy: 0.2917 - val_loss: 1.3751 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 58ms/step - accuracy: 0.4196 - loss: 1.2651 - val_accuracy: 0.3333 - val_loss: 1.3707 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.4375 - loss: 1.2233 - val_accuracy: 0.3750 - val_loss: 1.3649 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.1814 - val_accuracy: 0.3333 - val_loss: 1.3583 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5000 - loss: 1.1565 - val_accuracy: 0.3333 - val_loss: 1.3512 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.1367 - val_accuracy: 0.3333 - val_loss: 1.3442 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.0962 - val_accuracy: 0.3333 - val_loss: 1.3377 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0641 - val_accuracy: 0.3333 - val_loss: 1.3306 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.0666 - val_accuracy: 0.3333 - val_loss: 1.3226 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0350 - val_accuracy: 0.3750 - val_loss: 1.3136 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.6607 - loss: 0.9927 - val_accuracy: 0.3750 - val_loss: 1.3058 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 0.9868 - val_accuracy: 0.4167 - val_loss: 1.2998 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9700 - val_accuracy: 0.4167 - val_loss: 1.2935 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9430 - val_accuracy: 0.4167 - val_loss: 1.2877 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9144 - val_accuracy: 0.4167 - val_loss: 1.2818 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.8793 - val_accuracy: 0.4167 - val_loss: 1.2757 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8979 - val_accuracy: 0.4167 - val_loss: 1.2680 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 60ms/step - accuracy: 0.7143 - loss: 0.8929 - val_accuracy: 0.4167 - val_loss: 1.2632 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.8499 - val_accuracy: 0.4167 - val_loss: 1.2607 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 57ms/step - accuracy: 0.7321 - loss: 0.8452 - val_accuracy: 0.4167 - val_loss: 1.2597 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8291 - val_accuracy: 0.3750 - val_loss: 1.2598 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8324 - val_accuracy: 0.3750 - val_loss: 1.2608 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.8155 - val_accuracy: 0.3750 - val_loss: 1.2587 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.7820 - val_accuracy: 0.3750 - val_loss: 1.2518 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.7768 - loss: 0.7716 - val_accuracy: 0.3750 - val_loss: 1.2482 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7520 - val_accuracy: 0.3750 - val_loss: 1.2480 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.7411 - loss: 0.7795 - val_accuracy: 0.3750 - val_loss: 1.2534 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7486 - val_accuracy: 0.4167 - val_loss: 1.2576 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7373 - val_accuracy: 0.4583 - val_loss: 1.2553 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.7109 - val_accuracy: 0.4583 - val_loss: 1.2570 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7355 - val_accuracy: 0.5000 - val_loss: 1.2571 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.7052 - val_accuracy: 0.5000 - val_loss: 1.2592 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 42ms/step - accuracy: 0.7946 - loss: 0.7141 - val_accuracy: 0.4167 - val_loss: 1.2669 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.6890 - val_accuracy: 0.4167 - val_loss: 1.2717 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.6917 - val_accuracy: 0.4167 - val_loss: 1.2652 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.6495 - val_accuracy: 0.4167 - val_loss: 1.2552 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6572 - val_accuracy: 0.4167 - val_loss: 1.2552 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 41ms/step - accuracy: 0.8214 - loss: 0.6690 - val_accuracy: 0.4167 - val_loss: 1.2632 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 41ms/step - accuracy: 0.8750 - loss: 0.6608 - val_accuracy: 0.4167 - val_loss: 1.2790 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 41ms/step - accuracy: 0.8482 - loss: 0.6523 - val_accuracy: 0.4167 - val_loss: 1.2889 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5836 - val_accuracy: 0.4583 - val_loss: 1.2878 - learning_rate: 0.0010
Epoch 44: early stopping
Restoring model weights from the end of the best epoch: 29.
Training complete. Best epoch: 29 of 44. Best val_loss: 1.2480, val_accuracy: 0.3750

========== Evaluation: within-subject test / EMS0003 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         6         0         0         0
  min_intens         0         5         1         0
  medium_int         1         1         4         0
  max_intens         0         0         2         4

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.857     1.000     0.923         6
   min_intensity      0.833     0.833     0.833         6
medium_intensity      0.571     0.667     0.615         6
   max_intensity      1.000     0.667     0.800         6

        accuracy                          0.792        24
       macro avg      0.815     0.792     0.793        24
    weighted avg      0.815     0.792     0.793        24

Overall accuracy: 0.7917

Artifacts saved to /kaggle/working/within_all/EMS0003/

############################################################
# Subject 4/31: EMS0004
############################################################
Loaded EMS0004 from /kaggle/input/datasets/akablawi/ems-4class/EMS0004.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-8.27e-04, 1.89e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.83e-06, 2.89e-06]
  Per-channel std range:  [6.49e-06, 9.19e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.1875 - loss: 1.5045 - val_accuracy: 0.2500 - val_loss: 1.3860 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 66ms/step - accuracy: 0.3214 - loss: 1.3698 - val_accuracy: 0.2917 - val_loss: 1.3826 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.3482 - loss: 1.3269 - val_accuracy: 0.4167 - val_loss: 1.3791 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4464 - loss: 1.3075 - val_accuracy: 0.4167 - val_loss: 1.3747 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 58ms/step - accuracy: 0.4732 - loss: 1.2940 - val_accuracy: 0.5000 - val_loss: 1.3693 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.5000 - loss: 1.2765 - val_accuracy: 0.5000 - val_loss: 1.3628 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2358 - val_accuracy: 0.5417 - val_loss: 1.3552 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.5179 - loss: 1.2173 - val_accuracy: 0.5417 - val_loss: 1.3469 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5268 - loss: 1.2067 - val_accuracy: 0.5000 - val_loss: 1.3388 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.1618 - val_accuracy: 0.5000 - val_loss: 1.3303 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5357 - loss: 1.1534 - val_accuracy: 0.5000 - val_loss: 1.3211 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.5536 - loss: 1.1245 - val_accuracy: 0.5833 - val_loss: 1.3105 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.0953 - val_accuracy: 0.5833 - val_loss: 1.2968 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.1010 - val_accuracy: 0.5833 - val_loss: 1.2822 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 57ms/step - accuracy: 0.5982 - loss: 1.0489 - val_accuracy: 0.5833 - val_loss: 1.2683 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6696 - loss: 1.0170 - val_accuracy: 0.5833 - val_loss: 1.2566 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 1.0369 - val_accuracy: 0.5833 - val_loss: 1.2451 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.6161 - loss: 1.0079 - val_accuracy: 0.5833 - val_loss: 1.2328 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9876 - val_accuracy: 0.6250 - val_loss: 1.2192 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9376 - val_accuracy: 0.5833 - val_loss: 1.2040 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9556 - val_accuracy: 0.5417 - val_loss: 1.1967 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 0.9484 - val_accuracy: 0.5833 - val_loss: 1.1921 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 0.9212 - val_accuracy: 0.5833 - val_loss: 1.1854 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.8978 - val_accuracy: 0.5833 - val_loss: 1.1729 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8572 - val_accuracy: 0.5417 - val_loss: 1.1515 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 58ms/step - accuracy: 0.7054 - loss: 0.8772 - val_accuracy: 0.5417 - val_loss: 1.1405 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 43ms/step - accuracy: 0.6875 - loss: 0.8994 - val_accuracy: 0.5417 - val_loss: 1.1422 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8571 - val_accuracy: 0.5417 - val_loss: 1.1398 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.8576 - val_accuracy: 0.5833 - val_loss: 1.1266 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 57ms/step - accuracy: 0.7232 - loss: 0.8358 - val_accuracy: 0.6667 - val_loss: 1.1116 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 56ms/step - accuracy: 0.7411 - loss: 0.8178 - val_accuracy: 0.6667 - val_loss: 1.1044 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 57ms/step - accuracy: 0.7321 - loss: 0.8248 - val_accuracy: 0.6667 - val_loss: 1.0989 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 57ms/step - accuracy: 0.7857 - loss: 0.7879 - val_accuracy: 0.6667 - val_loss: 1.0875 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.7964 - val_accuracy: 0.6250 - val_loss: 1.0801 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 57ms/step - accuracy: 0.8036 - loss: 0.7780 - val_accuracy: 0.6250 - val_loss: 1.0795 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 57ms/step - accuracy: 0.8036 - loss: 0.7453 - val_accuracy: 0.6250 - val_loss: 1.0787 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.7667 - val_accuracy: 0.6667 - val_loss: 1.0607 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.7661 - val_accuracy: 0.6250 - val_loss: 1.0516 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.7568 - val_accuracy: 0.7083 - val_loss: 1.0503 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7698 - val_accuracy: 0.6667 - val_loss: 1.0528 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 57ms/step - accuracy: 0.7768 - loss: 0.7360 - val_accuracy: 0.7083 - val_loss: 1.0481 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.7142 - val_accuracy: 0.6667 - val_loss: 1.0326 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.7328 - val_accuracy: 0.6667 - val_loss: 1.0264 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.7276 - val_accuracy: 0.6667 - val_loss: 1.0262 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 63ms/step - accuracy: 0.8661 - loss: 0.6804 - val_accuracy: 0.6667 - val_loss: 1.0192 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6782 - val_accuracy: 0.6667 - val_loss: 1.0211 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 48ms/step - accuracy: 0.8214 - loss: 0.6909 - val_accuracy: 0.7083 - val_loss: 1.0238 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.6515 - val_accuracy: 0.7083 - val_loss: 1.0223 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.6695 - val_accuracy: 0.7500 - val_loss: 1.0231 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 57ms/step - accuracy: 0.7768 - loss: 0.6782 - val_accuracy: 0.7083 - val_loss: 1.0171 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.6561 - val_accuracy: 0.6667 - val_loss: 1.0087 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 60ms/step - accuracy: 0.8304 - loss: 0.6566 - val_accuracy: 0.5833 - val_loss: 0.9995 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.6515 - val_accuracy: 0.6250 - val_loss: 1.0007 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.6438 - val_accuracy: 0.5833 - val_loss: 1.0072 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.6369 - val_accuracy: 0.6250 - val_loss: 1.0090 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6151 - val_accuracy: 0.6667 - val_loss: 0.9887 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.5991 - val_accuracy: 0.6667 - val_loss: 0.9781 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.6081 - val_accuracy: 0.6667 - val_loss: 0.9775 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 57ms/step - accuracy: 0.8571 - loss: 0.6277 - val_accuracy: 0.6250 - val_loss: 0.9743 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.5840 - val_accuracy: 0.7083 - val_loss: 0.9621 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6031 - val_accuracy: 0.7083 - val_loss: 0.9622 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5758 - val_accuracy: 0.6250 - val_loss: 0.9837 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5774 - val_accuracy: 0.6667 - val_loss: 0.9831 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5664 - val_accuracy: 0.5833 - val_loss: 0.9767 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5766 - val_accuracy: 0.6667 - val_loss: 0.9628 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6110 - val_accuracy: 0.6667 - val_loss: 0.9671 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5464 - val_accuracy: 0.6667 - val_loss: 0.9860 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5695 - val_accuracy: 0.6250 - val_loss: 0.9877 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.5598 - val_accuracy: 0.5833 - val_loss: 0.9831 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5638 - val_accuracy: 0.5833 - val_loss: 0.9804 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5495 - val_accuracy: 0.6250 - val_loss: 0.9669 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5227 - val_accuracy: 0.5833 - val_loss: 0.9882 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5226 - val_accuracy: 0.5417 - val_loss: 0.9967 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.5402 - val_accuracy: 0.5417 - val_loss: 0.9973 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5374 - val_accuracy: 0.5417 - val_loss: 0.9859 - learning_rate: 0.0010
Epoch 75: early stopping
Restoring model weights from the end of the best epoch: 60.
Training complete. Best epoch: 60 of 75. Best val_loss: 0.9621, val_accuracy: 0.7083

========== Evaluation: within-subject test / EMS0004 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         1         1         0
  min_intens         2         1         2         1
  medium_int         0         0         5         1
  max_intens         0         1         3         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.667     0.667     0.667         6
   min_intensity      0.333     0.167     0.222         6
medium_intensity      0.455     0.833     0.588         6
   max_intensity      0.500     0.333     0.400         6

        accuracy                          0.500        24
       macro avg      0.489     0.500     0.469        24
    weighted avg      0.489     0.500     0.469        24

Overall accuracy: 0.5000

Artifacts saved to /kaggle/working/within_all/EMS0004/

############################################################
# Subject 5/31: EMS0005
############################################################
Loaded EMS0005 from /kaggle/input/datasets/akablawi/ems-4class/EMS0005.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.88e-04, 2.37e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.84e-06, 6.15e-07]
  Per-channel std range:  [2.68e-06, 2.74e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2679 - loss: 1.4431 - val_accuracy: 0.3750 - val_loss: 1.3846 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3393 - loss: 1.3605 - val_accuracy: 0.2917 - val_loss: 1.3828 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 58ms/step - accuracy: 0.3304 - loss: 1.3450 - val_accuracy: 0.2917 - val_loss: 1.3812 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.3571 - loss: 1.3400 - val_accuracy: 0.3333 - val_loss: 1.3795 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.4464 - loss: 1.2949 - val_accuracy: 0.3750 - val_loss: 1.3781 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 61ms/step - accuracy: 0.5000 - loss: 1.2817 - val_accuracy: 0.3750 - val_loss: 1.3774 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5357 - loss: 1.2557 - val_accuracy: 0.4583 - val_loss: 1.3768 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5268 - loss: 1.2369 - val_accuracy: 0.4167 - val_loss: 1.3747 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2182 - val_accuracy: 0.4583 - val_loss: 1.3715 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5000 - loss: 1.1973 - val_accuracy: 0.4583 - val_loss: 1.3675 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.5536 - loss: 1.1848 - val_accuracy: 0.4583 - val_loss: 1.3669 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.1709 - val_accuracy: 0.4583 - val_loss: 1.3658 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 43ms/step - accuracy: 0.6250 - loss: 1.1366 - val_accuracy: 0.4583 - val_loss: 1.3660 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.1387 - val_accuracy: 0.4167 - val_loss: 1.3622 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.1218 - val_accuracy: 0.4167 - val_loss: 1.3588 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.1114 - val_accuracy: 0.4167 - val_loss: 1.3581 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.1086 - val_accuracy: 0.4583 - val_loss: 1.3557 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 45ms/step - accuracy: 0.6518 - loss: 1.0564 - val_accuracy: 0.4167 - val_loss: 1.3559 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 44ms/step - accuracy: 0.7232 - loss: 1.0402 - val_accuracy: 0.4167 - val_loss: 1.3562 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.0682 - val_accuracy: 0.4167 - val_loss: 1.3519 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0509 - val_accuracy: 0.4167 - val_loss: 1.3510 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 1.0278 - val_accuracy: 0.4167 - val_loss: 1.3492 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 1.0166 - val_accuracy: 0.4167 - val_loss: 1.3484 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 43ms/step - accuracy: 0.6696 - loss: 1.0025 - val_accuracy: 0.4167 - val_loss: 1.3521 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.6964 - loss: 0.9877 - val_accuracy: 0.4167 - val_loss: 1.3439 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 1.0311 - val_accuracy: 0.4167 - val_loss: 1.3351 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9626 - val_accuracy: 0.4583 - val_loss: 1.3292 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 44ms/step - accuracy: 0.6964 - loss: 0.9776 - val_accuracy: 0.4167 - val_loss: 1.3410 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 45ms/step - accuracy: 0.7411 - loss: 0.9902 - val_accuracy: 0.3750 - val_loss: 1.3422 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 44ms/step - accuracy: 0.7054 - loss: 0.9613 - val_accuracy: 0.3750 - val_loss: 1.3436 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.9460 - val_accuracy: 0.3750 - val_loss: 1.3501 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.6786 - loss: 0.9280 - val_accuracy: 0.3750 - val_loss: 1.3455 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.6964 - loss: 0.9417 - val_accuracy: 0.3750 - val_loss: 1.3419 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.9009 - val_accuracy: 0.3333 - val_loss: 1.3353 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 47ms/step - accuracy: 0.7500 - loss: 0.9144 - val_accuracy: 0.2917 - val_loss: 1.3350 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 63ms/step - accuracy: 0.7411 - loss: 0.8996 - val_accuracy: 0.2917 - val_loss: 1.3280 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 63ms/step - accuracy: 0.7411 - loss: 0.8862 - val_accuracy: 0.3333 - val_loss: 1.3250 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 46ms/step - accuracy: 0.7321 - loss: 0.9094 - val_accuracy: 0.2917 - val_loss: 1.3387 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 44ms/step - accuracy: 0.7054 - loss: 0.8916 - val_accuracy: 0.2917 - val_loss: 1.3363 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7679 - loss: 0.8573 - val_accuracy: 0.3333 - val_loss: 1.3303 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8876 - val_accuracy: 0.3333 - val_loss: 1.3245 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.8781 - val_accuracy: 0.3333 - val_loss: 1.3265 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 42ms/step - accuracy: 0.7768 - loss: 0.8517 - val_accuracy: 0.3333 - val_loss: 1.3300 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8487 - val_accuracy: 0.2917 - val_loss: 1.3190 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.8336 - val_accuracy: 0.3333 - val_loss: 1.3274 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.7768 - loss: 0.8321 - val_accuracy: 0.2500 - val_loss: 1.3435 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.8561 - val_accuracy: 0.2500 - val_loss: 1.3401 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 57ms/step - accuracy: 0.7857 - loss: 0.8531 - val_accuracy: 0.2917 - val_loss: 1.3142 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 42ms/step - accuracy: 0.7321 - loss: 0.8561 - val_accuracy: 0.2917 - val_loss: 1.3283 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.8033 - val_accuracy: 0.2917 - val_loss: 1.3376 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 42ms/step - accuracy: 0.7768 - loss: 0.8413 - val_accuracy: 0.3333 - val_loss: 1.3211 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 42ms/step - accuracy: 0.7679 - loss: 0.8247 - val_accuracy: 0.2917 - val_loss: 1.3409 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.8080 - val_accuracy: 0.3333 - val_loss: 1.3255 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7913 - val_accuracy: 0.2083 - val_loss: 1.3387 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7957 - val_accuracy: 0.2083 - val_loss: 1.3495 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.7885 - val_accuracy: 0.2917 - val_loss: 1.3443 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7750 - val_accuracy: 0.3333 - val_loss: 1.3201 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.7411 - loss: 0.8271 - val_accuracy: 0.2500 - val_loss: 1.3230 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7784 - val_accuracy: 0.2083 - val_loss: 1.3696 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7783 - val_accuracy: 0.2083 - val_loss: 1.3375 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 42ms/step - accuracy: 0.7411 - loss: 0.7973 - val_accuracy: 0.2917 - val_loss: 1.3283 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.7708 - val_accuracy: 0.2917 - val_loss: 1.3414 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 44ms/step - accuracy: 0.8393 - loss: 0.7181 - val_accuracy: 0.2500 - val_loss: 1.3226 - learning_rate: 0.0010
Epoch 63: early stopping
Restoring model weights from the end of the best epoch: 48.
Training complete. Best epoch: 48 of 63. Best val_loss: 1.3142, val_accuracy: 0.2917

========== Evaluation: within-subject test / EMS0005 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         1         3         1         1
  min_intens         1         3         0         2
  medium_int         1         0         1         4
  max_intens         1         1         1         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.250     0.167     0.200         6
   min_intensity      0.429     0.500     0.462         6
medium_intensity      0.333     0.167     0.222         6
   max_intensity      0.300     0.500     0.375         6

        accuracy                          0.333        24
       macro avg      0.328     0.333     0.315        24
    weighted avg      0.328     0.333     0.315        24

Overall accuracy: 0.3333

Artifacts saved to /kaggle/working/within_all/EMS0005/

############################################################
# Subject 6/31: EMS0006
############################################################
Loaded EMS0006 from /kaggle/input/datasets/akablawi/ems-4class/EMS0006.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-2.90e-04, 3.62e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.58e-06, 6.59e-07]
  Per-channel std range:  [6.03e-06, 5.70e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2500 - loss: 1.4930 - val_accuracy: 0.2083 - val_loss: 1.3852 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.2857 - loss: 1.3851 - val_accuracy: 0.2917 - val_loss: 1.3846 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 62ms/step - accuracy: 0.3304 - loss: 1.3575 - val_accuracy: 0.3750 - val_loss: 1.3835 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4464 - loss: 1.3400 - val_accuracy: 0.3750 - val_loss: 1.3821 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.4018 - loss: 1.3120 - val_accuracy: 0.3333 - val_loss: 1.3800 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 60ms/step - accuracy: 0.5089 - loss: 1.2818 - val_accuracy: 0.3333 - val_loss: 1.3776 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 64ms/step - accuracy: 0.5089 - loss: 1.2730 - val_accuracy: 0.4167 - val_loss: 1.3748 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.4911 - loss: 1.2408 - val_accuracy: 0.4167 - val_loss: 1.3721 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.2328 - val_accuracy: 0.3750 - val_loss: 1.3695 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.4911 - loss: 1.2239 - val_accuracy: 0.3333 - val_loss: 1.3666 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 57ms/step - accuracy: 0.5804 - loss: 1.1982 - val_accuracy: 0.3333 - val_loss: 1.3639 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.5714 - loss: 1.1658 - val_accuracy: 0.3750 - val_loss: 1.3590 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.1678 - val_accuracy: 0.3750 - val_loss: 1.3532 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5446 - loss: 1.1595 - val_accuracy: 0.4167 - val_loss: 1.3485 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.1446 - val_accuracy: 0.4167 - val_loss: 1.3447 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 57ms/step - accuracy: 0.6607 - loss: 1.1157 - val_accuracy: 0.4583 - val_loss: 1.3394 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.1005 - val_accuracy: 0.4167 - val_loss: 1.3344 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.5893 - loss: 1.1277 - val_accuracy: 0.4583 - val_loss: 1.3328 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 57ms/step - accuracy: 0.6250 - loss: 1.0792 - val_accuracy: 0.5417 - val_loss: 1.3304 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0519 - val_accuracy: 0.5000 - val_loss: 1.3252 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 1.0397 - val_accuracy: 0.3750 - val_loss: 1.3235 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 61ms/step - accuracy: 0.6071 - loss: 1.0459 - val_accuracy: 0.4583 - val_loss: 1.3229 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0453 - val_accuracy: 0.3750 - val_loss: 1.3219 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.6964 - loss: 1.0150 - val_accuracy: 0.4167 - val_loss: 1.3168 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.9899 - val_accuracy: 0.4583 - val_loss: 1.3133 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 57ms/step - accuracy: 0.6250 - loss: 0.9935 - val_accuracy: 0.4583 - val_loss: 1.3097 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 0.9881 - val_accuracy: 0.4583 - val_loss: 1.3071 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 0.9588 - val_accuracy: 0.4167 - val_loss: 1.3060 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9295 - val_accuracy: 0.4583 - val_loss: 1.3020 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9572 - val_accuracy: 0.4167 - val_loss: 1.2970 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.9342 - val_accuracy: 0.4583 - val_loss: 1.2967 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.9091 - val_accuracy: 0.4167 - val_loss: 1.3001 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 44ms/step - accuracy: 0.7143 - loss: 0.9306 - val_accuracy: 0.4167 - val_loss: 1.3039 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.6786 - loss: 0.9291 - val_accuracy: 0.4583 - val_loss: 1.3009 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 42ms/step - accuracy: 0.7143 - loss: 0.9017 - val_accuracy: 0.4167 - val_loss: 1.2983 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 42ms/step - accuracy: 0.7143 - loss: 0.9061 - val_accuracy: 0.3750 - val_loss: 1.2976 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 42ms/step - accuracy: 0.7679 - loss: 0.8741 - val_accuracy: 0.3333 - val_loss: 1.3036 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 42ms/step - accuracy: 0.7232 - loss: 0.8812 - val_accuracy: 0.3333 - val_loss: 1.3101 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.7679 - loss: 0.8694 - val_accuracy: 0.3333 - val_loss: 1.3130 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 42ms/step - accuracy: 0.7589 - loss: 0.8617 - val_accuracy: 0.3333 - val_loss: 1.3117 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 41ms/step - accuracy: 0.7321 - loss: 0.8698 - val_accuracy: 0.3333 - val_loss: 1.3099 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.8289 - val_accuracy: 0.3750 - val_loss: 1.3145 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 41ms/step - accuracy: 0.7500 - loss: 0.8395 - val_accuracy: 0.2917 - val_loss: 1.3214 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 41ms/step - accuracy: 0.7500 - loss: 0.8378 - val_accuracy: 0.2917 - val_loss: 1.3256 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 41ms/step - accuracy: 0.7946 - loss: 0.8172 - val_accuracy: 0.2917 - val_loss: 1.3335 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.7679 - loss: 0.8231 - val_accuracy: 0.2917 - val_loss: 1.3375 - learning_rate: 0.0010
Epoch 46: early stopping
Restoring model weights from the end of the best epoch: 31.
Training complete. Best epoch: 31 of 46. Best val_loss: 1.2967, val_accuracy: 0.4583

========== Evaluation: within-subject test / EMS0006 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         1         1         1
  min_intens         1         2         1         2
  medium_int         0         0         3         3
  max_intens         2         0         2         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.500     0.500         6
   min_intensity      0.667     0.333     0.444         6
medium_intensity      0.429     0.500     0.462         6
   max_intensity      0.250     0.333     0.286         6

        accuracy                          0.417        24
       macro avg      0.461     0.417     0.423        24
    weighted avg      0.461     0.417     0.423        24

Overall accuracy: 0.4167

Artifacts saved to /kaggle/working/within_all/EMS0006/

############################################################
# Subject 7/31: EMS0007
############################################################
Loaded EMS0007 from /kaggle/input/datasets/akablawi/ems-4class/EMS0007.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.77e-03, 1.08e-02]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-9.22e-06, 2.10e-05]
  Per-channel std range:  [1.17e-05, 5.45e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3304 - loss: 1.5078 - val_accuracy: 0.2500 - val_loss: 1.3831 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 62ms/step - accuracy: 0.3750 - loss: 1.3477 - val_accuracy: 0.2917 - val_loss: 1.3821 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 62ms/step - accuracy: 0.3393 - loss: 1.3331 - val_accuracy: 0.2917 - val_loss: 1.3801 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4464 - loss: 1.2984 - val_accuracy: 0.4167 - val_loss: 1.3772 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 62ms/step - accuracy: 0.4018 - loss: 1.2966 - val_accuracy: 0.4583 - val_loss: 1.3742 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 61ms/step - accuracy: 0.4643 - loss: 1.2671 - val_accuracy: 0.4583 - val_loss: 1.3706 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5357 - loss: 1.2365 - val_accuracy: 0.4583 - val_loss: 1.3669 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2316 - val_accuracy: 0.4167 - val_loss: 1.3629 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 61ms/step - accuracy: 0.5089 - loss: 1.2362 - val_accuracy: 0.4167 - val_loss: 1.3592 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 61ms/step - accuracy: 0.5446 - loss: 1.1882 - val_accuracy: 0.4167 - val_loss: 1.3565 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5536 - loss: 1.1568 - val_accuracy: 0.4583 - val_loss: 1.3533 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 64ms/step - accuracy: 0.6339 - loss: 1.1405 - val_accuracy: 0.4583 - val_loss: 1.3496 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 61ms/step - accuracy: 0.5893 - loss: 1.1353 - val_accuracy: 0.4167 - val_loss: 1.3456 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 60ms/step - accuracy: 0.6250 - loss: 1.0937 - val_accuracy: 0.4167 - val_loss: 1.3395 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0834 - val_accuracy: 0.4167 - val_loss: 1.3329 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.0749 - val_accuracy: 0.4167 - val_loss: 1.3263 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0697 - val_accuracy: 0.4583 - val_loss: 1.3205 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0526 - val_accuracy: 0.4583 - val_loss: 1.3136 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.7143 - loss: 1.0078 - val_accuracy: 0.5000 - val_loss: 1.3073 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 60ms/step - accuracy: 0.6250 - loss: 1.0495 - val_accuracy: 0.5000 - val_loss: 1.3003 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9941 - val_accuracy: 0.5000 - val_loss: 1.2924 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.6161 - loss: 1.0226 - val_accuracy: 0.5417 - val_loss: 1.2883 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9896 - val_accuracy: 0.5000 - val_loss: 1.2848 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9633 - val_accuracy: 0.5417 - val_loss: 1.2798 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.9562 - val_accuracy: 0.5417 - val_loss: 1.2702 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 60ms/step - accuracy: 0.7679 - loss: 0.9453 - val_accuracy: 0.5417 - val_loss: 1.2616 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 0.9202 - val_accuracy: 0.5417 - val_loss: 1.2526 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9387 - val_accuracy: 0.5833 - val_loss: 1.2390 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8972 - val_accuracy: 0.5833 - val_loss: 1.2294 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 60ms/step - accuracy: 0.7768 - loss: 0.8916 - val_accuracy: 0.5417 - val_loss: 1.2233 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8962 - val_accuracy: 0.5833 - val_loss: 1.2185 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 61ms/step - accuracy: 0.8304 - loss: 0.8941 - val_accuracy: 0.5833 - val_loss: 1.2095 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.8613 - val_accuracy: 0.5833 - val_loss: 1.1973 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 63ms/step - accuracy: 0.7679 - loss: 0.8854 - val_accuracy: 0.5417 - val_loss: 1.1907 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.8365 - val_accuracy: 0.5417 - val_loss: 1.1898 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8635 - val_accuracy: 0.5833 - val_loss: 1.1856 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.8477 - val_accuracy: 0.5833 - val_loss: 1.1768 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.8325 - val_accuracy: 0.5833 - val_loss: 1.1667 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.7768 - loss: 0.8693 - val_accuracy: 0.5833 - val_loss: 1.1602 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 60ms/step - accuracy: 0.8214 - loss: 0.8064 - val_accuracy: 0.6667 - val_loss: 1.1526 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.7877 - val_accuracy: 0.6667 - val_loss: 1.1451 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7962 - val_accuracy: 0.6250 - val_loss: 1.1314 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 60ms/step - accuracy: 0.8304 - loss: 0.7900 - val_accuracy: 0.6250 - val_loss: 1.1214 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 66ms/step - accuracy: 0.8393 - loss: 0.7856 - val_accuracy: 0.6667 - val_loss: 1.1207 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7685 - val_accuracy: 0.7083 - val_loss: 1.1169 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7744 - val_accuracy: 0.7083 - val_loss: 1.1107 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 60ms/step - accuracy: 0.8393 - loss: 0.7575 - val_accuracy: 0.6667 - val_loss: 1.1039 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 61ms/step - accuracy: 0.8571 - loss: 0.7681 - val_accuracy: 0.6667 - val_loss: 1.0999 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 59ms/step - accuracy: 0.8482 - loss: 0.7545 - val_accuracy: 0.6667 - val_loss: 1.0938 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.7245 - val_accuracy: 0.6667 - val_loss: 1.0872 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.7298 - val_accuracy: 0.7083 - val_loss: 1.0782 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 59ms/step - accuracy: 0.9018 - loss: 0.7148 - val_accuracy: 0.7083 - val_loss: 1.0701 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7507 - val_accuracy: 0.6250 - val_loss: 1.0681 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 59ms/step - accuracy: 0.9018 - loss: 0.7206 - val_accuracy: 0.6667 - val_loss: 1.0648 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.7280 - val_accuracy: 0.6667 - val_loss: 1.0494 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 59ms/step - accuracy: 0.8482 - loss: 0.7060 - val_accuracy: 0.7917 - val_loss: 1.0304 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.6952 - val_accuracy: 0.7083 - val_loss: 1.0398 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.7167 - val_accuracy: 0.7083 - val_loss: 1.0377 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6989 - val_accuracy: 0.7083 - val_loss: 1.0313 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6986 - val_accuracy: 0.6667 - val_loss: 1.0351 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.6686 - val_accuracy: 0.7500 - val_loss: 1.0212 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6624 - val_accuracy: 0.7083 - val_loss: 1.0232 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6733 - val_accuracy: 0.6667 - val_loss: 1.0274 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6642 - val_accuracy: 0.6667 - val_loss: 1.0096 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.6558 - val_accuracy: 0.7083 - val_loss: 0.9955 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6508 - val_accuracy: 0.7500 - val_loss: 0.9992 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.6495 - val_accuracy: 0.6667 - val_loss: 1.0084 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 44ms/step - accuracy: 0.9107 - loss: 0.6416 - val_accuracy: 0.6667 - val_loss: 1.0002 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.6274 - val_accuracy: 0.7500 - val_loss: 0.9926 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6233 - val_accuracy: 0.7083 - val_loss: 0.9949 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.6052 - val_accuracy: 0.7500 - val_loss: 0.9796 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6246 - val_accuracy: 0.7083 - val_loss: 0.9823 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.5808 - val_accuracy: 0.7083 - val_loss: 0.9728 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 60ms/step - accuracy: 0.9107 - loss: 0.6083 - val_accuracy: 0.7500 - val_loss: 0.9648 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5914 - val_accuracy: 0.7083 - val_loss: 0.9824 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.6076 - val_accuracy: 0.7083 - val_loss: 0.9728 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6073 - val_accuracy: 0.8333 - val_loss: 0.9507 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.6180 - val_accuracy: 0.7500 - val_loss: 0.9551 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 58ms/step - accuracy: 0.9464 - loss: 0.6024 - val_accuracy: 0.8333 - val_loss: 0.9452 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.5539 - val_accuracy: 0.7917 - val_loss: 0.9504 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.5553 - val_accuracy: 0.7500 - val_loss: 0.9529 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 60ms/step - accuracy: 0.9375 - loss: 0.5829 - val_accuracy: 0.7500 - val_loss: 0.9358 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5509 - val_accuracy: 0.6667 - val_loss: 0.9403 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5700 - val_accuracy: 0.7083 - val_loss: 0.9417 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 58ms/step - accuracy: 0.9286 - loss: 0.5518 - val_accuracy: 0.7083 - val_loss: 0.9307 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5573 - val_accuracy: 0.6667 - val_loss: 0.9355 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.5352 - val_accuracy: 0.6667 - val_loss: 0.9241 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.5535 - val_accuracy: 0.6667 - val_loss: 0.9175 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.5451 - val_accuracy: 0.7083 - val_loss: 0.9237 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5592 - val_accuracy: 0.6667 - val_loss: 0.9278 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5557 - val_accuracy: 0.6667 - val_loss: 0.9266 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 61ms/step - accuracy: 0.9107 - loss: 0.5358 - val_accuracy: 0.7917 - val_loss: 0.9068 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 59ms/step - accuracy: 0.9375 - loss: 0.5382 - val_accuracy: 0.7500 - val_loss: 0.8933 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5261 - val_accuracy: 0.7500 - val_loss: 0.9071 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5181 - val_accuracy: 0.7500 - val_loss: 0.9168 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5233 - val_accuracy: 0.7500 - val_loss: 0.9001 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 60ms/step - accuracy: 0.9375 - loss: 0.5225 - val_accuracy: 0.7500 - val_loss: 0.8866 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.4899 - val_accuracy: 0.7917 - val_loss: 0.8762 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 60ms/step - accuracy: 0.9286 - loss: 0.5184 - val_accuracy: 0.7917 - val_loss: 0.8679 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4999 - val_accuracy: 0.6667 - val_loss: 0.8890 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4926 - val_accuracy: 0.7083 - val_loss: 0.8985 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.5079 - val_accuracy: 0.6667 - val_loss: 0.8857 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.5041 - val_accuracy: 0.7083 - val_loss: 0.8664 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5046 - val_accuracy: 0.7083 - val_loss: 0.8728 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 58ms/step - accuracy: 0.9464 - loss: 0.4923 - val_accuracy: 0.7500 - val_loss: 0.8656 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 58ms/step - accuracy: 0.9464 - loss: 0.5086 - val_accuracy: 0.7500 - val_loss: 0.8548 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4635 - val_accuracy: 0.7917 - val_loss: 0.8593 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.4687 - val_accuracy: 0.7917 - val_loss: 0.8521 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4682 - val_accuracy: 0.7500 - val_loss: 0.8578 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.4763 - val_accuracy: 0.7083 - val_loss: 0.8690 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4945 - val_accuracy: 0.6250 - val_loss: 0.8756 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 58ms/step - accuracy: 0.9732 - loss: 0.4913 - val_accuracy: 0.7500 - val_loss: 0.8457 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.4289 - val_accuracy: 0.7083 - val_loss: 0.8443 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.4823 - val_accuracy: 0.7083 - val_loss: 0.8667 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4631 - val_accuracy: 0.7083 - val_loss: 0.8597 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4817 - val_accuracy: 0.7083 - val_loss: 0.8474 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4527 - val_accuracy: 0.6667 - val_loss: 0.8827 - learning_rate: 0.0010
Epoch 118/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4345 - val_accuracy: 0.7083 - val_loss: 0.8677 - learning_rate: 0.0010
Epoch 119/500
4/4 - 0s - 58ms/step - accuracy: 0.9554 - loss: 0.4331 - val_accuracy: 0.7083 - val_loss: 0.8412 - learning_rate: 0.0010
Epoch 120/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4492 - val_accuracy: 0.6667 - val_loss: 0.8691 - learning_rate: 0.0010
Epoch 121/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.4636 - val_accuracy: 0.6250 - val_loss: 0.8650 - learning_rate: 0.0010
Epoch 122/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4197 - val_accuracy: 0.6250 - val_loss: 0.8558 - learning_rate: 0.0010
Epoch 123/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4549 - val_accuracy: 0.6667 - val_loss: 0.8654 - learning_rate: 0.0010
Epoch 124/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4032 - val_accuracy: 0.6667 - val_loss: 0.8820 - learning_rate: 0.0010
Epoch 125/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4238 - val_accuracy: 0.6250 - val_loss: 0.8758 - learning_rate: 0.0010
Epoch 126/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4628 - val_accuracy: 0.7500 - val_loss: 0.8607 - learning_rate: 0.0010
Epoch 127/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4292 - val_accuracy: 0.7083 - val_loss: 0.8723 - learning_rate: 0.0010
Epoch 128/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4132 - val_accuracy: 0.6667 - val_loss: 0.8447 - learning_rate: 0.0010
Epoch 129/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4304 - val_accuracy: 0.6667 - val_loss: 0.8415 - learning_rate: 0.0010
Epoch 130/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.4294 - val_accuracy: 0.6667 - val_loss: 0.8685 - learning_rate: 0.0010
Epoch 131/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4199 - val_accuracy: 0.6667 - val_loss: 0.8591 - learning_rate: 0.0010
Epoch 132/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4329 - val_accuracy: 0.6250 - val_loss: 0.8413 - learning_rate: 0.0010
Epoch 133/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4132 - val_accuracy: 0.6667 - val_loss: 0.8503 - learning_rate: 0.0010
Epoch 134/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.4037 - val_accuracy: 0.6250 - val_loss: 0.8498 - learning_rate: 0.0010
Epoch 134: early stopping
Restoring model weights from the end of the best epoch: 119.
Training complete. Best epoch: 119 of 134. Best val_loss: 0.8412, val_accuracy: 0.7083

========== Evaluation: within-subject test / EMS0007 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         2         2         0
  min_intens         4         1         1         0
  medium_int         2         0         2         2
  max_intens         0         1         2         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.250     0.333     0.286         6
   min_intensity      0.250     0.167     0.200         6
medium_intensity      0.286     0.333     0.308         6
   max_intensity      0.600     0.500     0.545         6

        accuracy                          0.333        24
       macro avg      0.346     0.333     0.335        24
    weighted avg      0.346     0.333     0.335        24

Overall accuracy: 0.3333

Artifacts saved to /kaggle/working/within_all/EMS0007/

############################################################
# Subject 8/31: EMS0008
############################################################
Loaded EMS0008 from /kaggle/input/datasets/akablawi/ems-4class/EMS0008.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-4.25e-04, 4.72e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.54e-06, 3.31e-06]
  Per-channel std range:  [5.09e-06, 3.42e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2321 - loss: 1.4500 - val_accuracy: 0.2500 - val_loss: 1.3851 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 62ms/step - accuracy: 0.3839 - loss: 1.3520 - val_accuracy: 0.2917 - val_loss: 1.3844 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.4732 - loss: 1.3256 - val_accuracy: 0.1667 - val_loss: 1.3829 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 58ms/step - accuracy: 0.4464 - loss: 1.3143 - val_accuracy: 0.2083 - val_loss: 1.3798 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.5089 - loss: 1.2802 - val_accuracy: 0.2083 - val_loss: 1.3752 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.4464 - loss: 1.2569 - val_accuracy: 0.2500 - val_loss: 1.3699 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 62ms/step - accuracy: 0.4821 - loss: 1.2363 - val_accuracy: 0.4167 - val_loss: 1.3638 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.5446 - loss: 1.1984 - val_accuracy: 0.4167 - val_loss: 1.3569 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.1671 - val_accuracy: 0.3750 - val_loss: 1.3498 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 60ms/step - accuracy: 0.5625 - loss: 1.1557 - val_accuracy: 0.3750 - val_loss: 1.3424 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.1055 - val_accuracy: 0.3750 - val_loss: 1.3349 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 60ms/step - accuracy: 0.6607 - loss: 1.0814 - val_accuracy: 0.3750 - val_loss: 1.3268 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0599 - val_accuracy: 0.4167 - val_loss: 1.3174 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0551 - val_accuracy: 0.4583 - val_loss: 1.3093 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.0382 - val_accuracy: 0.4167 - val_loss: 1.3025 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 1.0086 - val_accuracy: 0.4167 - val_loss: 1.2942 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 61ms/step - accuracy: 0.6696 - loss: 0.9970 - val_accuracy: 0.3750 - val_loss: 1.2863 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.0019 - val_accuracy: 0.4167 - val_loss: 1.2787 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.9521 - val_accuracy: 0.4583 - val_loss: 1.2708 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.6964 - loss: 0.9578 - val_accuracy: 0.4583 - val_loss: 1.2629 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9402 - val_accuracy: 0.4583 - val_loss: 1.2553 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9212 - val_accuracy: 0.5000 - val_loss: 1.2471 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9031 - val_accuracy: 0.5417 - val_loss: 1.2392 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8769 - val_accuracy: 0.5417 - val_loss: 1.2322 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 60ms/step - accuracy: 0.7232 - loss: 0.8834 - val_accuracy: 0.5417 - val_loss: 1.2256 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8870 - val_accuracy: 0.5833 - val_loss: 1.2157 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8542 - val_accuracy: 0.6250 - val_loss: 1.2080 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.8366 - val_accuracy: 0.7083 - val_loss: 1.1984 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 60ms/step - accuracy: 0.7500 - loss: 0.8441 - val_accuracy: 0.5833 - val_loss: 1.1981 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7971 - val_accuracy: 0.6250 - val_loss: 1.1900 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7968 - val_accuracy: 0.6667 - val_loss: 1.1782 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 60ms/step - accuracy: 0.7857 - loss: 0.7903 - val_accuracy: 0.5417 - val_loss: 1.1740 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7933 - val_accuracy: 0.5833 - val_loss: 1.1676 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7769 - val_accuracy: 0.5417 - val_loss: 1.1668 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.7648 - val_accuracy: 0.6250 - val_loss: 1.1572 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.7636 - val_accuracy: 0.6250 - val_loss: 1.1445 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 44ms/step - accuracy: 0.8393 - loss: 0.7272 - val_accuracy: 0.5833 - val_loss: 1.1469 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7453 - val_accuracy: 0.5417 - val_loss: 1.1364 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.7125 - val_accuracy: 0.5833 - val_loss: 1.1274 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.7297 - val_accuracy: 0.5417 - val_loss: 1.1318 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 44ms/step - accuracy: 0.8661 - loss: 0.6854 - val_accuracy: 0.5417 - val_loss: 1.1362 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7161 - val_accuracy: 0.5417 - val_loss: 1.1302 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6877 - val_accuracy: 0.5833 - val_loss: 1.1189 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6927 - val_accuracy: 0.5833 - val_loss: 1.1204 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.7016 - val_accuracy: 0.5833 - val_loss: 1.1242 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6575 - val_accuracy: 0.5417 - val_loss: 1.1342 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6438 - val_accuracy: 0.5833 - val_loss: 1.1188 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6479 - val_accuracy: 0.5833 - val_loss: 1.1157 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 48ms/step - accuracy: 0.8214 - loss: 0.6403 - val_accuracy: 0.5833 - val_loss: 1.1210 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 59ms/step - accuracy: 0.8482 - loss: 0.6407 - val_accuracy: 0.5417 - val_loss: 1.1131 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 45ms/step - accuracy: 0.8482 - loss: 0.6502 - val_accuracy: 0.5000 - val_loss: 1.1163 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6271 - val_accuracy: 0.5417 - val_loss: 1.1170 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 46ms/step - accuracy: 0.8750 - loss: 0.6436 - val_accuracy: 0.5417 - val_loss: 1.1153 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6401 - val_accuracy: 0.5417 - val_loss: 1.1152 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6147 - val_accuracy: 0.5417 - val_loss: 1.1122 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.6069 - val_accuracy: 0.5417 - val_loss: 1.0952 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5850 - val_accuracy: 0.5417 - val_loss: 1.0968 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.6246 - val_accuracy: 0.4583 - val_loss: 1.0911 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.5891 - val_accuracy: 0.5000 - val_loss: 1.0935 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.6148 - val_accuracy: 0.4583 - val_loss: 1.1044 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6003 - val_accuracy: 0.4583 - val_loss: 1.1054 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.5659 - val_accuracy: 0.4583 - val_loss: 1.0951 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 44ms/step - accuracy: 0.8393 - loss: 0.5918 - val_accuracy: 0.5000 - val_loss: 1.0936 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5788 - val_accuracy: 0.5000 - val_loss: 1.0926 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5441 - val_accuracy: 0.4583 - val_loss: 1.0849 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.5936 - val_accuracy: 0.4583 - val_loss: 1.1014 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5719 - val_accuracy: 0.4583 - val_loss: 1.0929 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5601 - val_accuracy: 0.4583 - val_loss: 1.1071 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.5612 - val_accuracy: 0.4583 - val_loss: 1.1190 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.5380 - val_accuracy: 0.4583 - val_loss: 1.0973 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.5530 - val_accuracy: 0.4583 - val_loss: 1.0971 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.5414 - val_accuracy: 0.4583 - val_loss: 1.0886 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5352 - val_accuracy: 0.4583 - val_loss: 1.1014 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5253 - val_accuracy: 0.5000 - val_loss: 1.0993 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.5054 - val_accuracy: 0.4583 - val_loss: 1.0779 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5145 - val_accuracy: 0.4167 - val_loss: 1.0859 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.5242 - val_accuracy: 0.4167 - val_loss: 1.1098 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.5088 - val_accuracy: 0.4167 - val_loss: 1.1124 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4861 - val_accuracy: 0.4167 - val_loss: 1.1129 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.4753 - val_accuracy: 0.4167 - val_loss: 1.1078 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5150 - val_accuracy: 0.4167 - val_loss: 1.1130 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5120 - val_accuracy: 0.4167 - val_loss: 1.1167 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.4954 - val_accuracy: 0.4167 - val_loss: 1.1007 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.4898 - val_accuracy: 0.4167 - val_loss: 1.1166 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.4829 - val_accuracy: 0.4167 - val_loss: 1.1047 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.4879 - val_accuracy: 0.4167 - val_loss: 1.1032 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.4770 - val_accuracy: 0.4583 - val_loss: 1.1261 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.4636 - val_accuracy: 0.4167 - val_loss: 1.0982 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.4630 - val_accuracy: 0.4167 - val_loss: 1.0962 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4642 - val_accuracy: 0.3750 - val_loss: 1.1373 - learning_rate: 0.0010
Epoch 90: early stopping
Restoring model weights from the end of the best epoch: 75.
Training complete. Best epoch: 75 of 90. Best val_loss: 1.0779, val_accuracy: 0.4583

========== Evaluation: within-subject test / EMS0008 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         2         0         1
  min_intens         2         4         0         0
  medium_int         2         2         0         2
  max_intens         0         2         1         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.429     0.500     0.462         6
   min_intensity      0.400     0.667     0.500         6
medium_intensity      0.000     0.000     0.000         6
   max_intensity      0.500     0.500     0.500         6

        accuracy                          0.417        24
       macro avg      0.332     0.417     0.365        24
    weighted avg      0.332     0.417     0.365        24

Overall accuracy: 0.4167

Artifacts saved to /kaggle/working/within_all/EMS0008/

############################################################
# Subject 9/31: EMS0009
############################################################
Loaded EMS0009 from /kaggle/input/datasets/akablawi/ems-4class/EMS0009.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-2.00e-04, 2.70e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.85e-06, 3.90e-06]
  Per-channel std range:  [5.82e-06, 4.63e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2857 - loss: 1.4287 - val_accuracy: 0.5833 - val_loss: 1.3775 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 58ms/step - accuracy: 0.5089 - loss: 1.2557 - val_accuracy: 0.5833 - val_loss: 1.3666 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.6071 - loss: 1.1890 - val_accuracy: 0.5833 - val_loss: 1.3534 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 58ms/step - accuracy: 0.6250 - loss: 1.1195 - val_accuracy: 0.5833 - val_loss: 1.3352 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 62ms/step - accuracy: 0.6161 - loss: 1.0706 - val_accuracy: 0.6250 - val_loss: 1.3145 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.0351 - val_accuracy: 0.5833 - val_loss: 1.2936 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.6607 - loss: 0.9845 - val_accuracy: 0.5833 - val_loss: 1.2739 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.9693 - val_accuracy: 0.5833 - val_loss: 1.2559 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 57ms/step - accuracy: 0.6786 - loss: 0.9440 - val_accuracy: 0.6667 - val_loss: 1.2373 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9124 - val_accuracy: 0.7500 - val_loss: 1.2186 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.7321 - loss: 0.8710 - val_accuracy: 0.7500 - val_loss: 1.2049 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 61ms/step - accuracy: 0.7143 - loss: 0.8736 - val_accuracy: 0.7500 - val_loss: 1.1939 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.8426 - val_accuracy: 0.7500 - val_loss: 1.1794 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8335 - val_accuracy: 0.7083 - val_loss: 1.1627 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 57ms/step - accuracy: 0.7500 - loss: 0.7981 - val_accuracy: 0.7083 - val_loss: 1.1481 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7626 - val_accuracy: 0.7083 - val_loss: 1.1250 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.7400 - val_accuracy: 0.7500 - val_loss: 1.1087 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7396 - val_accuracy: 0.7500 - val_loss: 1.0948 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.7316 - val_accuracy: 0.7500 - val_loss: 1.0895 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 60ms/step - accuracy: 0.8304 - loss: 0.7087 - val_accuracy: 0.7500 - val_loss: 1.0782 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.8482 - loss: 0.6971 - val_accuracy: 0.7083 - val_loss: 1.0680 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7082 - val_accuracy: 0.6667 - val_loss: 1.0638 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.6633 - val_accuracy: 0.7083 - val_loss: 1.0540 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.6853 - val_accuracy: 0.7500 - val_loss: 1.0325 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.6692 - val_accuracy: 0.7500 - val_loss: 1.0166 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6459 - val_accuracy: 0.6667 - val_loss: 1.0239 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.6356 - val_accuracy: 0.6667 - val_loss: 1.0267 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6238 - val_accuracy: 0.6667 - val_loss: 1.0197 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 57ms/step - accuracy: 0.8571 - loss: 0.6453 - val_accuracy: 0.6667 - val_loss: 1.0067 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 57ms/step - accuracy: 0.8482 - loss: 0.6184 - val_accuracy: 0.6250 - val_loss: 0.9979 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.6335 - val_accuracy: 0.5833 - val_loss: 1.0001 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 57ms/step - accuracy: 0.8929 - loss: 0.6086 - val_accuracy: 0.6667 - val_loss: 0.9892 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.5822 - val_accuracy: 0.5833 - val_loss: 0.9858 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 57ms/step - accuracy: 0.8125 - loss: 0.6133 - val_accuracy: 0.5833 - val_loss: 0.9855 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5960 - val_accuracy: 0.5833 - val_loss: 0.9859 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.5875 - val_accuracy: 0.6250 - val_loss: 0.9756 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5605 - val_accuracy: 0.6250 - val_loss: 0.9701 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.5727 - val_accuracy: 0.6250 - val_loss: 0.9623 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.5686 - val_accuracy: 0.6667 - val_loss: 0.9525 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5437 - val_accuracy: 0.6667 - val_loss: 0.9639 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5635 - val_accuracy: 0.6250 - val_loss: 0.9695 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5564 - val_accuracy: 0.6250 - val_loss: 0.9560 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.5598 - val_accuracy: 0.6250 - val_loss: 0.9352 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5280 - val_accuracy: 0.6250 - val_loss: 0.9537 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5199 - val_accuracy: 0.6250 - val_loss: 0.9367 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5175 - val_accuracy: 0.5833 - val_loss: 0.9589 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.5228 - val_accuracy: 0.6667 - val_loss: 0.9292 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.5132 - val_accuracy: 0.6667 - val_loss: 0.9196 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5164 - val_accuracy: 0.5833 - val_loss: 0.9485 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.4965 - val_accuracy: 0.5833 - val_loss: 0.9461 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.5100 - val_accuracy: 0.6667 - val_loss: 0.8976 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.4901 - val_accuracy: 0.6667 - val_loss: 0.9140 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 46ms/step - accuracy: 0.8929 - loss: 0.4806 - val_accuracy: 0.5833 - val_loss: 0.9332 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 45ms/step - accuracy: 0.8929 - loss: 0.4887 - val_accuracy: 0.6667 - val_loss: 0.9172 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.4839 - val_accuracy: 0.6667 - val_loss: 0.9077 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.4633 - val_accuracy: 0.5417 - val_loss: 0.9242 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.4754 - val_accuracy: 0.6250 - val_loss: 0.8974 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 56ms/step - accuracy: 0.9107 - loss: 0.4799 - val_accuracy: 0.6667 - val_loss: 0.8911 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.4585 - val_accuracy: 0.5833 - val_loss: 0.9322 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 56ms/step - accuracy: 0.8839 - loss: 0.4814 - val_accuracy: 0.6667 - val_loss: 0.8793 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 57ms/step - accuracy: 0.9286 - loss: 0.4309 - val_accuracy: 0.6667 - val_loss: 0.8685 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4352 - val_accuracy: 0.5833 - val_loss: 0.9152 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 56ms/step - accuracy: 0.9107 - loss: 0.4384 - val_accuracy: 0.6667 - val_loss: 0.8518 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 41ms/step - accuracy: 0.8750 - loss: 0.4528 - val_accuracy: 0.6667 - val_loss: 0.8591 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.4308 - val_accuracy: 0.5833 - val_loss: 0.9034 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 41ms/step - accuracy: 0.9196 - loss: 0.4320 - val_accuracy: 0.6250 - val_loss: 0.8657 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 56ms/step - accuracy: 0.9196 - loss: 0.4318 - val_accuracy: 0.7500 - val_loss: 0.8518 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.4187 - val_accuracy: 0.5833 - val_loss: 0.9056 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.4377 - val_accuracy: 0.5417 - val_loss: 0.8669 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 56ms/step - accuracy: 0.9107 - loss: 0.4362 - val_accuracy: 0.6667 - val_loss: 0.8288 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4117 - val_accuracy: 0.7083 - val_loss: 0.8369 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 40ms/step - accuracy: 0.9286 - loss: 0.4138 - val_accuracy: 0.6250 - val_loss: 0.8600 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.3918 - val_accuracy: 0.6250 - val_loss: 0.8614 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 40ms/step - accuracy: 0.9196 - loss: 0.4074 - val_accuracy: 0.6667 - val_loss: 0.8588 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.3986 - val_accuracy: 0.6667 - val_loss: 0.8630 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.3862 - val_accuracy: 0.7083 - val_loss: 0.8316 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 56ms/step - accuracy: 0.9196 - loss: 0.3800 - val_accuracy: 0.7083 - val_loss: 0.7888 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.3916 - val_accuracy: 0.7083 - val_loss: 0.8253 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.3901 - val_accuracy: 0.6250 - val_loss: 0.8678 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.3998 - val_accuracy: 0.6667 - val_loss: 0.8137 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.3741 - val_accuracy: 0.6667 - val_loss: 0.8289 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3771 - val_accuracy: 0.6667 - val_loss: 0.8333 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.3751 - val_accuracy: 0.7083 - val_loss: 0.7977 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.3697 - val_accuracy: 0.6250 - val_loss: 0.8182 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3494 - val_accuracy: 0.7083 - val_loss: 0.8495 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.3668 - val_accuracy: 0.7083 - val_loss: 0.8126 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 41ms/step - accuracy: 0.9018 - loss: 0.3658 - val_accuracy: 0.6667 - val_loss: 0.8004 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.3467 - val_accuracy: 0.6250 - val_loss: 0.8162 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.3703 - val_accuracy: 0.7083 - val_loss: 0.7768 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3633 - val_accuracy: 0.7083 - val_loss: 0.7839 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.3490 - val_accuracy: 0.6667 - val_loss: 0.8310 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.3404 - val_accuracy: 0.6667 - val_loss: 0.7883 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 57ms/step - accuracy: 0.9821 - loss: 0.3377 - val_accuracy: 0.7083 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 55ms/step - accuracy: 0.9464 - loss: 0.3359 - val_accuracy: 0.7083 - val_loss: 0.7429 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.3169 - val_accuracy: 0.6250 - val_loss: 0.7983 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.3382 - val_accuracy: 0.6667 - val_loss: 0.8003 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.3349 - val_accuracy: 0.7083 - val_loss: 0.7463 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.3358 - val_accuracy: 0.7083 - val_loss: 0.7598 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.3370 - val_accuracy: 0.6250 - val_loss: 0.8265 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.3544 - val_accuracy: 0.6667 - val_loss: 0.8005 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 40ms/step - accuracy: 0.9554 - loss: 0.3408 - val_accuracy: 0.6667 - val_loss: 0.7626 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.3181 - val_accuracy: 0.6667 - val_loss: 0.7876 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 40ms/step - accuracy: 0.9464 - loss: 0.3113 - val_accuracy: 0.6667 - val_loss: 0.7868 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 40ms/step - accuracy: 0.9643 - loss: 0.3112 - val_accuracy: 0.6250 - val_loss: 0.8384 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 40ms/step - accuracy: 0.9464 - loss: 0.3082 - val_accuracy: 0.7083 - val_loss: 0.7601 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 40ms/step - accuracy: 0.9732 - loss: 0.3108 - val_accuracy: 0.6667 - val_loss: 0.7744 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 40ms/step - accuracy: 0.9821 - loss: 0.2953 - val_accuracy: 0.6250 - val_loss: 0.7866 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 40ms/step - accuracy: 0.9732 - loss: 0.2744 - val_accuracy: 0.6250 - val_loss: 0.7902 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 40ms/step - accuracy: 0.9643 - loss: 0.3292 - val_accuracy: 0.6250 - val_loss: 0.7857 - learning_rate: 0.0010
Epoch 109: early stopping
Restoring model weights from the end of the best epoch: 94.
Training complete. Best epoch: 94 of 109. Best val_loss: 0.7429, val_accuracy: 0.7083

========== Evaluation: within-subject test / EMS0009 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         1         1         0
  min_intens         2         3         1         0
  medium_int         0         1         5         0
  max_intens         1         0         0         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.571     0.667     0.615         6
   min_intensity      0.600     0.500     0.545         6
medium_intensity      0.714     0.833     0.769         6
   max_intensity      1.000     0.833     0.909         6

        accuracy                          0.708        24
       macro avg      0.721     0.708     0.710        24
    weighted avg      0.721     0.708     0.710        24

Overall accuracy: 0.7083

Artifacts saved to /kaggle/working/within_all/EMS0009/

############################################################
# Subject 10/31: EMS0010
############################################################
Loaded EMS0010 from /kaggle/input/datasets/akablawi/ems-4class/EMS0010.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.12e-03, 8.81e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.63e-06, 8.12e-07]
  Per-channel std range:  [6.23e-06, 6.17e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3393 - loss: 1.4206 - val_accuracy: 0.2917 - val_loss: 1.3850 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.3304 - loss: 1.3652 - val_accuracy: 0.3750 - val_loss: 1.3823 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 62ms/step - accuracy: 0.4018 - loss: 1.3202 - val_accuracy: 0.5000 - val_loss: 1.3782 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 61ms/step - accuracy: 0.4732 - loss: 1.3046 - val_accuracy: 0.5000 - val_loss: 1.3726 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.4464 - loss: 1.2599 - val_accuracy: 0.5000 - val_loss: 1.3653 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.5446 - loss: 1.2363 - val_accuracy: 0.5417 - val_loss: 1.3559 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5625 - loss: 1.2161 - val_accuracy: 0.5000 - val_loss: 1.3441 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1663 - val_accuracy: 0.5417 - val_loss: 1.3305 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5089 - loss: 1.1369 - val_accuracy: 0.5417 - val_loss: 1.3144 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.1223 - val_accuracy: 0.5417 - val_loss: 1.2958 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5893 - loss: 1.0863 - val_accuracy: 0.5417 - val_loss: 1.2757 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.5714 - loss: 1.0696 - val_accuracy: 0.5833 - val_loss: 1.2550 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5982 - loss: 1.0307 - val_accuracy: 0.5417 - val_loss: 1.2378 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5179 - loss: 1.0488 - val_accuracy: 0.5417 - val_loss: 1.2264 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 0.9884 - val_accuracy: 0.5833 - val_loss: 1.2123 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 0.9577 - val_accuracy: 0.6250 - val_loss: 1.1898 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 0.9636 - val_accuracy: 0.5833 - val_loss: 1.1731 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9307 - val_accuracy: 0.5833 - val_loss: 1.1608 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9151 - val_accuracy: 0.5417 - val_loss: 1.1507 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8810 - val_accuracy: 0.5833 - val_loss: 1.1438 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8644 - val_accuracy: 0.5417 - val_loss: 1.1323 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8523 - val_accuracy: 0.5417 - val_loss: 1.1218 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8295 - val_accuracy: 0.5417 - val_loss: 1.1199 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8407 - val_accuracy: 0.5833 - val_loss: 1.1132 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.8587 - val_accuracy: 0.5417 - val_loss: 1.1064 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 58ms/step - accuracy: 0.7768 - loss: 0.8178 - val_accuracy: 0.5417 - val_loss: 1.1037 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 60ms/step - accuracy: 0.7946 - loss: 0.8057 - val_accuracy: 0.5833 - val_loss: 1.0994 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8052 - val_accuracy: 0.5417 - val_loss: 1.0906 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7834 - val_accuracy: 0.5417 - val_loss: 1.0711 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.7981 - val_accuracy: 0.5833 - val_loss: 1.0593 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.7848 - val_accuracy: 0.5417 - val_loss: 1.0587 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.7481 - val_accuracy: 0.5833 - val_loss: 1.0642 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.7556 - val_accuracy: 0.5833 - val_loss: 1.0586 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7487 - val_accuracy: 0.5833 - val_loss: 1.0564 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.7636 - val_accuracy: 0.5417 - val_loss: 1.0565 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7450 - val_accuracy: 0.5417 - val_loss: 1.0456 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.7199 - val_accuracy: 0.5417 - val_loss: 1.0342 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.7344 - val_accuracy: 0.5417 - val_loss: 1.0336 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7098 - val_accuracy: 0.5417 - val_loss: 1.0386 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.6882 - val_accuracy: 0.5417 - val_loss: 1.0420 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6945 - val_accuracy: 0.5417 - val_loss: 1.0403 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 60ms/step - accuracy: 0.8661 - loss: 0.6996 - val_accuracy: 0.5417 - val_loss: 1.0296 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 60ms/step - accuracy: 0.9107 - loss: 0.6678 - val_accuracy: 0.5417 - val_loss: 1.0237 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.6875 - val_accuracy: 0.5833 - val_loss: 1.0139 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.6593 - val_accuracy: 0.5417 - val_loss: 1.0167 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6647 - val_accuracy: 0.5417 - val_loss: 1.0219 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6432 - val_accuracy: 0.5833 - val_loss: 1.0170 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 47ms/step - accuracy: 0.8929 - loss: 0.6716 - val_accuracy: 0.5417 - val_loss: 1.0186 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 44ms/step - accuracy: 0.8304 - loss: 0.6682 - val_accuracy: 0.5417 - val_loss: 1.0196 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 60ms/step - accuracy: 0.8839 - loss: 0.6483 - val_accuracy: 0.5833 - val_loss: 1.0124 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 57ms/step - accuracy: 0.8571 - loss: 0.6416 - val_accuracy: 0.5417 - val_loss: 0.9999 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6626 - val_accuracy: 0.5833 - val_loss: 0.9963 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.6229 - val_accuracy: 0.5417 - val_loss: 0.9877 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 44ms/step - accuracy: 0.9107 - loss: 0.6150 - val_accuracy: 0.5000 - val_loss: 0.9936 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6300 - val_accuracy: 0.5833 - val_loss: 1.0011 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.6197 - val_accuracy: 0.5833 - val_loss: 0.9897 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 57ms/step - accuracy: 0.9107 - loss: 0.6171 - val_accuracy: 0.5417 - val_loss: 0.9734 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.6033 - val_accuracy: 0.5833 - val_loss: 0.9810 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.6000 - val_accuracy: 0.5833 - val_loss: 0.9909 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5924 - val_accuracy: 0.6250 - val_loss: 0.9885 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6037 - val_accuracy: 0.6250 - val_loss: 0.9840 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.6096 - val_accuracy: 0.5833 - val_loss: 0.9811 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5777 - val_accuracy: 0.5833 - val_loss: 0.9781 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5829 - val_accuracy: 0.6250 - val_loss: 0.9779 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.5756 - val_accuracy: 0.6250 - val_loss: 0.9732 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5625 - val_accuracy: 0.6250 - val_loss: 0.9752 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.5727 - val_accuracy: 0.5833 - val_loss: 0.9657 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5508 - val_accuracy: 0.6250 - val_loss: 0.9817 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5737 - val_accuracy: 0.5833 - val_loss: 0.9732 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 58ms/step - accuracy: 0.9286 - loss: 0.5428 - val_accuracy: 0.5833 - val_loss: 0.9555 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5568 - val_accuracy: 0.5833 - val_loss: 0.9620 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5624 - val_accuracy: 0.5833 - val_loss: 0.9636 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.5446 - val_accuracy: 0.5833 - val_loss: 0.9483 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.5308 - val_accuracy: 0.5833 - val_loss: 0.9372 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.5289 - val_accuracy: 0.5833 - val_loss: 0.9361 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5209 - val_accuracy: 0.5833 - val_loss: 0.9400 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5355 - val_accuracy: 0.6250 - val_loss: 0.9489 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5236 - val_accuracy: 0.6250 - val_loss: 0.9551 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5368 - val_accuracy: 0.5833 - val_loss: 0.9402 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.5048 - val_accuracy: 0.6250 - val_loss: 0.9380 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5156 - val_accuracy: 0.5833 - val_loss: 0.9446 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.5208 - val_accuracy: 0.6250 - val_loss: 0.9485 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 58ms/step - accuracy: 0.9643 - loss: 0.5096 - val_accuracy: 0.6250 - val_loss: 0.9329 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.4793 - val_accuracy: 0.5833 - val_loss: 0.9334 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5153 - val_accuracy: 0.5833 - val_loss: 0.9446 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.5125 - val_accuracy: 0.5833 - val_loss: 0.9465 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4999 - val_accuracy: 0.6667 - val_loss: 0.9415 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4827 - val_accuracy: 0.6250 - val_loss: 0.9425 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.4619 - val_accuracy: 0.6667 - val_loss: 0.9402 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4900 - val_accuracy: 0.6250 - val_loss: 0.9344 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 57ms/step - accuracy: 0.9196 - loss: 0.5028 - val_accuracy: 0.6250 - val_loss: 0.9301 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4680 - val_accuracy: 0.6250 - val_loss: 0.9435 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.4802 - val_accuracy: 0.5833 - val_loss: 0.9611 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4630 - val_accuracy: 0.5833 - val_loss: 0.9627 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.4585 - val_accuracy: 0.6250 - val_loss: 0.9435 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4374 - val_accuracy: 0.5833 - val_loss: 0.9379 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 57ms/step - accuracy: 0.9375 - loss: 0.4498 - val_accuracy: 0.6250 - val_loss: 0.9231 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 61ms/step - accuracy: 0.9821 - loss: 0.4367 - val_accuracy: 0.6250 - val_loss: 0.9215 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.4600 - val_accuracy: 0.6250 - val_loss: 0.9380 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 49ms/step - accuracy: 0.9643 - loss: 0.4474 - val_accuracy: 0.6250 - val_loss: 0.9391 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.4445 - val_accuracy: 0.6250 - val_loss: 0.9467 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.4616 - val_accuracy: 0.5417 - val_loss: 0.9477 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.4553 - val_accuracy: 0.5833 - val_loss: 0.9473 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.4210 - val_accuracy: 0.6250 - val_loss: 0.9427 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4345 - val_accuracy: 0.5833 - val_loss: 0.9484 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.4352 - val_accuracy: 0.5833 - val_loss: 0.9235 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 62ms/step - accuracy: 0.9464 - loss: 0.4430 - val_accuracy: 0.6667 - val_loss: 0.9139 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4437 - val_accuracy: 0.6667 - val_loss: 0.9297 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 58ms/step - accuracy: 0.9554 - loss: 0.4267 - val_accuracy: 0.6250 - val_loss: 0.9061 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.4430 - val_accuracy: 0.6667 - val_loss: 0.9191 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.4228 - val_accuracy: 0.7083 - val_loss: 0.9343 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4222 - val_accuracy: 0.5833 - val_loss: 0.9274 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 57ms/step - accuracy: 0.9911 - loss: 0.3966 - val_accuracy: 0.5833 - val_loss: 0.9032 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.4215 - val_accuracy: 0.6250 - val_loss: 0.9095 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4126 - val_accuracy: 0.6250 - val_loss: 0.9266 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.4026 - val_accuracy: 0.6250 - val_loss: 0.9205 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3846 - val_accuracy: 0.6250 - val_loss: 0.9114 - learning_rate: 0.0010
Epoch 118/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4133 - val_accuracy: 0.5833 - val_loss: 0.9117 - learning_rate: 0.0010
Epoch 119/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4068 - val_accuracy: 0.6667 - val_loss: 0.9273 - learning_rate: 0.0010
Epoch 120/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.3731 - val_accuracy: 0.6667 - val_loss: 0.9289 - learning_rate: 0.0010
Epoch 121/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.3860 - val_accuracy: 0.6667 - val_loss: 0.9303 - learning_rate: 0.0010
Epoch 122/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3831 - val_accuracy: 0.6250 - val_loss: 0.9278 - learning_rate: 0.0010
Epoch 123/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3805 - val_accuracy: 0.5417 - val_loss: 0.9277 - learning_rate: 0.0010
Epoch 124/500
4/4 - 0s - 41ms/step - accuracy: 0.9821 - loss: 0.3785 - val_accuracy: 0.6667 - val_loss: 0.9123 - learning_rate: 0.0010
Epoch 125/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.4226 - val_accuracy: 0.6667 - val_loss: 0.9127 - learning_rate: 0.0010
Epoch 126/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3853 - val_accuracy: 0.5833 - val_loss: 0.9189 - learning_rate: 0.0010
Epoch 127/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3935 - val_accuracy: 0.5833 - val_loss: 0.9447 - learning_rate: 0.0010
Epoch 128/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3933 - val_accuracy: 0.5833 - val_loss: 0.9513 - learning_rate: 0.0010
Epoch 128: early stopping
Restoring model weights from the end of the best epoch: 113.
Training complete. Best epoch: 113 of 128. Best val_loss: 0.9032, val_accuracy: 0.5833

========== Evaluation: within-subject test / EMS0010 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         1         0         1
  min_intens         4         1         1         0
  medium_int         0         0         5         1
  max_intens         0         1         2         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.667     0.571         6
   min_intensity      0.333     0.167     0.222         6
medium_intensity      0.625     0.833     0.714         6
   max_intensity      0.600     0.500     0.545         6

        accuracy                          0.542        24
       macro avg      0.515     0.542     0.513        24
    weighted avg      0.515     0.542     0.513        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0010/

############################################################
# Subject 11/31: EMS0011
############################################################
Loaded EMS0011 from /kaggle/input/datasets/akablawi/ems-4class/EMS0011.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-2.44e-04, 5.09e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.12e-06, 3.18e-06]
  Per-channel std range:  [3.70e-06, 7.16e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2589 - loss: 1.3918 - val_accuracy: 0.4583 - val_loss: 1.3848 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 59ms/step - accuracy: 0.3482 - loss: 1.3706 - val_accuracy: 0.4167 - val_loss: 1.3836 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 61ms/step - accuracy: 0.3571 - loss: 1.3613 - val_accuracy: 0.3750 - val_loss: 1.3822 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.4196 - loss: 1.3329 - val_accuracy: 0.4167 - val_loss: 1.3805 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4286 - loss: 1.3170 - val_accuracy: 0.2917 - val_loss: 1.3784 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.2865 - val_accuracy: 0.2500 - val_loss: 1.3758 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.2654 - val_accuracy: 0.2083 - val_loss: 1.3724 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2400 - val_accuracy: 0.2083 - val_loss: 1.3686 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.2072 - val_accuracy: 0.2917 - val_loss: 1.3647 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 57ms/step - accuracy: 0.6071 - loss: 1.1832 - val_accuracy: 0.2917 - val_loss: 1.3606 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.1561 - val_accuracy: 0.2917 - val_loss: 1.3560 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.6607 - loss: 1.1042 - val_accuracy: 0.2917 - val_loss: 1.3513 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 60ms/step - accuracy: 0.5982 - loss: 1.1073 - val_accuracy: 0.3750 - val_loss: 1.3463 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5893 - loss: 1.1055 - val_accuracy: 0.3333 - val_loss: 1.3390 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6250 - loss: 1.0939 - val_accuracy: 0.3750 - val_loss: 1.3329 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0708 - val_accuracy: 0.3333 - val_loss: 1.3314 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 1.0331 - val_accuracy: 0.2917 - val_loss: 1.3271 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 60ms/step - accuracy: 0.6339 - loss: 1.0367 - val_accuracy: 0.2917 - val_loss: 1.3231 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 1.0006 - val_accuracy: 0.3333 - val_loss: 1.3164 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9610 - val_accuracy: 0.3333 - val_loss: 1.3096 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 0.9918 - val_accuracy: 0.2500 - val_loss: 1.3070 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.9479 - val_accuracy: 0.3333 - val_loss: 1.3035 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.9351 - val_accuracy: 0.3333 - val_loss: 1.3002 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.9148 - val_accuracy: 0.3333 - val_loss: 1.2946 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.9045 - val_accuracy: 0.3333 - val_loss: 1.2882 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.9035 - val_accuracy: 0.3750 - val_loss: 1.2827 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.8798 - val_accuracy: 0.3750 - val_loss: 1.2809 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8549 - val_accuracy: 0.3750 - val_loss: 1.2783 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8696 - val_accuracy: 0.4167 - val_loss: 1.2737 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.8562 - val_accuracy: 0.4167 - val_loss: 1.2690 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 57ms/step - accuracy: 0.7321 - loss: 0.8569 - val_accuracy: 0.3750 - val_loss: 1.2648 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8223 - val_accuracy: 0.3750 - val_loss: 1.2639 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8214 - val_accuracy: 0.3333 - val_loss: 1.2590 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7805 - val_accuracy: 0.3333 - val_loss: 1.2574 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.7954 - val_accuracy: 0.3333 - val_loss: 1.2570 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7822 - val_accuracy: 0.3333 - val_loss: 1.2444 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7671 - val_accuracy: 0.3333 - val_loss: 1.2505 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7812 - val_accuracy: 0.3750 - val_loss: 1.2571 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.7556 - val_accuracy: 0.3333 - val_loss: 1.2473 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 42ms/step - accuracy: 0.7946 - loss: 0.7564 - val_accuracy: 0.3750 - val_loss: 1.2554 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 57ms/step - accuracy: 0.8036 - loss: 0.7180 - val_accuracy: 0.3750 - val_loss: 1.2432 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 57ms/step - accuracy: 0.8304 - loss: 0.7254 - val_accuracy: 0.4167 - val_loss: 1.2427 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 42ms/step - accuracy: 0.7857 - loss: 0.7418 - val_accuracy: 0.4583 - val_loss: 1.2446 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7260 - val_accuracy: 0.4167 - val_loss: 1.2333 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.6913 - val_accuracy: 0.4167 - val_loss: 1.2373 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7182 - val_accuracy: 0.4167 - val_loss: 1.2310 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6954 - val_accuracy: 0.4167 - val_loss: 1.2246 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.6840 - val_accuracy: 0.4167 - val_loss: 1.2232 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6954 - val_accuracy: 0.3750 - val_loss: 1.2175 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.6618 - val_accuracy: 0.3750 - val_loss: 1.2147 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6906 - val_accuracy: 0.4167 - val_loss: 1.2231 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6711 - val_accuracy: 0.4167 - val_loss: 1.2195 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6828 - val_accuracy: 0.3750 - val_loss: 1.2233 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 60ms/step - accuracy: 0.8661 - loss: 0.6480 - val_accuracy: 0.4167 - val_loss: 1.2047 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6446 - val_accuracy: 0.3750 - val_loss: 1.2067 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6714 - val_accuracy: 0.4167 - val_loss: 1.2258 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6185 - val_accuracy: 0.4167 - val_loss: 1.2236 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6206 - val_accuracy: 0.3750 - val_loss: 1.2171 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 41ms/step - accuracy: 0.8304 - loss: 0.6128 - val_accuracy: 0.3750 - val_loss: 1.2171 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5990 - val_accuracy: 0.3750 - val_loss: 1.2148 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5996 - val_accuracy: 0.4583 - val_loss: 1.2112 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 50ms/step - accuracy: 0.9018 - loss: 0.5906 - val_accuracy: 0.3333 - val_loss: 1.2371 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5843 - val_accuracy: 0.4583 - val_loss: 1.2257 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5857 - val_accuracy: 0.4167 - val_loss: 1.2278 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 41ms/step - accuracy: 0.8750 - loss: 0.5848 - val_accuracy: 0.4167 - val_loss: 1.2336 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 45ms/step - accuracy: 0.9018 - loss: 0.5837 - val_accuracy: 0.4583 - val_loss: 1.2087 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.5684 - val_accuracy: 0.4583 - val_loss: 1.2158 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 45ms/step - accuracy: 0.9018 - loss: 0.5883 - val_accuracy: 0.3333 - val_loss: 1.2382 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5382 - val_accuracy: 0.4167 - val_loss: 1.2565 - learning_rate: 0.0010
Epoch 69: early stopping
Restoring model weights from the end of the best epoch: 54.
Training complete. Best epoch: 54 of 69. Best val_loss: 1.2047, val_accuracy: 0.4167

========== Evaluation: within-subject test / EMS0011 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         1         1         0
  min_intens         5         0         0         1
  medium_int         0         1         5         0
  max_intens         0         1         3         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.444     0.667     0.533         6
   min_intensity      0.000     0.000     0.000         6
medium_intensity      0.556     0.833     0.667         6
   max_intensity      0.667     0.333     0.444         6

        accuracy                          0.458        24
       macro avg      0.417     0.458     0.411        24
    weighted avg      0.417     0.458     0.411        24

Overall accuracy: 0.4583

Artifacts saved to /kaggle/working/within_all/EMS0011/

############################################################
# Subject 12/31: EMS0012
############################################################
Loaded EMS0012 from /kaggle/input/datasets/akablawi/ems-4class/EMS0012.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.63e-03, 2.73e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-2.16e-06, 5.13e-06]
  Per-channel std range:  [1.12e-05, 2.68e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2857 - loss: 1.4410 - val_accuracy: 0.2083 - val_loss: 1.3848 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3125 - loss: 1.3543 - val_accuracy: 0.5000 - val_loss: 1.3829 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.3571 - loss: 1.3481 - val_accuracy: 0.4167 - val_loss: 1.3799 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.3929 - loss: 1.3106 - val_accuracy: 0.4167 - val_loss: 1.3768 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.3661 - loss: 1.3124 - val_accuracy: 0.4583 - val_loss: 1.3729 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.4196 - loss: 1.2780 - val_accuracy: 0.4583 - val_loss: 1.3687 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.3929 - loss: 1.2555 - val_accuracy: 0.4583 - val_loss: 1.3654 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.4375 - loss: 1.2306 - val_accuracy: 0.4167 - val_loss: 1.3623 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.4375 - loss: 1.2310 - val_accuracy: 0.4167 - val_loss: 1.3600 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.4732 - loss: 1.2061 - val_accuracy: 0.4167 - val_loss: 1.3582 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.4732 - loss: 1.2308 - val_accuracy: 0.4167 - val_loss: 1.3570 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.5357 - loss: 1.1776 - val_accuracy: 0.4167 - val_loss: 1.3566 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 44ms/step - accuracy: 0.4464 - loss: 1.1870 - val_accuracy: 0.4167 - val_loss: 1.3567 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5089 - loss: 1.1649 - val_accuracy: 0.3750 - val_loss: 1.3565 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 45ms/step - accuracy: 0.5268 - loss: 1.1610 - val_accuracy: 0.3750 - val_loss: 1.3577 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 43ms/step - accuracy: 0.5179 - loss: 1.1464 - val_accuracy: 0.3333 - val_loss: 1.3596 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 42ms/step - accuracy: 0.4643 - loss: 1.1731 - val_accuracy: 0.3333 - val_loss: 1.3605 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 43ms/step - accuracy: 0.5446 - loss: 1.1150 - val_accuracy: 0.3333 - val_loss: 1.3634 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 43ms/step - accuracy: 0.5000 - loss: 1.1167 - val_accuracy: 0.3333 - val_loss: 1.3657 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 42ms/step - accuracy: 0.5357 - loss: 1.1002 - val_accuracy: 0.3750 - val_loss: 1.3622 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 43ms/step - accuracy: 0.5893 - loss: 1.0596 - val_accuracy: 0.3750 - val_loss: 1.3590 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 42ms/step - accuracy: 0.5625 - loss: 1.0883 - val_accuracy: 0.3750 - val_loss: 1.3590 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 43ms/step - accuracy: 0.5982 - loss: 1.0510 - val_accuracy: 0.3750 - val_loss: 1.3569 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.0505 - val_accuracy: 0.3750 - val_loss: 1.3552 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 43ms/step - accuracy: 0.5714 - loss: 1.0465 - val_accuracy: 0.3750 - val_loss: 1.3571 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 43ms/step - accuracy: 0.6786 - loss: 0.9877 - val_accuracy: 0.3750 - val_loss: 1.3600 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 42ms/step - accuracy: 0.6696 - loss: 0.9896 - val_accuracy: 0.4167 - val_loss: 1.3611 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.0291 - val_accuracy: 0.3750 - val_loss: 1.3524 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 0.9941 - val_accuracy: 0.4167 - val_loss: 1.3443 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 42ms/step - accuracy: 0.6607 - loss: 0.9675 - val_accuracy: 0.3750 - val_loss: 1.3494 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 42ms/step - accuracy: 0.6696 - loss: 0.9577 - val_accuracy: 0.4167 - val_loss: 1.3609 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 42ms/step - accuracy: 0.6964 - loss: 0.9563 - val_accuracy: 0.3333 - val_loss: 1.3461 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 44ms/step - accuracy: 0.7589 - loss: 0.9143 - val_accuracy: 0.4167 - val_loss: 1.3471 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.7054 - loss: 0.9445 - val_accuracy: 0.3750 - val_loss: 1.3336 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9447 - val_accuracy: 0.3333 - val_loss: 1.3324 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 44ms/step - accuracy: 0.7500 - loss: 0.8919 - val_accuracy: 0.3750 - val_loss: 1.3416 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9404 - val_accuracy: 0.4167 - val_loss: 1.3312 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 44ms/step - accuracy: 0.7232 - loss: 0.8809 - val_accuracy: 0.3333 - val_loss: 1.3358 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.7143 - loss: 0.8848 - val_accuracy: 0.4583 - val_loss: 1.3069 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8667 - val_accuracy: 0.4167 - val_loss: 1.3170 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.8627 - val_accuracy: 0.4167 - val_loss: 1.3007 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.8504 - val_accuracy: 0.4167 - val_loss: 1.3159 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 44ms/step - accuracy: 0.7143 - loss: 0.8699 - val_accuracy: 0.4583 - val_loss: 1.3126 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.8363 - val_accuracy: 0.5000 - val_loss: 1.3023 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.8161 - val_accuracy: 0.5000 - val_loss: 1.2761 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 64ms/step - accuracy: 0.7679 - loss: 0.8148 - val_accuracy: 0.5000 - val_loss: 1.2660 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 44ms/step - accuracy: 0.7857 - loss: 0.8196 - val_accuracy: 0.5000 - val_loss: 1.2761 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 43ms/step - accuracy: 0.7500 - loss: 0.8323 - val_accuracy: 0.4167 - val_loss: 1.2848 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8076 - val_accuracy: 0.4167 - val_loss: 1.2838 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7798 - val_accuracy: 0.4583 - val_loss: 1.2763 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.7820 - val_accuracy: 0.5000 - val_loss: 1.2631 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7513 - val_accuracy: 0.4583 - val_loss: 1.2572 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 44ms/step - accuracy: 0.7589 - loss: 0.7637 - val_accuracy: 0.4167 - val_loss: 1.2603 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.7722 - val_accuracy: 0.4583 - val_loss: 1.2847 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 44ms/step - accuracy: 0.7768 - loss: 0.7691 - val_accuracy: 0.5000 - val_loss: 1.2743 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 45ms/step - accuracy: 0.7857 - loss: 0.7557 - val_accuracy: 0.4167 - val_loss: 1.2780 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.7389 - val_accuracy: 0.4167 - val_loss: 1.2636 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.7278 - val_accuracy: 0.3750 - val_loss: 1.2779 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7163 - val_accuracy: 0.3750 - val_loss: 1.2740 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.7252 - val_accuracy: 0.4167 - val_loss: 1.2704 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 45ms/step - accuracy: 0.8214 - loss: 0.7503 - val_accuracy: 0.4167 - val_loss: 1.2576 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.7203 - val_accuracy: 0.4167 - val_loss: 1.2388 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7083 - val_accuracy: 0.4167 - val_loss: 1.2572 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.7252 - val_accuracy: 0.4167 - val_loss: 1.2513 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6863 - val_accuracy: 0.4167 - val_loss: 1.2671 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7238 - val_accuracy: 0.4167 - val_loss: 1.2668 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7064 - val_accuracy: 0.4167 - val_loss: 1.2598 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 57ms/step - accuracy: 0.8214 - loss: 0.6743 - val_accuracy: 0.3750 - val_loss: 1.2373 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7003 - val_accuracy: 0.3750 - val_loss: 1.2562 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6987 - val_accuracy: 0.4167 - val_loss: 1.2424 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7006 - val_accuracy: 0.4167 - val_loss: 1.2311 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6733 - val_accuracy: 0.4167 - val_loss: 1.2341 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 44ms/step - accuracy: 0.8036 - loss: 0.6609 - val_accuracy: 0.3750 - val_loss: 1.2771 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7094 - val_accuracy: 0.4167 - val_loss: 1.2372 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6369 - val_accuracy: 0.3750 - val_loss: 1.2657 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.6805 - val_accuracy: 0.5000 - val_loss: 1.2212 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6397 - val_accuracy: 0.4167 - val_loss: 1.2722 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6886 - val_accuracy: 0.5417 - val_loss: 1.2173 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6521 - val_accuracy: 0.4167 - val_loss: 1.2271 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 45ms/step - accuracy: 0.8393 - loss: 0.6717 - val_accuracy: 0.4583 - val_loss: 1.2276 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6480 - val_accuracy: 0.4583 - val_loss: 1.2265 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.6281 - val_accuracy: 0.4583 - val_loss: 1.2170 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.6523 - val_accuracy: 0.4583 - val_loss: 1.2271 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6133 - val_accuracy: 0.4583 - val_loss: 1.2327 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5919 - val_accuracy: 0.4167 - val_loss: 1.2286 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5981 - val_accuracy: 0.4583 - val_loss: 1.2162 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5992 - val_accuracy: 0.4167 - val_loss: 1.2347 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6095 - val_accuracy: 0.4583 - val_loss: 1.2301 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5726 - val_accuracy: 0.4583 - val_loss: 1.2352 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6453 - val_accuracy: 0.5417 - val_loss: 1.1913 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.6230 - val_accuracy: 0.4167 - val_loss: 1.2183 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6295 - val_accuracy: 0.5417 - val_loss: 1.2103 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 45ms/step - accuracy: 0.8393 - loss: 0.6111 - val_accuracy: 0.4167 - val_loss: 1.2375 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.6741 - val_accuracy: 0.5417 - val_loss: 1.2032 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.5881 - val_accuracy: 0.4583 - val_loss: 1.2424 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6247 - val_accuracy: 0.4583 - val_loss: 1.2631 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6102 - val_accuracy: 0.3750 - val_loss: 1.2595 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.5714 - val_accuracy: 0.4167 - val_loss: 1.2382 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5634 - val_accuracy: 0.3750 - val_loss: 1.2361 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 46ms/step - accuracy: 0.8661 - loss: 0.5852 - val_accuracy: 0.3750 - val_loss: 1.2458 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5761 - val_accuracy: 0.4583 - val_loss: 1.2187 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5930 - val_accuracy: 0.3750 - val_loss: 1.2981 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5787 - val_accuracy: 0.4583 - val_loss: 1.2986 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.5823 - val_accuracy: 0.4167 - val_loss: 1.2859 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6118 - val_accuracy: 0.5417 - val_loss: 1.1951 - learning_rate: 0.0010
Epoch 105: early stopping
Restoring model weights from the end of the best epoch: 90.
Training complete. Best epoch: 90 of 105. Best val_loss: 1.1913, val_accuracy: 0.5417

========== Evaluation: within-subject test / EMS0012 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         0         3         3         0
  min_intens         0         0         2         4
  medium_int         2         2         2         0
  max_intens         0         0         1         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.000     0.000     0.000         6
   min_intensity      0.000     0.000     0.000         6
medium_intensity      0.250     0.333     0.286         6
   max_intensity      0.556     0.833     0.667         6

        accuracy                          0.292        24
       macro avg      0.201     0.292     0.238        24
    weighted avg      0.201     0.292     0.238        24

Overall accuracy: 0.2917

Artifacts saved to /kaggle/working/within_all/EMS0012/

############################################################
# Subject 13/31: EMS0013
############################################################
Loaded EMS0013 from /kaggle/input/datasets/akablawi/ems-4class/EMS0013.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.48e-04, 3.88e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-8.62e-07, 1.40e-06]
  Per-channel std range:  [7.68e-06, 5.81e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2768 - loss: 1.4475 - val_accuracy: 0.3333 - val_loss: 1.3878 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 62ms/step - accuracy: 0.4196 - loss: 1.3114 - val_accuracy: 0.2083 - val_loss: 1.3861 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4643 - loss: 1.3012 - val_accuracy: 0.2083 - val_loss: 1.3842 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4107 - loss: 1.2974 - val_accuracy: 0.2500 - val_loss: 1.3815 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 58ms/step - accuracy: 0.4464 - loss: 1.2413 - val_accuracy: 0.2500 - val_loss: 1.3786 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.4911 - loss: 1.2052 - val_accuracy: 0.2500 - val_loss: 1.3757 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5000 - loss: 1.1857 - val_accuracy: 0.2917 - val_loss: 1.3725 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.1603 - val_accuracy: 0.2917 - val_loss: 1.3695 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 60ms/step - accuracy: 0.4554 - loss: 1.1556 - val_accuracy: 0.2917 - val_loss: 1.3663 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.5446 - loss: 1.1255 - val_accuracy: 0.2917 - val_loss: 1.3633 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.0574 - val_accuracy: 0.2917 - val_loss: 1.3596 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.0672 - val_accuracy: 0.2917 - val_loss: 1.3546 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.6250 - loss: 1.0308 - val_accuracy: 0.2917 - val_loss: 1.3492 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 1.0353 - val_accuracy: 0.2917 - val_loss: 1.3420 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6607 - loss: 0.9917 - val_accuracy: 0.2917 - val_loss: 1.3342 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9784 - val_accuracy: 0.2917 - val_loss: 1.3285 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9562 - val_accuracy: 0.3750 - val_loss: 1.3200 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.9261 - val_accuracy: 0.3750 - val_loss: 1.3116 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9324 - val_accuracy: 0.4167 - val_loss: 1.2997 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9032 - val_accuracy: 0.4167 - val_loss: 1.2915 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8881 - val_accuracy: 0.4167 - val_loss: 1.2875 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.8794 - val_accuracy: 0.4583 - val_loss: 1.2782 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.8524 - val_accuracy: 0.4583 - val_loss: 1.2664 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 57ms/step - accuracy: 0.7679 - loss: 0.8259 - val_accuracy: 0.5000 - val_loss: 1.2599 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.8257 - val_accuracy: 0.4583 - val_loss: 1.2499 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8120 - val_accuracy: 0.4167 - val_loss: 1.2404 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 57ms/step - accuracy: 0.7946 - loss: 0.7786 - val_accuracy: 0.4583 - val_loss: 1.2390 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 60ms/step - accuracy: 0.8304 - loss: 0.7665 - val_accuracy: 0.4583 - val_loss: 1.2279 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7813 - val_accuracy: 0.5000 - val_loss: 1.2204 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.7502 - val_accuracy: 0.5417 - val_loss: 1.2171 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 60ms/step - accuracy: 0.8304 - loss: 0.7384 - val_accuracy: 0.5000 - val_loss: 1.1951 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.7407 - val_accuracy: 0.5000 - val_loss: 1.1845 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7369 - val_accuracy: 0.5417 - val_loss: 1.1893 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7021 - val_accuracy: 0.5417 - val_loss: 1.1867 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.7159 - val_accuracy: 0.5417 - val_loss: 1.1726 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.7065 - val_accuracy: 0.5417 - val_loss: 1.1658 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7193 - val_accuracy: 0.5417 - val_loss: 1.1729 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 62ms/step - accuracy: 0.8750 - loss: 0.6407 - val_accuracy: 0.5417 - val_loss: 1.1636 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6910 - val_accuracy: 0.5417 - val_loss: 1.1445 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6840 - val_accuracy: 0.5000 - val_loss: 1.1422 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6738 - val_accuracy: 0.5417 - val_loss: 1.1383 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6397 - val_accuracy: 0.5417 - val_loss: 1.1342 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6527 - val_accuracy: 0.5417 - val_loss: 1.1225 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6621 - val_accuracy: 0.5833 - val_loss: 1.1211 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6354 - val_accuracy: 0.5417 - val_loss: 1.1268 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6299 - val_accuracy: 0.5417 - val_loss: 1.1248 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6347 - val_accuracy: 0.5833 - val_loss: 1.1163 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.5906 - val_accuracy: 0.5833 - val_loss: 1.1089 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 57ms/step - accuracy: 0.8750 - loss: 0.6166 - val_accuracy: 0.5417 - val_loss: 1.0958 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6018 - val_accuracy: 0.5417 - val_loss: 1.1033 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5818 - val_accuracy: 0.5417 - val_loss: 1.1008 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5972 - val_accuracy: 0.5417 - val_loss: 1.0906 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5921 - val_accuracy: 0.5833 - val_loss: 1.0937 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5743 - val_accuracy: 0.5833 - val_loss: 1.0924 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.5645 - val_accuracy: 0.5417 - val_loss: 1.0756 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6148 - val_accuracy: 0.5417 - val_loss: 1.0783 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5509 - val_accuracy: 0.5833 - val_loss: 1.0840 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 57ms/step - accuracy: 0.9286 - loss: 0.5700 - val_accuracy: 0.5417 - val_loss: 1.0741 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5646 - val_accuracy: 0.5417 - val_loss: 1.0799 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5273 - val_accuracy: 0.5417 - val_loss: 1.0609 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.5485 - val_accuracy: 0.5417 - val_loss: 1.0589 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5208 - val_accuracy: 0.5833 - val_loss: 1.0617 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.5379 - val_accuracy: 0.5833 - val_loss: 1.0517 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5347 - val_accuracy: 0.5417 - val_loss: 1.0553 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5317 - val_accuracy: 0.5833 - val_loss: 1.0670 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 58ms/step - accuracy: 0.9286 - loss: 0.5037 - val_accuracy: 0.5417 - val_loss: 1.0416 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 60ms/step - accuracy: 0.8750 - loss: 0.5397 - val_accuracy: 0.5417 - val_loss: 1.0385 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.5343 - val_accuracy: 0.5833 - val_loss: 1.0452 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.4973 - val_accuracy: 0.5833 - val_loss: 1.0369 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4846 - val_accuracy: 0.6250 - val_loss: 1.0374 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 57ms/step - accuracy: 0.9107 - loss: 0.4862 - val_accuracy: 0.5833 - val_loss: 1.0304 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.4964 - val_accuracy: 0.5833 - val_loss: 1.0392 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5049 - val_accuracy: 0.5833 - val_loss: 1.0276 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 41ms/step - accuracy: 0.9018 - loss: 0.5084 - val_accuracy: 0.5833 - val_loss: 1.0327 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4804 - val_accuracy: 0.5417 - val_loss: 1.0553 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 55ms/step - accuracy: 0.9375 - loss: 0.4914 - val_accuracy: 0.6667 - val_loss: 1.0031 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 57ms/step - accuracy: 0.9375 - loss: 0.4928 - val_accuracy: 0.6667 - val_loss: 0.9920 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.4658 - val_accuracy: 0.5833 - val_loss: 1.0256 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4653 - val_accuracy: 0.6667 - val_loss: 1.0162 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.4647 - val_accuracy: 0.5833 - val_loss: 1.0099 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4650 - val_accuracy: 0.5833 - val_loss: 1.0195 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.4604 - val_accuracy: 0.6250 - val_loss: 0.9773 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 57ms/step - accuracy: 0.9286 - loss: 0.4703 - val_accuracy: 0.6250 - val_loss: 0.9767 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 55ms/step - accuracy: 0.9018 - loss: 0.4678 - val_accuracy: 0.6667 - val_loss: 0.9740 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.4502 - val_accuracy: 0.6667 - val_loss: 0.9675 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 64ms/step - accuracy: 0.9464 - loss: 0.4634 - val_accuracy: 0.6250 - val_loss: 0.9655 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.4434 - val_accuracy: 0.6250 - val_loss: 1.0067 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4521 - val_accuracy: 0.6250 - val_loss: 0.9931 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4270 - val_accuracy: 0.5833 - val_loss: 0.9887 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4303 - val_accuracy: 0.6250 - val_loss: 0.9805 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 45ms/step - accuracy: 0.9464 - loss: 0.4242 - val_accuracy: 0.6667 - val_loss: 0.9742 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 58ms/step - accuracy: 0.9732 - loss: 0.4010 - val_accuracy: 0.7083 - val_loss: 0.9539 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.4111 - val_accuracy: 0.7083 - val_loss: 0.9465 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4226 - val_accuracy: 0.6250 - val_loss: 0.9733 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4172 - val_accuracy: 0.6250 - val_loss: 0.9676 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4247 - val_accuracy: 0.5833 - val_loss: 0.9467 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 57ms/step - accuracy: 0.9375 - loss: 0.4390 - val_accuracy: 0.6667 - val_loss: 0.9199 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4046 - val_accuracy: 0.5833 - val_loss: 0.9512 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4162 - val_accuracy: 0.6250 - val_loss: 0.9423 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.4309 - val_accuracy: 0.7083 - val_loss: 0.9193 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4112 - val_accuracy: 0.7083 - val_loss: 0.9288 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4020 - val_accuracy: 0.6667 - val_loss: 0.9345 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.3927 - val_accuracy: 0.6250 - val_loss: 0.9404 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3963 - val_accuracy: 0.5833 - val_loss: 0.9443 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.4058 - val_accuracy: 0.6250 - val_loss: 0.9425 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3961 - val_accuracy: 0.5833 - val_loss: 0.9648 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.3988 - val_accuracy: 0.6250 - val_loss: 0.9249 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 58ms/step - accuracy: 0.9464 - loss: 0.4030 - val_accuracy: 0.6250 - val_loss: 0.9188 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3822 - val_accuracy: 0.6667 - val_loss: 0.9404 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3704 - val_accuracy: 0.6667 - val_loss: 0.9344 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 58ms/step - accuracy: 0.9554 - loss: 0.3799 - val_accuracy: 0.6667 - val_loss: 0.9127 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.3797 - val_accuracy: 0.5833 - val_loss: 0.9578 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3687 - val_accuracy: 0.6667 - val_loss: 0.9265 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.3738 - val_accuracy: 0.6250 - val_loss: 0.9085 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.3727 - val_accuracy: 0.5833 - val_loss: 0.9279 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3612 - val_accuracy: 0.6667 - val_loss: 0.9506 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.3626 - val_accuracy: 0.6250 - val_loss: 0.9491 - learning_rate: 0.0010
Epoch 118/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.3555 - val_accuracy: 0.6667 - val_loss: 0.9060 - learning_rate: 0.0010
Epoch 119/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3611 - val_accuracy: 0.6667 - val_loss: 0.9083 - learning_rate: 0.0010
Epoch 120/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3471 - val_accuracy: 0.6250 - val_loss: 0.9133 - learning_rate: 0.0010
Epoch 121/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3553 - val_accuracy: 0.6667 - val_loss: 0.9356 - learning_rate: 0.0010
Epoch 122/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3549 - val_accuracy: 0.6250 - val_loss: 0.9381 - learning_rate: 0.0010
Epoch 123/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3669 - val_accuracy: 0.6250 - val_loss: 0.9336 - learning_rate: 0.0010
Epoch 124/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3371 - val_accuracy: 0.6667 - val_loss: 0.9355 - learning_rate: 0.0010
Epoch 125/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3577 - val_accuracy: 0.7083 - val_loss: 0.9227 - learning_rate: 0.0010
Epoch 126/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.3293 - val_accuracy: 0.6250 - val_loss: 0.9107 - learning_rate: 0.0010
Epoch 127/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3384 - val_accuracy: 0.7083 - val_loss: 0.9073 - learning_rate: 0.0010
Epoch 128/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3601 - val_accuracy: 0.7083 - val_loss: 0.9162 - learning_rate: 0.0010
Epoch 129/500
4/4 - 0s - 56ms/step - accuracy: 0.9821 - loss: 0.3106 - val_accuracy: 0.6667 - val_loss: 0.8964 - learning_rate: 0.0010
Epoch 130/500
4/4 - 0s - 58ms/step - accuracy: 0.9732 - loss: 0.3343 - val_accuracy: 0.6667 - val_loss: 0.8856 - learning_rate: 0.0010
Epoch 131/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3495 - val_accuracy: 0.6667 - val_loss: 0.9017 - learning_rate: 0.0010
Epoch 132/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3606 - val_accuracy: 0.5833 - val_loss: 0.9133 - learning_rate: 0.0010
Epoch 133/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3193 - val_accuracy: 0.5833 - val_loss: 0.9464 - learning_rate: 0.0010
Epoch 134/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.3168 - val_accuracy: 0.6667 - val_loss: 0.9143 - learning_rate: 0.0010
Epoch 135/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3274 - val_accuracy: 0.6667 - val_loss: 0.8879 - learning_rate: 0.0010
Epoch 136/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.3330 - val_accuracy: 0.7500 - val_loss: 0.8762 - learning_rate: 0.0010
Epoch 137/500
4/4 - 0s - 56ms/step - accuracy: 0.9732 - loss: 0.3122 - val_accuracy: 0.6667 - val_loss: 0.8758 - learning_rate: 0.0010
Epoch 138/500
4/4 - 0s - 41ms/step - accuracy: 0.9732 - loss: 0.3179 - val_accuracy: 0.6250 - val_loss: 0.9051 - learning_rate: 0.0010
Epoch 139/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3250 - val_accuracy: 0.6250 - val_loss: 0.9322 - learning_rate: 0.0010
Epoch 140/500
4/4 - 0s - 46ms/step - accuracy: 0.9821 - loss: 0.3330 - val_accuracy: 0.6250 - val_loss: 0.8857 - learning_rate: 0.0010
Epoch 141/500
4/4 - 0s - 41ms/step - accuracy: 0.9643 - loss: 0.3025 - val_accuracy: 0.6667 - val_loss: 0.8972 - learning_rate: 0.0010
Epoch 142/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.3163 - val_accuracy: 0.5833 - val_loss: 0.8712 - learning_rate: 0.0010
Epoch 143/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.3415 - val_accuracy: 0.6667 - val_loss: 0.8597 - learning_rate: 0.0010
Epoch 144/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.3034 - val_accuracy: 0.6250 - val_loss: 0.9176 - learning_rate: 0.0010
Epoch 145/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.2926 - val_accuracy: 0.6667 - val_loss: 0.9075 - learning_rate: 0.0010
Epoch 146/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.2957 - val_accuracy: 0.5833 - val_loss: 0.9342 - learning_rate: 0.0010
Epoch 147/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3274 - val_accuracy: 0.5417 - val_loss: 0.9532 - learning_rate: 0.0010
Epoch 148/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.3110 - val_accuracy: 0.6250 - val_loss: 0.9347 - learning_rate: 0.0010
Epoch 149/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.2880 - val_accuracy: 0.6250 - val_loss: 0.9414 - learning_rate: 0.0010
Epoch 150/500
4/4 - 0s - 43ms/step - accuracy: 1.0000 - loss: 0.2710 - val_accuracy: 0.6667 - val_loss: 0.9105 - learning_rate: 0.0010
Epoch 151/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.3018 - val_accuracy: 0.6250 - val_loss: 0.9399 - learning_rate: 0.0010
Epoch 152/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.2835 - val_accuracy: 0.6667 - val_loss: 0.9049 - learning_rate: 0.0010
Epoch 153/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.2963 - val_accuracy: 0.6667 - val_loss: 0.9463 - learning_rate: 0.0010
Epoch 154/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.2911 - val_accuracy: 0.6667 - val_loss: 0.9508 - learning_rate: 0.0010
Epoch 155/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.2912 - val_accuracy: 0.6250 - val_loss: 0.9001 - learning_rate: 0.0010
Epoch 156/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3004 - val_accuracy: 0.6250 - val_loss: 0.9385 - learning_rate: 0.0010
Epoch 157/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3190 - val_accuracy: 0.5833 - val_loss: 0.9694 - learning_rate: 0.0010
Epoch 158/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.2753 - val_accuracy: 0.6667 - val_loss: 0.9277 - learning_rate: 0.0010
Epoch 158: early stopping
Restoring model weights from the end of the best epoch: 143.
Training complete. Best epoch: 143 of 158. Best val_loss: 0.8597, val_accuracy: 0.6667

========== Evaluation: within-subject test / EMS0013 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         0         4         0
  min_intens         0         5         1         0
  medium_int         0         0         6         0
  max_intens         0         0         1         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      1.000     0.333     0.500         6
   min_intensity      1.000     0.833     0.909         6
medium_intensity      0.500     1.000     0.667         6
   max_intensity      1.000     0.833     0.909         6

        accuracy                          0.750        24
       macro avg      0.875     0.750     0.746        24
    weighted avg      0.875     0.750     0.746        24

Overall accuracy: 0.7500

Artifacts saved to /kaggle/working/within_all/EMS0013/

############################################################
# Subject 14/31: EMS0014
############################################################
Loaded EMS0014 from /kaggle/input/datasets/akablawi/ems-4class/EMS0014.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.80e-04, 6.90e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.89e-06, 3.02e-06]
  Per-channel std range:  [6.36e-06, 1.02e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.1964 - loss: 1.5253 - val_accuracy: 0.2917 - val_loss: 1.3820 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.3125 - loss: 1.3649 - val_accuracy: 0.3333 - val_loss: 1.3795 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4286 - loss: 1.3248 - val_accuracy: 0.3333 - val_loss: 1.3777 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4196 - loss: 1.3147 - val_accuracy: 0.3750 - val_loss: 1.3756 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4643 - loss: 1.2900 - val_accuracy: 0.2917 - val_loss: 1.3733 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.4643 - loss: 1.2804 - val_accuracy: 0.2917 - val_loss: 1.3703 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.4911 - loss: 1.2669 - val_accuracy: 0.3333 - val_loss: 1.3675 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.5000 - loss: 1.2091 - val_accuracy: 0.3333 - val_loss: 1.3645 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 60ms/step - accuracy: 0.5179 - loss: 1.2021 - val_accuracy: 0.3333 - val_loss: 1.3610 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 60ms/step - accuracy: 0.5714 - loss: 1.1899 - val_accuracy: 0.4167 - val_loss: 1.3556 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 62ms/step - accuracy: 0.5268 - loss: 1.1713 - val_accuracy: 0.4167 - val_loss: 1.3480 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 64ms/step - accuracy: 0.5982 - loss: 1.1597 - val_accuracy: 0.4167 - val_loss: 1.3407 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 63ms/step - accuracy: 0.5179 - loss: 1.1527 - val_accuracy: 0.4167 - val_loss: 1.3357 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 63ms/step - accuracy: 0.5893 - loss: 1.1078 - val_accuracy: 0.5000 - val_loss: 1.3300 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.1135 - val_accuracy: 0.5000 - val_loss: 1.3217 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 58ms/step - accuracy: 0.5625 - loss: 1.0890 - val_accuracy: 0.5000 - val_loss: 1.3142 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 1.0692 - val_accuracy: 0.5417 - val_loss: 1.3067 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0605 - val_accuracy: 0.5417 - val_loss: 1.2975 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.5893 - loss: 1.0674 - val_accuracy: 0.5417 - val_loss: 1.2888 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.0280 - val_accuracy: 0.5833 - val_loss: 1.2799 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0055 - val_accuracy: 0.5000 - val_loss: 1.2701 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 0.9988 - val_accuracy: 0.5833 - val_loss: 1.2616 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 0.9867 - val_accuracy: 0.5833 - val_loss: 1.2523 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 60ms/step - accuracy: 0.6607 - loss: 0.9820 - val_accuracy: 0.5833 - val_loss: 1.2458 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9557 - val_accuracy: 0.6250 - val_loss: 1.2380 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 64ms/step - accuracy: 0.6429 - loss: 0.9615 - val_accuracy: 0.5417 - val_loss: 1.2278 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 0.9531 - val_accuracy: 0.5000 - val_loss: 1.2192 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9326 - val_accuracy: 0.5417 - val_loss: 1.2109 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.9198 - val_accuracy: 0.4583 - val_loss: 1.2081 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.6875 - loss: 0.9115 - val_accuracy: 0.5000 - val_loss: 1.2125 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8881 - val_accuracy: 0.5000 - val_loss: 1.2023 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.8733 - val_accuracy: 0.4583 - val_loss: 1.1948 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8823 - val_accuracy: 0.4583 - val_loss: 1.1867 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8449 - val_accuracy: 0.4583 - val_loss: 1.1825 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8610 - val_accuracy: 0.5000 - val_loss: 1.1745 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8416 - val_accuracy: 0.5000 - val_loss: 1.1700 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8004 - val_accuracy: 0.5000 - val_loss: 1.1698 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8316 - val_accuracy: 0.4583 - val_loss: 1.1596 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.7500 - loss: 0.8194 - val_accuracy: 0.5000 - val_loss: 1.1630 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 60ms/step - accuracy: 0.7768 - loss: 0.8128 - val_accuracy: 0.4583 - val_loss: 1.1502 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.7954 - val_accuracy: 0.4583 - val_loss: 1.1431 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 44ms/step - accuracy: 0.6607 - loss: 0.8546 - val_accuracy: 0.4583 - val_loss: 1.1435 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 57ms/step - accuracy: 0.7054 - loss: 0.8328 - val_accuracy: 0.5000 - val_loss: 1.1386 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.7942 - val_accuracy: 0.5000 - val_loss: 1.1412 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.7663 - val_accuracy: 0.5000 - val_loss: 1.1372 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 61ms/step - accuracy: 0.7589 - loss: 0.7848 - val_accuracy: 0.4583 - val_loss: 1.1274 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7883 - val_accuracy: 0.4583 - val_loss: 1.1352 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 44ms/step - accuracy: 0.8304 - loss: 0.7552 - val_accuracy: 0.4583 - val_loss: 1.1362 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.7592 - val_accuracy: 0.5000 - val_loss: 1.1372 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.7188 - val_accuracy: 0.5417 - val_loss: 1.1331 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.7309 - val_accuracy: 0.5417 - val_loss: 1.1255 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.7506 - val_accuracy: 0.5000 - val_loss: 1.1031 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7402 - val_accuracy: 0.5000 - val_loss: 1.1003 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 60ms/step - accuracy: 0.7679 - loss: 0.7220 - val_accuracy: 0.5417 - val_loss: 1.0961 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7293 - val_accuracy: 0.5000 - val_loss: 1.0974 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.6932 - val_accuracy: 0.5417 - val_loss: 1.1029 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 42ms/step - accuracy: 0.7946 - loss: 0.7222 - val_accuracy: 0.5000 - val_loss: 1.0969 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 57ms/step - accuracy: 0.8304 - loss: 0.6958 - val_accuracy: 0.4583 - val_loss: 1.0920 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.7080 - val_accuracy: 0.5417 - val_loss: 1.0890 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.6833 - val_accuracy: 0.5417 - val_loss: 1.1040 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 41ms/step - accuracy: 0.8304 - loss: 0.6767 - val_accuracy: 0.5417 - val_loss: 1.1020 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 57ms/step - accuracy: 0.8304 - loss: 0.6973 - val_accuracy: 0.5000 - val_loss: 1.0833 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 56ms/step - accuracy: 0.8036 - loss: 0.6947 - val_accuracy: 0.5833 - val_loss: 1.0737 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 41ms/step - accuracy: 0.8304 - loss: 0.6733 - val_accuracy: 0.5833 - val_loss: 1.0962 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 41ms/step - accuracy: 0.8304 - loss: 0.6675 - val_accuracy: 0.5833 - val_loss: 1.0873 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 56ms/step - accuracy: 0.8125 - loss: 0.6762 - val_accuracy: 0.5000 - val_loss: 1.0717 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 56ms/step - accuracy: 0.8304 - loss: 0.6583 - val_accuracy: 0.5417 - val_loss: 1.0717 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 57ms/step - accuracy: 0.8482 - loss: 0.6628 - val_accuracy: 0.5000 - val_loss: 1.0710 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 56ms/step - accuracy: 0.8304 - loss: 0.6581 - val_accuracy: 0.4167 - val_loss: 1.0614 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.6306 - val_accuracy: 0.5000 - val_loss: 1.0681 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 57ms/step - accuracy: 0.8839 - loss: 0.6297 - val_accuracy: 0.4583 - val_loss: 1.0549 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 40ms/step - accuracy: 0.8482 - loss: 0.6109 - val_accuracy: 0.4583 - val_loss: 1.0807 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6535 - val_accuracy: 0.5000 - val_loss: 1.0911 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.6224 - val_accuracy: 0.5000 - val_loss: 1.0477 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.6260 - val_accuracy: 0.5000 - val_loss: 1.0583 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6274 - val_accuracy: 0.5417 - val_loss: 1.0685 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 56ms/step - accuracy: 0.8482 - loss: 0.6182 - val_accuracy: 0.5417 - val_loss: 1.0430 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 57ms/step - accuracy: 0.8393 - loss: 0.6157 - val_accuracy: 0.5417 - val_loss: 1.0360 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.6161 - val_accuracy: 0.5417 - val_loss: 1.0436 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 57ms/step - accuracy: 0.8571 - loss: 0.5845 - val_accuracy: 0.6250 - val_loss: 1.0358 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5910 - val_accuracy: 0.5833 - val_loss: 1.0329 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.6047 - val_accuracy: 0.5833 - val_loss: 1.0370 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.5747 - val_accuracy: 0.5833 - val_loss: 1.0441 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5655 - val_accuracy: 0.5417 - val_loss: 1.0440 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5466 - val_accuracy: 0.6250 - val_loss: 1.0557 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.5461 - val_accuracy: 0.5000 - val_loss: 1.0387 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6013 - val_accuracy: 0.5833 - val_loss: 1.0534 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 41ms/step - accuracy: 0.8482 - loss: 0.5811 - val_accuracy: 0.5417 - val_loss: 1.0418 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 57ms/step - accuracy: 0.8929 - loss: 0.5613 - val_accuracy: 0.5000 - val_loss: 1.0006 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5462 - val_accuracy: 0.5833 - val_loss: 1.0119 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5364 - val_accuracy: 0.5417 - val_loss: 1.0579 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5204 - val_accuracy: 0.5417 - val_loss: 1.0424 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 41ms/step - accuracy: 0.8750 - loss: 0.5425 - val_accuracy: 0.5833 - val_loss: 1.0099 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 56ms/step - accuracy: 0.9018 - loss: 0.5151 - val_accuracy: 0.6250 - val_loss: 0.9967 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5358 - val_accuracy: 0.5833 - val_loss: 1.0093 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5139 - val_accuracy: 0.5833 - val_loss: 1.0176 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.5198 - val_accuracy: 0.5833 - val_loss: 1.0243 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.5177 - val_accuracy: 0.5417 - val_loss: 1.0228 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 57ms/step - accuracy: 0.8929 - loss: 0.5347 - val_accuracy: 0.5833 - val_loss: 0.9894 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 41ms/step - accuracy: 0.9196 - loss: 0.5281 - val_accuracy: 0.5833 - val_loss: 1.0011 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5315 - val_accuracy: 0.5417 - val_loss: 1.0321 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 57ms/step - accuracy: 0.8929 - loss: 0.5391 - val_accuracy: 0.5417 - val_loss: 0.9858 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 41ms/step - accuracy: 0.8929 - loss: 0.5137 - val_accuracy: 0.5833 - val_loss: 1.0154 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 40ms/step - accuracy: 0.9018 - loss: 0.5109 - val_accuracy: 0.5417 - val_loss: 0.9934 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 55ms/step - accuracy: 0.9286 - loss: 0.4971 - val_accuracy: 0.5417 - val_loss: 0.9588 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.4664 - val_accuracy: 0.5417 - val_loss: 0.9728 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.4871 - val_accuracy: 0.5000 - val_loss: 1.0325 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 40ms/step - accuracy: 0.8750 - loss: 0.4974 - val_accuracy: 0.6250 - val_loss: 0.9670 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 40ms/step - accuracy: 0.8929 - loss: 0.5183 - val_accuracy: 0.5417 - val_loss: 1.0038 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 40ms/step - accuracy: 0.9196 - loss: 0.4813 - val_accuracy: 0.5833 - val_loss: 0.9902 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.4682 - val_accuracy: 0.5833 - val_loss: 0.9704 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 41ms/step - accuracy: 0.9196 - loss: 0.4600 - val_accuracy: 0.5417 - val_loss: 1.0578 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.4875 - val_accuracy: 0.5417 - val_loss: 0.9931 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 40ms/step - accuracy: 0.9196 - loss: 0.4573 - val_accuracy: 0.5417 - val_loss: 0.9891 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 40ms/step - accuracy: 0.9107 - loss: 0.4450 - val_accuracy: 0.5000 - val_loss: 1.0235 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 40ms/step - accuracy: 0.9196 - loss: 0.4664 - val_accuracy: 0.5417 - val_loss: 1.0177 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 40ms/step - accuracy: 0.9554 - loss: 0.4505 - val_accuracy: 0.5000 - val_loss: 0.9869 - learning_rate: 0.0010
Epoch 118/500
4/4 - 0s - 40ms/step - accuracy: 0.9107 - loss: 0.4604 - val_accuracy: 0.5417 - val_loss: 1.0136 - learning_rate: 0.0010
Epoch 119/500
4/4 - 0s - 40ms/step - accuracy: 0.9196 - loss: 0.4631 - val_accuracy: 0.5000 - val_loss: 1.0210 - learning_rate: 0.0010
Epoch 120/500
4/4 - 0s - 39ms/step - accuracy: 0.9286 - loss: 0.4643 - val_accuracy: 0.5417 - val_loss: 1.0074 - learning_rate: 0.0010
Epoch 120: early stopping
Restoring model weights from the end of the best epoch: 105.
Training complete. Best epoch: 105 of 120. Best val_loss: 0.9588, val_accuracy: 0.5417

========== Evaluation: within-subject test / EMS0014 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         5         0         0         1
  min_intens         3         1         2         0
  medium_int         0         1         2         3
  max_intens         1         0         3         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.556     0.833     0.667         6
   min_intensity      0.500     0.167     0.250         6
medium_intensity      0.286     0.333     0.308         6
   max_intensity      0.333     0.333     0.333         6

        accuracy                          0.417        24
       macro avg      0.419     0.417     0.389        24
    weighted avg      0.419     0.417     0.389        24

Overall accuracy: 0.4167

Artifacts saved to /kaggle/working/within_all/EMS0014/

############################################################
# Subject 15/31: EMS0015
############################################################
Loaded EMS0015 from /kaggle/input/datasets/akablawi/ems-4class/EMS0015.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-4.84e-04, 4.51e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-4.50e-06, 1.06e-06]
  Per-channel std range:  [5.27e-06, 6.43e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2679 - loss: 1.4745 - val_accuracy: 0.2917 - val_loss: 1.3859 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 44ms/step - accuracy: 0.3393 - loss: 1.3681 - val_accuracy: 0.2917 - val_loss: 1.3884 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 44ms/step - accuracy: 0.3482 - loss: 1.3404 - val_accuracy: 0.3333 - val_loss: 1.3911 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 43ms/step - accuracy: 0.4286 - loss: 1.2958 - val_accuracy: 0.3333 - val_loss: 1.3945 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 45ms/step - accuracy: 0.4375 - loss: 1.2978 - val_accuracy: 0.3333 - val_loss: 1.3979 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 43ms/step - accuracy: 0.5000 - loss: 1.2404 - val_accuracy: 0.2500 - val_loss: 1.4022 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 46ms/step - accuracy: 0.5089 - loss: 1.2306 - val_accuracy: 0.2500 - val_loss: 1.4061 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 44ms/step - accuracy: 0.4643 - loss: 1.2151 - val_accuracy: 0.2500 - val_loss: 1.4094 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 43ms/step - accuracy: 0.4911 - loss: 1.2211 - val_accuracy: 0.2500 - val_loss: 1.4109 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 43ms/step - accuracy: 0.5982 - loss: 1.1771 - val_accuracy: 0.2083 - val_loss: 1.4097 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 42ms/step - accuracy: 0.5000 - loss: 1.1692 - val_accuracy: 0.2500 - val_loss: 1.4062 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 43ms/step - accuracy: 0.5714 - loss: 1.1421 - val_accuracy: 0.2500 - val_loss: 1.4034 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 44ms/step - accuracy: 0.5714 - loss: 1.1499 - val_accuracy: 0.2917 - val_loss: 1.4032 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 43ms/step - accuracy: 0.5893 - loss: 1.0877 - val_accuracy: 0.3333 - val_loss: 1.4029 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 43ms/step - accuracy: 0.5893 - loss: 1.1030 - val_accuracy: 0.4167 - val_loss: 1.4032 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 43ms/step - accuracy: 0.6071 - loss: 1.0743 - val_accuracy: 0.4167 - val_loss: 1.3995 - learning_rate: 0.0010
Epoch 16: early stopping
Restoring model weights from the end of the best epoch: 1.
Training complete. Best epoch: 1 of 16. Best val_loss: 1.3859, val_accuracy: 0.2917

========== Evaluation: within-subject test / EMS0015 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         1         0         3         2
  min_intens         2         1         2         1
  medium_int         1         1         3         1
  max_intens         1         1         2         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.200     0.167     0.182         6
   min_intensity      0.333     0.167     0.222         6
medium_intensity      0.300     0.500     0.375         6
   max_intensity      0.333     0.333     0.333         6

        accuracy                          0.292        24
       macro avg      0.292     0.292     0.278        24
    weighted avg      0.292     0.292     0.278        24

Overall accuracy: 0.2917

Artifacts saved to /kaggle/working/within_all/EMS0015/

############################################################
# Subject 16/31: EMS0016
############################################################
Loaded EMS0016 from /kaggle/input/datasets/akablawi/ems-4class/EMS0016.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-4.63e-04, 5.87e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-9.73e-07, 2.15e-06]
  Per-channel std range:  [5.35e-06, 4.65e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2321 - loss: 1.4391 - val_accuracy: 0.4583 - val_loss: 1.3821 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.4375 - loss: 1.3365 - val_accuracy: 0.4583 - val_loss: 1.3755 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4375 - loss: 1.3050 - val_accuracy: 0.3750 - val_loss: 1.3662 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.4554 - loss: 1.2769 - val_accuracy: 0.3333 - val_loss: 1.3548 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2144 - val_accuracy: 0.3750 - val_loss: 1.3433 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.4375 - loss: 1.2141 - val_accuracy: 0.4167 - val_loss: 1.3329 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5268 - loss: 1.1554 - val_accuracy: 0.4583 - val_loss: 1.3232 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.4911 - loss: 1.1550 - val_accuracy: 0.5000 - val_loss: 1.3146 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5446 - loss: 1.1139 - val_accuracy: 0.5000 - val_loss: 1.3048 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 60ms/step - accuracy: 0.5714 - loss: 1.1003 - val_accuracy: 0.5000 - val_loss: 1.2939 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.0799 - val_accuracy: 0.5833 - val_loss: 1.2837 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.0452 - val_accuracy: 0.5833 - val_loss: 1.2745 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 1.0269 - val_accuracy: 0.5833 - val_loss: 1.2662 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0175 - val_accuracy: 0.5833 - val_loss: 1.2570 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.6607 - loss: 0.9901 - val_accuracy: 0.5833 - val_loss: 1.2457 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.9682 - val_accuracy: 0.5833 - val_loss: 1.2367 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9445 - val_accuracy: 0.5833 - val_loss: 1.2290 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 60ms/step - accuracy: 0.6964 - loss: 0.8946 - val_accuracy: 0.5417 - val_loss: 1.2210 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8993 - val_accuracy: 0.5000 - val_loss: 1.2168 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.8625 - val_accuracy: 0.5000 - val_loss: 1.2139 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9017 - val_accuracy: 0.5000 - val_loss: 1.2107 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.7232 - loss: 0.8555 - val_accuracy: 0.5000 - val_loss: 1.2078 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8422 - val_accuracy: 0.5000 - val_loss: 1.2034 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8611 - val_accuracy: 0.5000 - val_loss: 1.2003 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8163 - val_accuracy: 0.5000 - val_loss: 1.1985 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8250 - val_accuracy: 0.5000 - val_loss: 1.1951 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.7956 - val_accuracy: 0.5000 - val_loss: 1.1912 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 44ms/step - accuracy: 0.7589 - loss: 0.7960 - val_accuracy: 0.5000 - val_loss: 1.1914 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7713 - val_accuracy: 0.5000 - val_loss: 1.1943 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.7740 - val_accuracy: 0.5000 - val_loss: 1.1956 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.7374 - val_accuracy: 0.4583 - val_loss: 1.1977 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7012 - val_accuracy: 0.4583 - val_loss: 1.2031 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7409 - val_accuracy: 0.4583 - val_loss: 1.2096 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.7186 - val_accuracy: 0.4583 - val_loss: 1.2080 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 46ms/step - accuracy: 0.8482 - loss: 0.6843 - val_accuracy: 0.4583 - val_loss: 1.2063 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6823 - val_accuracy: 0.4583 - val_loss: 1.2131 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6868 - val_accuracy: 0.5000 - val_loss: 1.2221 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.6639 - val_accuracy: 0.4583 - val_loss: 1.2228 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6532 - val_accuracy: 0.4583 - val_loss: 1.2268 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 41ms/step - accuracy: 0.8482 - loss: 0.6404 - val_accuracy: 0.5000 - val_loss: 1.2338 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6347 - val_accuracy: 0.5000 - val_loss: 1.2466 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6357 - val_accuracy: 0.4583 - val_loss: 1.2631 - learning_rate: 0.0010
Epoch 42: early stopping
Restoring model weights from the end of the best epoch: 27.
Training complete. Best epoch: 27 of 42. Best val_loss: 1.1912, val_accuracy: 0.5000

========== Evaluation: within-subject test / EMS0016 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         2         0         0
  min_intens         1         2         3         0
  medium_int         1         1         3         1
  max_intens         0         1         1         4

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.667     0.667     0.667         6
   min_intensity      0.333     0.333     0.333         6
medium_intensity      0.429     0.500     0.462         6
   max_intensity      0.800     0.667     0.727         6

        accuracy                          0.542        24
       macro avg      0.557     0.542     0.547        24
    weighted avg      0.557     0.542     0.547        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0016/

############################################################
# Subject 17/31: EMS0017
############################################################
Loaded EMS0017 from /kaggle/input/datasets/akablawi/ems-4class/EMS0017.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-2.50e-04, 3.12e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.15e-06, 5.72e-07]
  Per-channel std range:  [5.63e-06, 8.61e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2857 - loss: 1.4901 - val_accuracy: 0.2500 - val_loss: 1.3851 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.4554 - loss: 1.3117 - val_accuracy: 0.3333 - val_loss: 1.3830 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 58ms/step - accuracy: 0.4286 - loss: 1.3068 - val_accuracy: 0.3333 - val_loss: 1.3797 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 58ms/step - accuracy: 0.4464 - loss: 1.2522 - val_accuracy: 0.3333 - val_loss: 1.3754 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 58ms/step - accuracy: 0.4821 - loss: 1.2320 - val_accuracy: 0.2917 - val_loss: 1.3712 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 61ms/step - accuracy: 0.4821 - loss: 1.2282 - val_accuracy: 0.2917 - val_loss: 1.3677 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.5268 - loss: 1.1949 - val_accuracy: 0.2917 - val_loss: 1.3643 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.5625 - loss: 1.1445 - val_accuracy: 0.2917 - val_loss: 1.3602 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 60ms/step - accuracy: 0.4732 - loss: 1.1746 - val_accuracy: 0.2917 - val_loss: 1.3557 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 60ms/step - accuracy: 0.5357 - loss: 1.1345 - val_accuracy: 0.2500 - val_loss: 1.3506 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.5268 - loss: 1.1255 - val_accuracy: 0.3750 - val_loss: 1.3451 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 62ms/step - accuracy: 0.5179 - loss: 1.1123 - val_accuracy: 0.3750 - val_loss: 1.3401 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.0829 - val_accuracy: 0.3750 - val_loss: 1.3359 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.1072 - val_accuracy: 0.3750 - val_loss: 1.3345 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.0829 - val_accuracy: 0.3333 - val_loss: 1.3328 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6429 - loss: 1.0419 - val_accuracy: 0.3750 - val_loss: 1.3310 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.0389 - val_accuracy: 0.3750 - val_loss: 1.3269 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 60ms/step - accuracy: 0.6429 - loss: 1.0239 - val_accuracy: 0.3333 - val_loss: 1.3214 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0160 - val_accuracy: 0.3333 - val_loss: 1.3105 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 60ms/step - accuracy: 0.6161 - loss: 1.0148 - val_accuracy: 0.3750 - val_loss: 1.3020 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0060 - val_accuracy: 0.4167 - val_loss: 1.2978 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9630 - val_accuracy: 0.4167 - val_loss: 1.2949 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9574 - val_accuracy: 0.3750 - val_loss: 1.2881 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9625 - val_accuracy: 0.4167 - val_loss: 1.2803 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 45ms/step - accuracy: 0.7321 - loss: 0.9671 - val_accuracy: 0.4167 - val_loss: 1.2818 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 44ms/step - accuracy: 0.7232 - loss: 0.9375 - val_accuracy: 0.3750 - val_loss: 1.2878 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 0.9488 - val_accuracy: 0.3750 - val_loss: 1.2794 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.9445 - val_accuracy: 0.5417 - val_loss: 1.2639 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 60ms/step - accuracy: 0.7321 - loss: 0.8825 - val_accuracy: 0.5000 - val_loss: 1.2578 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.8881 - val_accuracy: 0.5000 - val_loss: 1.2585 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.9014 - val_accuracy: 0.5000 - val_loss: 1.2573 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 61ms/step - accuracy: 0.7143 - loss: 0.8897 - val_accuracy: 0.3750 - val_loss: 1.2545 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.8762 - val_accuracy: 0.4583 - val_loss: 1.2579 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8858 - val_accuracy: 0.5000 - val_loss: 1.2471 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8880 - val_accuracy: 0.4583 - val_loss: 1.2305 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 65ms/step - accuracy: 0.7411 - loss: 0.8886 - val_accuracy: 0.5833 - val_loss: 1.2301 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 44ms/step - accuracy: 0.7411 - loss: 0.8515 - val_accuracy: 0.5417 - val_loss: 1.2354 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.7679 - loss: 0.8577 - val_accuracy: 0.5417 - val_loss: 1.2236 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 44ms/step - accuracy: 0.7500 - loss: 0.8570 - val_accuracy: 0.5833 - val_loss: 1.2237 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.8408 - val_accuracy: 0.6250 - val_loss: 1.2237 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.8397 - val_accuracy: 0.5833 - val_loss: 1.2266 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 60ms/step - accuracy: 0.7589 - loss: 0.8494 - val_accuracy: 0.5417 - val_loss: 1.2232 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8110 - val_accuracy: 0.5417 - val_loss: 1.2181 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 44ms/step - accuracy: 0.7857 - loss: 0.8123 - val_accuracy: 0.5000 - val_loss: 1.2263 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8257 - val_accuracy: 0.5833 - val_loss: 1.2131 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8141 - val_accuracy: 0.5417 - val_loss: 1.1958 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.7900 - val_accuracy: 0.5417 - val_loss: 1.1955 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7760 - val_accuracy: 0.5417 - val_loss: 1.2072 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7922 - val_accuracy: 0.5417 - val_loss: 1.2106 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 45ms/step - accuracy: 0.8125 - loss: 0.7792 - val_accuracy: 0.5417 - val_loss: 1.1968 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 47ms/step - accuracy: 0.7857 - loss: 0.7554 - val_accuracy: 0.5833 - val_loss: 1.1992 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7533 - val_accuracy: 0.5833 - val_loss: 1.1906 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7369 - val_accuracy: 0.6250 - val_loss: 1.1830 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.7301 - val_accuracy: 0.5417 - val_loss: 1.2004 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 44ms/step - accuracy: 0.8036 - loss: 0.7542 - val_accuracy: 0.5417 - val_loss: 1.1997 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.7481 - val_accuracy: 0.5000 - val_loss: 1.2110 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7334 - val_accuracy: 0.5000 - val_loss: 1.2038 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.7046 - val_accuracy: 0.5833 - val_loss: 1.1975 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 45ms/step - accuracy: 0.8304 - loss: 0.7003 - val_accuracy: 0.5417 - val_loss: 1.2045 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7154 - val_accuracy: 0.5833 - val_loss: 1.1927 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.7196 - val_accuracy: 0.5417 - val_loss: 1.1989 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.7111 - val_accuracy: 0.5833 - val_loss: 1.1930 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.7024 - val_accuracy: 0.5833 - val_loss: 1.2011 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 61ms/step - accuracy: 0.8393 - loss: 0.7010 - val_accuracy: 0.5833 - val_loss: 1.1810 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6751 - val_accuracy: 0.5833 - val_loss: 1.1841 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.6811 - val_accuracy: 0.5833 - val_loss: 1.1929 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6694 - val_accuracy: 0.5417 - val_loss: 1.1860 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6814 - val_accuracy: 0.5833 - val_loss: 1.1932 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6885 - val_accuracy: 0.6250 - val_loss: 1.1772 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6880 - val_accuracy: 0.5833 - val_loss: 1.1976 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6463 - val_accuracy: 0.5833 - val_loss: 1.1841 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6662 - val_accuracy: 0.6250 - val_loss: 1.1714 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6343 - val_accuracy: 0.5000 - val_loss: 1.2265 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 44ms/step - accuracy: 0.8304 - loss: 0.6648 - val_accuracy: 0.5833 - val_loss: 1.1863 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6461 - val_accuracy: 0.6250 - val_loss: 1.1357 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6525 - val_accuracy: 0.6250 - val_loss: 1.1480 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.6510 - val_accuracy: 0.6250 - val_loss: 1.1220 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6124 - val_accuracy: 0.5417 - val_loss: 1.1720 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6161 - val_accuracy: 0.5417 - val_loss: 1.1881 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.6038 - val_accuracy: 0.5833 - val_loss: 1.1484 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6052 - val_accuracy: 0.5833 - val_loss: 1.1665 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5931 - val_accuracy: 0.6250 - val_loss: 1.1567 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6105 - val_accuracy: 0.6250 - val_loss: 1.1546 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5682 - val_accuracy: 0.5833 - val_loss: 1.1547 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5720 - val_accuracy: 0.5833 - val_loss: 1.1636 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5872 - val_accuracy: 0.5833 - val_loss: 1.1437 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5902 - val_accuracy: 0.5833 - val_loss: 1.1378 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.5551 - val_accuracy: 0.5417 - val_loss: 1.1830 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5715 - val_accuracy: 0.5833 - val_loss: 1.1537 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5601 - val_accuracy: 0.5833 - val_loss: 1.1843 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5471 - val_accuracy: 0.5833 - val_loss: 1.1843 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 44ms/step - accuracy: 0.8661 - loss: 0.5636 - val_accuracy: 0.6250 - val_loss: 1.1355 - learning_rate: 0.0010
Epoch 92: early stopping
Restoring model weights from the end of the best epoch: 77.
Training complete. Best epoch: 77 of 92. Best val_loss: 1.1220, val_accuracy: 0.6250

========== Evaluation: within-subject test / EMS0017 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         5         0         1         0
  min_intens         1         0         5         0
  medium_int         1         2         3         0
  max_intens         0         0         4         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.714     0.833     0.769         6
   min_intensity      0.000     0.000     0.000         6
medium_intensity      0.231     0.500     0.316         6
   max_intensity      1.000     0.333     0.500         6

        accuracy                          0.417        24
       macro avg      0.486     0.417     0.396        24
    weighted avg      0.486     0.417     0.396        24

Overall accuracy: 0.4167

Artifacts saved to /kaggle/working/within_all/EMS0017/

############################################################
# Subject 18/31: EMS0018
############################################################
Loaded EMS0018 from /kaggle/input/datasets/akablawi/ems-4class/EMS0018.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-7.81e-04, 8.66e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-8.18e-07, 6.61e-07]
  Per-channel std range:  [4.77e-06, 8.35e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2679 - loss: 1.4975 - val_accuracy: 0.2083 - val_loss: 1.3832 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.4643 - loss: 1.3309 - val_accuracy: 0.4167 - val_loss: 1.3807 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4464 - loss: 1.3129 - val_accuracy: 0.4167 - val_loss: 1.3772 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.2697 - val_accuracy: 0.4167 - val_loss: 1.3717 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.5179 - loss: 1.2315 - val_accuracy: 0.4583 - val_loss: 1.3635 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.1967 - val_accuracy: 0.4167 - val_loss: 1.3528 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.5714 - loss: 1.1654 - val_accuracy: 0.4167 - val_loss: 1.3395 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.1229 - val_accuracy: 0.4583 - val_loss: 1.3244 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.6250 - loss: 1.1047 - val_accuracy: 0.5000 - val_loss: 1.3073 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 1.0729 - val_accuracy: 0.5417 - val_loss: 1.2899 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 1.0381 - val_accuracy: 0.5417 - val_loss: 1.2715 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 60ms/step - accuracy: 0.6607 - loss: 1.0318 - val_accuracy: 0.6250 - val_loss: 1.2546 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 1.0018 - val_accuracy: 0.5833 - val_loss: 1.2401 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9854 - val_accuracy: 0.5833 - val_loss: 1.2272 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.9595 - val_accuracy: 0.5833 - val_loss: 1.2143 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.7411 - loss: 0.9424 - val_accuracy: 0.5417 - val_loss: 1.2034 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 60ms/step - accuracy: 0.7143 - loss: 0.9511 - val_accuracy: 0.5000 - val_loss: 1.1934 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.9123 - val_accuracy: 0.5000 - val_loss: 1.1855 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.9158 - val_accuracy: 0.4167 - val_loss: 1.1822 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8951 - val_accuracy: 0.4167 - val_loss: 1.1794 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8866 - val_accuracy: 0.4583 - val_loss: 1.1775 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.8574 - val_accuracy: 0.4167 - val_loss: 1.1778 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.8705 - val_accuracy: 0.3750 - val_loss: 1.1794 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 45ms/step - accuracy: 0.7679 - loss: 0.8335 - val_accuracy: 0.3750 - val_loss: 1.1794 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.8324 - val_accuracy: 0.3750 - val_loss: 1.1793 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.8144 - val_accuracy: 0.3750 - val_loss: 1.1845 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7706 - val_accuracy: 0.3750 - val_loss: 1.1916 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.7588 - val_accuracy: 0.3750 - val_loss: 1.1990 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7700 - val_accuracy: 0.3750 - val_loss: 1.2058 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7466 - val_accuracy: 0.3750 - val_loss: 1.2020 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.7346 - val_accuracy: 0.3750 - val_loss: 1.2005 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7173 - val_accuracy: 0.3750 - val_loss: 1.2003 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.7111 - val_accuracy: 0.3333 - val_loss: 1.2171 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.7212 - val_accuracy: 0.3333 - val_loss: 1.2297 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.7006 - val_accuracy: 0.3333 - val_loss: 1.2311 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6830 - val_accuracy: 0.3333 - val_loss: 1.2358 - learning_rate: 0.0010
Epoch 36: early stopping
Restoring model weights from the end of the best epoch: 21.
Training complete. Best epoch: 21 of 36. Best val_loss: 1.1775, val_accuracy: 0.4583

========== Evaluation: within-subject test / EMS0018 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         4         0         0
  min_intens         1         3         2         0
  medium_int         1         1         2         2
  max_intens         0         0         0         6

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.333     0.400         6
   min_intensity      0.375     0.500     0.429         6
medium_intensity      0.500     0.333     0.400         6
   max_intensity      0.750     1.000     0.857         6

        accuracy                          0.542        24
       macro avg      0.531     0.542     0.521        24
    weighted avg      0.531     0.542     0.521        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0018/

############################################################
# Subject 19/31: EMS0019
############################################################
Loaded EMS0019 from /kaggle/input/datasets/akablawi/ems-4class/EMS0019.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.97e-03, 3.45e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.25e-06, 4.55e-06]
  Per-channel std range:  [7.07e-06, 1.54e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3125 - loss: 1.5693 - val_accuracy: 0.3750 - val_loss: 1.3849 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 63ms/step - accuracy: 0.4554 - loss: 1.3401 - val_accuracy: 0.3333 - val_loss: 1.3845 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.3929 - loss: 1.3346 - val_accuracy: 0.2917 - val_loss: 1.3839 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 61ms/step - accuracy: 0.4018 - loss: 1.3314 - val_accuracy: 0.2917 - val_loss: 1.3826 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.3092 - val_accuracy: 0.2917 - val_loss: 1.3817 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 60ms/step - accuracy: 0.5446 - loss: 1.2521 - val_accuracy: 0.2500 - val_loss: 1.3814 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2710 - val_accuracy: 0.2917 - val_loss: 1.3812 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2461 - val_accuracy: 0.2917 - val_loss: 1.3798 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2299 - val_accuracy: 0.2500 - val_loss: 1.3765 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2234 - val_accuracy: 0.2917 - val_loss: 1.3726 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.5179 - loss: 1.2111 - val_accuracy: 0.2917 - val_loss: 1.3706 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 62ms/step - accuracy: 0.5893 - loss: 1.1722 - val_accuracy: 0.2917 - val_loss: 1.3683 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 44ms/step - accuracy: 0.6161 - loss: 1.1406 - val_accuracy: 0.3333 - val_loss: 1.3694 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.5536 - loss: 1.1422 - val_accuracy: 0.2917 - val_loss: 1.3680 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.5893 - loss: 1.1076 - val_accuracy: 0.2917 - val_loss: 1.3595 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0988 - val_accuracy: 0.2917 - val_loss: 1.3546 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 44ms/step - accuracy: 0.6339 - loss: 1.0966 - val_accuracy: 0.3333 - val_loss: 1.3559 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 44ms/step - accuracy: 0.5893 - loss: 1.0805 - val_accuracy: 0.3750 - val_loss: 1.3585 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.0701 - val_accuracy: 0.3750 - val_loss: 1.3481 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6071 - loss: 1.0363 - val_accuracy: 0.3750 - val_loss: 1.3402 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 44ms/step - accuracy: 0.6339 - loss: 1.0282 - val_accuracy: 0.3750 - val_loss: 1.3444 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 44ms/step - accuracy: 0.6607 - loss: 1.0154 - val_accuracy: 0.3750 - val_loss: 1.3468 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9990 - val_accuracy: 0.4167 - val_loss: 1.3352 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 0.9932 - val_accuracy: 0.4167 - val_loss: 1.3338 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.9669 - val_accuracy: 0.4167 - val_loss: 1.3400 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.9707 - val_accuracy: 0.4167 - val_loss: 1.3336 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.9642 - val_accuracy: 0.4167 - val_loss: 1.3284 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 43ms/step - accuracy: 0.6964 - loss: 0.9488 - val_accuracy: 0.4167 - val_loss: 1.3323 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 44ms/step - accuracy: 0.6607 - loss: 0.9319 - val_accuracy: 0.4167 - val_loss: 1.3317 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.9206 - val_accuracy: 0.4167 - val_loss: 1.3212 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.7143 - loss: 0.9178 - val_accuracy: 0.4167 - val_loss: 1.3391 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 44ms/step - accuracy: 0.7232 - loss: 0.9341 - val_accuracy: 0.4167 - val_loss: 1.3228 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.8929 - val_accuracy: 0.4167 - val_loss: 1.3127 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.8906 - val_accuracy: 0.4583 - val_loss: 1.3313 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 44ms/step - accuracy: 0.7411 - loss: 0.8890 - val_accuracy: 0.4583 - val_loss: 1.3228 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.8467 - val_accuracy: 0.4583 - val_loss: 1.3183 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.7500 - loss: 0.8406 - val_accuracy: 0.4583 - val_loss: 1.3201 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8667 - val_accuracy: 0.4583 - val_loss: 1.3154 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 44ms/step - accuracy: 0.7589 - loss: 0.8624 - val_accuracy: 0.4167 - val_loss: 1.3224 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 57ms/step - accuracy: 0.7232 - loss: 0.8578 - val_accuracy: 0.4167 - val_loss: 1.3022 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8243 - val_accuracy: 0.4583 - val_loss: 1.3022 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 57ms/step - accuracy: 0.7679 - loss: 0.8419 - val_accuracy: 0.5000 - val_loss: 1.2955 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 44ms/step - accuracy: 0.7500 - loss: 0.8176 - val_accuracy: 0.4583 - val_loss: 1.3073 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 44ms/step - accuracy: 0.7768 - loss: 0.7995 - val_accuracy: 0.4583 - val_loss: 1.3073 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7699 - val_accuracy: 0.4583 - val_loss: 1.3067 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.7742 - val_accuracy: 0.4583 - val_loss: 1.2989 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 45ms/step - accuracy: 0.8393 - loss: 0.7490 - val_accuracy: 0.5000 - val_loss: 1.2981 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 60ms/step - accuracy: 0.7946 - loss: 0.7698 - val_accuracy: 0.5000 - val_loss: 1.2913 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7853 - val_accuracy: 0.5000 - val_loss: 1.2910 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 46ms/step - accuracy: 0.8125 - loss: 0.7659 - val_accuracy: 0.5000 - val_loss: 1.3045 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.7361 - val_accuracy: 0.5000 - val_loss: 1.2853 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 47ms/step - accuracy: 0.8304 - loss: 0.7312 - val_accuracy: 0.5000 - val_loss: 1.2879 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.7216 - val_accuracy: 0.5000 - val_loss: 1.3027 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.7615 - val_accuracy: 0.5000 - val_loss: 1.2842 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.7343 - val_accuracy: 0.5000 - val_loss: 1.2870 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.7282 - val_accuracy: 0.5000 - val_loss: 1.2837 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.7091 - val_accuracy: 0.5000 - val_loss: 1.2904 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6995 - val_accuracy: 0.4583 - val_loss: 1.3099 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7006 - val_accuracy: 0.4583 - val_loss: 1.2810 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 44ms/step - accuracy: 0.8036 - loss: 0.6797 - val_accuracy: 0.5000 - val_loss: 1.2927 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.7003 - val_accuracy: 0.4583 - val_loss: 1.2744 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.6837 - val_accuracy: 0.5000 - val_loss: 1.2931 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6645 - val_accuracy: 0.5000 - val_loss: 1.2924 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 60ms/step - accuracy: 0.8750 - loss: 0.6514 - val_accuracy: 0.5000 - val_loss: 1.2643 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6506 - val_accuracy: 0.5000 - val_loss: 1.2902 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6482 - val_accuracy: 0.5000 - val_loss: 1.2973 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.6494 - val_accuracy: 0.4583 - val_loss: 1.2574 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6560 - val_accuracy: 0.5000 - val_loss: 1.2974 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6411 - val_accuracy: 0.4583 - val_loss: 1.2621 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.6334 - val_accuracy: 0.4583 - val_loss: 1.2509 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6360 - val_accuracy: 0.4583 - val_loss: 1.2538 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.6250 - val_accuracy: 0.4583 - val_loss: 1.2558 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6251 - val_accuracy: 0.4583 - val_loss: 1.2834 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.6444 - val_accuracy: 0.4583 - val_loss: 1.2595 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.6268 - val_accuracy: 0.5000 - val_loss: 1.2427 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6060 - val_accuracy: 0.5000 - val_loss: 1.2730 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5961 - val_accuracy: 0.3333 - val_loss: 1.2557 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5947 - val_accuracy: 0.5000 - val_loss: 1.2630 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 57ms/step - accuracy: 0.8482 - loss: 0.6102 - val_accuracy: 0.4583 - val_loss: 1.2408 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.5931 - val_accuracy: 0.3750 - val_loss: 1.2752 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.5843 - val_accuracy: 0.3750 - val_loss: 1.2623 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5700 - val_accuracy: 0.5000 - val_loss: 1.2100 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5588 - val_accuracy: 0.4583 - val_loss: 1.2340 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.6028 - val_accuracy: 0.3750 - val_loss: 1.2503 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5436 - val_accuracy: 0.3750 - val_loss: 1.2538 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5301 - val_accuracy: 0.4167 - val_loss: 1.2649 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.5592 - val_accuracy: 0.4167 - val_loss: 1.2528 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5436 - val_accuracy: 0.4583 - val_loss: 1.2765 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5518 - val_accuracy: 0.5000 - val_loss: 1.2548 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5559 - val_accuracy: 0.4167 - val_loss: 1.2389 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5274 - val_accuracy: 0.4583 - val_loss: 1.2890 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5475 - val_accuracy: 0.5000 - val_loss: 1.2170 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5326 - val_accuracy: 0.4583 - val_loss: 1.2412 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5392 - val_accuracy: 0.4583 - val_loss: 1.2584 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.5156 - val_accuracy: 0.4167 - val_loss: 1.2841 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5386 - val_accuracy: 0.5833 - val_loss: 1.2450 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 57ms/step - accuracy: 0.9018 - loss: 0.5110 - val_accuracy: 0.5000 - val_loss: 1.1734 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5060 - val_accuracy: 0.5000 - val_loss: 1.2488 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5096 - val_accuracy: 0.5417 - val_loss: 1.2720 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5194 - val_accuracy: 0.5833 - val_loss: 1.2550 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.4986 - val_accuracy: 0.5417 - val_loss: 1.2384 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4748 - val_accuracy: 0.5833 - val_loss: 1.2193 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4775 - val_accuracy: 0.5417 - val_loss: 1.2531 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.4980 - val_accuracy: 0.5417 - val_loss: 1.2307 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 46ms/step - accuracy: 0.9196 - loss: 0.4911 - val_accuracy: 0.5000 - val_loss: 1.2811 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5075 - val_accuracy: 0.5000 - val_loss: 1.2507 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.4578 - val_accuracy: 0.4583 - val_loss: 1.2475 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4707 - val_accuracy: 0.5000 - val_loss: 1.2274 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.4743 - val_accuracy: 0.5417 - val_loss: 1.2449 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4534 - val_accuracy: 0.4583 - val_loss: 1.2802 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.4751 - val_accuracy: 0.5417 - val_loss: 1.2542 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.4420 - val_accuracy: 0.5417 - val_loss: 1.2401 - learning_rate: 0.0010
Epoch 112: early stopping
Restoring model weights from the end of the best epoch: 97.
Training complete. Best epoch: 97 of 112. Best val_loss: 1.1734, val_accuracy: 0.5000

========== Evaluation: within-subject test / EMS0019 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         1         1         2
  min_intens         4         2         0         0
  medium_int         1         1         3         1
  max_intens         1         1         2         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.250     0.333     0.286         6
   min_intensity      0.400     0.333     0.364         6
medium_intensity      0.500     0.500     0.500         6
   max_intensity      0.400     0.333     0.364         6

        accuracy                          0.375        24
       macro avg      0.387     0.375     0.378        24
    weighted avg      0.388     0.375     0.378        24

Overall accuracy: 0.3750

Artifacts saved to /kaggle/working/within_all/EMS0019/

############################################################
# Subject 20/31: EMS0020
############################################################
Loaded EMS0020 from /kaggle/input/datasets/akablawi/ems-4class/EMS0020.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-7.80e-04, 5.08e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-4.53e-06, 1.54e-05]
  Per-channel std range:  [1.06e-05, 8.51e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2232 - loss: 1.5160 - val_accuracy: 0.3750 - val_loss: 1.3831 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.4464 - loss: 1.3221 - val_accuracy: 0.5417 - val_loss: 1.3774 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.5893 - loss: 1.2409 - val_accuracy: 0.5417 - val_loss: 1.3679 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.1679 - val_accuracy: 0.5833 - val_loss: 1.3531 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0914 - val_accuracy: 0.5833 - val_loss: 1.3300 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 1.0429 - val_accuracy: 0.7083 - val_loss: 1.3004 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9922 - val_accuracy: 0.7083 - val_loss: 1.2676 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.9747 - val_accuracy: 0.6250 - val_loss: 1.2333 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 0.9433 - val_accuracy: 0.6250 - val_loss: 1.2024 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.7143 - loss: 0.8989 - val_accuracy: 0.6250 - val_loss: 1.1769 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.8735 - val_accuracy: 0.6250 - val_loss: 1.1574 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.8469 - val_accuracy: 0.6250 - val_loss: 1.1427 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8304 - val_accuracy: 0.6250 - val_loss: 1.1333 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8094 - val_accuracy: 0.6250 - val_loss: 1.1265 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.7989 - val_accuracy: 0.6250 - val_loss: 1.1205 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.7856 - val_accuracy: 0.6250 - val_loss: 1.1139 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8036 - val_accuracy: 0.6250 - val_loss: 1.1059 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.7687 - val_accuracy: 0.5833 - val_loss: 1.1007 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.7416 - val_accuracy: 0.5417 - val_loss: 1.0990 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.7461 - val_accuracy: 0.5833 - val_loss: 1.0981 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 44ms/step - accuracy: 0.7321 - loss: 0.7145 - val_accuracy: 0.5833 - val_loss: 1.0992 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.7255 - val_accuracy: 0.5833 - val_loss: 1.0975 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.7039 - val_accuracy: 0.5833 - val_loss: 1.0787 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.6904 - val_accuracy: 0.5833 - val_loss: 1.0650 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.6829 - val_accuracy: 0.5833 - val_loss: 1.0616 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.6808 - val_accuracy: 0.5833 - val_loss: 1.0614 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.6691 - val_accuracy: 0.5833 - val_loss: 1.0489 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.6391 - val_accuracy: 0.5833 - val_loss: 1.0348 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.6510 - val_accuracy: 0.5833 - val_loss: 1.0295 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 57ms/step - accuracy: 0.7768 - loss: 0.6573 - val_accuracy: 0.5833 - val_loss: 1.0264 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.6394 - val_accuracy: 0.5833 - val_loss: 1.0144 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.6314 - val_accuracy: 0.5833 - val_loss: 0.9982 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.6130 - val_accuracy: 0.5833 - val_loss: 0.9906 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 61ms/step - accuracy: 0.8214 - loss: 0.6051 - val_accuracy: 0.5833 - val_loss: 0.9873 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 65ms/step - accuracy: 0.8214 - loss: 0.6142 - val_accuracy: 0.5833 - val_loss: 0.9827 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.5925 - val_accuracy: 0.5833 - val_loss: 0.9766 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.5789 - val_accuracy: 0.6250 - val_loss: 0.9771 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.5774 - val_accuracy: 0.5833 - val_loss: 0.9717 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.5833 - val_accuracy: 0.6250 - val_loss: 0.9675 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.5734 - val_accuracy: 0.6250 - val_loss: 0.9640 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.5894 - val_accuracy: 0.6667 - val_loss: 0.9565 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.5778 - val_accuracy: 0.6667 - val_loss: 0.9563 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5481 - val_accuracy: 0.6250 - val_loss: 0.9551 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.5454 - val_accuracy: 0.6667 - val_loss: 0.9455 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.5615 - val_accuracy: 0.7083 - val_loss: 0.9324 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.5356 - val_accuracy: 0.7083 - val_loss: 0.9392 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5449 - val_accuracy: 0.6667 - val_loss: 0.9417 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5282 - val_accuracy: 0.6667 - val_loss: 0.9392 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 57ms/step - accuracy: 0.8393 - loss: 0.5231 - val_accuracy: 0.6667 - val_loss: 0.9277 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.5161 - val_accuracy: 0.7083 - val_loss: 0.9208 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.5272 - val_accuracy: 0.6667 - val_loss: 0.9086 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.5199 - val_accuracy: 0.6667 - val_loss: 0.9020 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 44ms/step - accuracy: 0.8661 - loss: 0.4919 - val_accuracy: 0.7500 - val_loss: 0.9086 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5151 - val_accuracy: 0.7500 - val_loss: 0.9154 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5038 - val_accuracy: 0.7083 - val_loss: 0.9123 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.5115 - val_accuracy: 0.7083 - val_loss: 0.9137 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.4783 - val_accuracy: 0.7083 - val_loss: 0.9084 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.4931 - val_accuracy: 0.7083 - val_loss: 0.8948 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.4848 - val_accuracy: 0.7083 - val_loss: 0.8985 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4700 - val_accuracy: 0.7500 - val_loss: 0.9132 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.4981 - val_accuracy: 0.7500 - val_loss: 0.8958 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 57ms/step - accuracy: 0.8929 - loss: 0.4593 - val_accuracy: 0.7500 - val_loss: 0.8914 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.4924 - val_accuracy: 0.7500 - val_loss: 0.8952 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.4913 - val_accuracy: 0.7500 - val_loss: 0.8839 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4655 - val_accuracy: 0.7083 - val_loss: 0.8845 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.4557 - val_accuracy: 0.7083 - val_loss: 0.9010 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.4683 - val_accuracy: 0.7500 - val_loss: 0.9164 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.4571 - val_accuracy: 0.7083 - val_loss: 0.9009 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4315 - val_accuracy: 0.7083 - val_loss: 0.8995 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.4414 - val_accuracy: 0.7083 - val_loss: 0.9043 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4381 - val_accuracy: 0.7500 - val_loss: 0.8886 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 59ms/step - accuracy: 0.9286 - loss: 0.4325 - val_accuracy: 0.7500 - val_loss: 0.8678 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4142 - val_accuracy: 0.7083 - val_loss: 0.8739 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4129 - val_accuracy: 0.7500 - val_loss: 0.9018 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4159 - val_accuracy: 0.7083 - val_loss: 0.9100 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.4288 - val_accuracy: 0.7500 - val_loss: 0.8872 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.3981 - val_accuracy: 0.7917 - val_loss: 0.8672 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.4367 - val_accuracy: 0.7083 - val_loss: 0.8786 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.4155 - val_accuracy: 0.7500 - val_loss: 0.8836 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.4175 - val_accuracy: 0.7500 - val_loss: 0.8808 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4015 - val_accuracy: 0.7500 - val_loss: 0.9006 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.3942 - val_accuracy: 0.7500 - val_loss: 0.8673 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.3867 - val_accuracy: 0.7500 - val_loss: 0.8598 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.3865 - val_accuracy: 0.7500 - val_loss: 0.8820 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4106 - val_accuracy: 0.7500 - val_loss: 0.8958 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 46ms/step - accuracy: 0.9107 - loss: 0.3989 - val_accuracy: 0.7500 - val_loss: 0.8865 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3857 - val_accuracy: 0.7500 - val_loss: 0.8808 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.3910 - val_accuracy: 0.7500 - val_loss: 0.8695 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.3910 - val_accuracy: 0.7500 - val_loss: 0.8789 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.3954 - val_accuracy: 0.7500 - val_loss: 0.8916 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3551 - val_accuracy: 0.7500 - val_loss: 0.8852 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.3812 - val_accuracy: 0.7500 - val_loss: 0.8755 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.3511 - val_accuracy: 0.7500 - val_loss: 0.8991 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3589 - val_accuracy: 0.7500 - val_loss: 0.8771 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 57ms/step - accuracy: 0.9196 - loss: 0.3638 - val_accuracy: 0.7500 - val_loss: 0.8557 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.3571 - val_accuracy: 0.7500 - val_loss: 0.8570 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3354 - val_accuracy: 0.7500 - val_loss: 0.8820 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3388 - val_accuracy: 0.7500 - val_loss: 0.8893 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.3426 - val_accuracy: 0.7500 - val_loss: 0.8879 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3382 - val_accuracy: 0.7500 - val_loss: 0.8882 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.3424 - val_accuracy: 0.7500 - val_loss: 0.8861 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3269 - val_accuracy: 0.7083 - val_loss: 0.9141 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3170 - val_accuracy: 0.7083 - val_loss: 0.8914 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.3482 - val_accuracy: 0.7500 - val_loss: 0.8664 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 41ms/step - accuracy: 0.9464 - loss: 0.3358 - val_accuracy: 0.6667 - val_loss: 0.8989 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3190 - val_accuracy: 0.7500 - val_loss: 0.8827 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.3214 - val_accuracy: 0.7500 - val_loss: 0.8805 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.3156 - val_accuracy: 0.7083 - val_loss: 0.8863 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 41ms/step - accuracy: 0.9554 - loss: 0.3175 - val_accuracy: 0.7500 - val_loss: 0.8612 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 42ms/step - accuracy: 0.9643 - loss: 0.3211 - val_accuracy: 0.7083 - val_loss: 0.8569 - learning_rate: 0.0010
Epoch 110: early stopping
Restoring model weights from the end of the best epoch: 95.
Training complete. Best epoch: 95 of 110. Best val_loss: 0.8557, val_accuracy: 0.7500

========== Evaluation: within-subject test / EMS0020 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         1         1         0
  min_intens         0         3         3         0
  medium_int         0         3         3         0
  max_intens         1         0         1         4

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.800     0.667     0.727         6
   min_intensity      0.429     0.500     0.462         6
medium_intensity      0.375     0.500     0.429         6
   max_intensity      1.000     0.667     0.800         6

        accuracy                          0.583        24
       macro avg      0.651     0.583     0.604        24
    weighted avg      0.651     0.583     0.604        24

Overall accuracy: 0.5833

Artifacts saved to /kaggle/working/within_all/EMS0020/

############################################################
# Subject 21/31: EMS0021
############################################################
Loaded EMS0021 from /kaggle/input/datasets/akablawi/ems-4class/EMS0021.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.46e-03, 1.28e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-9.65e-07, 1.53e-06]
  Per-channel std range:  [6.60e-06, 5.51e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2946 - loss: 1.4280 - val_accuracy: 0.2917 - val_loss: 1.3845 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3661 - loss: 1.3318 - val_accuracy: 0.3750 - val_loss: 1.3820 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 61ms/step - accuracy: 0.4286 - loss: 1.2972 - val_accuracy: 0.4583 - val_loss: 1.3784 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.5000 - loss: 1.2675 - val_accuracy: 0.4583 - val_loss: 1.3744 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4554 - loss: 1.2486 - val_accuracy: 0.5000 - val_loss: 1.3696 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 60ms/step - accuracy: 0.5268 - loss: 1.2384 - val_accuracy: 0.5000 - val_loss: 1.3642 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.5357 - loss: 1.1977 - val_accuracy: 0.5417 - val_loss: 1.3580 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.1577 - val_accuracy: 0.5417 - val_loss: 1.3500 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 60ms/step - accuracy: 0.5268 - loss: 1.1487 - val_accuracy: 0.5000 - val_loss: 1.3413 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5536 - loss: 1.1274 - val_accuracy: 0.4583 - val_loss: 1.3328 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.5536 - loss: 1.1217 - val_accuracy: 0.4167 - val_loss: 1.3234 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.0812 - val_accuracy: 0.4167 - val_loss: 1.3138 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 60ms/step - accuracy: 0.6250 - loss: 1.0863 - val_accuracy: 0.4167 - val_loss: 1.3025 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 60ms/step - accuracy: 0.5893 - loss: 1.0455 - val_accuracy: 0.4583 - val_loss: 1.2863 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.5982 - loss: 1.0437 - val_accuracy: 0.4167 - val_loss: 1.2730 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.0322 - val_accuracy: 0.4583 - val_loss: 1.2647 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0284 - val_accuracy: 0.4583 - val_loss: 1.2552 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.0092 - val_accuracy: 0.4583 - val_loss: 1.2470 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.6518 - loss: 0.9761 - val_accuracy: 0.4583 - val_loss: 1.2402 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 60ms/step - accuracy: 0.6429 - loss: 0.9803 - val_accuracy: 0.4583 - val_loss: 1.2307 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 62ms/step - accuracy: 0.6250 - loss: 0.9742 - val_accuracy: 0.4583 - val_loss: 1.2218 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 58ms/step - accuracy: 0.6250 - loss: 0.9818 - val_accuracy: 0.4583 - val_loss: 1.2149 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 62ms/step - accuracy: 0.6518 - loss: 0.9444 - val_accuracy: 0.4583 - val_loss: 1.2059 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 0.9582 - val_accuracy: 0.4583 - val_loss: 1.1952 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.6875 - loss: 0.9407 - val_accuracy: 0.5417 - val_loss: 1.1826 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7232 - loss: 0.9103 - val_accuracy: 0.5417 - val_loss: 1.1705 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.9176 - val_accuracy: 0.5000 - val_loss: 1.1593 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8975 - val_accuracy: 0.5000 - val_loss: 1.1486 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.7143 - loss: 0.8858 - val_accuracy: 0.5417 - val_loss: 1.1383 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8898 - val_accuracy: 0.5000 - val_loss: 1.1306 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8632 - val_accuracy: 0.5000 - val_loss: 1.1239 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8426 - val_accuracy: 0.5417 - val_loss: 1.1123 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 60ms/step - accuracy: 0.7411 - loss: 0.8504 - val_accuracy: 0.5000 - val_loss: 1.1021 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 0.8533 - val_accuracy: 0.5417 - val_loss: 1.0953 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 60ms/step - accuracy: 0.7143 - loss: 0.8536 - val_accuracy: 0.5000 - val_loss: 1.0929 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.8407 - val_accuracy: 0.5833 - val_loss: 1.0864 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 60ms/step - accuracy: 0.7768 - loss: 0.8161 - val_accuracy: 0.5417 - val_loss: 1.0708 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.7232 - loss: 0.8402 - val_accuracy: 0.5833 - val_loss: 1.0520 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7724 - val_accuracy: 0.5417 - val_loss: 1.0508 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.7888 - val_accuracy: 0.5417 - val_loss: 1.0483 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8301 - val_accuracy: 0.5833 - val_loss: 1.0395 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.7897 - val_accuracy: 0.5833 - val_loss: 1.0502 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7676 - val_accuracy: 0.5417 - val_loss: 1.0580 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7879 - val_accuracy: 0.6250 - val_loss: 1.0407 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.7572 - val_accuracy: 0.6250 - val_loss: 1.0301 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.7703 - val_accuracy: 0.6250 - val_loss: 1.0321 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.7610 - val_accuracy: 0.5833 - val_loss: 1.0370 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7389 - val_accuracy: 0.5417 - val_loss: 1.0438 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7483 - val_accuracy: 0.6250 - val_loss: 1.0448 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7140 - val_accuracy: 0.6667 - val_loss: 1.0306 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7066 - val_accuracy: 0.6667 - val_loss: 1.0321 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7089 - val_accuracy: 0.5833 - val_loss: 1.0444 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7032 - val_accuracy: 0.6250 - val_loss: 1.0267 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6960 - val_accuracy: 0.5833 - val_loss: 1.0373 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.6876 - val_accuracy: 0.5833 - val_loss: 1.0573 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.7017 - val_accuracy: 0.5833 - val_loss: 1.0311 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6622 - val_accuracy: 0.5833 - val_loss: 1.0371 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.6681 - val_accuracy: 0.6250 - val_loss: 1.0688 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6601 - val_accuracy: 0.5833 - val_loss: 1.0593 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.7150 - val_accuracy: 0.5833 - val_loss: 1.0472 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6564 - val_accuracy: 0.5833 - val_loss: 1.0291 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6659 - val_accuracy: 0.5833 - val_loss: 1.0133 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6558 - val_accuracy: 0.5833 - val_loss: 1.0121 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6357 - val_accuracy: 0.5833 - val_loss: 1.0275 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6717 - val_accuracy: 0.5833 - val_loss: 1.0476 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 41ms/step - accuracy: 0.8661 - loss: 0.6284 - val_accuracy: 0.5417 - val_loss: 1.0445 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6045 - val_accuracy: 0.5833 - val_loss: 1.0274 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6060 - val_accuracy: 0.5833 - val_loss: 1.0249 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 63ms/step - accuracy: 0.9018 - loss: 0.6061 - val_accuracy: 0.5833 - val_loss: 0.9930 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6371 - val_accuracy: 0.6667 - val_loss: 0.9980 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6037 - val_accuracy: 0.6667 - val_loss: 1.0110 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6239 - val_accuracy: 0.6667 - val_loss: 0.9947 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.5882 - val_accuracy: 0.6250 - val_loss: 0.9823 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.6014 - val_accuracy: 0.6250 - val_loss: 0.9986 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.5991 - val_accuracy: 0.5417 - val_loss: 1.0069 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5707 - val_accuracy: 0.5833 - val_loss: 0.9998 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5533 - val_accuracy: 0.5833 - val_loss: 1.0088 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5646 - val_accuracy: 0.6250 - val_loss: 0.9952 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 44ms/step - accuracy: 0.9286 - loss: 0.5431 - val_accuracy: 0.6250 - val_loss: 1.0188 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5706 - val_accuracy: 0.5833 - val_loss: 0.9973 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.5421 - val_accuracy: 0.5417 - val_loss: 1.0089 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5495 - val_accuracy: 0.5000 - val_loss: 1.0094 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 57ms/step - accuracy: 0.9107 - loss: 0.5366 - val_accuracy: 0.5417 - val_loss: 0.9765 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5172 - val_accuracy: 0.5417 - val_loss: 0.9770 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5184 - val_accuracy: 0.5833 - val_loss: 1.0092 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5230 - val_accuracy: 0.5833 - val_loss: 0.9986 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5159 - val_accuracy: 0.5417 - val_loss: 0.9974 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.5313 - val_accuracy: 0.5833 - val_loss: 1.0208 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5064 - val_accuracy: 0.5417 - val_loss: 1.0156 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.4920 - val_accuracy: 0.5833 - val_loss: 1.0172 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 44ms/step - accuracy: 0.9107 - loss: 0.4936 - val_accuracy: 0.5000 - val_loss: 1.0191 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 44ms/step - accuracy: 0.9107 - loss: 0.4804 - val_accuracy: 0.5417 - val_loss: 1.0178 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4844 - val_accuracy: 0.6250 - val_loss: 1.0064 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5111 - val_accuracy: 0.6250 - val_loss: 1.0081 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.4723 - val_accuracy: 0.5000 - val_loss: 1.0165 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4777 - val_accuracy: 0.5833 - val_loss: 0.9999 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.4661 - val_accuracy: 0.6667 - val_loss: 1.0215 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4681 - val_accuracy: 0.6250 - val_loss: 1.0370 - learning_rate: 0.0010
Epoch 98: early stopping
Restoring model weights from the end of the best epoch: 83.
Training complete. Best epoch: 83 of 98. Best val_loss: 0.9765, val_accuracy: 0.5417

========== Evaluation: within-subject test / EMS0021 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         1         2         1
  min_intens         2         2         2         0
  medium_int         2         0         4         0
  max_intens         0         0         0         6

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.333     0.333     0.333         6
   min_intensity      0.667     0.333     0.444         6
medium_intensity      0.500     0.667     0.571         6
   max_intensity      0.857     1.000     0.923         6

        accuracy                          0.583        24
       macro avg      0.589     0.583     0.568        24
    weighted avg      0.589     0.583     0.568        24

Overall accuracy: 0.5833

Artifacts saved to /kaggle/working/within_all/EMS0021/

############################################################
# Subject 22/31: EMS0022
############################################################
Loaded EMS0022 from /kaggle/input/datasets/akablawi/ems-4class/EMS0022.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.91e-03, 2.26e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-2.85e-06, 1.22e-06]
  Per-channel std range:  [6.30e-06, 1.39e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2500 - loss: 1.4617 - val_accuracy: 0.2917 - val_loss: 1.3850 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3750 - loss: 1.3396 - val_accuracy: 0.4583 - val_loss: 1.3822 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.3839 - loss: 1.3119 - val_accuracy: 0.5000 - val_loss: 1.3787 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.3839 - loss: 1.2891 - val_accuracy: 0.5417 - val_loss: 1.3748 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2431 - val_accuracy: 0.5417 - val_loss: 1.3707 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 60ms/step - accuracy: 0.5268 - loss: 1.2170 - val_accuracy: 0.6250 - val_loss: 1.3663 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5000 - loss: 1.2111 - val_accuracy: 0.6250 - val_loss: 1.3617 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.1560 - val_accuracy: 0.5833 - val_loss: 1.3569 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.1734 - val_accuracy: 0.5833 - val_loss: 1.3510 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.5357 - loss: 1.1512 - val_accuracy: 0.5833 - val_loss: 1.3445 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5446 - loss: 1.1376 - val_accuracy: 0.5833 - val_loss: 1.3384 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 60ms/step - accuracy: 0.5893 - loss: 1.1013 - val_accuracy: 0.5000 - val_loss: 1.3320 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0785 - val_accuracy: 0.5000 - val_loss: 1.3245 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 62ms/step - accuracy: 0.6339 - loss: 1.0966 - val_accuracy: 0.5417 - val_loss: 1.3168 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6161 - loss: 1.0733 - val_accuracy: 0.5417 - val_loss: 1.3098 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 61ms/step - accuracy: 0.6607 - loss: 1.0297 - val_accuracy: 0.5417 - val_loss: 1.2991 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 61ms/step - accuracy: 0.6250 - loss: 1.0256 - val_accuracy: 0.5417 - val_loss: 1.2901 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 61ms/step - accuracy: 0.6607 - loss: 1.0226 - val_accuracy: 0.5417 - val_loss: 1.2876 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 1.0037 - val_accuracy: 0.5417 - val_loss: 1.2836 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 0.9939 - val_accuracy: 0.5417 - val_loss: 1.2704 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 0.9820 - val_accuracy: 0.5417 - val_loss: 1.2588 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.9587 - val_accuracy: 0.4583 - val_loss: 1.2611 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 44ms/step - accuracy: 0.7232 - loss: 0.9561 - val_accuracy: 0.4583 - val_loss: 1.2633 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 42ms/step - accuracy: 0.6786 - loss: 0.9413 - val_accuracy: 0.4583 - val_loss: 1.2605 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 0.9546 - val_accuracy: 0.5417 - val_loss: 1.2489 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 0.9327 - val_accuracy: 0.5417 - val_loss: 1.2423 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9299 - val_accuracy: 0.4583 - val_loss: 1.2374 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.9163 - val_accuracy: 0.4167 - val_loss: 1.2390 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.8818 - val_accuracy: 0.5000 - val_loss: 1.2423 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.9082 - val_accuracy: 0.4583 - val_loss: 1.2364 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.8776 - val_accuracy: 0.5000 - val_loss: 1.2374 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8882 - val_accuracy: 0.4167 - val_loss: 1.2331 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8747 - val_accuracy: 0.4167 - val_loss: 1.2252 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7679 - loss: 0.8337 - val_accuracy: 0.4167 - val_loss: 1.2262 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.8613 - val_accuracy: 0.4167 - val_loss: 1.2191 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.7946 - loss: 0.8324 - val_accuracy: 0.4583 - val_loss: 1.2187 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 44ms/step - accuracy: 0.8125 - loss: 0.8481 - val_accuracy: 0.5417 - val_loss: 1.2279 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 57ms/step - accuracy: 0.8125 - loss: 0.8255 - val_accuracy: 0.4583 - val_loss: 1.2065 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 57ms/step - accuracy: 0.7946 - loss: 0.8247 - val_accuracy: 0.4583 - val_loss: 1.2049 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.8557 - val_accuracy: 0.5000 - val_loss: 1.2225 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 44ms/step - accuracy: 0.7768 - loss: 0.8307 - val_accuracy: 0.5000 - val_loss: 1.2208 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.8062 - val_accuracy: 0.5000 - val_loss: 1.2255 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7909 - val_accuracy: 0.5417 - val_loss: 1.2164 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.7411 - loss: 0.8454 - val_accuracy: 0.5000 - val_loss: 1.2074 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 42ms/step - accuracy: 0.7946 - loss: 0.8082 - val_accuracy: 0.5417 - val_loss: 1.2241 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.8145 - val_accuracy: 0.5000 - val_loss: 1.2107 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7807 - val_accuracy: 0.5000 - val_loss: 1.2074 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.8007 - val_accuracy: 0.5000 - val_loss: 1.2229 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.8060 - val_accuracy: 0.5000 - val_loss: 1.2245 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 42ms/step - accuracy: 0.8214 - loss: 0.7838 - val_accuracy: 0.4583 - val_loss: 1.2057 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.7775 - val_accuracy: 0.5000 - val_loss: 1.2180 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.7746 - val_accuracy: 0.4583 - val_loss: 1.2045 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.7700 - val_accuracy: 0.4583 - val_loss: 1.1969 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.7701 - val_accuracy: 0.5000 - val_loss: 1.2182 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.7857 - loss: 0.7725 - val_accuracy: 0.4583 - val_loss: 1.2199 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.7414 - val_accuracy: 0.4583 - val_loss: 1.2041 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.7371 - val_accuracy: 0.5000 - val_loss: 1.2185 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 42ms/step - accuracy: 0.8304 - loss: 0.7306 - val_accuracy: 0.5000 - val_loss: 1.2100 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 42ms/step - accuracy: 0.7946 - loss: 0.7396 - val_accuracy: 0.4583 - val_loss: 1.2029 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7191 - val_accuracy: 0.5417 - val_loss: 1.2034 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.7106 - val_accuracy: 0.5417 - val_loss: 1.1948 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.7288 - val_accuracy: 0.5417 - val_loss: 1.1921 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.7139 - val_accuracy: 0.5417 - val_loss: 1.1843 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7149 - val_accuracy: 0.5000 - val_loss: 1.1847 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7009 - val_accuracy: 0.4583 - val_loss: 1.2036 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 45ms/step - accuracy: 0.8839 - loss: 0.6824 - val_accuracy: 0.4583 - val_loss: 1.2123 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.6767 - val_accuracy: 0.4583 - val_loss: 1.2143 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 49ms/step - accuracy: 0.8750 - loss: 0.6823 - val_accuracy: 0.4167 - val_loss: 1.2110 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.7114 - val_accuracy: 0.4583 - val_loss: 1.1934 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 45ms/step - accuracy: 0.8929 - loss: 0.6406 - val_accuracy: 0.5417 - val_loss: 1.2013 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6491 - val_accuracy: 0.5417 - val_loss: 1.2139 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6397 - val_accuracy: 0.4583 - val_loss: 1.2049 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6734 - val_accuracy: 0.4583 - val_loss: 1.1999 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.6535 - val_accuracy: 0.4583 - val_loss: 1.2048 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6397 - val_accuracy: 0.4583 - val_loss: 1.2054 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6635 - val_accuracy: 0.5417 - val_loss: 1.2011 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 57ms/step - accuracy: 0.9018 - loss: 0.6440 - val_accuracy: 0.5417 - val_loss: 1.1829 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6364 - val_accuracy: 0.4583 - val_loss: 1.1973 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5956 - val_accuracy: 0.5000 - val_loss: 1.2181 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6401 - val_accuracy: 0.5417 - val_loss: 1.1912 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 57ms/step - accuracy: 0.9464 - loss: 0.5988 - val_accuracy: 0.4583 - val_loss: 1.1784 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6146 - val_accuracy: 0.5000 - val_loss: 1.2060 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5993 - val_accuracy: 0.4583 - val_loss: 1.2107 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6165 - val_accuracy: 0.4583 - val_loss: 1.2132 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6340 - val_accuracy: 0.5000 - val_loss: 1.2168 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5871 - val_accuracy: 0.4167 - val_loss: 1.2061 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6003 - val_accuracy: 0.5417 - val_loss: 1.1941 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.6036 - val_accuracy: 0.5417 - val_loss: 1.1896 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 41ms/step - accuracy: 0.9286 - loss: 0.5668 - val_accuracy: 0.4583 - val_loss: 1.1903 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5879 - val_accuracy: 0.5417 - val_loss: 1.2106 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 41ms/step - accuracy: 0.9107 - loss: 0.6155 - val_accuracy: 0.4583 - val_loss: 1.1903 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 57ms/step - accuracy: 0.8839 - loss: 0.5781 - val_accuracy: 0.5000 - val_loss: 1.1758 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 42ms/step - accuracy: 0.8929 - loss: 0.5578 - val_accuracy: 0.5417 - val_loss: 1.2013 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5514 - val_accuracy: 0.4583 - val_loss: 1.2021 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5722 - val_accuracy: 0.5000 - val_loss: 1.1891 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5371 - val_accuracy: 0.5417 - val_loss: 1.1920 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5721 - val_accuracy: 0.3333 - val_loss: 1.2066 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 42ms/step - accuracy: 0.8571 - loss: 0.5524 - val_accuracy: 0.4583 - val_loss: 1.2003 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.5234 - val_accuracy: 0.5000 - val_loss: 1.2085 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5282 - val_accuracy: 0.4583 - val_loss: 1.2254 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5259 - val_accuracy: 0.5000 - val_loss: 1.2037 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5498 - val_accuracy: 0.4583 - val_loss: 1.2085 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.4940 - val_accuracy: 0.3333 - val_loss: 1.2220 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5528 - val_accuracy: 0.4583 - val_loss: 1.2175 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5314 - val_accuracy: 0.4583 - val_loss: 1.2024 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.5282 - val_accuracy: 0.4167 - val_loss: 1.1993 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4967 - val_accuracy: 0.3750 - val_loss: 1.2301 - learning_rate: 0.0010
Epoch 107: early stopping
Restoring model weights from the end of the best epoch: 92.
Training complete. Best epoch: 92 of 107. Best val_loss: 1.1758, val_accuracy: 0.5000

========== Evaluation: within-subject test / EMS0022 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         2         2         2         0
  min_intens         0         4         2         0
  medium_int         0         1         4         1
  max_intens         0         0         0         6

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      1.000     0.333     0.500         6
   min_intensity      0.571     0.667     0.615         6
medium_intensity      0.500     0.667     0.571         6
   max_intensity      0.857     1.000     0.923         6

        accuracy                          0.667        24
       macro avg      0.732     0.667     0.652        24
    weighted avg      0.732     0.667     0.652        24

Overall accuracy: 0.6667

Artifacts saved to /kaggle/working/within_all/EMS0022/

############################################################
# Subject 23/31: EMS0023
############################################################
Loaded EMS0023 from /kaggle/input/datasets/akablawi/ems-4class/EMS0023.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-7.97e-03, 8.09e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.99e-06, 6.65e-06]
  Per-channel std range:  [2.07e-05, 4.74e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3661 - loss: 1.3555 - val_accuracy: 0.1250 - val_loss: 1.3891 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.2946 - loss: 1.3289 - val_accuracy: 0.1250 - val_loss: 1.3874 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4107 - loss: 1.3043 - val_accuracy: 0.2083 - val_loss: 1.3852 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 58ms/step - accuracy: 0.4821 - loss: 1.2939 - val_accuracy: 0.2083 - val_loss: 1.3830 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.5000 - loss: 1.2665 - val_accuracy: 0.2500 - val_loss: 1.3810 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.2757 - val_accuracy: 0.2917 - val_loss: 1.3794 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.4643 - loss: 1.2481 - val_accuracy: 0.2917 - val_loss: 1.3783 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5357 - loss: 1.2216 - val_accuracy: 0.3333 - val_loss: 1.3777 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1868 - val_accuracy: 0.3333 - val_loss: 1.3771 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 61ms/step - accuracy: 0.5714 - loss: 1.1931 - val_accuracy: 0.2917 - val_loss: 1.3760 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1580 - val_accuracy: 0.3333 - val_loss: 1.3753 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.5982 - loss: 1.1346 - val_accuracy: 0.3333 - val_loss: 1.3748 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.1280 - val_accuracy: 0.3333 - val_loss: 1.3744 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.1085 - val_accuracy: 0.3750 - val_loss: 1.3727 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.5804 - loss: 1.0868 - val_accuracy: 0.3750 - val_loss: 1.3707 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.0740 - val_accuracy: 0.4583 - val_loss: 1.3694 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 1.0744 - val_accuracy: 0.3750 - val_loss: 1.3679 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0375 - val_accuracy: 0.2917 - val_loss: 1.3671 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.5982 - loss: 1.0463 - val_accuracy: 0.2917 - val_loss: 1.3643 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.6607 - loss: 1.0231 - val_accuracy: 0.3333 - val_loss: 1.3581 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 61ms/step - accuracy: 0.6786 - loss: 1.0086 - val_accuracy: 0.3333 - val_loss: 1.3538 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 62ms/step - accuracy: 0.6964 - loss: 1.0012 - val_accuracy: 0.3333 - val_loss: 1.3494 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 63ms/step - accuracy: 0.6786 - loss: 0.9703 - val_accuracy: 0.3333 - val_loss: 1.3471 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 63ms/step - accuracy: 0.6696 - loss: 0.9594 - val_accuracy: 0.2917 - val_loss: 1.3458 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 62ms/step - accuracy: 0.7232 - loss: 0.9448 - val_accuracy: 0.2917 - val_loss: 1.3420 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 62ms/step - accuracy: 0.6964 - loss: 0.9178 - val_accuracy: 0.2917 - val_loss: 1.3367 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 62ms/step - accuracy: 0.7232 - loss: 0.9049 - val_accuracy: 0.2917 - val_loss: 1.3327 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.9125 - val_accuracy: 0.2917 - val_loss: 1.3323 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.9157 - val_accuracy: 0.2917 - val_loss: 1.3321 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.6964 - loss: 0.9184 - val_accuracy: 0.2917 - val_loss: 1.3271 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.7321 - loss: 0.8951 - val_accuracy: 0.3333 - val_loss: 1.3190 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.8865 - val_accuracy: 0.3333 - val_loss: 1.3140 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 60ms/step - accuracy: 0.7679 - loss: 0.8723 - val_accuracy: 0.3333 - val_loss: 1.3098 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8691 - val_accuracy: 0.3333 - val_loss: 1.3062 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8629 - val_accuracy: 0.3333 - val_loss: 1.3064 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.8715 - val_accuracy: 0.3750 - val_loss: 1.3012 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8496 - val_accuracy: 0.3750 - val_loss: 1.3028 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 57ms/step - accuracy: 0.8125 - loss: 0.8171 - val_accuracy: 0.4167 - val_loss: 1.2989 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 57ms/step - accuracy: 0.7946 - loss: 0.8191 - val_accuracy: 0.4167 - val_loss: 1.2968 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 42ms/step - accuracy: 0.7857 - loss: 0.8113 - val_accuracy: 0.3750 - val_loss: 1.2999 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 57ms/step - accuracy: 0.7589 - loss: 0.8111 - val_accuracy: 0.4583 - val_loss: 1.2965 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8046 - val_accuracy: 0.5417 - val_loss: 1.2948 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.7845 - val_accuracy: 0.4167 - val_loss: 1.3002 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 42ms/step - accuracy: 0.7589 - loss: 0.7962 - val_accuracy: 0.4583 - val_loss: 1.3000 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 57ms/step - accuracy: 0.8036 - loss: 0.7790 - val_accuracy: 0.5000 - val_loss: 1.2909 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.7321 - val_accuracy: 0.4583 - val_loss: 1.2984 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.7365 - val_accuracy: 0.4583 - val_loss: 1.2850 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.7315 - val_accuracy: 0.5000 - val_loss: 1.2976 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.8214 - loss: 0.7407 - val_accuracy: 0.4583 - val_loss: 1.2947 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7451 - val_accuracy: 0.4167 - val_loss: 1.2859 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7208 - val_accuracy: 0.3750 - val_loss: 1.2968 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.7397 - val_accuracy: 0.3750 - val_loss: 1.2942 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7218 - val_accuracy: 0.3750 - val_loss: 1.2778 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6941 - val_accuracy: 0.3750 - val_loss: 1.2811 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 62ms/step - accuracy: 0.8571 - loss: 0.7078 - val_accuracy: 0.4583 - val_loss: 1.2727 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6950 - val_accuracy: 0.4167 - val_loss: 1.2774 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 44ms/step - accuracy: 0.9018 - loss: 0.6707 - val_accuracy: 0.4167 - val_loss: 1.2765 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6768 - val_accuracy: 0.3333 - val_loss: 1.2983 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.6779 - val_accuracy: 0.4583 - val_loss: 1.2737 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6775 - val_accuracy: 0.4167 - val_loss: 1.2803 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.6619 - val_accuracy: 0.4167 - val_loss: 1.2781 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 58ms/step - accuracy: 0.8661 - loss: 0.6405 - val_accuracy: 0.5000 - val_loss: 1.2561 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6480 - val_accuracy: 0.5000 - val_loss: 1.2633 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6487 - val_accuracy: 0.4583 - val_loss: 1.2630 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.8750 - loss: 0.6404 - val_accuracy: 0.4583 - val_loss: 1.3010 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 44ms/step - accuracy: 0.8214 - loss: 0.6652 - val_accuracy: 0.4583 - val_loss: 1.2687 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 42ms/step - accuracy: 0.8393 - loss: 0.6635 - val_accuracy: 0.5000 - val_loss: 1.2704 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.6427 - val_accuracy: 0.4583 - val_loss: 1.2836 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 42ms/step - accuracy: 0.8036 - loss: 0.6561 - val_accuracy: 0.4167 - val_loss: 1.2732 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6450 - val_accuracy: 0.4167 - val_loss: 1.2820 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.6338 - val_accuracy: 0.4583 - val_loss: 1.2349 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6172 - val_accuracy: 0.5000 - val_loss: 1.2507 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6243 - val_accuracy: 0.5000 - val_loss: 1.2733 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.8661 - loss: 0.5947 - val_accuracy: 0.5000 - val_loss: 1.2599 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.6003 - val_accuracy: 0.5000 - val_loss: 1.2653 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.6129 - val_accuracy: 0.4583 - val_loss: 1.2490 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.6030 - val_accuracy: 0.4583 - val_loss: 1.2627 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 41ms/step - accuracy: 0.8571 - loss: 0.5953 - val_accuracy: 0.4583 - val_loss: 1.2653 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5764 - val_accuracy: 0.4167 - val_loss: 1.2432 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5735 - val_accuracy: 0.4583 - val_loss: 1.2781 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 41ms/step - accuracy: 0.9375 - loss: 0.5565 - val_accuracy: 0.3750 - val_loss: 1.2881 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 41ms/step - accuracy: 0.9018 - loss: 0.5640 - val_accuracy: 0.4583 - val_loss: 1.2749 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 41ms/step - accuracy: 0.9196 - loss: 0.5377 - val_accuracy: 0.4583 - val_loss: 1.2719 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 41ms/step - accuracy: 0.8839 - loss: 0.5507 - val_accuracy: 0.4583 - val_loss: 1.2501 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 41ms/step - accuracy: 0.9018 - loss: 0.5767 - val_accuracy: 0.4583 - val_loss: 1.2765 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 41ms/step - accuracy: 0.9018 - loss: 0.5551 - val_accuracy: 0.4583 - val_loss: 1.2383 - learning_rate: 0.0010
Epoch 86: early stopping
Restoring model weights from the end of the best epoch: 71.
Training complete. Best epoch: 71 of 86. Best val_loss: 1.2349, val_accuracy: 0.4583

========== Evaluation: within-subject test / EMS0023 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         0         2         0
  min_intens         0         5         1         0
  medium_int         3         2         1         0
  max_intens         1         2         0         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.667     0.571         6
   min_intensity      0.556     0.833     0.667         6
medium_intensity      0.250     0.167     0.200         6
   max_intensity      1.000     0.500     0.667         6

        accuracy                          0.542        24
       macro avg      0.576     0.542     0.526        24
    weighted avg      0.576     0.542     0.526        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0023/

############################################################
# Subject 24/31: EMS0024
############################################################
Loaded EMS0024 from /kaggle/input/datasets/akablawi/ems-4class/EMS0024.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.54e-03, 7.32e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.66e-06, 6.50e-06]
  Per-channel std range:  [7.40e-06, 5.45e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2500 - loss: 1.5797 - val_accuracy: 0.2917 - val_loss: 1.3776 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.4107 - loss: 1.3034 - val_accuracy: 0.4167 - val_loss: 1.3693 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 58ms/step - accuracy: 0.5268 - loss: 1.2381 - val_accuracy: 0.5000 - val_loss: 1.3585 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 63ms/step - accuracy: 0.4911 - loss: 1.1822 - val_accuracy: 0.5417 - val_loss: 1.3448 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.1160 - val_accuracy: 0.5000 - val_loss: 1.3293 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0960 - val_accuracy: 0.4583 - val_loss: 1.3131 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5804 - loss: 1.0613 - val_accuracy: 0.5000 - val_loss: 1.2977 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 1.0308 - val_accuracy: 0.5000 - val_loss: 1.2814 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.7232 - loss: 0.9802 - val_accuracy: 0.5000 - val_loss: 1.2647 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 60ms/step - accuracy: 0.6518 - loss: 0.9622 - val_accuracy: 0.5000 - val_loss: 1.2490 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.6696 - loss: 0.9487 - val_accuracy: 0.5417 - val_loss: 1.2338 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9259 - val_accuracy: 0.5000 - val_loss: 1.2202 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 60ms/step - accuracy: 0.7232 - loss: 0.9080 - val_accuracy: 0.5000 - val_loss: 1.2071 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 66ms/step - accuracy: 0.7411 - loss: 0.8946 - val_accuracy: 0.5000 - val_loss: 1.1926 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 66ms/step - accuracy: 0.7500 - loss: 0.8575 - val_accuracy: 0.5000 - val_loss: 1.1806 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 63ms/step - accuracy: 0.7321 - loss: 0.8449 - val_accuracy: 0.4583 - val_loss: 1.1693 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8498 - val_accuracy: 0.5000 - val_loss: 1.1586 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 58ms/step - accuracy: 0.8036 - loss: 0.8288 - val_accuracy: 0.5000 - val_loss: 1.1501 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 59ms/step - accuracy: 0.6964 - loss: 0.8201 - val_accuracy: 0.5000 - val_loss: 1.1400 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 60ms/step - accuracy: 0.7679 - loss: 0.7931 - val_accuracy: 0.5000 - val_loss: 1.1278 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7612 - val_accuracy: 0.5000 - val_loss: 1.1189 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.7946 - loss: 0.7890 - val_accuracy: 0.5000 - val_loss: 1.1133 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 61ms/step - accuracy: 0.8125 - loss: 0.7633 - val_accuracy: 0.5000 - val_loss: 1.1074 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.7571 - val_accuracy: 0.5000 - val_loss: 1.0997 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7540 - val_accuracy: 0.5000 - val_loss: 1.0915 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7401 - val_accuracy: 0.5000 - val_loss: 1.0810 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.7191 - val_accuracy: 0.5000 - val_loss: 1.0729 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.7235 - val_accuracy: 0.5417 - val_loss: 1.0644 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7334 - val_accuracy: 0.5833 - val_loss: 1.0558 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.6929 - val_accuracy: 0.5833 - val_loss: 1.0533 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.6923 - val_accuracy: 0.6250 - val_loss: 1.0558 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6906 - val_accuracy: 0.6250 - val_loss: 1.0540 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.6906 - val_accuracy: 0.6250 - val_loss: 1.0467 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.6757 - val_accuracy: 0.5833 - val_loss: 1.0371 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.6790 - val_accuracy: 0.5833 - val_loss: 1.0338 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.6434 - val_accuracy: 0.5833 - val_loss: 1.0387 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.6634 - val_accuracy: 0.5833 - val_loss: 1.0383 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.6484 - val_accuracy: 0.5833 - val_loss: 1.0269 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.6488 - val_accuracy: 0.5833 - val_loss: 1.0165 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.6415 - val_accuracy: 0.5833 - val_loss: 1.0103 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 59ms/step - accuracy: 0.8571 - loss: 0.6518 - val_accuracy: 0.5833 - val_loss: 1.0052 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.6188 - val_accuracy: 0.5833 - val_loss: 1.0034 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 59ms/step - accuracy: 0.9018 - loss: 0.6178 - val_accuracy: 0.6250 - val_loss: 1.0028 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 58ms/step - accuracy: 0.8750 - loss: 0.6187 - val_accuracy: 0.6250 - val_loss: 0.9999 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 61ms/step - accuracy: 0.8571 - loss: 0.6336 - val_accuracy: 0.6250 - val_loss: 0.9998 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.6136 - val_accuracy: 0.5833 - val_loss: 1.0024 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.9107 - loss: 0.5959 - val_accuracy: 0.5833 - val_loss: 1.0025 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.5996 - val_accuracy: 0.5833 - val_loss: 0.9927 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.5869 - val_accuracy: 0.5833 - val_loss: 0.9913 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.5728 - val_accuracy: 0.5833 - val_loss: 0.9882 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.8839 - loss: 0.5782 - val_accuracy: 0.5833 - val_loss: 0.9842 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 57ms/step - accuracy: 0.8750 - loss: 0.5919 - val_accuracy: 0.5833 - val_loss: 0.9836 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5883 - val_accuracy: 0.5833 - val_loss: 0.9843 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5502 - val_accuracy: 0.5833 - val_loss: 0.9926 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5647 - val_accuracy: 0.5833 - val_loss: 0.9951 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5623 - val_accuracy: 0.5417 - val_loss: 0.9947 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5599 - val_accuracy: 0.5417 - val_loss: 0.9857 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 59ms/step - accuracy: 0.9196 - loss: 0.5517 - val_accuracy: 0.5833 - val_loss: 0.9695 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 60ms/step - accuracy: 0.9375 - loss: 0.5575 - val_accuracy: 0.5833 - val_loss: 0.9667 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 45ms/step - accuracy: 0.9107 - loss: 0.5559 - val_accuracy: 0.5417 - val_loss: 0.9734 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 47ms/step - accuracy: 0.9286 - loss: 0.5308 - val_accuracy: 0.5833 - val_loss: 0.9771 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 44ms/step - accuracy: 0.9286 - loss: 0.5394 - val_accuracy: 0.5833 - val_loss: 0.9783 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5225 - val_accuracy: 0.5417 - val_loss: 0.9859 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.5279 - val_accuracy: 0.5833 - val_loss: 0.9819 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.5122 - val_accuracy: 0.5833 - val_loss: 0.9724 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4918 - val_accuracy: 0.5833 - val_loss: 0.9688 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 58ms/step - accuracy: 0.9643 - loss: 0.4799 - val_accuracy: 0.5833 - val_loss: 0.9587 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 58ms/step - accuracy: 0.9643 - loss: 0.4936 - val_accuracy: 0.5833 - val_loss: 0.9498 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4845 - val_accuracy: 0.5833 - val_loss: 0.9579 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5064 - val_accuracy: 0.5833 - val_loss: 0.9599 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.4646 - val_accuracy: 0.5833 - val_loss: 0.9348 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 58ms/step - accuracy: 0.9464 - loss: 0.4522 - val_accuracy: 0.5833 - val_loss: 0.9307 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.4556 - val_accuracy: 0.5833 - val_loss: 0.9418 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4814 - val_accuracy: 0.5417 - val_loss: 0.9423 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4477 - val_accuracy: 0.5417 - val_loss: 0.9410 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 42ms/step - accuracy: 0.9196 - loss: 0.4648 - val_accuracy: 0.5417 - val_loss: 0.9430 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4536 - val_accuracy: 0.5000 - val_loss: 0.9467 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.4436 - val_accuracy: 0.5417 - val_loss: 0.9370 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.4360 - val_accuracy: 0.5417 - val_loss: 0.9252 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4368 - val_accuracy: 0.5417 - val_loss: 0.9280 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 1.0000 - loss: 0.4099 - val_accuracy: 0.5417 - val_loss: 0.9253 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 57ms/step - accuracy: 0.9732 - loss: 0.4121 - val_accuracy: 0.5833 - val_loss: 0.9080 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.4144 - val_accuracy: 0.5417 - val_loss: 0.9066 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 44ms/step - accuracy: 0.9821 - loss: 0.4133 - val_accuracy: 0.5833 - val_loss: 0.9104 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 45ms/step - accuracy: 0.9554 - loss: 0.3879 - val_accuracy: 0.5833 - val_loss: 0.9203 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.4077 - val_accuracy: 0.5833 - val_loss: 0.9277 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 45ms/step - accuracy: 0.9732 - loss: 0.3774 - val_accuracy: 0.5833 - val_loss: 0.9183 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3941 - val_accuracy: 0.5833 - val_loss: 0.9115 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 58ms/step - accuracy: 0.9821 - loss: 0.4024 - val_accuracy: 0.5833 - val_loss: 0.9024 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 60ms/step - accuracy: 0.9821 - loss: 0.3765 - val_accuracy: 0.5833 - val_loss: 0.8942 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 43ms/step - accuracy: 1.0000 - loss: 0.3735 - val_accuracy: 0.6250 - val_loss: 0.8964 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.3594 - val_accuracy: 0.6250 - val_loss: 0.8976 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.3559 - val_accuracy: 0.5833 - val_loss: 0.8969 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.3586 - val_accuracy: 0.5833 - val_loss: 0.8971 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 57ms/step - accuracy: 0.9911 - loss: 0.3522 - val_accuracy: 0.5833 - val_loss: 0.8930 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 58ms/step - accuracy: 0.9821 - loss: 0.3629 - val_accuracy: 0.5833 - val_loss: 0.8833 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 59ms/step - accuracy: 0.9643 - loss: 0.3783 - val_accuracy: 0.5833 - val_loss: 0.8795 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3436 - val_accuracy: 0.6250 - val_loss: 0.8815 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 44ms/step - accuracy: 0.9911 - loss: 0.3498 - val_accuracy: 0.6250 - val_loss: 0.8807 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 58ms/step - accuracy: 0.9911 - loss: 0.3302 - val_accuracy: 0.6250 - val_loss: 0.8778 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 58ms/step - accuracy: 0.9821 - loss: 0.3318 - val_accuracy: 0.5833 - val_loss: 0.8572 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.3169 - val_accuracy: 0.6250 - val_loss: 0.8760 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 42ms/step - accuracy: 1.0000 - loss: 0.3259 - val_accuracy: 0.6250 - val_loss: 0.8977 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3152 - val_accuracy: 0.6250 - val_loss: 0.9183 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.3209 - val_accuracy: 0.5833 - val_loss: 0.8790 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.3259 - val_accuracy: 0.6250 - val_loss: 0.8867 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3063 - val_accuracy: 0.6250 - val_loss: 0.8876 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.2816 - val_accuracy: 0.6250 - val_loss: 0.8845 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3073 - val_accuracy: 0.5833 - val_loss: 0.8821 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.3066 - val_accuracy: 0.5833 - val_loss: 0.9024 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 43ms/step - accuracy: 1.0000 - loss: 0.2917 - val_accuracy: 0.6250 - val_loss: 0.8921 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.2881 - val_accuracy: 0.6250 - val_loss: 0.8775 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 50ms/step - accuracy: 1.0000 - loss: 0.2647 - val_accuracy: 0.6250 - val_loss: 0.8955 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.2893 - val_accuracy: 0.6250 - val_loss: 0.8916 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 42ms/step - accuracy: 1.0000 - loss: 0.2823 - val_accuracy: 0.6250 - val_loss: 0.8977 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 42ms/step - accuracy: 0.9911 - loss: 0.2910 - val_accuracy: 0.6667 - val_loss: 0.9159 - learning_rate: 0.0010
Epoch 116: early stopping
Restoring model weights from the end of the best epoch: 101.
Training complete. Best epoch: 101 of 116. Best val_loss: 0.8572, val_accuracy: 0.5833

========== Evaluation: within-subject test / EMS0024 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         2         0         0
  min_intens         5         0         1         0
  medium_int         0         0         4         2
  max_intens         0         0         1         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.444     0.667     0.533         6
   min_intensity      0.000     0.000     0.000         6
medium_intensity      0.667     0.667     0.667         6
   max_intensity      0.714     0.833     0.769         6

        accuracy                          0.542        24
       macro avg      0.456     0.542     0.492        24
    weighted avg      0.456     0.542     0.492        24

Overall accuracy: 0.5417

Artifacts saved to /kaggle/working/within_all/EMS0024/

############################################################
# Subject 25/31: EMS0025
############################################################
Loaded EMS0025 from /kaggle/input/datasets/akablawi/ems-4class/EMS0025.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.42e-04, 3.83e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-7.23e-07, 7.66e-07]
  Per-channel std range:  [5.06e-06, 4.79e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2321 - loss: 1.5465 - val_accuracy: 0.2917 - val_loss: 1.3843 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3304 - loss: 1.3643 - val_accuracy: 0.3333 - val_loss: 1.3839 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.3393 - loss: 1.3526 - val_accuracy: 0.4167 - val_loss: 1.3833 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.4196 - loss: 1.3315 - val_accuracy: 0.3750 - val_loss: 1.3822 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.4554 - loss: 1.3107 - val_accuracy: 0.3750 - val_loss: 1.3804 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 61ms/step - accuracy: 0.5000 - loss: 1.2776 - val_accuracy: 0.3333 - val_loss: 1.3788 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 60ms/step - accuracy: 0.4554 - loss: 1.2657 - val_accuracy: 0.3333 - val_loss: 1.3768 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.5625 - loss: 1.2384 - val_accuracy: 0.3750 - val_loss: 1.3745 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5446 - loss: 1.1950 - val_accuracy: 0.4583 - val_loss: 1.3719 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.1851 - val_accuracy: 0.4583 - val_loss: 1.3688 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.1435 - val_accuracy: 0.4583 - val_loss: 1.3659 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 60ms/step - accuracy: 0.5804 - loss: 1.1212 - val_accuracy: 0.3750 - val_loss: 1.3626 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5893 - loss: 1.0859 - val_accuracy: 0.4167 - val_loss: 1.3589 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 1.0503 - val_accuracy: 0.4167 - val_loss: 1.3561 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.6429 - loss: 1.0521 - val_accuracy: 0.4167 - val_loss: 1.3498 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6250 - loss: 1.0110 - val_accuracy: 0.4583 - val_loss: 1.3417 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 0.9972 - val_accuracy: 0.4167 - val_loss: 1.3336 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9715 - val_accuracy: 0.4583 - val_loss: 1.3281 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9684 - val_accuracy: 0.5000 - val_loss: 1.3254 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.9097 - val_accuracy: 0.5000 - val_loss: 1.3215 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9378 - val_accuracy: 0.5000 - val_loss: 1.3142 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9122 - val_accuracy: 0.5000 - val_loss: 1.3093 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8863 - val_accuracy: 0.5000 - val_loss: 1.3062 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 60ms/step - accuracy: 0.7411 - loss: 0.8918 - val_accuracy: 0.5417 - val_loss: 1.3030 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.8584 - val_accuracy: 0.4583 - val_loss: 1.2950 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 61ms/step - accuracy: 0.7857 - loss: 0.8490 - val_accuracy: 0.4583 - val_loss: 1.2873 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8318 - val_accuracy: 0.4583 - val_loss: 1.2829 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 60ms/step - accuracy: 0.7768 - loss: 0.8367 - val_accuracy: 0.5000 - val_loss: 1.2787 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.8145 - val_accuracy: 0.4583 - val_loss: 1.2669 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8257 - val_accuracy: 0.5000 - val_loss: 1.2660 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.7883 - val_accuracy: 0.4583 - val_loss: 1.2693 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.8053 - val_accuracy: 0.4583 - val_loss: 1.2560 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.7519 - val_accuracy: 0.5000 - val_loss: 1.2512 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.7500 - loss: 0.8122 - val_accuracy: 0.5000 - val_loss: 1.2468 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.8036 - loss: 0.7736 - val_accuracy: 0.5417 - val_loss: 1.2403 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.7549 - val_accuracy: 0.5417 - val_loss: 1.2379 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 61ms/step - accuracy: 0.8304 - loss: 0.7310 - val_accuracy: 0.4583 - val_loss: 1.2335 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.7270 - val_accuracy: 0.5417 - val_loss: 1.2329 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.7473 - val_accuracy: 0.5417 - val_loss: 1.2333 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7331 - val_accuracy: 0.5417 - val_loss: 1.2247 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7313 - val_accuracy: 0.5000 - val_loss: 1.2367 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 44ms/step - accuracy: 0.8304 - loss: 0.7258 - val_accuracy: 0.5000 - val_loss: 1.2282 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.7178 - val_accuracy: 0.5417 - val_loss: 1.2191 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8393 - loss: 0.7040 - val_accuracy: 0.5000 - val_loss: 1.2273 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 58ms/step - accuracy: 0.8571 - loss: 0.7076 - val_accuracy: 0.5417 - val_loss: 1.2182 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 44ms/step - accuracy: 0.8571 - loss: 0.7230 - val_accuracy: 0.5417 - val_loss: 1.2249 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6916 - val_accuracy: 0.5000 - val_loss: 1.2357 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6634 - val_accuracy: 0.5000 - val_loss: 1.2248 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6772 - val_accuracy: 0.5000 - val_loss: 1.2216 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 57ms/step - accuracy: 0.8661 - loss: 0.6743 - val_accuracy: 0.5000 - val_loss: 1.2105 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 43ms/step - accuracy: 0.8304 - loss: 0.6948 - val_accuracy: 0.5000 - val_loss: 1.2162 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6542 - val_accuracy: 0.5417 - val_loss: 1.2194 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6735 - val_accuracy: 0.5417 - val_loss: 1.2206 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6450 - val_accuracy: 0.5417 - val_loss: 1.2169 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 60ms/step - accuracy: 0.8393 - loss: 0.6371 - val_accuracy: 0.5000 - val_loss: 1.2092 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6710 - val_accuracy: 0.5000 - val_loss: 1.2043 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.6493 - val_accuracy: 0.5000 - val_loss: 1.2357 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.6364 - val_accuracy: 0.5000 - val_loss: 1.2165 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 44ms/step - accuracy: 0.8482 - loss: 0.6457 - val_accuracy: 0.5417 - val_loss: 1.2134 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6326 - val_accuracy: 0.5417 - val_loss: 1.2093 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6223 - val_accuracy: 0.5417 - val_loss: 1.2302 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 44ms/step - accuracy: 0.8839 - loss: 0.6200 - val_accuracy: 0.5417 - val_loss: 1.2471 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6133 - val_accuracy: 0.5417 - val_loss: 1.2264 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.5830 - val_accuracy: 0.5417 - val_loss: 1.1980 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.6167 - val_accuracy: 0.5833 - val_loss: 1.2216 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 58ms/step - accuracy: 0.9018 - loss: 0.5869 - val_accuracy: 0.5417 - val_loss: 1.1965 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5968 - val_accuracy: 0.5833 - val_loss: 1.2427 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5776 - val_accuracy: 0.5000 - val_loss: 1.2215 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5754 - val_accuracy: 0.5833 - val_loss: 1.2344 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5457 - val_accuracy: 0.5833 - val_loss: 1.2269 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5805 - val_accuracy: 0.5833 - val_loss: 1.2335 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5678 - val_accuracy: 0.5833 - val_loss: 1.2461 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5476 - val_accuracy: 0.5833 - val_loss: 1.2167 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5472 - val_accuracy: 0.5833 - val_loss: 1.2620 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.8839 - loss: 0.5671 - val_accuracy: 0.5833 - val_loss: 1.2388 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5504 - val_accuracy: 0.5833 - val_loss: 1.2312 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 43ms/step - accuracy: 0.9196 - loss: 0.5386 - val_accuracy: 0.5833 - val_loss: 1.2378 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.9286 - loss: 0.5445 - val_accuracy: 0.5833 - val_loss: 1.2475 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5272 - val_accuracy: 0.6250 - val_loss: 1.2776 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5141 - val_accuracy: 0.5833 - val_loss: 1.2413 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 42ms/step - accuracy: 0.9018 - loss: 0.5415 - val_accuracy: 0.5833 - val_loss: 1.2455 - learning_rate: 0.0010
Epoch 81: early stopping
Restoring model weights from the end of the best epoch: 66.
Training complete. Best epoch: 66 of 81. Best val_loss: 1.1965, val_accuracy: 0.5417

========== Evaluation: within-subject test / EMS0025 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         5         0         0         1
  min_intens         2         4         0         0
  medium_int         0         2         2         2
  max_intens         1         0         0         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.625     0.833     0.714         6
   min_intensity      0.667     0.667     0.667         6
medium_intensity      1.000     0.333     0.500         6
   max_intensity      0.625     0.833     0.714         6

        accuracy                          0.667        24
       macro avg      0.729     0.667     0.649        24
    weighted avg      0.729     0.667     0.649        24

Overall accuracy: 0.6667

Artifacts saved to /kaggle/working/within_all/EMS0025/

############################################################
# Subject 26/31: EMS0026
############################################################
Loaded EMS0026 from /kaggle/input/datasets/akablawi/ems-4class/EMS0026.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.27e-03, 2.78e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-5.36e-07, 8.27e-07]
  Per-channel std range:  [5.05e-06, 4.18e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3036 - loss: 1.4341 - val_accuracy: 0.0833 - val_loss: 1.3878 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 47ms/step - accuracy: 0.2946 - loss: 1.3642 - val_accuracy: 0.0833 - val_loss: 1.3894 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 45ms/step - accuracy: 0.3571 - loss: 1.3394 - val_accuracy: 0.0833 - val_loss: 1.3901 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 48ms/step - accuracy: 0.4196 - loss: 1.3324 - val_accuracy: 0.2083 - val_loss: 1.3903 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 44ms/step - accuracy: 0.4464 - loss: 1.2889 - val_accuracy: 0.2500 - val_loss: 1.3905 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 44ms/step - accuracy: 0.4196 - loss: 1.2896 - val_accuracy: 0.2917 - val_loss: 1.3905 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 43ms/step - accuracy: 0.4554 - loss: 1.2782 - val_accuracy: 0.2917 - val_loss: 1.3902 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 43ms/step - accuracy: 0.4464 - loss: 1.2749 - val_accuracy: 0.2917 - val_loss: 1.3898 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 43ms/step - accuracy: 0.5268 - loss: 1.2325 - val_accuracy: 0.2500 - val_loss: 1.3908 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 44ms/step - accuracy: 0.5089 - loss: 1.2075 - val_accuracy: 0.2500 - val_loss: 1.3913 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 43ms/step - accuracy: 0.4375 - loss: 1.2009 - val_accuracy: 0.2500 - val_loss: 1.3908 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 44ms/step - accuracy: 0.5357 - loss: 1.1848 - val_accuracy: 0.2500 - val_loss: 1.3896 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 44ms/step - accuracy: 0.5536 - loss: 1.1369 - val_accuracy: 0.2500 - val_loss: 1.3884 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 43ms/step - accuracy: 0.5982 - loss: 1.1355 - val_accuracy: 0.2917 - val_loss: 1.3880 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6161 - loss: 1.1139 - val_accuracy: 0.2917 - val_loss: 1.3864 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.5714 - loss: 1.1108 - val_accuracy: 0.2500 - val_loss: 1.3847 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.5893 - loss: 1.0975 - val_accuracy: 0.2500 - val_loss: 1.3830 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 43ms/step - accuracy: 0.5982 - loss: 1.0926 - val_accuracy: 0.2917 - val_loss: 1.3832 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 43ms/step - accuracy: 0.6250 - loss: 1.0414 - val_accuracy: 0.2917 - val_loss: 1.3840 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 43ms/step - accuracy: 0.6339 - loss: 1.0461 - val_accuracy: 0.2500 - val_loss: 1.3868 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 44ms/step - accuracy: 0.6696 - loss: 1.0248 - val_accuracy: 0.2500 - val_loss: 1.3891 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 42ms/step - accuracy: 0.6250 - loss: 1.0364 - val_accuracy: 0.2500 - val_loss: 1.3851 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 42ms/step - accuracy: 0.6607 - loss: 1.0033 - val_accuracy: 0.2500 - val_loss: 1.3835 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 43ms/step - accuracy: 0.6429 - loss: 0.9735 - val_accuracy: 0.2083 - val_loss: 1.3901 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 43ms/step - accuracy: 0.6429 - loss: 0.9992 - val_accuracy: 0.2083 - val_loss: 1.3919 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 43ms/step - accuracy: 0.6696 - loss: 0.9637 - val_accuracy: 0.3333 - val_loss: 1.3840 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.6518 - loss: 0.9719 - val_accuracy: 0.3333 - val_loss: 1.3800 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 43ms/step - accuracy: 0.6696 - loss: 0.9234 - val_accuracy: 0.3333 - val_loss: 1.3860 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.9239 - val_accuracy: 0.3333 - val_loss: 1.3887 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.7411 - loss: 0.8861 - val_accuracy: 0.3750 - val_loss: 1.3827 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 43ms/step - accuracy: 0.7143 - loss: 0.8954 - val_accuracy: 0.3750 - val_loss: 1.3852 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8979 - val_accuracy: 0.3333 - val_loss: 1.3878 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8411 - val_accuracy: 0.3333 - val_loss: 1.3870 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 45ms/step - accuracy: 0.7143 - loss: 0.8835 - val_accuracy: 0.3333 - val_loss: 1.3841 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 44ms/step - accuracy: 0.7054 - loss: 0.8669 - val_accuracy: 0.3333 - val_loss: 1.3823 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.6875 - loss: 0.8692 - val_accuracy: 0.3333 - val_loss: 1.3852 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.8308 - val_accuracy: 0.3333 - val_loss: 1.3898 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 43ms/step - accuracy: 0.8036 - loss: 0.7940 - val_accuracy: 0.2500 - val_loss: 1.4014 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.8507 - val_accuracy: 0.2500 - val_loss: 1.4079 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.7895 - val_accuracy: 0.3750 - val_loss: 1.3992 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.7321 - loss: 0.8273 - val_accuracy: 0.3750 - val_loss: 1.3937 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 43ms/step - accuracy: 0.7500 - loss: 0.8049 - val_accuracy: 0.4167 - val_loss: 1.3930 - learning_rate: 0.0010
Epoch 42: early stopping
Restoring model weights from the end of the best epoch: 27.
Training complete. Best epoch: 27 of 42. Best val_loss: 1.3800, val_accuracy: 0.3333

========== Evaluation: within-subject test / EMS0026 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         2         0         1
  min_intens         3         1         1         1
  medium_int         1         0         3         2
  max_intens         2         0         0         4

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.333     0.500     0.400         6
   min_intensity      0.333     0.167     0.222         6
medium_intensity      0.750     0.500     0.600         6
   max_intensity      0.500     0.667     0.571         6

        accuracy                          0.458        24
       macro avg      0.479     0.458     0.448        24
    weighted avg      0.479     0.458     0.448        24

Overall accuracy: 0.4583

Artifacts saved to /kaggle/working/within_all/EMS0026/

############################################################
# Subject 27/31: EMS0027
############################################################
Loaded EMS0027 from /kaggle/input/datasets/akablawi/ems-4class/EMS0027.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-3.38e-04, 3.64e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.15e-06, 2.30e-06]
  Per-channel std range:  [5.29e-06, 4.29e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2411 - loss: 1.4312 - val_accuracy: 0.2500 - val_loss: 1.3814 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3750 - loss: 1.3511 - val_accuracy: 0.2917 - val_loss: 1.3767 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 60ms/step - accuracy: 0.4107 - loss: 1.3176 - val_accuracy: 0.2917 - val_loss: 1.3706 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.3661 - loss: 1.3066 - val_accuracy: 0.3333 - val_loss: 1.3629 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4554 - loss: 1.2543 - val_accuracy: 0.3750 - val_loss: 1.3531 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 60ms/step - accuracy: 0.4643 - loss: 1.2368 - val_accuracy: 0.3750 - val_loss: 1.3428 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 61ms/step - accuracy: 0.4821 - loss: 1.2269 - val_accuracy: 0.3333 - val_loss: 1.3338 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.4643 - loss: 1.1900 - val_accuracy: 0.3333 - val_loss: 1.3257 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 65ms/step - accuracy: 0.5536 - loss: 1.1563 - val_accuracy: 0.3333 - val_loss: 1.3182 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.1449 - val_accuracy: 0.3333 - val_loss: 1.3120 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.5179 - loss: 1.1418 - val_accuracy: 0.3333 - val_loss: 1.3057 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.5268 - loss: 1.1452 - val_accuracy: 0.3333 - val_loss: 1.2987 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5982 - loss: 1.1092 - val_accuracy: 0.3333 - val_loss: 1.2918 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5357 - loss: 1.1230 - val_accuracy: 0.3750 - val_loss: 1.2867 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0856 - val_accuracy: 0.3750 - val_loss: 1.2821 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 44ms/step - accuracy: 0.5714 - loss: 1.1092 - val_accuracy: 0.3750 - val_loss: 1.2825 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.6339 - loss: 1.0561 - val_accuracy: 0.4167 - val_loss: 1.2816 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.5982 - loss: 1.0520 - val_accuracy: 0.4167 - val_loss: 1.2784 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.6518 - loss: 1.0155 - val_accuracy: 0.4167 - val_loss: 1.2714 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.6250 - loss: 1.0315 - val_accuracy: 0.3750 - val_loss: 1.2701 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 44ms/step - accuracy: 0.6786 - loss: 1.0092 - val_accuracy: 0.3750 - val_loss: 1.2712 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 43ms/step - accuracy: 0.6071 - loss: 0.9853 - val_accuracy: 0.3750 - val_loss: 1.2730 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 43ms/step - accuracy: 0.7500 - loss: 0.9641 - val_accuracy: 0.4167 - val_loss: 1.2793 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 43ms/step - accuracy: 0.7054 - loss: 0.9649 - val_accuracy: 0.3750 - val_loss: 1.2722 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 0.9460 - val_accuracy: 0.3750 - val_loss: 1.2686 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 44ms/step - accuracy: 0.7143 - loss: 0.9273 - val_accuracy: 0.3333 - val_loss: 1.2783 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 43ms/step - accuracy: 0.6786 - loss: 0.9453 - val_accuracy: 0.3333 - val_loss: 1.2783 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.9181 - val_accuracy: 0.3750 - val_loss: 1.2717 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.8928 - val_accuracy: 0.3750 - val_loss: 1.2730 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 44ms/step - accuracy: 0.7679 - loss: 0.8836 - val_accuracy: 0.3750 - val_loss: 1.2770 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 45ms/step - accuracy: 0.7143 - loss: 0.8593 - val_accuracy: 0.4167 - val_loss: 1.2742 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8531 - val_accuracy: 0.4167 - val_loss: 1.2781 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 44ms/step - accuracy: 0.7857 - loss: 0.8537 - val_accuracy: 0.4167 - val_loss: 1.2798 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7589 - loss: 0.8496 - val_accuracy: 0.3750 - val_loss: 1.2745 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.8362 - val_accuracy: 0.4167 - val_loss: 1.2876 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.8118 - val_accuracy: 0.4167 - val_loss: 1.2859 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.8129 - val_accuracy: 0.4167 - val_loss: 1.2844 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 44ms/step - accuracy: 0.8036 - loss: 0.8026 - val_accuracy: 0.3750 - val_loss: 1.2929 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 43ms/step - accuracy: 0.8125 - loss: 0.8249 - val_accuracy: 0.3333 - val_loss: 1.2791 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 43ms/step - accuracy: 0.7946 - loss: 0.7994 - val_accuracy: 0.3333 - val_loss: 1.2877 - learning_rate: 0.0010
Epoch 40: early stopping
Restoring model weights from the end of the best epoch: 25.
Training complete. Best epoch: 25 of 40. Best val_loss: 1.2686, val_accuracy: 0.3750

========== Evaluation: within-subject test / EMS0027 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         1         2         0
  min_intens         0         3         3         0
  medium_int         1         1         4         0
  max_intens         2         0         3         1

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.500     0.500         6
   min_intensity      0.600     0.500     0.545         6
medium_intensity      0.333     0.667     0.444         6
   max_intensity      1.000     0.167     0.286         6

        accuracy                          0.458        24
       macro avg      0.608     0.458     0.444        24
    weighted avg      0.608     0.458     0.444        24

Overall accuracy: 0.4583

Artifacts saved to /kaggle/working/within_all/EMS0027/

############################################################
# Subject 28/31: EMS0028
############################################################
Loaded EMS0028 from /kaggle/input/datasets/akablawi/ems-4class/EMS0028.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.91e-03, 1.09e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.68e-06, 2.14e-06]
  Per-channel std range:  [7.26e-06, 7.74e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3125 - loss: 1.4353 - val_accuracy: 0.3750 - val_loss: 1.3812 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 61ms/step - accuracy: 0.4018 - loss: 1.3347 - val_accuracy: 0.4167 - val_loss: 1.3760 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.5893 - loss: 1.2828 - val_accuracy: 0.4583 - val_loss: 1.3693 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.5179 - loss: 1.2699 - val_accuracy: 0.4583 - val_loss: 1.3606 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 60ms/step - accuracy: 0.5804 - loss: 1.2391 - val_accuracy: 0.5417 - val_loss: 1.3507 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.1880 - val_accuracy: 0.5417 - val_loss: 1.3396 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.5446 - loss: 1.1781 - val_accuracy: 0.5833 - val_loss: 1.3281 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 1.1221 - val_accuracy: 0.5833 - val_loss: 1.3157 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1144 - val_accuracy: 0.5000 - val_loss: 1.3008 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 61ms/step - accuracy: 0.6696 - loss: 1.0685 - val_accuracy: 0.5000 - val_loss: 1.2846 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 60ms/step - accuracy: 0.6429 - loss: 1.0625 - val_accuracy: 0.5417 - val_loss: 1.2688 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 65ms/step - accuracy: 0.6607 - loss: 1.0088 - val_accuracy: 0.5000 - val_loss: 1.2550 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 1.0080 - val_accuracy: 0.5000 - val_loss: 1.2412 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 60ms/step - accuracy: 0.6786 - loss: 0.9869 - val_accuracy: 0.5000 - val_loss: 1.2261 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 0.9755 - val_accuracy: 0.5000 - val_loss: 1.2093 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9409 - val_accuracy: 0.5000 - val_loss: 1.1956 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 60ms/step - accuracy: 0.7321 - loss: 0.9058 - val_accuracy: 0.5417 - val_loss: 1.1853 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.7411 - loss: 0.8824 - val_accuracy: 0.5417 - val_loss: 1.1741 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.7589 - loss: 0.8624 - val_accuracy: 0.5417 - val_loss: 1.1601 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.7589 - loss: 0.8514 - val_accuracy: 0.5417 - val_loss: 1.1525 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 60ms/step - accuracy: 0.7589 - loss: 0.8493 - val_accuracy: 0.5417 - val_loss: 1.1451 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.8036 - loss: 0.8273 - val_accuracy: 0.5417 - val_loss: 1.1273 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.8164 - val_accuracy: 0.5833 - val_loss: 1.1202 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 60ms/step - accuracy: 0.7589 - loss: 0.7910 - val_accuracy: 0.5833 - val_loss: 1.1148 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8242 - val_accuracy: 0.5417 - val_loss: 1.1050 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 60ms/step - accuracy: 0.8036 - loss: 0.7852 - val_accuracy: 0.5417 - val_loss: 1.0939 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.7688 - val_accuracy: 0.5833 - val_loss: 1.0779 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.7681 - val_accuracy: 0.5833 - val_loss: 1.0662 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7285 - val_accuracy: 0.5833 - val_loss: 1.0595 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 60ms/step - accuracy: 0.8393 - loss: 0.7386 - val_accuracy: 0.5417 - val_loss: 1.0525 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7249 - val_accuracy: 0.5417 - val_loss: 1.0440 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.7328 - val_accuracy: 0.5833 - val_loss: 1.0403 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7092 - val_accuracy: 0.5833 - val_loss: 1.0392 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 60ms/step - accuracy: 0.8750 - loss: 0.6940 - val_accuracy: 0.5833 - val_loss: 1.0340 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6858 - val_accuracy: 0.5833 - val_loss: 1.0304 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 61ms/step - accuracy: 0.8482 - loss: 0.6782 - val_accuracy: 0.5833 - val_loss: 1.0239 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.6614 - val_accuracy: 0.5833 - val_loss: 1.0161 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.8661 - loss: 0.6663 - val_accuracy: 0.5833 - val_loss: 1.0086 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 60ms/step - accuracy: 0.8929 - loss: 0.6513 - val_accuracy: 0.6250 - val_loss: 1.0064 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 61ms/step - accuracy: 0.8839 - loss: 0.6446 - val_accuracy: 0.5833 - val_loss: 0.9930 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6330 - val_accuracy: 0.6667 - val_loss: 0.9816 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 60ms/step - accuracy: 0.8839 - loss: 0.6220 - val_accuracy: 0.6667 - val_loss: 0.9790 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 62ms/step - accuracy: 0.9018 - loss: 0.6163 - val_accuracy: 0.6667 - val_loss: 0.9758 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 61ms/step - accuracy: 0.8929 - loss: 0.6162 - val_accuracy: 0.7083 - val_loss: 0.9663 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.9196 - loss: 0.5799 - val_accuracy: 0.7083 - val_loss: 0.9604 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 60ms/step - accuracy: 0.8929 - loss: 0.5891 - val_accuracy: 0.7083 - val_loss: 0.9591 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.5988 - val_accuracy: 0.7083 - val_loss: 0.9596 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.5847 - val_accuracy: 0.7083 - val_loss: 0.9506 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.5866 - val_accuracy: 0.7083 - val_loss: 0.9527 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 44ms/step - accuracy: 0.8750 - loss: 0.5506 - val_accuracy: 0.7083 - val_loss: 0.9541 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 60ms/step - accuracy: 0.9286 - loss: 0.5467 - val_accuracy: 0.7083 - val_loss: 0.9326 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 61ms/step - accuracy: 0.9286 - loss: 0.5627 - val_accuracy: 0.7083 - val_loss: 0.9172 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.5319 - val_accuracy: 0.7500 - val_loss: 0.9205 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5104 - val_accuracy: 0.6667 - val_loss: 0.9196 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 61ms/step - accuracy: 0.9286 - loss: 0.5316 - val_accuracy: 0.7500 - val_loss: 0.9059 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 60ms/step - accuracy: 0.9196 - loss: 0.5192 - val_accuracy: 0.7500 - val_loss: 0.8942 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 45ms/step - accuracy: 0.9375 - loss: 0.4911 - val_accuracy: 0.7083 - val_loss: 0.8986 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 60ms/step - accuracy: 0.9107 - loss: 0.5209 - val_accuracy: 0.7083 - val_loss: 0.8816 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 44ms/step - accuracy: 0.9196 - loss: 0.4826 - val_accuracy: 0.7083 - val_loss: 0.8853 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 45ms/step - accuracy: 0.9375 - loss: 0.4971 - val_accuracy: 0.7083 - val_loss: 0.8902 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 63ms/step - accuracy: 0.9196 - loss: 0.4943 - val_accuracy: 0.7083 - val_loss: 0.8731 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 45ms/step - accuracy: 0.9286 - loss: 0.4858 - val_accuracy: 0.7083 - val_loss: 0.8757 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.4618 - val_accuracy: 0.6667 - val_loss: 0.8946 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 45ms/step - accuracy: 0.9554 - loss: 0.4789 - val_accuracy: 0.7083 - val_loss: 0.8748 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 60ms/step - accuracy: 0.9554 - loss: 0.4704 - val_accuracy: 0.7083 - val_loss: 0.8723 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 45ms/step - accuracy: 0.9464 - loss: 0.4645 - val_accuracy: 0.7500 - val_loss: 0.8847 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.4788 - val_accuracy: 0.7083 - val_loss: 0.8742 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 61ms/step - accuracy: 0.9375 - loss: 0.4721 - val_accuracy: 0.7083 - val_loss: 0.8616 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.4512 - val_accuracy: 0.7917 - val_loss: 0.8485 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.4238 - val_accuracy: 0.7917 - val_loss: 0.8535 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.4388 - val_accuracy: 0.7083 - val_loss: 0.8573 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 46ms/step - accuracy: 0.9375 - loss: 0.4336 - val_accuracy: 0.7083 - val_loss: 0.8663 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 46ms/step - accuracy: 0.9464 - loss: 0.4290 - val_accuracy: 0.7500 - val_loss: 0.8669 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 60ms/step - accuracy: 0.9464 - loss: 0.4315 - val_accuracy: 0.7083 - val_loss: 0.8449 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4339 - val_accuracy: 0.7083 - val_loss: 0.8605 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4186 - val_accuracy: 0.6667 - val_loss: 0.8617 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 60ms/step - accuracy: 0.9464 - loss: 0.4186 - val_accuracy: 0.7500 - val_loss: 0.8144 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.4064 - val_accuracy: 0.7500 - val_loss: 0.8009 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.4164 - val_accuracy: 0.7500 - val_loss: 0.8356 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.4072 - val_accuracy: 0.7083 - val_loss: 0.8280 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.4183 - val_accuracy: 0.7500 - val_loss: 0.7967 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.3818 - val_accuracy: 0.7500 - val_loss: 0.8029 - learning_rate: 0.0010
Epoch 83/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.3778 - val_accuracy: 0.7083 - val_loss: 0.8261 - learning_rate: 0.0010
Epoch 84/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.3921 - val_accuracy: 0.7083 - val_loss: 0.8339 - learning_rate: 0.0010
Epoch 85/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3878 - val_accuracy: 0.7083 - val_loss: 0.8478 - learning_rate: 0.0010
Epoch 86/500
4/4 - 0s - 44ms/step - accuracy: 0.9821 - loss: 0.3491 - val_accuracy: 0.7500 - val_loss: 0.8582 - learning_rate: 0.0010
Epoch 87/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.3714 - val_accuracy: 0.7500 - val_loss: 0.8253 - learning_rate: 0.0010
Epoch 88/500
4/4 - 0s - 60ms/step - accuracy: 0.9821 - loss: 0.3696 - val_accuracy: 0.7917 - val_loss: 0.7940 - learning_rate: 0.0010
Epoch 89/500
4/4 - 0s - 59ms/step - accuracy: 0.9643 - loss: 0.3728 - val_accuracy: 0.7917 - val_loss: 0.7805 - learning_rate: 0.0010
Epoch 90/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3543 - val_accuracy: 0.7500 - val_loss: 0.8079 - learning_rate: 0.0010
Epoch 91/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3715 - val_accuracy: 0.7500 - val_loss: 0.8299 - learning_rate: 0.0010
Epoch 92/500
4/4 - 0s - 44ms/step - accuracy: 0.9464 - loss: 0.3692 - val_accuracy: 0.7917 - val_loss: 0.8123 - learning_rate: 0.0010
Epoch 93/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3440 - val_accuracy: 0.7917 - val_loss: 0.8402 - learning_rate: 0.0010
Epoch 94/500
4/4 - 0s - 44ms/step - accuracy: 0.9643 - loss: 0.3248 - val_accuracy: 0.7917 - val_loss: 0.8324 - learning_rate: 0.0010
Epoch 95/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3276 - val_accuracy: 0.7917 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 96/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3344 - val_accuracy: 0.7083 - val_loss: 0.8057 - learning_rate: 0.0010
Epoch 97/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3369 - val_accuracy: 0.7917 - val_loss: 0.8052 - learning_rate: 0.0010
Epoch 98/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3287 - val_accuracy: 0.7917 - val_loss: 0.8057 - learning_rate: 0.0010
Epoch 99/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.3383 - val_accuracy: 0.7917 - val_loss: 0.7902 - learning_rate: 0.0010
Epoch 100/500
4/4 - 0s - 44ms/step - accuracy: 0.9554 - loss: 0.3284 - val_accuracy: 0.7083 - val_loss: 0.8089 - learning_rate: 0.0010
Epoch 101/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3135 - val_accuracy: 0.7500 - val_loss: 0.8033 - learning_rate: 0.0010
Epoch 102/500
4/4 - 0s - 59ms/step - accuracy: 0.9554 - loss: 0.3394 - val_accuracy: 0.7917 - val_loss: 0.7416 - learning_rate: 0.0010
Epoch 103/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.3283 - val_accuracy: 0.7917 - val_loss: 0.7605 - learning_rate: 0.0010
Epoch 104/500
4/4 - 0s - 46ms/step - accuracy: 0.9464 - loss: 0.3499 - val_accuracy: 0.7083 - val_loss: 0.8106 - learning_rate: 0.0010
Epoch 105/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.2945 - val_accuracy: 0.7083 - val_loss: 0.8486 - learning_rate: 0.0010
Epoch 106/500
4/4 - 0s - 48ms/step - accuracy: 0.9821 - loss: 0.3147 - val_accuracy: 0.7500 - val_loss: 0.8440 - learning_rate: 0.0010
Epoch 107/500
4/4 - 0s - 42ms/step - accuracy: 0.9821 - loss: 0.3040 - val_accuracy: 0.6667 - val_loss: 0.8208 - learning_rate: 0.0010
Epoch 108/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3012 - val_accuracy: 0.7500 - val_loss: 0.7952 - learning_rate: 0.0010
Epoch 109/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.3055 - val_accuracy: 0.7917 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 110/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3172 - val_accuracy: 0.7917 - val_loss: 0.7842 - learning_rate: 0.0010
Epoch 111/500
4/4 - 0s - 42ms/step - accuracy: 0.9732 - loss: 0.2964 - val_accuracy: 0.7500 - val_loss: 0.8120 - learning_rate: 0.0010
Epoch 112/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3143 - val_accuracy: 0.7500 - val_loss: 0.7821 - learning_rate: 0.0010
Epoch 113/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.3173 - val_accuracy: 0.6667 - val_loss: 0.8095 - learning_rate: 0.0010
Epoch 114/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.2905 - val_accuracy: 0.6667 - val_loss: 0.8115 - learning_rate: 0.0010
Epoch 115/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.3119 - val_accuracy: 0.7083 - val_loss: 0.8307 - learning_rate: 0.0010
Epoch 116/500
4/4 - 0s - 43ms/step - accuracy: 0.9911 - loss: 0.2880 - val_accuracy: 0.6667 - val_loss: 0.8093 - learning_rate: 0.0010
Epoch 117/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.2896 - val_accuracy: 0.7083 - val_loss: 0.7901 - learning_rate: 0.0010
Epoch 117: early stopping
Restoring model weights from the end of the best epoch: 102.
Training complete. Best epoch: 102 of 117. Best val_loss: 0.7416, val_accuracy: 0.7917

========== Evaluation: within-subject test / EMS0028 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         5         1         0         0
  min_intens         3         2         1         0
  medium_int         2         0         3         1
  max_intens         0         0         1         5

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.500     0.833     0.625         6
   min_intensity      0.667     0.333     0.444         6
medium_intensity      0.600     0.500     0.545         6
   max_intensity      0.833     0.833     0.833         6

        accuracy                          0.625        24
       macro avg      0.650     0.625     0.612        24
    weighted avg      0.650     0.625     0.612        24

Overall accuracy: 0.6250

Artifacts saved to /kaggle/working/within_all/EMS0028/

############################################################
# Subject 29/31: EMS0029
############################################################
Loaded EMS0029 from /kaggle/input/datasets/akablawi/ems-4class/EMS0029.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.60e-03, 1.07e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.10e-06, 1.33e-06]
  Per-channel std range:  [6.72e-06, 1.24e-04]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2589 - loss: 1.5211 - val_accuracy: 0.2500 - val_loss: 1.3860 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.2857 - loss: 1.3721 - val_accuracy: 0.3333 - val_loss: 1.3835 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.4375 - loss: 1.3304 - val_accuracy: 0.3750 - val_loss: 1.3811 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.2913 - val_accuracy: 0.3750 - val_loss: 1.3787 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.2483 - val_accuracy: 0.3333 - val_loss: 1.3758 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.2050 - val_accuracy: 0.2917 - val_loss: 1.3716 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.1624 - val_accuracy: 0.2917 - val_loss: 1.3664 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 60ms/step - accuracy: 0.5893 - loss: 1.1352 - val_accuracy: 0.2917 - val_loss: 1.3604 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 59ms/step - accuracy: 0.6875 - loss: 1.0825 - val_accuracy: 0.3333 - val_loss: 1.3543 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.6339 - loss: 1.0560 - val_accuracy: 0.3333 - val_loss: 1.3489 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.6696 - loss: 1.0231 - val_accuracy: 0.3333 - val_loss: 1.3424 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 59ms/step - accuracy: 0.6429 - loss: 1.0004 - val_accuracy: 0.3750 - val_loss: 1.3344 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.6786 - loss: 0.9754 - val_accuracy: 0.3750 - val_loss: 1.3231 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 61ms/step - accuracy: 0.6964 - loss: 0.9396 - val_accuracy: 0.3750 - val_loss: 1.3076 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 59ms/step - accuracy: 0.7054 - loss: 0.9321 - val_accuracy: 0.3750 - val_loss: 1.2926 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.7411 - loss: 0.9090 - val_accuracy: 0.4167 - val_loss: 1.2820 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 58ms/step - accuracy: 0.7321 - loss: 0.8923 - val_accuracy: 0.4167 - val_loss: 1.2750 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 60ms/step - accuracy: 0.7589 - loss: 0.8604 - val_accuracy: 0.4167 - val_loss: 1.2697 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.8610 - val_accuracy: 0.4167 - val_loss: 1.2663 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 58ms/step - accuracy: 0.7500 - loss: 0.8430 - val_accuracy: 0.4167 - val_loss: 1.2518 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8139 - val_accuracy: 0.4583 - val_loss: 1.2301 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 60ms/step - accuracy: 0.8125 - loss: 0.8064 - val_accuracy: 0.4583 - val_loss: 1.2189 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.8016 - val_accuracy: 0.4583 - val_loss: 1.2103 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.7857 - val_accuracy: 0.5000 - val_loss: 1.1997 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7689 - val_accuracy: 0.5000 - val_loss: 1.1852 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7946 - loss: 0.7595 - val_accuracy: 0.5000 - val_loss: 1.1767 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.7453 - val_accuracy: 0.5000 - val_loss: 1.1735 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.7343 - val_accuracy: 0.5417 - val_loss: 1.1641 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.7168 - val_accuracy: 0.5000 - val_loss: 1.1492 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 60ms/step - accuracy: 0.8571 - loss: 0.7281 - val_accuracy: 0.4583 - val_loss: 1.1470 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 46ms/step - accuracy: 0.8214 - loss: 0.7192 - val_accuracy: 0.4583 - val_loss: 1.1551 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 44ms/step - accuracy: 0.7946 - loss: 0.7182 - val_accuracy: 0.5000 - val_loss: 1.1559 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6929 - val_accuracy: 0.5000 - val_loss: 1.1479 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 59ms/step - accuracy: 0.8125 - loss: 0.7008 - val_accuracy: 0.4583 - val_loss: 1.1467 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.8304 - loss: 0.6865 - val_accuracy: 0.4583 - val_loss: 1.1423 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6673 - val_accuracy: 0.4583 - val_loss: 1.1474 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 59ms/step - accuracy: 0.8661 - loss: 0.6509 - val_accuracy: 0.4583 - val_loss: 1.1394 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 60ms/step - accuracy: 0.8482 - loss: 0.6320 - val_accuracy: 0.4583 - val_loss: 1.1319 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.6474 - val_accuracy: 0.4583 - val_loss: 1.1220 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 44ms/step - accuracy: 0.8929 - loss: 0.6072 - val_accuracy: 0.5000 - val_loss: 1.1411 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.6404 - val_accuracy: 0.5000 - val_loss: 1.1383 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 61ms/step - accuracy: 0.8661 - loss: 0.6448 - val_accuracy: 0.5000 - val_loss: 1.1199 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 44ms/step - accuracy: 0.8393 - loss: 0.6215 - val_accuracy: 0.5000 - val_loss: 1.1372 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.6204 - val_accuracy: 0.5000 - val_loss: 1.1613 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6221 - val_accuracy: 0.5000 - val_loss: 1.1320 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.5914 - val_accuracy: 0.5000 - val_loss: 1.1309 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.5932 - val_accuracy: 0.5000 - val_loss: 1.1589 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 42ms/step - accuracy: 0.8750 - loss: 0.6039 - val_accuracy: 0.5000 - val_loss: 1.1586 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 42ms/step - accuracy: 0.8839 - loss: 0.5774 - val_accuracy: 0.5000 - val_loss: 1.1412 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5911 - val_accuracy: 0.5000 - val_loss: 1.1479 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 43ms/step - accuracy: 0.8482 - loss: 0.5730 - val_accuracy: 0.5000 - val_loss: 1.1540 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.5595 - val_accuracy: 0.5000 - val_loss: 1.1641 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 42ms/step - accuracy: 0.8482 - loss: 0.5627 - val_accuracy: 0.5000 - val_loss: 1.1566 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 43ms/step - accuracy: 0.8661 - loss: 0.5567 - val_accuracy: 0.5000 - val_loss: 1.1678 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 43ms/step - accuracy: 0.8929 - loss: 0.5298 - val_accuracy: 0.5000 - val_loss: 1.1746 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 45ms/step - accuracy: 0.9107 - loss: 0.5375 - val_accuracy: 0.5000 - val_loss: 1.1669 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 43ms/step - accuracy: 0.8571 - loss: 0.5603 - val_accuracy: 0.5000 - val_loss: 1.1666 - learning_rate: 0.0010
Epoch 57: early stopping
Restoring model weights from the end of the best epoch: 42.
Training complete. Best epoch: 42 of 57. Best val_loss: 1.1199, val_accuracy: 0.5000

========== Evaluation: within-subject test / EMS0029 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         3         2         1         0
  min_intens         1         4         1         0
  medium_int         3         0         3         0
  max_intens         0         0         4         2

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.429     0.500     0.462         6
   min_intensity      0.667     0.667     0.667         6
medium_intensity      0.333     0.500     0.400         6
   max_intensity      1.000     0.333     0.500         6

        accuracy                          0.500        24
       macro avg      0.607     0.500     0.507        24
    weighted avg      0.607     0.500     0.507        24

Overall accuracy: 0.5000

Artifacts saved to /kaggle/working/within_all/EMS0029/

############################################################
# Subject 30/31: EMS0030
############################################################
Loaded EMS0030 from /kaggle/input/datasets/akablawi/ems-4class/EMS0030.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-4.35e-03, 4.80e-03]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.14e-06, 4.80e-06]
  Per-channel std range:  [5.58e-06, 7.61e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.3125 - loss: 1.4610 - val_accuracy: 0.1250 - val_loss: 1.3887 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 59ms/step - accuracy: 0.2768 - loss: 1.3832 - val_accuracy: 0.2083 - val_loss: 1.3881 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 59ms/step - accuracy: 0.3304 - loss: 1.3545 - val_accuracy: 0.2083 - val_loss: 1.3874 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.3393 - loss: 1.3316 - val_accuracy: 0.4167 - val_loss: 1.3865 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 59ms/step - accuracy: 0.4732 - loss: 1.2985 - val_accuracy: 0.4583 - val_loss: 1.3856 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.3839 - loss: 1.3161 - val_accuracy: 0.5000 - val_loss: 1.3850 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 58ms/step - accuracy: 0.4643 - loss: 1.2997 - val_accuracy: 0.5000 - val_loss: 1.3842 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 58ms/step - accuracy: 0.4464 - loss: 1.2952 - val_accuracy: 0.4583 - val_loss: 1.3830 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 58ms/step - accuracy: 0.5357 - loss: 1.2637 - val_accuracy: 0.4583 - val_loss: 1.3816 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 58ms/step - accuracy: 0.5536 - loss: 1.2257 - val_accuracy: 0.4583 - val_loss: 1.3803 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 58ms/step - accuracy: 0.4911 - loss: 1.2423 - val_accuracy: 0.5000 - val_loss: 1.3790 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 58ms/step - accuracy: 0.5357 - loss: 1.2256 - val_accuracy: 0.5000 - val_loss: 1.3776 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 58ms/step - accuracy: 0.5714 - loss: 1.2070 - val_accuracy: 0.4167 - val_loss: 1.3759 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 58ms/step - accuracy: 0.5982 - loss: 1.1616 - val_accuracy: 0.4167 - val_loss: 1.3734 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 58ms/step - accuracy: 0.6429 - loss: 1.1633 - val_accuracy: 0.3750 - val_loss: 1.3716 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6250 - loss: 1.1274 - val_accuracy: 0.4167 - val_loss: 1.3695 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 63ms/step - accuracy: 0.5893 - loss: 1.1377 - val_accuracy: 0.4167 - val_loss: 1.3667 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.6071 - loss: 1.1002 - val_accuracy: 0.4167 - val_loss: 1.3641 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 1.0756 - val_accuracy: 0.4167 - val_loss: 1.3633 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.0754 - val_accuracy: 0.2917 - val_loss: 1.3631 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 43ms/step - accuracy: 0.5714 - loss: 1.0499 - val_accuracy: 0.2917 - val_loss: 1.3642 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 44ms/step - accuracy: 0.6518 - loss: 1.0342 - val_accuracy: 0.2500 - val_loss: 1.3652 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 44ms/step - accuracy: 0.6339 - loss: 1.0299 - val_accuracy: 0.2500 - val_loss: 1.3666 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 59ms/step - accuracy: 0.6518 - loss: 1.0051 - val_accuracy: 0.2500 - val_loss: 1.3629 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 59ms/step - accuracy: 0.6607 - loss: 1.0016 - val_accuracy: 0.1667 - val_loss: 1.3594 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 43ms/step - accuracy: 0.6161 - loss: 0.9938 - val_accuracy: 0.2500 - val_loss: 1.3609 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 43ms/step - accuracy: 0.6518 - loss: 0.9746 - val_accuracy: 0.2917 - val_loss: 1.3655 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 44ms/step - accuracy: 0.6607 - loss: 0.9722 - val_accuracy: 0.2917 - val_loss: 1.3656 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 43ms/step - accuracy: 0.6250 - loss: 0.9479 - val_accuracy: 0.2083 - val_loss: 1.3631 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 43ms/step - accuracy: 0.6875 - loss: 0.9210 - val_accuracy: 0.1667 - val_loss: 1.3612 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 58ms/step - accuracy: 0.7411 - loss: 0.9309 - val_accuracy: 0.2500 - val_loss: 1.3542 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 58ms/step - accuracy: 0.7143 - loss: 0.9051 - val_accuracy: 0.2500 - val_loss: 1.3463 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.6786 - loss: 0.9086 - val_accuracy: 0.1667 - val_loss: 1.3458 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.8696 - val_accuracy: 0.1667 - val_loss: 1.3500 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 43ms/step - accuracy: 0.7768 - loss: 0.8677 - val_accuracy: 0.1667 - val_loss: 1.3575 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 43ms/step - accuracy: 0.7232 - loss: 0.8779 - val_accuracy: 0.1667 - val_loss: 1.3576 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 42ms/step - accuracy: 0.7768 - loss: 0.8399 - val_accuracy: 0.2083 - val_loss: 1.3563 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 43ms/step - accuracy: 0.7411 - loss: 0.8475 - val_accuracy: 0.2083 - val_loss: 1.3543 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 41ms/step - accuracy: 0.7679 - loss: 0.8183 - val_accuracy: 0.2083 - val_loss: 1.3510 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 42ms/step - accuracy: 0.7500 - loss: 0.8559 - val_accuracy: 0.2083 - val_loss: 1.3531 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 41ms/step - accuracy: 0.7679 - loss: 0.8100 - val_accuracy: 0.2917 - val_loss: 1.3511 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 42ms/step - accuracy: 0.8125 - loss: 0.7913 - val_accuracy: 0.2917 - val_loss: 1.3471 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 41ms/step - accuracy: 0.7857 - loss: 0.8238 - val_accuracy: 0.2917 - val_loss: 1.3472 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 41ms/step - accuracy: 0.7946 - loss: 0.7882 - val_accuracy: 0.2500 - val_loss: 1.3519 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 41ms/step - accuracy: 0.7857 - loss: 0.7926 - val_accuracy: 0.2500 - val_loss: 1.3583 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 41ms/step - accuracy: 0.8214 - loss: 0.7800 - val_accuracy: 0.2083 - val_loss: 1.3647 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 41ms/step - accuracy: 0.7946 - loss: 0.7736 - val_accuracy: 0.2917 - val_loss: 1.3623 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 41ms/step - accuracy: 0.7946 - loss: 0.7914 - val_accuracy: 0.3333 - val_loss: 1.3508 - learning_rate: 0.0010
Epoch 48: early stopping
Restoring model weights from the end of the best epoch: 33.
Training complete. Best epoch: 33 of 48. Best val_loss: 1.3458, val_accuracy: 0.1667

========== Evaluation: within-subject test / EMS0030 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         1         1         3         1
  min_intens         1         0         4         1
  medium_int         2         1         3         0
  max_intens         2         0         1         3

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.167     0.167     0.167         6
   min_intensity      0.000     0.000     0.000         6
medium_intensity      0.273     0.500     0.353         6
   max_intensity      0.600     0.500     0.545         6

        accuracy                          0.292        24
       macro avg      0.260     0.292     0.266        24
    weighted avg      0.260     0.292     0.266        24

Overall accuracy: 0.2917

Artifacts saved to /kaggle/working/within_all/EMS0030/

############################################################
# Subject 31/31: EMS0031
############################################################
Loaded EMS0031 from /kaggle/input/datasets/akablawi/ems-4class/EMS0031.npz
  X: shape=(160, 60, 425), dtype=float32, range=[-1.95e-04, 2.63e-04]
  y: shape=(160,), dtype=int64, class counts={0: 40, 1: 40, 2: 40, 3: 40}
  sfreq: 250.0 Hz, channels: 60
Split sizes: train=112, val=24, test=24
Fitted scaler on 112 epochs, 60 channels.
  Per-channel mean range: [-1.20e-06, 4.38e-06]
  Per-channel std range:  [5.56e-06, 5.22e-05]
Class weights: {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
Building EEGNet: C=60, T=425, kernLength=125
Epoch 1/500
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
4/4 - 9s - 2s/step - accuracy: 0.2411 - loss: 1.3894 - val_accuracy: 0.5417 - val_loss: 1.3842 - learning_rate: 0.0010
Epoch 2/500
4/4 - 0s - 60ms/step - accuracy: 0.3750 - loss: 1.3632 - val_accuracy: 0.5417 - val_loss: 1.3823 - learning_rate: 0.0010
Epoch 3/500
4/4 - 0s - 58ms/step - accuracy: 0.4107 - loss: 1.3411 - val_accuracy: 0.5417 - val_loss: 1.3806 - learning_rate: 0.0010
Epoch 4/500
4/4 - 0s - 60ms/step - accuracy: 0.4911 - loss: 1.2877 - val_accuracy: 0.5000 - val_loss: 1.3783 - learning_rate: 0.0010
Epoch 5/500
4/4 - 0s - 61ms/step - accuracy: 0.4732 - loss: 1.2575 - val_accuracy: 0.4583 - val_loss: 1.3748 - learning_rate: 0.0010
Epoch 6/500
4/4 - 0s - 59ms/step - accuracy: 0.5357 - loss: 1.2528 - val_accuracy: 0.4583 - val_loss: 1.3704 - learning_rate: 0.0010
Epoch 7/500
4/4 - 0s - 59ms/step - accuracy: 0.5089 - loss: 1.2302 - val_accuracy: 0.4583 - val_loss: 1.3652 - learning_rate: 0.0010
Epoch 8/500
4/4 - 0s - 59ms/step - accuracy: 0.5179 - loss: 1.2122 - val_accuracy: 0.4583 - val_loss: 1.3595 - learning_rate: 0.0010
Epoch 9/500
4/4 - 0s - 60ms/step - accuracy: 0.5179 - loss: 1.1732 - val_accuracy: 0.4583 - val_loss: 1.3527 - learning_rate: 0.0010
Epoch 10/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.1480 - val_accuracy: 0.5000 - val_loss: 1.3451 - learning_rate: 0.0010
Epoch 11/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.1254 - val_accuracy: 0.5000 - val_loss: 1.3374 - learning_rate: 0.0010
Epoch 12/500
4/4 - 0s - 63ms/step - accuracy: 0.6161 - loss: 1.0902 - val_accuracy: 0.5000 - val_loss: 1.3298 - learning_rate: 0.0010
Epoch 13/500
4/4 - 0s - 59ms/step - accuracy: 0.5804 - loss: 1.0788 - val_accuracy: 0.5417 - val_loss: 1.3205 - learning_rate: 0.0010
Epoch 14/500
4/4 - 0s - 61ms/step - accuracy: 0.5893 - loss: 1.0851 - val_accuracy: 0.5417 - val_loss: 1.3112 - learning_rate: 0.0010
Epoch 15/500
4/4 - 0s - 60ms/step - accuracy: 0.6696 - loss: 1.0507 - val_accuracy: 0.5417 - val_loss: 1.3010 - learning_rate: 0.0010
Epoch 16/500
4/4 - 0s - 60ms/step - accuracy: 0.6518 - loss: 1.0212 - val_accuracy: 0.5417 - val_loss: 1.2905 - learning_rate: 0.0010
Epoch 17/500
4/4 - 0s - 60ms/step - accuracy: 0.6875 - loss: 1.0021 - val_accuracy: 0.5833 - val_loss: 1.2785 - learning_rate: 0.0010
Epoch 18/500
4/4 - 0s - 59ms/step - accuracy: 0.5625 - loss: 1.0215 - val_accuracy: 0.5833 - val_loss: 1.2676 - learning_rate: 0.0010
Epoch 19/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.9465 - val_accuracy: 0.5833 - val_loss: 1.2555 - learning_rate: 0.0010
Epoch 20/500
4/4 - 0s - 61ms/step - accuracy: 0.7143 - loss: 0.9452 - val_accuracy: 0.5833 - val_loss: 1.2441 - learning_rate: 0.0010
Epoch 21/500
4/4 - 0s - 61ms/step - accuracy: 0.7054 - loss: 0.9424 - val_accuracy: 0.5833 - val_loss: 1.2336 - learning_rate: 0.0010
Epoch 22/500
4/4 - 0s - 59ms/step - accuracy: 0.7857 - loss: 0.8955 - val_accuracy: 0.5833 - val_loss: 1.2256 - learning_rate: 0.0010
Epoch 23/500
4/4 - 0s - 58ms/step - accuracy: 0.6964 - loss: 0.9126 - val_accuracy: 0.5833 - val_loss: 1.2153 - learning_rate: 0.0010
Epoch 24/500
4/4 - 0s - 58ms/step - accuracy: 0.7857 - loss: 0.8746 - val_accuracy: 0.5833 - val_loss: 1.2032 - learning_rate: 0.0010
Epoch 25/500
4/4 - 0s - 60ms/step - accuracy: 0.7054 - loss: 0.8962 - val_accuracy: 0.5833 - val_loss: 1.1896 - learning_rate: 0.0010
Epoch 26/500
4/4 - 0s - 59ms/step - accuracy: 0.7679 - loss: 0.8574 - val_accuracy: 0.6667 - val_loss: 1.1701 - learning_rate: 0.0010
Epoch 27/500
4/4 - 0s - 58ms/step - accuracy: 0.7679 - loss: 0.8498 - val_accuracy: 0.6250 - val_loss: 1.1577 - learning_rate: 0.0010
Epoch 28/500
4/4 - 0s - 58ms/step - accuracy: 0.8214 - loss: 0.8310 - val_accuracy: 0.6250 - val_loss: 1.1498 - learning_rate: 0.0010
Epoch 29/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8327 - val_accuracy: 0.6667 - val_loss: 1.1429 - learning_rate: 0.0010
Epoch 30/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.7997 - val_accuracy: 0.6667 - val_loss: 1.1321 - learning_rate: 0.0010
Epoch 31/500
4/4 - 0s - 59ms/step - accuracy: 0.7768 - loss: 0.8081 - val_accuracy: 0.7083 - val_loss: 1.1209 - learning_rate: 0.0010
Epoch 32/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.7817 - val_accuracy: 0.7500 - val_loss: 1.1093 - learning_rate: 0.0010
Epoch 33/500
4/4 - 0s - 58ms/step - accuracy: 0.8125 - loss: 0.7739 - val_accuracy: 0.6667 - val_loss: 1.0940 - learning_rate: 0.0010
Epoch 34/500
4/4 - 0s - 58ms/step - accuracy: 0.8304 - loss: 0.7926 - val_accuracy: 0.7500 - val_loss: 1.0854 - learning_rate: 0.0010
Epoch 35/500
4/4 - 0s - 59ms/step - accuracy: 0.8214 - loss: 0.7726 - val_accuracy: 0.7500 - val_loss: 1.0716 - learning_rate: 0.0010
Epoch 36/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.7546 - val_accuracy: 0.7500 - val_loss: 1.0642 - learning_rate: 0.0010
Epoch 37/500
4/4 - 0s - 59ms/step - accuracy: 0.8393 - loss: 0.7382 - val_accuracy: 0.7500 - val_loss: 1.0576 - learning_rate: 0.0010
Epoch 38/500
4/4 - 0s - 58ms/step - accuracy: 0.8393 - loss: 0.7292 - val_accuracy: 0.7917 - val_loss: 1.0450 - learning_rate: 0.0010
Epoch 39/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.7159 - val_accuracy: 0.7500 - val_loss: 1.0272 - learning_rate: 0.0010
Epoch 40/500
4/4 - 0s - 58ms/step - accuracy: 0.8482 - loss: 0.7429 - val_accuracy: 0.8333 - val_loss: 1.0263 - learning_rate: 0.0010
Epoch 41/500
4/4 - 0s - 58ms/step - accuracy: 0.8929 - loss: 0.7066 - val_accuracy: 0.8333 - val_loss: 1.0223 - learning_rate: 0.0010
Epoch 42/500
4/4 - 0s - 59ms/step - accuracy: 0.8839 - loss: 0.6813 - val_accuracy: 0.7500 - val_loss: 1.0038 - learning_rate: 0.0010
Epoch 43/500
4/4 - 0s - 59ms/step - accuracy: 0.8482 - loss: 0.7066 - val_accuracy: 0.8333 - val_loss: 1.0033 - learning_rate: 0.0010
Epoch 44/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.6799 - val_accuracy: 0.7917 - val_loss: 0.9949 - learning_rate: 0.0010
Epoch 45/500
4/4 - 0s - 59ms/step - accuracy: 0.8750 - loss: 0.7014 - val_accuracy: 0.7500 - val_loss: 0.9811 - learning_rate: 0.0010
Epoch 46/500
4/4 - 0s - 59ms/step - accuracy: 0.9107 - loss: 0.6503 - val_accuracy: 0.7917 - val_loss: 0.9766 - learning_rate: 0.0010
Epoch 47/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.6644 - val_accuracy: 0.7917 - val_loss: 0.9589 - learning_rate: 0.0010
Epoch 48/500
4/4 - 0s - 59ms/step - accuracy: 0.8929 - loss: 0.6785 - val_accuracy: 0.7500 - val_loss: 0.9537 - learning_rate: 0.0010
Epoch 49/500
4/4 - 0s - 45ms/step - accuracy: 0.8750 - loss: 0.6853 - val_accuracy: 0.7917 - val_loss: 0.9557 - learning_rate: 0.0010
Epoch 50/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.6348 - val_accuracy: 0.8333 - val_loss: 0.9396 - learning_rate: 0.0010
Epoch 51/500
4/4 - 0s - 58ms/step - accuracy: 0.9107 - loss: 0.6353 - val_accuracy: 0.8333 - val_loss: 0.9206 - learning_rate: 0.0010
Epoch 52/500
4/4 - 0s - 43ms/step - accuracy: 0.9018 - loss: 0.6231 - val_accuracy: 0.7917 - val_loss: 0.9222 - learning_rate: 0.0010
Epoch 53/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.6043 - val_accuracy: 0.7500 - val_loss: 0.9172 - learning_rate: 0.0010
Epoch 54/500
4/4 - 0s - 59ms/step - accuracy: 0.9464 - loss: 0.6018 - val_accuracy: 0.7917 - val_loss: 0.9080 - learning_rate: 0.0010
Epoch 55/500
4/4 - 0s - 59ms/step - accuracy: 0.9375 - loss: 0.5917 - val_accuracy: 0.7500 - val_loss: 0.9040 - learning_rate: 0.0010
Epoch 56/500
4/4 - 0s - 48ms/step - accuracy: 0.9107 - loss: 0.6031 - val_accuracy: 0.7500 - val_loss: 0.9082 - learning_rate: 0.0010
Epoch 57/500
4/4 - 0s - 44ms/step - accuracy: 0.9107 - loss: 0.6068 - val_accuracy: 0.7500 - val_loss: 0.9150 - learning_rate: 0.0010
Epoch 58/500
4/4 - 0s - 43ms/step - accuracy: 0.9286 - loss: 0.5692 - val_accuracy: 0.7083 - val_loss: 0.9084 - learning_rate: 0.0010
Epoch 59/500
4/4 - 0s - 58ms/step - accuracy: 0.9196 - loss: 0.5895 - val_accuracy: 0.7917 - val_loss: 0.9029 - learning_rate: 0.0010
Epoch 60/500
4/4 - 0s - 57ms/step - accuracy: 0.9554 - loss: 0.5484 - val_accuracy: 0.7500 - val_loss: 0.8997 - learning_rate: 0.0010
Epoch 61/500
4/4 - 0s - 57ms/step - accuracy: 0.9375 - loss: 0.5502 - val_accuracy: 0.7917 - val_loss: 0.8922 - learning_rate: 0.0010
Epoch 62/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.5606 - val_accuracy: 0.7917 - val_loss: 0.8920 - learning_rate: 0.0010
Epoch 63/500
4/4 - 0s - 42ms/step - accuracy: 0.9107 - loss: 0.5476 - val_accuracy: 0.7500 - val_loss: 0.8975 - learning_rate: 0.0010
Epoch 64/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.5488 - val_accuracy: 0.7083 - val_loss: 0.9043 - learning_rate: 0.0010
Epoch 65/500
4/4 - 0s - 43ms/step - accuracy: 0.9464 - loss: 0.5343 - val_accuracy: 0.7500 - val_loss: 0.9001 - learning_rate: 0.0010
Epoch 66/500
4/4 - 0s - 58ms/step - accuracy: 0.9375 - loss: 0.5403 - val_accuracy: 0.7500 - val_loss: 0.8895 - learning_rate: 0.0010
Epoch 67/500
4/4 - 0s - 58ms/step - accuracy: 0.9643 - loss: 0.5338 - val_accuracy: 0.7500 - val_loss: 0.8777 - learning_rate: 0.0010
Epoch 68/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5339 - val_accuracy: 0.7083 - val_loss: 0.8814 - learning_rate: 0.0010
Epoch 69/500
4/4 - 0s - 44ms/step - accuracy: 0.9375 - loss: 0.5054 - val_accuracy: 0.7500 - val_loss: 0.8897 - learning_rate: 0.0010
Epoch 70/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.4931 - val_accuracy: 0.7083 - val_loss: 0.8874 - learning_rate: 0.0010
Epoch 71/500
4/4 - 0s - 44ms/step - accuracy: 0.9732 - loss: 0.4857 - val_accuracy: 0.7083 - val_loss: 0.8952 - learning_rate: 0.0010
Epoch 72/500
4/4 - 0s - 43ms/step - accuracy: 0.9643 - loss: 0.4863 - val_accuracy: 0.7083 - val_loss: 0.9024 - learning_rate: 0.0010
Epoch 73/500
4/4 - 0s - 43ms/step - accuracy: 0.9375 - loss: 0.5006 - val_accuracy: 0.7083 - val_loss: 0.8919 - learning_rate: 0.0010
Epoch 74/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.5004 - val_accuracy: 0.7083 - val_loss: 0.8863 - learning_rate: 0.0010
Epoch 75/500
4/4 - 0s - 42ms/step - accuracy: 0.9464 - loss: 0.5036 - val_accuracy: 0.7083 - val_loss: 0.9098 - learning_rate: 0.0010
Epoch 76/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.4617 - val_accuracy: 0.7083 - val_loss: 0.9079 - learning_rate: 0.0010
Epoch 77/500
4/4 - 0s - 43ms/step - accuracy: 0.9821 - loss: 0.4721 - val_accuracy: 0.7500 - val_loss: 0.8868 - learning_rate: 0.0010
Epoch 78/500
4/4 - 0s - 42ms/step - accuracy: 0.9375 - loss: 0.4927 - val_accuracy: 0.7500 - val_loss: 0.8917 - learning_rate: 0.0010
Epoch 79/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4720 - val_accuracy: 0.7083 - val_loss: 0.9012 - learning_rate: 0.0010
Epoch 80/500
4/4 - 0s - 43ms/step - accuracy: 0.9732 - loss: 0.4497 - val_accuracy: 0.6667 - val_loss: 0.8818 - learning_rate: 0.0010
Epoch 81/500
4/4 - 0s - 43ms/step - accuracy: 0.9554 - loss: 0.4575 - val_accuracy: 0.6667 - val_loss: 0.8789 - learning_rate: 0.0010
Epoch 82/500
4/4 - 0s - 42ms/step - accuracy: 0.9554 - loss: 0.4605 - val_accuracy: 0.7083 - val_loss: 0.8880 - learning_rate: 0.0010
Epoch 82: early stopping
Restoring model weights from the end of the best epoch: 67.
Training complete. Best epoch: 67 of 82. Best val_loss: 0.8777, val_accuracy: 0.7500

========== Evaluation: within-subject test / EMS0031 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  min_inte  medium_i  max_inte
  no_stimula         4         2         0         0
  min_intens         3         2         1         0
  medium_int         0         0         6         0
  max_intens         0         1         1         4

Classification report:
                  precision    recall  f1-score   support

  no_stimulation      0.571     0.667     0.615         6
   min_intensity      0.400     0.333     0.364         6
medium_intensity      0.750     1.000     0.857         6
   max_intensity      1.000     0.667     0.800         6

        accuracy                          0.667        24
       macro avg      0.680     0.667     0.659        24
    weighted avg      0.680     0.667     0.659        24

Overall accuracy: 0.6667

Artifacts saved to /kaggle/working/within_all/EMS0031/

============================================================
WITHIN-SUBJECT SWEEP SUMMARY
============================================================
Subjects: 31 / 31
Mean accuracy: 0.5161 ± 0.1395
Range: [0.2917, 0.7917]

Per-subject accuracies:
  EMS0001: 0.750
  EMS0002: 0.542
  EMS0003: 0.792
  EMS0004: 0.500
  EMS0005: 0.333
  EMS0006: 0.417
  EMS0007: 0.333
  EMS0008: 0.417
  EMS0009: 0.708
  EMS0010: 0.542
  EMS0011: 0.458
  EMS0012: 0.292
  EMS0013: 0.750
  EMS0014: 0.417
  EMS0015: 0.292
  EMS0016: 0.542
  EMS0017: 0.417
  EMS0018: 0.542
  EMS0019: 0.375
  EMS0020: 0.583
  EMS0021: 0.583
  EMS0022: 0.667
  EMS0023: 0.542
  EMS0024: 0.542
  EMS0025: 0.667
  EMS0026: 0.458
  EMS0027: 0.458
  EMS0028: 0.625
  EMS0029: 0.500
  EMS0030: 0.292
  EMS0031: 0.667

Aggregated confusion matrix (sum across 31 subjects):
[[ 99  38  35  14]
 [ 56  70  46  14]
 [ 28  25 101  32]
 [ 16  13  43 114]]

Per-class recall:
  no_stimulation: 0.532
  min_intensity: 0.376
  medium_intensity: 0.543
  max_intensity: 0.613