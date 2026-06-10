Loaded 30 subjects, 4800 total epochs.
  Unique subjects: 30
  Class distribution: {np.int64(0): np.int64(1200), np.int64(1): np.int64(2400), np.int64(2): np.int64(1200)}

============================================================
Fold 1 of 30: holding out EMS0001
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.32e-07, 1.10e-06]
  Per-channel std range:  [7.27e-06, 1.12e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 123ms/step - accuracy: 0.4518 - loss: 1.0191 - val_accuracy: 0.4885 - val_loss: 1.0309 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5489 - loss: 0.8876 - val_accuracy: 0.5115 - val_loss: 0.9462 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5609 - loss: 0.8464 - val_accuracy: 0.5345 - val_loss: 0.9090 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 22ms/step - accuracy: 0.5705 - loss: 0.8182 - val_accuracy: 0.5503 - val_loss: 0.8913 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5895 - loss: 0.8014 - val_accuracy: 0.5374 - val_loss: 0.8881 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 22ms/step - accuracy: 0.5936 - loss: 0.7818 - val_accuracy: 0.5690 - val_loss: 0.8578 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 22ms/step - accuracy: 0.6050 - loss: 0.7676 - val_accuracy: 0.5761 - val_loss: 0.8525 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 22ms/step - accuracy: 0.6062 - loss: 0.7544 - val_accuracy: 0.5647 - val_loss: 0.8464 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6111 - loss: 0.7464 - val_accuracy: 0.5891 - val_loss: 0.8383 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 22ms/step - accuracy: 0.6055 - loss: 0.7418 - val_accuracy: 0.5790 - val_loss: 0.8357 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 22ms/step - accuracy: 0.6225 - loss: 0.7331 - val_accuracy: 0.5733 - val_loss: 0.8347 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6222 - loss: 0.7260 - val_accuracy: 0.5833 - val_loss: 0.8255 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6217 - loss: 0.7186 - val_accuracy: 0.5920 - val_loss: 0.8144 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 22ms/step - accuracy: 0.6225 - loss: 0.7160 - val_accuracy: 0.5862 - val_loss: 0.8148 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6293 - loss: 0.7079 - val_accuracy: 0.6006 - val_loss: 0.8042 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 22ms/step - accuracy: 0.6306 - loss: 0.7024 - val_accuracy: 0.5819 - val_loss: 0.7981 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 22ms/step - accuracy: 0.6400 - loss: 0.6966 - val_accuracy: 0.5920 - val_loss: 0.8029 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6927 - val_accuracy: 0.6034 - val_loss: 0.7972 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 22ms/step - accuracy: 0.6410 - loss: 0.6854 - val_accuracy: 0.5934 - val_loss: 0.7990 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6846 - val_accuracy: 0.6063 - val_loss: 0.7846 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 22ms/step - accuracy: 0.6491 - loss: 0.6762 - val_accuracy: 0.6193 - val_loss: 0.7847 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 22ms/step - accuracy: 0.6427 - loss: 0.6768 - val_accuracy: 0.6020 - val_loss: 0.7916 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 22ms/step - accuracy: 0.6529 - loss: 0.6759 - val_accuracy: 0.6020 - val_loss: 0.8023 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 22ms/step - accuracy: 0.6496 - loss: 0.6704 - val_accuracy: 0.5991 - val_loss: 0.7968 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6613 - val_accuracy: 0.6207 - val_loss: 0.7767 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 22ms/step - accuracy: 0.6547 - loss: 0.6573 - val_accuracy: 0.6135 - val_loss: 0.7774 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6630 - loss: 0.6557 - val_accuracy: 0.6135 - val_loss: 0.7730 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6628 - loss: 0.6521 - val_accuracy: 0.6063 - val_loss: 0.7666 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 22ms/step - accuracy: 0.6590 - loss: 0.6542 - val_accuracy: 0.6063 - val_loss: 0.7679 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6648 - loss: 0.6449 - val_accuracy: 0.5920 - val_loss: 0.7865 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6590 - loss: 0.6445 - val_accuracy: 0.6236 - val_loss: 0.7598 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 22ms/step - accuracy: 0.6681 - loss: 0.6437 - val_accuracy: 0.6078 - val_loss: 0.7701 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 22ms/step - accuracy: 0.6706 - loss: 0.6392 - val_accuracy: 0.6106 - val_loss: 0.7810 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 22ms/step - accuracy: 0.6709 - loss: 0.6372 - val_accuracy: 0.6178 - val_loss: 0.7788 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 22ms/step - accuracy: 0.6691 - loss: 0.6364 - val_accuracy: 0.6106 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 22ms/step - accuracy: 0.6752 - loss: 0.6356 - val_accuracy: 0.6106 - val_loss: 0.7770 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6284 - val_accuracy: 0.6279 - val_loss: 0.7598 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 22ms/step - accuracy: 0.6709 - loss: 0.6329 - val_accuracy: 0.6193 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6734 - loss: 0.6225 - val_accuracy: 0.6178 - val_loss: 0.7662 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6272 - val_accuracy: 0.6279 - val_loss: 0.7649 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.6220 - val_accuracy: 0.6149 - val_loss: 0.7762 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6208 - val_accuracy: 0.6236 - val_loss: 0.7652 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6232 - val_accuracy: 0.6207 - val_loss: 0.7641 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6177 - val_accuracy: 0.6164 - val_loss: 0.7678 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6130 - val_accuracy: 0.6193 - val_loss: 0.7883 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 22ms/step - accuracy: 0.6864 - loss: 0.6146 - val_accuracy: 0.6106 - val_loss: 0.7851 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 22ms/step - accuracy: 0.6871 - loss: 0.6092 - val_accuracy: 0.6207 - val_loss: 0.7789 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.6100 - val_accuracy: 0.6236 - val_loss: 0.7689 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6091 - val_accuracy: 0.6408 - val_loss: 0.7523 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6099 - val_accuracy: 0.6307 - val_loss: 0.7518 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6833 - loss: 0.6101 - val_accuracy: 0.6020 - val_loss: 0.7821 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6838 - loss: 0.6044 - val_accuracy: 0.6236 - val_loss: 0.7576 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.6043 - val_accuracy: 0.6422 - val_loss: 0.7402 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.5957 - val_accuracy: 0.6193 - val_loss: 0.7634 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.6003 - val_accuracy: 0.6422 - val_loss: 0.7545 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.6031 - val_accuracy: 0.6193 - val_loss: 0.7667 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6891 - loss: 0.6021 - val_accuracy: 0.6135 - val_loss: 0.7713 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.6035 - val_accuracy: 0.6221 - val_loss: 0.7545 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.5983 - val_accuracy: 0.6207 - val_loss: 0.7616 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5883 - val_accuracy: 0.6293 - val_loss: 0.7623 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.5969 - val_accuracy: 0.6264 - val_loss: 0.7435 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5979 - val_accuracy: 0.6178 - val_loss: 0.7589 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.5895 - val_accuracy: 0.6236 - val_loss: 0.7767 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5909 - val_accuracy: 0.6365 - val_loss: 0.7623 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5776 - val_accuracy: 0.6049 - val_loss: 0.7836 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5906 - val_accuracy: 0.6236 - val_loss: 0.7649 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5835 - val_accuracy: 0.6135 - val_loss: 0.7730 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5962 - val_accuracy: 0.6149 - val_loss: 0.7582 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.5925 - val_accuracy: 0.6063 - val_loss: 0.7711 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5854 - val_accuracy: 0.6322 - val_loss: 0.7735 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6965 - loss: 0.5852 - val_accuracy: 0.6164 - val_loss: 0.7796 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5798 - val_accuracy: 0.6264 - val_loss: 0.7737 - learning_rate: 0.0010
Epoch 73/500

Epoch 73: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7044 - loss: 0.5778 - val_accuracy: 0.6221 - val_loss: 0.7643 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7170 - loss: 0.5577 - val_accuracy: 0.6365 - val_loss: 0.7476 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5571 - val_accuracy: 0.6408 - val_loss: 0.7510 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5527 - val_accuracy: 0.6307 - val_loss: 0.7540 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5530 - val_accuracy: 0.6279 - val_loss: 0.7558 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5503 - val_accuracy: 0.6250 - val_loss: 0.7633 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5421 - val_accuracy: 0.6164 - val_loss: 0.7805 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7355 - loss: 0.5367 - val_accuracy: 0.6293 - val_loss: 0.7723 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7213 - loss: 0.5350 - val_accuracy: 0.6322 - val_loss: 0.7517 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7181 - loss: 0.5430 - val_accuracy: 0.6365 - val_loss: 0.7543 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5476 - val_accuracy: 0.6322 - val_loss: 0.7615 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7229 - loss: 0.5459 - val_accuracy: 0.6250 - val_loss: 0.7570 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5400 - val_accuracy: 0.6250 - val_loss: 0.7540 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5445 - val_accuracy: 0.6293 - val_loss: 0.7613 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7234 - loss: 0.5468 - val_accuracy: 0.6264 - val_loss: 0.7693 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5422 - val_accuracy: 0.6207 - val_loss: 0.7666 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7284 - loss: 0.5367 - val_accuracy: 0.6336 - val_loss: 0.7563 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7277 - loss: 0.5325 - val_accuracy: 0.6293 - val_loss: 0.7531 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7231 - loss: 0.5442 - val_accuracy: 0.6121 - val_loss: 0.7646 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7320 - loss: 0.5394 - val_accuracy: 0.6178 - val_loss: 0.7711 - learning_rate: 5.0000e-04
Epoch 93/500

Epoch 93: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7305 - loss: 0.5377 - val_accuracy: 0.6322 - val_loss: 0.7571 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5211 - val_accuracy: 0.6092 - val_loss: 0.7593 - learning_rate: 2.5000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7447 - loss: 0.5147 - val_accuracy: 0.6236 - val_loss: 0.7731 - learning_rate: 2.5000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7366 - loss: 0.5189 - val_accuracy: 0.6264 - val_loss: 0.7739 - learning_rate: 2.5000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.5154 - val_accuracy: 0.6193 - val_loss: 0.7713 - learning_rate: 2.5000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5168 - val_accuracy: 0.6193 - val_loss: 0.7837 - learning_rate: 2.5000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5154 - val_accuracy: 0.6279 - val_loss: 0.7656 - learning_rate: 2.5000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5113 - val_accuracy: 0.6264 - val_loss: 0.7738 - learning_rate: 2.5000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5095 - val_accuracy: 0.6164 - val_loss: 0.7735 - learning_rate: 2.5000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5164 - val_accuracy: 0.6264 - val_loss: 0.7744 - learning_rate: 2.5000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.5055 - val_accuracy: 0.6207 - val_loss: 0.7817 - learning_rate: 2.5000e-04
Epoch 103: early stopping
Restoring model weights from the end of the best epoch: 53.
Training complete. Best epoch: 53 of 103. Best val_loss: 0.7402, val_accuracy: 0.6422

========== Evaluation: LOSO fold 1 / held-out EMS0001 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        26        14         0
  intermedia        18        62         0
  max_intens         1        15        24

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.578     0.650     0.612        40
intermediate_intensity      0.681     0.775     0.725        80
         max_intensity      1.000     0.600     0.750        40

              accuracy                          0.700       160
             macro avg      0.753     0.675     0.696       160
          weighted avg      0.735     0.700     0.703       160

Overall accuracy: 0.7000

============================================================
Fold 2 of 30: holding out EMS0002
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.38e-07, 1.11e-06]
  Per-channel std range:  [7.30e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4399 - loss: 1.0264 - val_accuracy: 0.4899 - val_loss: 1.0397 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5188 - loss: 0.9213 - val_accuracy: 0.5259 - val_loss: 0.9451 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5700 - loss: 0.8540 - val_accuracy: 0.5618 - val_loss: 0.8839 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5887 - loss: 0.8189 - val_accuracy: 0.5589 - val_loss: 0.8719 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5941 - loss: 0.7964 - val_accuracy: 0.5733 - val_loss: 0.8427 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.6075 - loss: 0.7738 - val_accuracy: 0.5704 - val_loss: 0.8369 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.6040 - loss: 0.7610 - val_accuracy: 0.5747 - val_loss: 0.8418 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6075 - loss: 0.7524 - val_accuracy: 0.5848 - val_loss: 0.8318 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6149 - loss: 0.7414 - val_accuracy: 0.5819 - val_loss: 0.8288 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6217 - loss: 0.7382 - val_accuracy: 0.5761 - val_loss: 0.8223 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6329 - loss: 0.7265 - val_accuracy: 0.5963 - val_loss: 0.8034 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6237 - loss: 0.7204 - val_accuracy: 0.6063 - val_loss: 0.8080 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6293 - loss: 0.7111 - val_accuracy: 0.5991 - val_loss: 0.8018 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6255 - loss: 0.7119 - val_accuracy: 0.6121 - val_loss: 0.7925 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6311 - loss: 0.7024 - val_accuracy: 0.6221 - val_loss: 0.7849 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6389 - loss: 0.6980 - val_accuracy: 0.6006 - val_loss: 0.7947 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6430 - loss: 0.6949 - val_accuracy: 0.6178 - val_loss: 0.7817 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6417 - loss: 0.6855 - val_accuracy: 0.5977 - val_loss: 0.7929 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6308 - loss: 0.6846 - val_accuracy: 0.6250 - val_loss: 0.7877 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6769 - val_accuracy: 0.6336 - val_loss: 0.7795 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6504 - loss: 0.6705 - val_accuracy: 0.6236 - val_loss: 0.7772 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6496 - loss: 0.6697 - val_accuracy: 0.6135 - val_loss: 0.7861 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6519 - loss: 0.6654 - val_accuracy: 0.6365 - val_loss: 0.7680 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6542 - val_accuracy: 0.6293 - val_loss: 0.7755 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6577 - loss: 0.6561 - val_accuracy: 0.6135 - val_loss: 0.8003 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6544 - loss: 0.6580 - val_accuracy: 0.6336 - val_loss: 0.7694 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6686 - loss: 0.6442 - val_accuracy: 0.6135 - val_loss: 0.7819 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6628 - loss: 0.6422 - val_accuracy: 0.6394 - val_loss: 0.7513 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6656 - loss: 0.6397 - val_accuracy: 0.6207 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6366 - val_accuracy: 0.6221 - val_loss: 0.7834 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6648 - loss: 0.6388 - val_accuracy: 0.6164 - val_loss: 0.7787 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6356 - val_accuracy: 0.6207 - val_loss: 0.7700 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6696 - loss: 0.6311 - val_accuracy: 0.6121 - val_loss: 0.7746 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6744 - loss: 0.6356 - val_accuracy: 0.6264 - val_loss: 0.7551 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6309 - val_accuracy: 0.6135 - val_loss: 0.7882 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6701 - loss: 0.6290 - val_accuracy: 0.6408 - val_loss: 0.7486 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6291 - val_accuracy: 0.6164 - val_loss: 0.7712 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6201 - val_accuracy: 0.6164 - val_loss: 0.7716 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6694 - loss: 0.6219 - val_accuracy: 0.6221 - val_loss: 0.7715 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6689 - loss: 0.6199 - val_accuracy: 0.6336 - val_loss: 0.7671 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6790 - loss: 0.6143 - val_accuracy: 0.6365 - val_loss: 0.7633 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6139 - val_accuracy: 0.6293 - val_loss: 0.7557 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6250 - val_accuracy: 0.6193 - val_loss: 0.7798 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6826 - loss: 0.6169 - val_accuracy: 0.6394 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6042 - val_accuracy: 0.6336 - val_loss: 0.7726 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.6035 - val_accuracy: 0.6422 - val_loss: 0.7533 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6770 - loss: 0.6026 - val_accuracy: 0.6250 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.6045 - val_accuracy: 0.6379 - val_loss: 0.7721 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6035 - val_accuracy: 0.6279 - val_loss: 0.7680 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.5941 - val_accuracy: 0.6279 - val_loss: 0.7723 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6093 - val_accuracy: 0.6509 - val_loss: 0.7522 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.5992 - val_accuracy: 0.6293 - val_loss: 0.7485 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.5966 - val_accuracy: 0.6437 - val_loss: 0.7489 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.6008 - val_accuracy: 0.6336 - val_loss: 0.7706 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.5913 - val_accuracy: 0.6293 - val_loss: 0.7613 - learning_rate: 0.0010
Epoch 56/500

Epoch 56: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5912 - val_accuracy: 0.6351 - val_loss: 0.7542 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5740 - val_accuracy: 0.6408 - val_loss: 0.7529 - learning_rate: 5.0000e-04
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5629 - val_accuracy: 0.6422 - val_loss: 0.7558 - learning_rate: 5.0000e-04
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7130 - loss: 0.5582 - val_accuracy: 0.6466 - val_loss: 0.7401 - learning_rate: 5.0000e-04
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7145 - loss: 0.5638 - val_accuracy: 0.6494 - val_loss: 0.7435 - learning_rate: 5.0000e-04
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5665 - val_accuracy: 0.6437 - val_loss: 0.7613 - learning_rate: 5.0000e-04
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7142 - loss: 0.5568 - val_accuracy: 0.6307 - val_loss: 0.7492 - learning_rate: 5.0000e-04
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5596 - val_accuracy: 0.6422 - val_loss: 0.7368 - learning_rate: 5.0000e-04
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7059 - loss: 0.5596 - val_accuracy: 0.6523 - val_loss: 0.7393 - learning_rate: 5.0000e-04
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7213 - loss: 0.5553 - val_accuracy: 0.6480 - val_loss: 0.7390 - learning_rate: 5.0000e-04
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5585 - val_accuracy: 0.6494 - val_loss: 0.7401 - learning_rate: 5.0000e-04
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7203 - loss: 0.5549 - val_accuracy: 0.6422 - val_loss: 0.7544 - learning_rate: 5.0000e-04
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7112 - loss: 0.5549 - val_accuracy: 0.6451 - val_loss: 0.7529 - learning_rate: 5.0000e-04
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5470 - val_accuracy: 0.6365 - val_loss: 0.7550 - learning_rate: 5.0000e-04
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7097 - loss: 0.5547 - val_accuracy: 0.6509 - val_loss: 0.7338 - learning_rate: 5.0000e-04
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7224 - loss: 0.5405 - val_accuracy: 0.6523 - val_loss: 0.7455 - learning_rate: 5.0000e-04
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5451 - val_accuracy: 0.6523 - val_loss: 0.7348 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7201 - loss: 0.5468 - val_accuracy: 0.6451 - val_loss: 0.7464 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7193 - loss: 0.5479 - val_accuracy: 0.6580 - val_loss: 0.7451 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7234 - loss: 0.5467 - val_accuracy: 0.6509 - val_loss: 0.7509 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7208 - loss: 0.5403 - val_accuracy: 0.6365 - val_loss: 0.7694 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5350 - val_accuracy: 0.6566 - val_loss: 0.7491 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5440 - val_accuracy: 0.6710 - val_loss: 0.7348 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5446 - val_accuracy: 0.6638 - val_loss: 0.7475 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7148 - loss: 0.5456 - val_accuracy: 0.6509 - val_loss: 0.7503 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7252 - loss: 0.5334 - val_accuracy: 0.6681 - val_loss: 0.7328 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7254 - loss: 0.5432 - val_accuracy: 0.6552 - val_loss: 0.7387 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5433 - val_accuracy: 0.6566 - val_loss: 0.7375 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5438 - val_accuracy: 0.6624 - val_loss: 0.7357 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5409 - val_accuracy: 0.6480 - val_loss: 0.7464 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5397 - val_accuracy: 0.6523 - val_loss: 0.7484 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5386 - val_accuracy: 0.6537 - val_loss: 0.7450 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5381 - val_accuracy: 0.6595 - val_loss: 0.7500 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7193 - loss: 0.5413 - val_accuracy: 0.6724 - val_loss: 0.7317 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7284 - loss: 0.5352 - val_accuracy: 0.6494 - val_loss: 0.7493 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5275 - val_accuracy: 0.6652 - val_loss: 0.7418 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7290 - loss: 0.5289 - val_accuracy: 0.6552 - val_loss: 0.7535 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5271 - val_accuracy: 0.6566 - val_loss: 0.7424 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5273 - val_accuracy: 0.6480 - val_loss: 0.7503 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7229 - loss: 0.5375 - val_accuracy: 0.6480 - val_loss: 0.7469 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7279 - loss: 0.5327 - val_accuracy: 0.6580 - val_loss: 0.7359 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7269 - loss: 0.5312 - val_accuracy: 0.6695 - val_loss: 0.7352 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5287 - val_accuracy: 0.6494 - val_loss: 0.7395 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5329 - val_accuracy: 0.6681 - val_loss: 0.7470 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5289 - val_accuracy: 0.6566 - val_loss: 0.7504 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5267 - val_accuracy: 0.6595 - val_loss: 0.7469 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7252 - loss: 0.5283 - val_accuracy: 0.6681 - val_loss: 0.7385 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5299 - val_accuracy: 0.6681 - val_loss: 0.7429 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7338 - loss: 0.5228 - val_accuracy: 0.6739 - val_loss: 0.7358 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7333 - loss: 0.5252 - val_accuracy: 0.6638 - val_loss: 0.7352 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5276 - val_accuracy: 0.6710 - val_loss: 0.7367 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7272 - loss: 0.5268 - val_accuracy: 0.6595 - val_loss: 0.7600 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5140 - val_accuracy: 0.6652 - val_loss: 0.7524 - learning_rate: 5.0000e-04
Epoch 109/500

Epoch 109: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7348 - loss: 0.5227 - val_accuracy: 0.6523 - val_loss: 0.7640 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7444 - loss: 0.5134 - val_accuracy: 0.6566 - val_loss: 0.7642 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4978 - val_accuracy: 0.6710 - val_loss: 0.7521 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5089 - val_accuracy: 0.6681 - val_loss: 0.7489 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4955 - val_accuracy: 0.6580 - val_loss: 0.7457 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.5015 - val_accuracy: 0.6566 - val_loss: 0.7503 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5084 - val_accuracy: 0.6724 - val_loss: 0.7555 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.4989 - val_accuracy: 0.6595 - val_loss: 0.7527 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.4958 - val_accuracy: 0.6796 - val_loss: 0.7357 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7383 - loss: 0.5115 - val_accuracy: 0.6710 - val_loss: 0.7430 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7467 - loss: 0.4984 - val_accuracy: 0.6580 - val_loss: 0.7532 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5004 - val_accuracy: 0.6695 - val_loss: 0.7429 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.5017 - val_accuracy: 0.6767 - val_loss: 0.7430 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4920 - val_accuracy: 0.6710 - val_loss: 0.7440 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.4975 - val_accuracy: 0.6796 - val_loss: 0.7367 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.5064 - val_accuracy: 0.6667 - val_loss: 0.7530 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.4963 - val_accuracy: 0.6695 - val_loss: 0.7442 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.5000 - val_accuracy: 0.6724 - val_loss: 0.7442 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7558 - loss: 0.4915 - val_accuracy: 0.6580 - val_loss: 0.7597 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.4995 - val_accuracy: 0.6753 - val_loss: 0.7495 - learning_rate: 2.5000e-04
Epoch 129/500

Epoch 129: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5068 - val_accuracy: 0.6724 - val_loss: 0.7450 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4929 - val_accuracy: 0.6753 - val_loss: 0.7431 - learning_rate: 1.2500e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4851 - val_accuracy: 0.6681 - val_loss: 0.7488 - learning_rate: 1.2500e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4877 - val_accuracy: 0.6667 - val_loss: 0.7464 - learning_rate: 1.2500e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4787 - val_accuracy: 0.6753 - val_loss: 0.7453 - learning_rate: 1.2500e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4798 - val_accuracy: 0.6595 - val_loss: 0.7459 - learning_rate: 1.2500e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4891 - val_accuracy: 0.6724 - val_loss: 0.7539 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7586 - loss: 0.4880 - val_accuracy: 0.6710 - val_loss: 0.7552 - learning_rate: 1.2500e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4888 - val_accuracy: 0.6710 - val_loss: 0.7475 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4896 - val_accuracy: 0.6753 - val_loss: 0.7524 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4869 - val_accuracy: 0.6580 - val_loss: 0.7515 - learning_rate: 1.2500e-04
Epoch 139: early stopping
Restoring model weights from the end of the best epoch: 89.
Training complete. Best epoch: 89 of 139. Best val_loss: 0.7317, val_accuracy: 0.6724

========== Evaluation: LOSO fold 2 / held-out EMS0002 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        37         3         0
  intermedia        34        26        20
  max_intens         0         1        39

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.521     0.925     0.667        40
intermediate_intensity      0.867     0.325     0.473        80
         max_intensity      0.661     0.975     0.788        40

              accuracy                          0.637       160
             macro avg      0.683     0.742     0.642       160
          weighted avg      0.729     0.637     0.600       160

Overall accuracy: 0.6375

============================================================
Fold 3 of 30: holding out EMS0003
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.30e-07, 1.11e-06]
  Per-channel std range:  [7.27e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4394 - loss: 1.0298 - val_accuracy: 0.4253 - val_loss: 1.0517 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5134 - loss: 0.9130 - val_accuracy: 0.4899 - val_loss: 0.9751 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5428 - loss: 0.8649 - val_accuracy: 0.5359 - val_loss: 0.9298 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5573 - loss: 0.8384 - val_accuracy: 0.5374 - val_loss: 0.8982 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5712 - loss: 0.8158 - val_accuracy: 0.5402 - val_loss: 0.8930 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5819 - loss: 0.8013 - val_accuracy: 0.5560 - val_loss: 0.8673 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.5877 - loss: 0.7855 - val_accuracy: 0.5733 - val_loss: 0.8544 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.5852 - loss: 0.7761 - val_accuracy: 0.5733 - val_loss: 0.8536 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.5986 - loss: 0.7594 - val_accuracy: 0.5934 - val_loss: 0.8406 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6037 - loss: 0.7520 - val_accuracy: 0.5991 - val_loss: 0.8415 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6095 - loss: 0.7380 - val_accuracy: 0.5905 - val_loss: 0.8454 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6070 - loss: 0.7342 - val_accuracy: 0.5963 - val_loss: 0.8078 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6182 - loss: 0.7214 - val_accuracy: 0.6193 - val_loss: 0.8085 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6204 - loss: 0.7196 - val_accuracy: 0.6078 - val_loss: 0.8157 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6222 - loss: 0.7157 - val_accuracy: 0.6020 - val_loss: 0.8189 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6354 - loss: 0.6979 - val_accuracy: 0.6106 - val_loss: 0.8152 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6318 - loss: 0.6964 - val_accuracy: 0.6135 - val_loss: 0.8024 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6339 - loss: 0.6905 - val_accuracy: 0.6236 - val_loss: 0.8062 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6427 - loss: 0.6819 - val_accuracy: 0.6264 - val_loss: 0.8031 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6860 - val_accuracy: 0.6078 - val_loss: 0.7996 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6359 - loss: 0.6805 - val_accuracy: 0.6279 - val_loss: 0.7971 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6468 - loss: 0.6760 - val_accuracy: 0.6164 - val_loss: 0.8030 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6509 - loss: 0.6684 - val_accuracy: 0.6063 - val_loss: 0.7985 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6468 - loss: 0.6654 - val_accuracy: 0.6164 - val_loss: 0.7909 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6529 - loss: 0.6612 - val_accuracy: 0.6135 - val_loss: 0.7937 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 22ms/step - accuracy: 0.6468 - loss: 0.6593 - val_accuracy: 0.6049 - val_loss: 0.8009 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 22ms/step - accuracy: 0.6544 - loss: 0.6572 - val_accuracy: 0.6078 - val_loss: 0.8028 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6553 - val_accuracy: 0.6135 - val_loss: 0.7957 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6552 - loss: 0.6514 - val_accuracy: 0.6207 - val_loss: 0.7798 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6600 - loss: 0.6427 - val_accuracy: 0.6279 - val_loss: 0.7938 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6678 - loss: 0.6408 - val_accuracy: 0.6279 - val_loss: 0.7914 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6445 - val_accuracy: 0.6336 - val_loss: 0.7899 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6434 - val_accuracy: 0.6250 - val_loss: 0.7943 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6734 - loss: 0.6301 - val_accuracy: 0.6322 - val_loss: 0.7801 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6795 - loss: 0.6264 - val_accuracy: 0.6307 - val_loss: 0.7770 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6345 - val_accuracy: 0.6250 - val_loss: 0.7950 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6646 - loss: 0.6360 - val_accuracy: 0.6279 - val_loss: 0.7861 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6382 - val_accuracy: 0.6221 - val_loss: 0.7845 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6214 - val_accuracy: 0.6437 - val_loss: 0.7834 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6304 - val_accuracy: 0.6207 - val_loss: 0.7951 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6749 - loss: 0.6242 - val_accuracy: 0.6307 - val_loss: 0.7887 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6717 - loss: 0.6275 - val_accuracy: 0.6164 - val_loss: 0.8023 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6173 - val_accuracy: 0.6279 - val_loss: 0.8048 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6164 - val_accuracy: 0.6351 - val_loss: 0.7921 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6137 - val_accuracy: 0.6408 - val_loss: 0.7905 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.6100 - val_accuracy: 0.6422 - val_loss: 0.7744 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.6014 - val_accuracy: 0.6365 - val_loss: 0.7877 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6800 - loss: 0.6135 - val_accuracy: 0.6193 - val_loss: 0.7933 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.6024 - val_accuracy: 0.6394 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6861 - loss: 0.6022 - val_accuracy: 0.6264 - val_loss: 0.8172 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.6058 - val_accuracy: 0.6336 - val_loss: 0.7903 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5972 - val_accuracy: 0.6437 - val_loss: 0.8165 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.6048 - val_accuracy: 0.6336 - val_loss: 0.7946 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.5969 - val_accuracy: 0.6437 - val_loss: 0.7801 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.6019 - val_accuracy: 0.6250 - val_loss: 0.8022 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6046 - val_accuracy: 0.6437 - val_loss: 0.7700 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.5897 - val_accuracy: 0.6307 - val_loss: 0.7898 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5866 - val_accuracy: 0.6307 - val_loss: 0.8114 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6917 - loss: 0.5968 - val_accuracy: 0.6509 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5935 - val_accuracy: 0.6236 - val_loss: 0.8062 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5798 - val_accuracy: 0.6394 - val_loss: 0.7869 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.5870 - val_accuracy: 0.6394 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5855 - val_accuracy: 0.6078 - val_loss: 0.8096 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5823 - val_accuracy: 0.6264 - val_loss: 0.7942 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5862 - val_accuracy: 0.6451 - val_loss: 0.7850 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5878 - val_accuracy: 0.6279 - val_loss: 0.7948 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5750 - val_accuracy: 0.6394 - val_loss: 0.7776 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5846 - val_accuracy: 0.6408 - val_loss: 0.7956 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5858 - val_accuracy: 0.6193 - val_loss: 0.7958 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5826 - val_accuracy: 0.6250 - val_loss: 0.7842 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5706 - val_accuracy: 0.6279 - val_loss: 0.8113 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5761 - val_accuracy: 0.6437 - val_loss: 0.7927 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5737 - val_accuracy: 0.6437 - val_loss: 0.7830 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5594 - val_accuracy: 0.6250 - val_loss: 0.7845 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7097 - loss: 0.5788 - val_accuracy: 0.6494 - val_loss: 0.7888 - learning_rate: 0.0010
Epoch 76/500

Epoch 76: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5676 - val_accuracy: 0.6322 - val_loss: 0.8109 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7249 - loss: 0.5449 - val_accuracy: 0.6509 - val_loss: 0.7712 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7300 - loss: 0.5404 - val_accuracy: 0.6336 - val_loss: 0.7847 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7290 - loss: 0.5380 - val_accuracy: 0.6408 - val_loss: 0.8003 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5374 - val_accuracy: 0.6236 - val_loss: 0.8114 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5364 - val_accuracy: 0.6437 - val_loss: 0.7847 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5334 - val_accuracy: 0.6236 - val_loss: 0.8079 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5347 - val_accuracy: 0.6322 - val_loss: 0.8000 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5298 - val_accuracy: 0.6509 - val_loss: 0.7886 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7282 - loss: 0.5302 - val_accuracy: 0.6365 - val_loss: 0.7948 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7317 - loss: 0.5332 - val_accuracy: 0.6365 - val_loss: 0.7962 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5328 - val_accuracy: 0.6422 - val_loss: 0.7914 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7317 - loss: 0.5297 - val_accuracy: 0.6394 - val_loss: 0.8058 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5285 - val_accuracy: 0.6509 - val_loss: 0.7813 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5261 - val_accuracy: 0.6379 - val_loss: 0.7978 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5253 - val_accuracy: 0.6307 - val_loss: 0.7973 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7312 - loss: 0.5291 - val_accuracy: 0.6279 - val_loss: 0.8142 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5231 - val_accuracy: 0.6537 - val_loss: 0.7921 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5264 - val_accuracy: 0.6394 - val_loss: 0.7927 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5289 - val_accuracy: 0.6379 - val_loss: 0.8022 - learning_rate: 5.0000e-04
Epoch 96/500

Epoch 96: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7348 - loss: 0.5244 - val_accuracy: 0.6408 - val_loss: 0.7998 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7490 - loss: 0.5108 - val_accuracy: 0.6437 - val_loss: 0.8112 - learning_rate: 2.5000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.5018 - val_accuracy: 0.6322 - val_loss: 0.8067 - learning_rate: 2.5000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5078 - val_accuracy: 0.6336 - val_loss: 0.8018 - learning_rate: 2.5000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4970 - val_accuracy: 0.6336 - val_loss: 0.8052 - learning_rate: 2.5000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7525 - loss: 0.5021 - val_accuracy: 0.6422 - val_loss: 0.7991 - learning_rate: 2.5000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.5029 - val_accuracy: 0.6322 - val_loss: 0.8138 - learning_rate: 2.5000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4966 - val_accuracy: 0.6293 - val_loss: 0.8203 - learning_rate: 2.5000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7614 - loss: 0.4956 - val_accuracy: 0.6279 - val_loss: 0.8192 - learning_rate: 2.5000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.5038 - val_accuracy: 0.6322 - val_loss: 0.8086 - learning_rate: 2.5000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7505 - loss: 0.5039 - val_accuracy: 0.6437 - val_loss: 0.7916 - learning_rate: 2.5000e-04
Epoch 106: early stopping
Restoring model weights from the end of the best epoch: 56.
Training complete. Best epoch: 56 of 106. Best val_loss: 0.7700, val_accuracy: 0.6437

========== Evaluation: LOSO fold 3 / held-out EMS0003 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        35         4         1
  intermedia        10        68         2
  max_intens         0        27        13

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.778     0.875     0.824        40
intermediate_intensity      0.687     0.850     0.760        80
         max_intensity      0.812     0.325     0.464        40

              accuracy                          0.725       160
             macro avg      0.759     0.683     0.683       160
          weighted avg      0.741     0.725     0.702       160

Overall accuracy: 0.7250

============================================================
Fold 4 of 30: holding out EMS0004
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.30e-07, 1.11e-06]
  Per-channel std range:  [7.24e-06, 1.12e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4561 - loss: 1.0120 - val_accuracy: 0.4626 - val_loss: 1.0354 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5299 - loss: 0.9145 - val_accuracy: 0.5014 - val_loss: 0.9678 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5573 - loss: 0.8701 - val_accuracy: 0.5187 - val_loss: 0.9348 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5669 - loss: 0.8467 - val_accuracy: 0.5201 - val_loss: 0.9168 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5730 - loss: 0.8198 - val_accuracy: 0.5560 - val_loss: 0.8943 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5875 - loss: 0.7984 - val_accuracy: 0.5575 - val_loss: 0.8782 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6055 - loss: 0.7813 - val_accuracy: 0.5675 - val_loss: 0.8584 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.5969 - loss: 0.7681 - val_accuracy: 0.5675 - val_loss: 0.8495 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6090 - loss: 0.7519 - val_accuracy: 0.5776 - val_loss: 0.8370 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6034 - loss: 0.7510 - val_accuracy: 0.5948 - val_loss: 0.8218 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6159 - loss: 0.7334 - val_accuracy: 0.5977 - val_loss: 0.8184 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6123 - loss: 0.7312 - val_accuracy: 0.5862 - val_loss: 0.8097 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6263 - loss: 0.7204 - val_accuracy: 0.6063 - val_loss: 0.8003 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6225 - loss: 0.7117 - val_accuracy: 0.6034 - val_loss: 0.8029 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6245 - loss: 0.7098 - val_accuracy: 0.6063 - val_loss: 0.7929 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6334 - loss: 0.6955 - val_accuracy: 0.5862 - val_loss: 0.8039 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6359 - loss: 0.6974 - val_accuracy: 0.5977 - val_loss: 0.8047 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6250 - loss: 0.7021 - val_accuracy: 0.6078 - val_loss: 0.8074 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6483 - loss: 0.6841 - val_accuracy: 0.6078 - val_loss: 0.7975 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6407 - loss: 0.6836 - val_accuracy: 0.6049 - val_loss: 0.7970 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6291 - loss: 0.6849 - val_accuracy: 0.6121 - val_loss: 0.7978 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6498 - loss: 0.6686 - val_accuracy: 0.6106 - val_loss: 0.7844 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6400 - loss: 0.6782 - val_accuracy: 0.6121 - val_loss: 0.8040 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6521 - loss: 0.6694 - val_accuracy: 0.6437 - val_loss: 0.7734 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6594 - val_accuracy: 0.6207 - val_loss: 0.7842 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6471 - loss: 0.6683 - val_accuracy: 0.6049 - val_loss: 0.7908 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6638 - loss: 0.6531 - val_accuracy: 0.6250 - val_loss: 0.7897 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6547 - loss: 0.6541 - val_accuracy: 0.6322 - val_loss: 0.7935 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6595 - loss: 0.6545 - val_accuracy: 0.6422 - val_loss: 0.7717 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6661 - loss: 0.6506 - val_accuracy: 0.6279 - val_loss: 0.7941 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6678 - loss: 0.6406 - val_accuracy: 0.6480 - val_loss: 0.7826 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6495 - val_accuracy: 0.6422 - val_loss: 0.7732 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6463 - val_accuracy: 0.6149 - val_loss: 0.7917 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6590 - loss: 0.6454 - val_accuracy: 0.6221 - val_loss: 0.7870 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6630 - loss: 0.6416 - val_accuracy: 0.6279 - val_loss: 0.7934 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6661 - loss: 0.6352 - val_accuracy: 0.6193 - val_loss: 0.7812 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6701 - loss: 0.6338 - val_accuracy: 0.6250 - val_loss: 0.7973 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6661 - loss: 0.6357 - val_accuracy: 0.6336 - val_loss: 0.7891 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6592 - loss: 0.6405 - val_accuracy: 0.6336 - val_loss: 0.7860 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6651 - loss: 0.6357 - val_accuracy: 0.6322 - val_loss: 0.7863 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6259 - val_accuracy: 0.6279 - val_loss: 0.7861 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6290 - val_accuracy: 0.6322 - val_loss: 0.7788 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6717 - loss: 0.6245 - val_accuracy: 0.6652 - val_loss: 0.7634 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6300 - val_accuracy: 0.6236 - val_loss: 0.7865 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6168 - val_accuracy: 0.6336 - val_loss: 0.7763 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6755 - loss: 0.6275 - val_accuracy: 0.6307 - val_loss: 0.7720 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6264 - val_accuracy: 0.6351 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6165 - val_accuracy: 0.6408 - val_loss: 0.7791 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6160 - val_accuracy: 0.6336 - val_loss: 0.7802 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6775 - loss: 0.6221 - val_accuracy: 0.6236 - val_loss: 0.7796 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6818 - loss: 0.6128 - val_accuracy: 0.6379 - val_loss: 0.7593 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.6118 - val_accuracy: 0.6379 - val_loss: 0.7735 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6106 - val_accuracy: 0.6523 - val_loss: 0.7805 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.6151 - val_accuracy: 0.6351 - val_loss: 0.8078 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6831 - loss: 0.6024 - val_accuracy: 0.6394 - val_loss: 0.7819 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6103 - val_accuracy: 0.6408 - val_loss: 0.7579 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.6028 - val_accuracy: 0.6322 - val_loss: 0.7784 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.6013 - val_accuracy: 0.6336 - val_loss: 0.7704 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6833 - loss: 0.6008 - val_accuracy: 0.6322 - val_loss: 0.7819 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6012 - val_accuracy: 0.6264 - val_loss: 0.7925 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6790 - loss: 0.6175 - val_accuracy: 0.6264 - val_loss: 0.7901 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5978 - val_accuracy: 0.6365 - val_loss: 0.8030 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6035 - val_accuracy: 0.6422 - val_loss: 0.7905 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6864 - loss: 0.6078 - val_accuracy: 0.6480 - val_loss: 0.7801 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.5946 - val_accuracy: 0.6422 - val_loss: 0.7884 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.5945 - val_accuracy: 0.6236 - val_loss: 0.7886 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.5937 - val_accuracy: 0.6293 - val_loss: 0.8000 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.5969 - val_accuracy: 0.6451 - val_loss: 0.7904 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5987 - val_accuracy: 0.6351 - val_loss: 0.8050 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6965 - loss: 0.5838 - val_accuracy: 0.6437 - val_loss: 0.8058 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5854 - val_accuracy: 0.6408 - val_loss: 0.8057 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5833 - val_accuracy: 0.6336 - val_loss: 0.8222 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5889 - val_accuracy: 0.6149 - val_loss: 0.8084 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.5882 - val_accuracy: 0.6408 - val_loss: 0.7935 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5908 - val_accuracy: 0.6408 - val_loss: 0.7992 - learning_rate: 0.0010
Epoch 76/500

Epoch 76: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5867 - val_accuracy: 0.6379 - val_loss: 0.7985 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7092 - loss: 0.5614 - val_accuracy: 0.6379 - val_loss: 0.7665 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7274 - loss: 0.5500 - val_accuracy: 0.6537 - val_loss: 0.7684 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7168 - loss: 0.5508 - val_accuracy: 0.6408 - val_loss: 0.7860 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7208 - loss: 0.5420 - val_accuracy: 0.6552 - val_loss: 0.7637 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5473 - val_accuracy: 0.6552 - val_loss: 0.7464 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5427 - val_accuracy: 0.6494 - val_loss: 0.7582 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5465 - val_accuracy: 0.6494 - val_loss: 0.7585 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5514 - val_accuracy: 0.6509 - val_loss: 0.7695 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7239 - loss: 0.5412 - val_accuracy: 0.6523 - val_loss: 0.7640 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7307 - loss: 0.5416 - val_accuracy: 0.6523 - val_loss: 0.7678 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5494 - val_accuracy: 0.6480 - val_loss: 0.7778 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7148 - loss: 0.5496 - val_accuracy: 0.6451 - val_loss: 0.7798 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7274 - loss: 0.5459 - val_accuracy: 0.6537 - val_loss: 0.7666 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5373 - val_accuracy: 0.6580 - val_loss: 0.7723 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7148 - loss: 0.5459 - val_accuracy: 0.6609 - val_loss: 0.7745 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7310 - loss: 0.5384 - val_accuracy: 0.6537 - val_loss: 0.7794 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7229 - loss: 0.5450 - val_accuracy: 0.6552 - val_loss: 0.7572 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5451 - val_accuracy: 0.6523 - val_loss: 0.7841 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5292 - val_accuracy: 0.6509 - val_loss: 0.7797 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7277 - loss: 0.5334 - val_accuracy: 0.6580 - val_loss: 0.7522 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7274 - loss: 0.5329 - val_accuracy: 0.6537 - val_loss: 0.7440 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7272 - loss: 0.5369 - val_accuracy: 0.6638 - val_loss: 0.7553 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7254 - loss: 0.5375 - val_accuracy: 0.6580 - val_loss: 0.7600 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5328 - val_accuracy: 0.6523 - val_loss: 0.7709 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5314 - val_accuracy: 0.6523 - val_loss: 0.7524 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5316 - val_accuracy: 0.6537 - val_loss: 0.7700 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5345 - val_accuracy: 0.6638 - val_loss: 0.7516 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7290 - loss: 0.5324 - val_accuracy: 0.6566 - val_loss: 0.7778 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5354 - val_accuracy: 0.6624 - val_loss: 0.7630 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7312 - loss: 0.5288 - val_accuracy: 0.6595 - val_loss: 0.7627 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5277 - val_accuracy: 0.6624 - val_loss: 0.7632 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5276 - val_accuracy: 0.6537 - val_loss: 0.7637 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7264 - loss: 0.5326 - val_accuracy: 0.6552 - val_loss: 0.7626 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7249 - loss: 0.5378 - val_accuracy: 0.6523 - val_loss: 0.7525 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5276 - val_accuracy: 0.6552 - val_loss: 0.7626 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7264 - loss: 0.5283 - val_accuracy: 0.6595 - val_loss: 0.7637 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7363 - loss: 0.5249 - val_accuracy: 0.6552 - val_loss: 0.7792 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5272 - val_accuracy: 0.6782 - val_loss: 0.7554 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7409 - loss: 0.5272 - val_accuracy: 0.6595 - val_loss: 0.7671 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5358 - val_accuracy: 0.6580 - val_loss: 0.7463 - learning_rate: 5.0000e-04
Epoch 117/500

Epoch 117: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5267 - val_accuracy: 0.6681 - val_loss: 0.7584 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7381 - loss: 0.5221 - val_accuracy: 0.6624 - val_loss: 0.7639 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5080 - val_accuracy: 0.6580 - val_loss: 0.7644 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.5029 - val_accuracy: 0.6523 - val_loss: 0.7662 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5037 - val_accuracy: 0.6537 - val_loss: 0.7733 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5016 - val_accuracy: 0.6365 - val_loss: 0.7961 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.4974 - val_accuracy: 0.6566 - val_loss: 0.7750 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7447 - loss: 0.5068 - val_accuracy: 0.6667 - val_loss: 0.7659 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.5023 - val_accuracy: 0.6609 - val_loss: 0.7680 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5074 - val_accuracy: 0.6638 - val_loss: 0.7682 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7525 - loss: 0.5048 - val_accuracy: 0.6609 - val_loss: 0.7630 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5047 - val_accuracy: 0.6566 - val_loss: 0.7685 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.5017 - val_accuracy: 0.6695 - val_loss: 0.7508 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4988 - val_accuracy: 0.6681 - val_loss: 0.7631 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5027 - val_accuracy: 0.6537 - val_loss: 0.7648 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.4992 - val_accuracy: 0.6609 - val_loss: 0.7559 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.4976 - val_accuracy: 0.6710 - val_loss: 0.7533 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4974 - val_accuracy: 0.6537 - val_loss: 0.7811 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5023 - val_accuracy: 0.6638 - val_loss: 0.7671 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4901 - val_accuracy: 0.6724 - val_loss: 0.7614 - learning_rate: 2.5000e-04
Epoch 137/500

Epoch 137: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7568 - loss: 0.4985 - val_accuracy: 0.6595 - val_loss: 0.7746 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4915 - val_accuracy: 0.6681 - val_loss: 0.7504 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4909 - val_accuracy: 0.6695 - val_loss: 0.7528 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4881 - val_accuracy: 0.6695 - val_loss: 0.7546 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4826 - val_accuracy: 0.6667 - val_loss: 0.7521 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4844 - val_accuracy: 0.6739 - val_loss: 0.7465 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7541 - loss: 0.4872 - val_accuracy: 0.6810 - val_loss: 0.7468 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4917 - val_accuracy: 0.6681 - val_loss: 0.7599 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4858 - val_accuracy: 0.6710 - val_loss: 0.7486 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4852 - val_accuracy: 0.6739 - val_loss: 0.7622 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7523 - loss: 0.4883 - val_accuracy: 0.6724 - val_loss: 0.7515 - learning_rate: 1.2500e-04
Epoch 147: early stopping
Restoring model weights from the end of the best epoch: 97.
Training complete. Best epoch: 97 of 147. Best val_loss: 0.7440, val_accuracy: 0.6537

========== Evaluation: LOSO fold 4 / held-out EMS0004 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        25        15         0
  intermedia        17        44        19
  max_intens         0        13        27

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.595     0.625     0.610        40
intermediate_intensity      0.611     0.550     0.579        80
         max_intensity      0.587     0.675     0.628        40

              accuracy                          0.600       160
             macro avg      0.598     0.617     0.606       160
          weighted avg      0.601     0.600     0.599       160

Overall accuracy: 0.6000

============================================================
Fold 5 of 30: holding out EMS0005
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.22e-07, 1.11e-06]
  Per-channel std range:  [7.32e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4622 - loss: 1.0123 - val_accuracy: 0.4598 - val_loss: 1.0355 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5312 - loss: 0.9020 - val_accuracy: 0.5230 - val_loss: 0.9454 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5662 - loss: 0.8482 - val_accuracy: 0.5431 - val_loss: 0.8975 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5822 - loss: 0.8169 - val_accuracy: 0.5517 - val_loss: 0.8794 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5890 - loss: 0.7983 - val_accuracy: 0.5718 - val_loss: 0.8565 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.6004 - loss: 0.7775 - val_accuracy: 0.5733 - val_loss: 0.8454 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6055 - loss: 0.7664 - val_accuracy: 0.5733 - val_loss: 0.8337 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6065 - loss: 0.7547 - val_accuracy: 0.5733 - val_loss: 0.8187 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6098 - loss: 0.7410 - val_accuracy: 0.5704 - val_loss: 0.8290 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6232 - loss: 0.7355 - val_accuracy: 0.5733 - val_loss: 0.8206 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6237 - loss: 0.7260 - val_accuracy: 0.5805 - val_loss: 0.8086 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6298 - loss: 0.7188 - val_accuracy: 0.5920 - val_loss: 0.7952 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6420 - loss: 0.7077 - val_accuracy: 0.6034 - val_loss: 0.7945 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6407 - loss: 0.7035 - val_accuracy: 0.6020 - val_loss: 0.7992 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6488 - loss: 0.6923 - val_accuracy: 0.6149 - val_loss: 0.7921 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6478 - loss: 0.6858 - val_accuracy: 0.6236 - val_loss: 0.7956 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6585 - loss: 0.6808 - val_accuracy: 0.6135 - val_loss: 0.7877 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6547 - loss: 0.6703 - val_accuracy: 0.6164 - val_loss: 0.7789 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6509 - loss: 0.6734 - val_accuracy: 0.6293 - val_loss: 0.7701 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6613 - loss: 0.6655 - val_accuracy: 0.6322 - val_loss: 0.7761 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6580 - loss: 0.6675 - val_accuracy: 0.6063 - val_loss: 0.7969 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6633 - loss: 0.6567 - val_accuracy: 0.6221 - val_loss: 0.7806 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6658 - loss: 0.6547 - val_accuracy: 0.6293 - val_loss: 0.7823 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6663 - loss: 0.6478 - val_accuracy: 0.6437 - val_loss: 0.7701 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6694 - loss: 0.6443 - val_accuracy: 0.6422 - val_loss: 0.7600 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6412 - val_accuracy: 0.6322 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6303 - val_accuracy: 0.6322 - val_loss: 0.7740 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6691 - loss: 0.6406 - val_accuracy: 0.6264 - val_loss: 0.7669 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6853 - loss: 0.6217 - val_accuracy: 0.6178 - val_loss: 0.7580 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6826 - loss: 0.6234 - val_accuracy: 0.6379 - val_loss: 0.7585 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.6209 - val_accuracy: 0.6221 - val_loss: 0.7956 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6937 - loss: 0.6108 - val_accuracy: 0.6322 - val_loss: 0.7704 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6180 - val_accuracy: 0.6408 - val_loss: 0.7629 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.6089 - val_accuracy: 0.6336 - val_loss: 0.7653 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6167 - val_accuracy: 0.6451 - val_loss: 0.7636 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6701 - loss: 0.6221 - val_accuracy: 0.6236 - val_loss: 0.7636 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.6041 - val_accuracy: 0.6408 - val_loss: 0.7512 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5970 - val_accuracy: 0.6279 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6088 - val_accuracy: 0.6207 - val_loss: 0.7740 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5937 - val_accuracy: 0.6379 - val_loss: 0.7494 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.6007 - val_accuracy: 0.6379 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5849 - val_accuracy: 0.6279 - val_loss: 0.7648 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5891 - val_accuracy: 0.6264 - val_loss: 0.7770 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6973 - loss: 0.5899 - val_accuracy: 0.6236 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5881 - val_accuracy: 0.6279 - val_loss: 0.7542 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.5959 - val_accuracy: 0.6135 - val_loss: 0.7823 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5850 - val_accuracy: 0.6307 - val_loss: 0.7766 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5755 - val_accuracy: 0.6250 - val_loss: 0.7666 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5794 - val_accuracy: 0.6336 - val_loss: 0.7539 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5903 - val_accuracy: 0.6365 - val_loss: 0.7585 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.6980 - loss: 0.5753 - val_accuracy: 0.6351 - val_loss: 0.7392 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5898 - val_accuracy: 0.6336 - val_loss: 0.7703 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.7039 - loss: 0.5777 - val_accuracy: 0.6494 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5725 - val_accuracy: 0.6408 - val_loss: 0.7619 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7074 - loss: 0.5804 - val_accuracy: 0.6365 - val_loss: 0.7608 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7120 - loss: 0.5711 - val_accuracy: 0.6307 - val_loss: 0.7548 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5687 - val_accuracy: 0.6293 - val_loss: 0.7505 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5761 - val_accuracy: 0.6494 - val_loss: 0.7560 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5682 - val_accuracy: 0.6351 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5748 - val_accuracy: 0.6408 - val_loss: 0.7721 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5648 - val_accuracy: 0.6422 - val_loss: 0.7430 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5650 - val_accuracy: 0.6207 - val_loss: 0.7760 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5583 - val_accuracy: 0.6336 - val_loss: 0.7804 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5688 - val_accuracy: 0.6466 - val_loss: 0.7727 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5670 - val_accuracy: 0.6193 - val_loss: 0.7677 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5635 - val_accuracy: 0.6351 - val_loss: 0.7521 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5616 - val_accuracy: 0.6422 - val_loss: 0.7640 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7254 - loss: 0.5530 - val_accuracy: 0.6466 - val_loss: 0.7699 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7135 - loss: 0.5583 - val_accuracy: 0.6394 - val_loss: 0.7797 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7163 - loss: 0.5608 - val_accuracy: 0.6365 - val_loss: 0.7678 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7183 - loss: 0.5539 - val_accuracy: 0.6351 - val_loss: 0.7792 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7153 - loss: 0.5591 - val_accuracy: 0.6394 - val_loss: 0.7656 - learning_rate: 0.0010
Epoch 73/500

Epoch 73: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7203 - loss: 0.5567 - val_accuracy: 0.6336 - val_loss: 0.7650 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7333 - loss: 0.5337 - val_accuracy: 0.6667 - val_loss: 0.7328 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5272 - val_accuracy: 0.6681 - val_loss: 0.7208 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7404 - loss: 0.5174 - val_accuracy: 0.6681 - val_loss: 0.7289 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5234 - val_accuracy: 0.6652 - val_loss: 0.7305 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7396 - loss: 0.5210 - val_accuracy: 0.6681 - val_loss: 0.7320 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5212 - val_accuracy: 0.6652 - val_loss: 0.7331 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5232 - val_accuracy: 0.6638 - val_loss: 0.7310 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5213 - val_accuracy: 0.6825 - val_loss: 0.7256 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5114 - val_accuracy: 0.6681 - val_loss: 0.7311 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7432 - loss: 0.5175 - val_accuracy: 0.6767 - val_loss: 0.7195 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5202 - val_accuracy: 0.6624 - val_loss: 0.7277 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5167 - val_accuracy: 0.6523 - val_loss: 0.7453 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5157 - val_accuracy: 0.6638 - val_loss: 0.7340 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7447 - loss: 0.5137 - val_accuracy: 0.6724 - val_loss: 0.7216 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5141 - val_accuracy: 0.6710 - val_loss: 0.7309 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5175 - val_accuracy: 0.6624 - val_loss: 0.7429 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5135 - val_accuracy: 0.6695 - val_loss: 0.7329 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5135 - val_accuracy: 0.6724 - val_loss: 0.7433 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5157 - val_accuracy: 0.6566 - val_loss: 0.7347 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5120 - val_accuracy: 0.6710 - val_loss: 0.7276 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7366 - loss: 0.5214 - val_accuracy: 0.6667 - val_loss: 0.7339 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.5135 - val_accuracy: 0.6681 - val_loss: 0.7277 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5095 - val_accuracy: 0.6667 - val_loss: 0.7442 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7467 - loss: 0.5049 - val_accuracy: 0.6652 - val_loss: 0.7470 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5087 - val_accuracy: 0.6652 - val_loss: 0.7319 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5109 - val_accuracy: 0.6710 - val_loss: 0.7473 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5079 - val_accuracy: 0.6710 - val_loss: 0.7462 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5131 - val_accuracy: 0.6753 - val_loss: 0.7378 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.5050 - val_accuracy: 0.6652 - val_loss: 0.7359 - learning_rate: 5.0000e-04
Epoch 103/500

Epoch 103: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4980 - val_accuracy: 0.6681 - val_loss: 0.7324 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4884 - val_accuracy: 0.6782 - val_loss: 0.7464 - learning_rate: 2.5000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7657 - loss: 0.4856 - val_accuracy: 0.6767 - val_loss: 0.7469 - learning_rate: 2.5000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4925 - val_accuracy: 0.6695 - val_loss: 0.7431 - learning_rate: 2.5000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4848 - val_accuracy: 0.6825 - val_loss: 0.7405 - learning_rate: 2.5000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7657 - loss: 0.4828 - val_accuracy: 0.6839 - val_loss: 0.7387 - learning_rate: 2.5000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4865 - val_accuracy: 0.6782 - val_loss: 0.7475 - learning_rate: 2.5000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4832 - val_accuracy: 0.6739 - val_loss: 0.7489 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4770 - val_accuracy: 0.6925 - val_loss: 0.7318 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4874 - val_accuracy: 0.6853 - val_loss: 0.7381 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4846 - val_accuracy: 0.6739 - val_loss: 0.7462 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4792 - val_accuracy: 0.6796 - val_loss: 0.7364 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4818 - val_accuracy: 0.6925 - val_loss: 0.7356 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4821 - val_accuracy: 0.6853 - val_loss: 0.7410 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7665 - loss: 0.4776 - val_accuracy: 0.6810 - val_loss: 0.7434 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4855 - val_accuracy: 0.6724 - val_loss: 0.7456 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4801 - val_accuracy: 0.6911 - val_loss: 0.7263 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4774 - val_accuracy: 0.6968 - val_loss: 0.7389 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4794 - val_accuracy: 0.6839 - val_loss: 0.7363 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4796 - val_accuracy: 0.6767 - val_loss: 0.7418 - learning_rate: 2.5000e-04
Epoch 123/500

Epoch 123: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4833 - val_accuracy: 0.6925 - val_loss: 0.7350 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4675 - val_accuracy: 0.6782 - val_loss: 0.7313 - learning_rate: 1.2500e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7807 - loss: 0.4606 - val_accuracy: 0.6782 - val_loss: 0.7347 - learning_rate: 1.2500e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4619 - val_accuracy: 0.6825 - val_loss: 0.7367 - learning_rate: 1.2500e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4691 - val_accuracy: 0.6810 - val_loss: 0.7399 - learning_rate: 1.2500e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4623 - val_accuracy: 0.6767 - val_loss: 0.7481 - learning_rate: 1.2500e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7741 - loss: 0.4672 - val_accuracy: 0.6868 - val_loss: 0.7375 - learning_rate: 1.2500e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4670 - val_accuracy: 0.6767 - val_loss: 0.7399 - learning_rate: 1.2500e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4700 - val_accuracy: 0.6782 - val_loss: 0.7411 - learning_rate: 1.2500e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4668 - val_accuracy: 0.6897 - val_loss: 0.7388 - learning_rate: 1.2500e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4666 - val_accuracy: 0.6853 - val_loss: 0.7462 - learning_rate: 1.2500e-04
Epoch 133: early stopping
Restoring model weights from the end of the best epoch: 83.
Training complete. Best epoch: 83 of 133. Best val_loss: 0.7195, val_accuracy: 0.6767

========== Evaluation: LOSO fold 5 / held-out EMS0005 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        38         2         0
  intermedia        58        22         0
  max_intens        21        19         0

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.325     0.950     0.484        40
intermediate_intensity      0.512     0.275     0.358        80
         max_intensity      0.000     0.000     0.000        40

              accuracy                          0.375       160
             macro avg      0.279     0.408     0.281       160
          weighted avg      0.337     0.375     0.300       160

Overall accuracy: 0.3750

============================================================
Fold 6 of 30: holding out EMS0006
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.21e-07, 1.11e-06]
  Per-channel std range:  [7.25e-06, 1.12e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4523 - loss: 1.0144 - val_accuracy: 0.4914 - val_loss: 1.0245 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5401 - loss: 0.9003 - val_accuracy: 0.5489 - val_loss: 0.9325 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5586 - loss: 0.8499 - val_accuracy: 0.5704 - val_loss: 0.8898 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5806 - loss: 0.8180 - val_accuracy: 0.5733 - val_loss: 0.8745 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5801 - loss: 0.7982 - val_accuracy: 0.5675 - val_loss: 0.8617 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5910 - loss: 0.7831 - val_accuracy: 0.5761 - val_loss: 0.8570 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6029 - loss: 0.7691 - val_accuracy: 0.5848 - val_loss: 0.8394 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6128 - loss: 0.7534 - val_accuracy: 0.5920 - val_loss: 0.8389 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6040 - loss: 0.7488 - val_accuracy: 0.5805 - val_loss: 0.8364 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6116 - loss: 0.7374 - val_accuracy: 0.5977 - val_loss: 0.8282 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6095 - loss: 0.7356 - val_accuracy: 0.6034 - val_loss: 0.8326 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6171 - loss: 0.7241 - val_accuracy: 0.6207 - val_loss: 0.8058 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6298 - loss: 0.7173 - val_accuracy: 0.5934 - val_loss: 0.8306 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6326 - loss: 0.7049 - val_accuracy: 0.6106 - val_loss: 0.8136 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6268 - loss: 0.7061 - val_accuracy: 0.5934 - val_loss: 0.8165 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6311 - loss: 0.7029 - val_accuracy: 0.6193 - val_loss: 0.8148 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6318 - loss: 0.6962 - val_accuracy: 0.6006 - val_loss: 0.8174 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6402 - loss: 0.6863 - val_accuracy: 0.6020 - val_loss: 0.8120 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6384 - loss: 0.6815 - val_accuracy: 0.6049 - val_loss: 0.8267 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6741 - val_accuracy: 0.6049 - val_loss: 0.8180 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6466 - loss: 0.6770 - val_accuracy: 0.6178 - val_loss: 0.7976 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6713 - val_accuracy: 0.6063 - val_loss: 0.8093 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6498 - loss: 0.6688 - val_accuracy: 0.6078 - val_loss: 0.7922 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6587 - loss: 0.6613 - val_accuracy: 0.6106 - val_loss: 0.8066 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6613 - loss: 0.6587 - val_accuracy: 0.6092 - val_loss: 0.8016 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6567 - loss: 0.6533 - val_accuracy: 0.5848 - val_loss: 0.8114 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6640 - loss: 0.6522 - val_accuracy: 0.6034 - val_loss: 0.8046 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6699 - loss: 0.6471 - val_accuracy: 0.6078 - val_loss: 0.8055 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6676 - loss: 0.6455 - val_accuracy: 0.6092 - val_loss: 0.7995 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6355 - val_accuracy: 0.6121 - val_loss: 0.7959 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6428 - val_accuracy: 0.6092 - val_loss: 0.8099 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6714 - loss: 0.6377 - val_accuracy: 0.6106 - val_loss: 0.7914 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6770 - loss: 0.6307 - val_accuracy: 0.6135 - val_loss: 0.7901 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6275 - val_accuracy: 0.6193 - val_loss: 0.7977 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6823 - loss: 0.6226 - val_accuracy: 0.6178 - val_loss: 0.7831 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6242 - val_accuracy: 0.6178 - val_loss: 0.7951 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.6127 - val_accuracy: 0.6207 - val_loss: 0.7972 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6217 - val_accuracy: 0.6149 - val_loss: 0.8143 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.6152 - val_accuracy: 0.6250 - val_loss: 0.7985 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.6078 - val_accuracy: 0.6135 - val_loss: 0.7969 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6118 - val_accuracy: 0.6121 - val_loss: 0.7832 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.6134 - val_accuracy: 0.6221 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.6078 - val_accuracy: 0.6221 - val_loss: 0.7792 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.6018 - val_accuracy: 0.6149 - val_loss: 0.8046 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.6033 - val_accuracy: 0.6307 - val_loss: 0.7874 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.5967 - val_accuracy: 0.6336 - val_loss: 0.7706 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6940 - loss: 0.5980 - val_accuracy: 0.6221 - val_loss: 0.7780 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5949 - val_accuracy: 0.6149 - val_loss: 0.7834 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5954 - val_accuracy: 0.6034 - val_loss: 0.7860 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5936 - val_accuracy: 0.6293 - val_loss: 0.7774 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5988 - val_accuracy: 0.6207 - val_loss: 0.7979 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5939 - val_accuracy: 0.6279 - val_loss: 0.7969 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.5991 - val_accuracy: 0.6264 - val_loss: 0.7869 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5888 - val_accuracy: 0.6106 - val_loss: 0.8082 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5915 - val_accuracy: 0.6279 - val_loss: 0.7742 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5911 - val_accuracy: 0.6250 - val_loss: 0.7712 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5814 - val_accuracy: 0.6264 - val_loss: 0.7824 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5795 - val_accuracy: 0.6293 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7155 - loss: 0.5741 - val_accuracy: 0.6307 - val_loss: 0.7632 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5874 - val_accuracy: 0.6250 - val_loss: 0.7568 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7056 - loss: 0.5805 - val_accuracy: 0.6135 - val_loss: 0.7924 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5874 - val_accuracy: 0.6394 - val_loss: 0.7469 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5808 - val_accuracy: 0.6322 - val_loss: 0.7743 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5764 - val_accuracy: 0.6221 - val_loss: 0.7949 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7153 - loss: 0.5742 - val_accuracy: 0.6307 - val_loss: 0.7938 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5750 - val_accuracy: 0.6063 - val_loss: 0.8202 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5736 - val_accuracy: 0.6336 - val_loss: 0.8013 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5707 - val_accuracy: 0.6264 - val_loss: 0.7870 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5697 - val_accuracy: 0.6336 - val_loss: 0.7729 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5727 - val_accuracy: 0.6149 - val_loss: 0.7711 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5644 - val_accuracy: 0.6293 - val_loss: 0.7928 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7125 - loss: 0.5659 - val_accuracy: 0.6207 - val_loss: 0.7831 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7130 - loss: 0.5656 - val_accuracy: 0.6351 - val_loss: 0.7852 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5619 - val_accuracy: 0.6394 - val_loss: 0.7734 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5565 - val_accuracy: 0.6264 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7112 - loss: 0.5604 - val_accuracy: 0.6351 - val_loss: 0.7783 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7148 - loss: 0.5647 - val_accuracy: 0.6394 - val_loss: 0.7704 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5586 - val_accuracy: 0.6422 - val_loss: 0.7876 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5573 - val_accuracy: 0.6351 - val_loss: 0.7769 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5593 - val_accuracy: 0.6293 - val_loss: 0.7960 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5581 - val_accuracy: 0.6135 - val_loss: 0.8023 - learning_rate: 0.0010
Epoch 82/500

Epoch 82: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5564 - val_accuracy: 0.6279 - val_loss: 0.7926 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5331 - val_accuracy: 0.6537 - val_loss: 0.7486 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5292 - val_accuracy: 0.6537 - val_loss: 0.7488 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5316 - val_accuracy: 0.6667 - val_loss: 0.7412 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5259 - val_accuracy: 0.6710 - val_loss: 0.7387 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5221 - val_accuracy: 0.6609 - val_loss: 0.7443 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7231 - loss: 0.5259 - val_accuracy: 0.6466 - val_loss: 0.7536 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5265 - val_accuracy: 0.6652 - val_loss: 0.7473 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7310 - loss: 0.5237 - val_accuracy: 0.6466 - val_loss: 0.7558 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5244 - val_accuracy: 0.6523 - val_loss: 0.7647 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7305 - loss: 0.5296 - val_accuracy: 0.6753 - val_loss: 0.7427 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5257 - val_accuracy: 0.6566 - val_loss: 0.7539 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5192 - val_accuracy: 0.6695 - val_loss: 0.7578 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5204 - val_accuracy: 0.6480 - val_loss: 0.7529 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5236 - val_accuracy: 0.6437 - val_loss: 0.7544 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5177 - val_accuracy: 0.6523 - val_loss: 0.7592 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7444 - loss: 0.5099 - val_accuracy: 0.6595 - val_loss: 0.7513 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5190 - val_accuracy: 0.6566 - val_loss: 0.7523 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5157 - val_accuracy: 0.6437 - val_loss: 0.7571 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5217 - val_accuracy: 0.6609 - val_loss: 0.7452 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.5178 - val_accuracy: 0.6552 - val_loss: 0.7583 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5180 - val_accuracy: 0.6667 - val_loss: 0.7405 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5163 - val_accuracy: 0.6624 - val_loss: 0.7601 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5226 - val_accuracy: 0.6552 - val_loss: 0.7476 - learning_rate: 5.0000e-04
Epoch 106/500

Epoch 106: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.5093 - val_accuracy: 0.6580 - val_loss: 0.7491 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.4996 - val_accuracy: 0.6480 - val_loss: 0.7673 - learning_rate: 2.5000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4929 - val_accuracy: 0.6466 - val_loss: 0.7662 - learning_rate: 2.5000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4987 - val_accuracy: 0.6523 - val_loss: 0.7689 - learning_rate: 2.5000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4950 - val_accuracy: 0.6509 - val_loss: 0.7753 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4886 - val_accuracy: 0.6394 - val_loss: 0.7752 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4934 - val_accuracy: 0.6494 - val_loss: 0.7620 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4866 - val_accuracy: 0.6466 - val_loss: 0.7613 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7568 - loss: 0.4915 - val_accuracy: 0.6451 - val_loss: 0.7673 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4852 - val_accuracy: 0.6580 - val_loss: 0.7575 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4859 - val_accuracy: 0.6451 - val_loss: 0.7700 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7558 - loss: 0.4885 - val_accuracy: 0.6509 - val_loss: 0.7668 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4895 - val_accuracy: 0.6480 - val_loss: 0.7659 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4798 - val_accuracy: 0.6379 - val_loss: 0.7743 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4830 - val_accuracy: 0.6537 - val_loss: 0.7605 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4891 - val_accuracy: 0.6566 - val_loss: 0.7646 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4900 - val_accuracy: 0.6537 - val_loss: 0.7706 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7650 - loss: 0.4861 - val_accuracy: 0.6480 - val_loss: 0.7702 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4917 - val_accuracy: 0.6451 - val_loss: 0.7730 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4824 - val_accuracy: 0.6523 - val_loss: 0.7578 - learning_rate: 2.5000e-04
Epoch 126/500

Epoch 126: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4807 - val_accuracy: 0.6609 - val_loss: 0.7637 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4745 - val_accuracy: 0.6609 - val_loss: 0.7545 - learning_rate: 1.2500e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7667 - loss: 0.4729 - val_accuracy: 0.6638 - val_loss: 0.7560 - learning_rate: 1.2500e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4692 - val_accuracy: 0.6695 - val_loss: 0.7467 - learning_rate: 1.2500e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4744 - val_accuracy: 0.6652 - val_loss: 0.7520 - learning_rate: 1.2500e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4737 - val_accuracy: 0.6638 - val_loss: 0.7555 - learning_rate: 1.2500e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4759 - val_accuracy: 0.6595 - val_loss: 0.7603 - learning_rate: 1.2500e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4709 - val_accuracy: 0.6566 - val_loss: 0.7594 - learning_rate: 1.2500e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4711 - val_accuracy: 0.6494 - val_loss: 0.7599 - learning_rate: 1.2500e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4705 - val_accuracy: 0.6537 - val_loss: 0.7560 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4670 - val_accuracy: 0.6609 - val_loss: 0.7563 - learning_rate: 1.2500e-04
Epoch 136: early stopping
Restoring model weights from the end of the best epoch: 86.
Training complete. Best epoch: 86 of 136. Best val_loss: 0.7387, val_accuracy: 0.6710

========== Evaluation: LOSO fold 6 / held-out EMS0006 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        28         9         3
  intermedia        37        38         5
  max_intens         2        22        16

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.418     0.700     0.523        40
intermediate_intensity      0.551     0.475     0.510        80
         max_intensity      0.667     0.400     0.500        40

              accuracy                          0.512       160
             macro avg      0.545     0.525     0.511       160
          weighted avg      0.547     0.512     0.511       160

Overall accuracy: 0.5125

============================================================
Fold 7 of 30: holding out EMS0007
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.11e-07, 5.01e-07]
  Per-channel std range:  [6.99e-06, 8.94e-05]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 116ms/step - accuracy: 0.4419 - loss: 1.0144 - val_accuracy: 0.4713 - val_loss: 1.0322 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5216 - loss: 0.9128 - val_accuracy: 0.5057 - val_loss: 0.9569 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5581 - loss: 0.8554 - val_accuracy: 0.5187 - val_loss: 0.9118 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5766 - loss: 0.8195 - val_accuracy: 0.5445 - val_loss: 0.8829 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5898 - loss: 0.7980 - val_accuracy: 0.5546 - val_loss: 0.8571 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.6014 - loss: 0.7822 - val_accuracy: 0.5647 - val_loss: 0.8546 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6032 - loss: 0.7722 - val_accuracy: 0.5603 - val_loss: 0.8344 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6154 - loss: 0.7529 - val_accuracy: 0.5546 - val_loss: 0.8408 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6100 - loss: 0.7445 - val_accuracy: 0.5661 - val_loss: 0.8278 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6237 - loss: 0.7358 - val_accuracy: 0.5862 - val_loss: 0.8146 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6207 - loss: 0.7262 - val_accuracy: 0.5704 - val_loss: 0.8241 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6237 - loss: 0.7221 - val_accuracy: 0.5819 - val_loss: 0.8068 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6296 - loss: 0.7031 - val_accuracy: 0.5948 - val_loss: 0.8086 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6268 - loss: 0.7052 - val_accuracy: 0.5848 - val_loss: 0.8065 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6389 - loss: 0.6935 - val_accuracy: 0.5977 - val_loss: 0.8127 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6349 - loss: 0.6933 - val_accuracy: 0.6063 - val_loss: 0.8064 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6346 - loss: 0.6865 - val_accuracy: 0.6092 - val_loss: 0.7948 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6466 - loss: 0.6799 - val_accuracy: 0.6178 - val_loss: 0.7909 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6458 - loss: 0.6856 - val_accuracy: 0.6049 - val_loss: 0.7980 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6789 - val_accuracy: 0.6034 - val_loss: 0.7893 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6425 - loss: 0.6772 - val_accuracy: 0.6063 - val_loss: 0.8012 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6506 - loss: 0.6617 - val_accuracy: 0.6178 - val_loss: 0.7802 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6534 - loss: 0.6635 - val_accuracy: 0.6164 - val_loss: 0.8031 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6511 - loss: 0.6597 - val_accuracy: 0.6063 - val_loss: 0.8102 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6562 - loss: 0.6551 - val_accuracy: 0.6164 - val_loss: 0.8036 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6537 - loss: 0.6587 - val_accuracy: 0.6121 - val_loss: 0.7900 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6534 - loss: 0.6540 - val_accuracy: 0.6006 - val_loss: 0.8156 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6608 - loss: 0.6485 - val_accuracy: 0.6020 - val_loss: 0.8055 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6562 - loss: 0.6521 - val_accuracy: 0.6178 - val_loss: 0.7750 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6666 - loss: 0.6459 - val_accuracy: 0.6063 - val_loss: 0.8033 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6625 - loss: 0.6348 - val_accuracy: 0.6365 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6696 - loss: 0.6332 - val_accuracy: 0.6106 - val_loss: 0.7900 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6663 - loss: 0.6360 - val_accuracy: 0.6250 - val_loss: 0.7802 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6628 - loss: 0.6327 - val_accuracy: 0.6336 - val_loss: 0.7757 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6752 - loss: 0.6275 - val_accuracy: 0.6250 - val_loss: 0.7936 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6285 - val_accuracy: 0.6221 - val_loss: 0.7860 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6322 - val_accuracy: 0.6149 - val_loss: 0.7733 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6253 - val_accuracy: 0.6135 - val_loss: 0.7911 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6722 - loss: 0.6191 - val_accuracy: 0.6293 - val_loss: 0.7668 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6671 - loss: 0.6271 - val_accuracy: 0.6221 - val_loss: 0.7752 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6190 - val_accuracy: 0.6279 - val_loss: 0.7677 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6162 - val_accuracy: 0.6135 - val_loss: 0.7828 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6742 - loss: 0.6213 - val_accuracy: 0.6049 - val_loss: 0.7856 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6145 - val_accuracy: 0.6178 - val_loss: 0.7769 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6067 - val_accuracy: 0.6193 - val_loss: 0.7811 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6760 - loss: 0.6142 - val_accuracy: 0.6207 - val_loss: 0.7716 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6046 - val_accuracy: 0.6365 - val_loss: 0.7546 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6057 - val_accuracy: 0.6365 - val_loss: 0.7512 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.6074 - val_accuracy: 0.6149 - val_loss: 0.7844 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6853 - loss: 0.6068 - val_accuracy: 0.6178 - val_loss: 0.7858 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.6048 - val_accuracy: 0.6264 - val_loss: 0.7607 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6071 - val_accuracy: 0.6178 - val_loss: 0.7838 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.5973 - val_accuracy: 0.6207 - val_loss: 0.7747 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6853 - loss: 0.5977 - val_accuracy: 0.6336 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6009 - val_accuracy: 0.6365 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.5987 - val_accuracy: 0.6365 - val_loss: 0.7660 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5911 - val_accuracy: 0.6221 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5965 - val_accuracy: 0.6451 - val_loss: 0.7551 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.5903 - val_accuracy: 0.6236 - val_loss: 0.7629 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.5983 - val_accuracy: 0.6279 - val_loss: 0.7653 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5909 - val_accuracy: 0.6121 - val_loss: 0.7872 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5940 - val_accuracy: 0.6279 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.5934 - val_accuracy: 0.6164 - val_loss: 0.7741 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6965 - loss: 0.5852 - val_accuracy: 0.6408 - val_loss: 0.7476 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5771 - val_accuracy: 0.6121 - val_loss: 0.7666 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6922 - loss: 0.5941 - val_accuracy: 0.6236 - val_loss: 0.7811 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5803 - val_accuracy: 0.6394 - val_loss: 0.7630 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5791 - val_accuracy: 0.6379 - val_loss: 0.7505 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5913 - val_accuracy: 0.6193 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5797 - val_accuracy: 0.6193 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5779 - val_accuracy: 0.6408 - val_loss: 0.7478 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5786 - val_accuracy: 0.6351 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5847 - val_accuracy: 0.6336 - val_loss: 0.7478 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.6973 - loss: 0.5850 - val_accuracy: 0.6236 - val_loss: 0.7424 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5693 - val_accuracy: 0.6322 - val_loss: 0.7606 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5767 - val_accuracy: 0.6293 - val_loss: 0.7680 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7011 - loss: 0.5785 - val_accuracy: 0.6078 - val_loss: 0.7912 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5786 - val_accuracy: 0.6149 - val_loss: 0.7654 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5680 - val_accuracy: 0.6236 - val_loss: 0.7580 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5647 - val_accuracy: 0.6164 - val_loss: 0.7854 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5741 - val_accuracy: 0.6293 - val_loss: 0.7561 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5713 - val_accuracy: 0.6207 - val_loss: 0.7661 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5669 - val_accuracy: 0.6135 - val_loss: 0.7920 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7107 - loss: 0.5771 - val_accuracy: 0.6451 - val_loss: 0.7519 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7170 - loss: 0.5621 - val_accuracy: 0.6264 - val_loss: 0.7542 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7130 - loss: 0.5704 - val_accuracy: 0.6121 - val_loss: 0.7860 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5746 - val_accuracy: 0.6193 - val_loss: 0.7607 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5639 - val_accuracy: 0.6121 - val_loss: 0.7804 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5659 - val_accuracy: 0.6307 - val_loss: 0.7555 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5600 - val_accuracy: 0.6279 - val_loss: 0.7565 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5619 - val_accuracy: 0.6106 - val_loss: 0.7817 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5561 - val_accuracy: 0.6351 - val_loss: 0.7659 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5642 - val_accuracy: 0.6379 - val_loss: 0.7590 - learning_rate: 0.0010
Epoch 94/500

Epoch 94: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.5745 - val_accuracy: 0.6121 - val_loss: 0.7740 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7315 - loss: 0.5349 - val_accuracy: 0.6566 - val_loss: 0.7251 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7376 - loss: 0.5226 - val_accuracy: 0.6422 - val_loss: 0.7221 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5275 - val_accuracy: 0.6523 - val_loss: 0.7171 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7343 - loss: 0.5250 - val_accuracy: 0.6451 - val_loss: 0.7367 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5215 - val_accuracy: 0.6494 - val_loss: 0.7375 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7320 - loss: 0.5233 - val_accuracy: 0.6537 - val_loss: 0.7340 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5116 - val_accuracy: 0.6422 - val_loss: 0.7317 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5098 - val_accuracy: 0.6494 - val_loss: 0.7318 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5153 - val_accuracy: 0.6566 - val_loss: 0.7301 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5149 - val_accuracy: 0.6480 - val_loss: 0.7205 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5140 - val_accuracy: 0.6552 - val_loss: 0.7254 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7388 - loss: 0.5167 - val_accuracy: 0.6437 - val_loss: 0.7439 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5172 - val_accuracy: 0.6293 - val_loss: 0.7681 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.5065 - val_accuracy: 0.6480 - val_loss: 0.7311 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5120 - val_accuracy: 0.6509 - val_loss: 0.7384 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5206 - val_accuracy: 0.6480 - val_loss: 0.7293 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5253 - val_accuracy: 0.6480 - val_loss: 0.7387 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7381 - loss: 0.5166 - val_accuracy: 0.6552 - val_loss: 0.7252 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5144 - val_accuracy: 0.6422 - val_loss: 0.7322 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5109 - val_accuracy: 0.6509 - val_loss: 0.7392 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7388 - loss: 0.5070 - val_accuracy: 0.6580 - val_loss: 0.7353 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5083 - val_accuracy: 0.6466 - val_loss: 0.7429 - learning_rate: 5.0000e-04
Epoch 117/500

Epoch 117: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5068 - val_accuracy: 0.6480 - val_loss: 0.7378 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4850 - val_accuracy: 0.6394 - val_loss: 0.7388 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4880 - val_accuracy: 0.6494 - val_loss: 0.7398 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4883 - val_accuracy: 0.6437 - val_loss: 0.7359 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7533 - loss: 0.4908 - val_accuracy: 0.6394 - val_loss: 0.7542 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7612 - loss: 0.4886 - val_accuracy: 0.6480 - val_loss: 0.7356 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4870 - val_accuracy: 0.6379 - val_loss: 0.7469 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4858 - val_accuracy: 0.6422 - val_loss: 0.7496 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7563 - loss: 0.4893 - val_accuracy: 0.6307 - val_loss: 0.7614 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4886 - val_accuracy: 0.6595 - val_loss: 0.7339 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7518 - loss: 0.4932 - val_accuracy: 0.6537 - val_loss: 0.7389 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4849 - val_accuracy: 0.6422 - val_loss: 0.7407 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4857 - val_accuracy: 0.6422 - val_loss: 0.7435 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4862 - val_accuracy: 0.6480 - val_loss: 0.7536 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4869 - val_accuracy: 0.6566 - val_loss: 0.7418 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4886 - val_accuracy: 0.6552 - val_loss: 0.7344 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4851 - val_accuracy: 0.6537 - val_loss: 0.7384 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4907 - val_accuracy: 0.6379 - val_loss: 0.7429 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7614 - loss: 0.4850 - val_accuracy: 0.6379 - val_loss: 0.7384 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4852 - val_accuracy: 0.6437 - val_loss: 0.7426 - learning_rate: 2.5000e-04
Epoch 137/500

Epoch 137: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7612 - loss: 0.4764 - val_accuracy: 0.6365 - val_loss: 0.7454 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4761 - val_accuracy: 0.6537 - val_loss: 0.7330 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4719 - val_accuracy: 0.6638 - val_loss: 0.7246 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7736 - loss: 0.4729 - val_accuracy: 0.6638 - val_loss: 0.7223 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7650 - loss: 0.4780 - val_accuracy: 0.6580 - val_loss: 0.7365 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7665 - loss: 0.4733 - val_accuracy: 0.6595 - val_loss: 0.7325 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7655 - loss: 0.4713 - val_accuracy: 0.6667 - val_loss: 0.7303 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7708 - loss: 0.4693 - val_accuracy: 0.6681 - val_loss: 0.7244 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4737 - val_accuracy: 0.6652 - val_loss: 0.7197 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4717 - val_accuracy: 0.6667 - val_loss: 0.7247 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7708 - loss: 0.4749 - val_accuracy: 0.6638 - val_loss: 0.7343 - learning_rate: 1.2500e-04
Epoch 147: early stopping
Restoring model weights from the end of the best epoch: 97.
Training complete. Best epoch: 97 of 147. Best val_loss: 0.7171, val_accuracy: 0.6523

========== Evaluation: LOSO fold 7 / held-out EMS0007 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula         6        25         9
  intermedia        10        51        19
  max_intens         4        26        10

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.300     0.150     0.200        40
intermediate_intensity      0.500     0.637     0.560        80
         max_intensity      0.263     0.250     0.256        40

              accuracy                          0.419       160
             macro avg      0.354     0.346     0.339       160
          weighted avg      0.391     0.419     0.394       160

Overall accuracy: 0.4188

============================================================
Fold 8 of 30: holding out EMS0008
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.16e-07, 9.70e-07]
  Per-channel std range:  [7.25e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4597 - loss: 1.0203 - val_accuracy: 0.4569 - val_loss: 1.0357 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5292 - loss: 0.9012 - val_accuracy: 0.5259 - val_loss: 0.9373 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5614 - loss: 0.8482 - val_accuracy: 0.5402 - val_loss: 0.9001 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5827 - loss: 0.8216 - val_accuracy: 0.5129 - val_loss: 0.8789 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5936 - loss: 0.7992 - val_accuracy: 0.5187 - val_loss: 0.8777 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5956 - loss: 0.7825 - val_accuracy: 0.5417 - val_loss: 0.8610 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.5956 - loss: 0.7732 - val_accuracy: 0.5848 - val_loss: 0.8386 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6004 - loss: 0.7568 - val_accuracy: 0.5805 - val_loss: 0.8412 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6161 - loss: 0.7455 - val_accuracy: 0.5848 - val_loss: 0.8226 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6263 - loss: 0.7295 - val_accuracy: 0.6020 - val_loss: 0.8121 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6222 - loss: 0.7317 - val_accuracy: 0.5675 - val_loss: 0.8196 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6247 - loss: 0.7167 - val_accuracy: 0.5761 - val_loss: 0.8091 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6308 - loss: 0.7080 - val_accuracy: 0.5862 - val_loss: 0.8132 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6405 - loss: 0.7074 - val_accuracy: 0.5948 - val_loss: 0.7898 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6280 - loss: 0.6984 - val_accuracy: 0.6092 - val_loss: 0.7703 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6369 - loss: 0.6931 - val_accuracy: 0.5991 - val_loss: 0.7945 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6476 - loss: 0.6891 - val_accuracy: 0.6063 - val_loss: 0.7879 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6455 - loss: 0.6794 - val_accuracy: 0.5790 - val_loss: 0.8037 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6569 - loss: 0.6778 - val_accuracy: 0.5862 - val_loss: 0.7944 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6506 - loss: 0.6710 - val_accuracy: 0.6034 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6468 - loss: 0.6809 - val_accuracy: 0.5848 - val_loss: 0.7966 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6610 - loss: 0.6623 - val_accuracy: 0.5977 - val_loss: 0.7885 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6663 - loss: 0.6544 - val_accuracy: 0.6034 - val_loss: 0.7829 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6539 - loss: 0.6632 - val_accuracy: 0.6106 - val_loss: 0.7727 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6633 - loss: 0.6487 - val_accuracy: 0.6034 - val_loss: 0.7801 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6684 - loss: 0.6440 - val_accuracy: 0.5905 - val_loss: 0.7846 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6608 - loss: 0.6446 - val_accuracy: 0.6020 - val_loss: 0.7745 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6393 - val_accuracy: 0.6106 - val_loss: 0.7649 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6727 - loss: 0.6414 - val_accuracy: 0.6006 - val_loss: 0.7752 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6676 - loss: 0.6368 - val_accuracy: 0.6078 - val_loss: 0.7611 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6678 - loss: 0.6313 - val_accuracy: 0.6020 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6772 - loss: 0.6209 - val_accuracy: 0.6250 - val_loss: 0.7667 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6767 - loss: 0.6246 - val_accuracy: 0.5920 - val_loss: 0.7858 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6266 - val_accuracy: 0.5991 - val_loss: 0.7865 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6178 - val_accuracy: 0.5948 - val_loss: 0.7940 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6238 - val_accuracy: 0.5948 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6818 - loss: 0.6239 - val_accuracy: 0.5833 - val_loss: 0.7992 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6157 - val_accuracy: 0.6149 - val_loss: 0.7661 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6160 - val_accuracy: 0.6149 - val_loss: 0.7764 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6081 - val_accuracy: 0.6135 - val_loss: 0.7690 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6859 - loss: 0.6120 - val_accuracy: 0.6078 - val_loss: 0.7795 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6069 - val_accuracy: 0.6135 - val_loss: 0.7689 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6141 - val_accuracy: 0.6164 - val_loss: 0.7775 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6118 - val_accuracy: 0.6063 - val_loss: 0.7964 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.6038 - val_accuracy: 0.6207 - val_loss: 0.7678 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6110 - val_accuracy: 0.6178 - val_loss: 0.7823 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6856 - loss: 0.6029 - val_accuracy: 0.6063 - val_loss: 0.7907 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.6006 - val_accuracy: 0.5991 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5978 - val_accuracy: 0.6193 - val_loss: 0.7757 - learning_rate: 0.0010
Epoch 50/500

Epoch 50: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5961 - val_accuracy: 0.6193 - val_loss: 0.7885 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5782 - val_accuracy: 0.6092 - val_loss: 0.7717 - learning_rate: 5.0000e-04
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5728 - val_accuracy: 0.6121 - val_loss: 0.7765 - learning_rate: 5.0000e-04
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.7115 - loss: 0.5710 - val_accuracy: 0.6106 - val_loss: 0.7690 - learning_rate: 5.0000e-04
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5624 - val_accuracy: 0.6178 - val_loss: 0.7697 - learning_rate: 5.0000e-04
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5635 - val_accuracy: 0.6092 - val_loss: 0.7716 - learning_rate: 5.0000e-04
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7170 - loss: 0.5659 - val_accuracy: 0.6034 - val_loss: 0.7750 - learning_rate: 5.0000e-04
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7145 - loss: 0.5616 - val_accuracy: 0.6193 - val_loss: 0.7628 - learning_rate: 5.0000e-04
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5536 - val_accuracy: 0.6221 - val_loss: 0.7655 - learning_rate: 5.0000e-04
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7201 - loss: 0.5577 - val_accuracy: 0.6092 - val_loss: 0.7763 - learning_rate: 5.0000e-04
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5588 - val_accuracy: 0.6293 - val_loss: 0.7697 - learning_rate: 5.0000e-04
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7155 - loss: 0.5595 - val_accuracy: 0.6106 - val_loss: 0.7719 - learning_rate: 5.0000e-04
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5622 - val_accuracy: 0.6078 - val_loss: 0.7741 - learning_rate: 5.0000e-04
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7297 - loss: 0.5492 - val_accuracy: 0.6092 - val_loss: 0.7677 - learning_rate: 5.0000e-04
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5573 - val_accuracy: 0.6207 - val_loss: 0.7714 - learning_rate: 5.0000e-04
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7224 - loss: 0.5547 - val_accuracy: 0.6178 - val_loss: 0.7605 - learning_rate: 5.0000e-04
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7226 - loss: 0.5506 - val_accuracy: 0.6365 - val_loss: 0.7611 - learning_rate: 5.0000e-04
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5508 - val_accuracy: 0.5991 - val_loss: 0.8011 - learning_rate: 5.0000e-04
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7239 - loss: 0.5573 - val_accuracy: 0.6092 - val_loss: 0.7714 - learning_rate: 5.0000e-04
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7231 - loss: 0.5495 - val_accuracy: 0.6034 - val_loss: 0.7790 - learning_rate: 5.0000e-04
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5478 - val_accuracy: 0.6264 - val_loss: 0.7735 - learning_rate: 5.0000e-04
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5472 - val_accuracy: 0.6121 - val_loss: 0.7711 - learning_rate: 5.0000e-04
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7234 - loss: 0.5468 - val_accuracy: 0.6207 - val_loss: 0.7678 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7282 - loss: 0.5479 - val_accuracy: 0.6351 - val_loss: 0.7730 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5469 - val_accuracy: 0.6207 - val_loss: 0.7753 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7252 - loss: 0.5454 - val_accuracy: 0.6221 - val_loss: 0.7652 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7274 - loss: 0.5470 - val_accuracy: 0.6034 - val_loss: 0.7835 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5395 - val_accuracy: 0.6279 - val_loss: 0.7748 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5420 - val_accuracy: 0.6135 - val_loss: 0.7744 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7244 - loss: 0.5421 - val_accuracy: 0.6149 - val_loss: 0.7738 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5332 - val_accuracy: 0.6049 - val_loss: 0.7794 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7262 - loss: 0.5457 - val_accuracy: 0.6236 - val_loss: 0.7700 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7366 - loss: 0.5386 - val_accuracy: 0.6221 - val_loss: 0.7742 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5365 - val_accuracy: 0.6193 - val_loss: 0.7796 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7300 - loss: 0.5416 - val_accuracy: 0.6164 - val_loss: 0.7822 - learning_rate: 5.0000e-04
Epoch 85/500

Epoch 85: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7213 - loss: 0.5476 - val_accuracy: 0.5977 - val_loss: 0.7994 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5200 - val_accuracy: 0.6106 - val_loss: 0.7848 - learning_rate: 2.5000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5289 - val_accuracy: 0.6164 - val_loss: 0.7775 - learning_rate: 2.5000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.5095 - val_accuracy: 0.6121 - val_loss: 0.7768 - learning_rate: 2.5000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7525 - loss: 0.5123 - val_accuracy: 0.6207 - val_loss: 0.7714 - learning_rate: 2.5000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5103 - val_accuracy: 0.6006 - val_loss: 0.7812 - learning_rate: 2.5000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5140 - val_accuracy: 0.6049 - val_loss: 0.7879 - learning_rate: 2.5000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5168 - val_accuracy: 0.6063 - val_loss: 0.7820 - learning_rate: 2.5000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7444 - loss: 0.5135 - val_accuracy: 0.6121 - val_loss: 0.7894 - learning_rate: 2.5000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.5074 - val_accuracy: 0.6121 - val_loss: 0.7757 - learning_rate: 2.5000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5169 - val_accuracy: 0.6121 - val_loss: 0.7847 - learning_rate: 2.5000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5176 - val_accuracy: 0.6063 - val_loss: 0.7897 - learning_rate: 2.5000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5141 - val_accuracy: 0.6178 - val_loss: 0.7730 - learning_rate: 2.5000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7470 - loss: 0.5110 - val_accuracy: 0.6178 - val_loss: 0.7798 - learning_rate: 2.5000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.5093 - val_accuracy: 0.6221 - val_loss: 0.7791 - learning_rate: 2.5000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5095 - val_accuracy: 0.6078 - val_loss: 0.7900 - learning_rate: 2.5000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.5098 - val_accuracy: 0.6178 - val_loss: 0.7902 - learning_rate: 2.5000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7467 - loss: 0.5137 - val_accuracy: 0.6178 - val_loss: 0.7759 - learning_rate: 2.5000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.5083 - val_accuracy: 0.6149 - val_loss: 0.7872 - learning_rate: 2.5000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.5019 - val_accuracy: 0.6164 - val_loss: 0.7802 - learning_rate: 2.5000e-04
Epoch 105/500

Epoch 105: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5103 - val_accuracy: 0.6092 - val_loss: 0.7765 - learning_rate: 2.5000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5027 - val_accuracy: 0.6264 - val_loss: 0.7656 - learning_rate: 1.2500e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4971 - val_accuracy: 0.6293 - val_loss: 0.7673 - learning_rate: 1.2500e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4953 - val_accuracy: 0.6164 - val_loss: 0.7694 - learning_rate: 1.2500e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.5001 - val_accuracy: 0.6236 - val_loss: 0.7752 - learning_rate: 1.2500e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4970 - val_accuracy: 0.6236 - val_loss: 0.7684 - learning_rate: 1.2500e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7543 - loss: 0.5005 - val_accuracy: 0.6250 - val_loss: 0.7621 - learning_rate: 1.2500e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4967 - val_accuracy: 0.6236 - val_loss: 0.7682 - learning_rate: 1.2500e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4973 - val_accuracy: 0.6250 - val_loss: 0.7696 - learning_rate: 1.2500e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4925 - val_accuracy: 0.6236 - val_loss: 0.7682 - learning_rate: 1.2500e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7586 - loss: 0.5008 - val_accuracy: 0.6236 - val_loss: 0.7682 - learning_rate: 1.2500e-04
Epoch 115: early stopping
Restoring model weights from the end of the best epoch: 65.
Training complete. Best epoch: 65 of 115. Best val_loss: 0.7605, val_accuracy: 0.6178

========== Evaluation: LOSO fold 8 / held-out EMS0008 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        35         5         0
  intermedia        42        31         7
  max_intens         3         9        28

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.438     0.875     0.583        40
intermediate_intensity      0.689     0.388     0.496        80
         max_intensity      0.800     0.700     0.747        40

              accuracy                          0.588       160
             macro avg      0.642     0.654     0.609       160
          weighted avg      0.654     0.588     0.581       160

Overall accuracy: 0.5875

============================================================
Fold 9 of 30: holding out EMS0009
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.16e-07, 9.93e-07]
  Per-channel std range:  [7.29e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4381 - loss: 1.0258 - val_accuracy: 0.4871 - val_loss: 1.0463 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5190 - loss: 0.9150 - val_accuracy: 0.5144 - val_loss: 0.9549 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5454 - loss: 0.8609 - val_accuracy: 0.5316 - val_loss: 0.9064 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5692 - loss: 0.8243 - val_accuracy: 0.5647 - val_loss: 0.8832 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5710 - loss: 0.8036 - val_accuracy: 0.5489 - val_loss: 0.8725 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5862 - loss: 0.7822 - val_accuracy: 0.5776 - val_loss: 0.8375 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.6007 - loss: 0.7685 - val_accuracy: 0.5833 - val_loss: 0.8465 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.5999 - loss: 0.7591 - val_accuracy: 0.5733 - val_loss: 0.8428 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6009 - loss: 0.7490 - val_accuracy: 0.5891 - val_loss: 0.8240 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6090 - loss: 0.7435 - val_accuracy: 0.5718 - val_loss: 0.8268 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6164 - loss: 0.7299 - val_accuracy: 0.5920 - val_loss: 0.8168 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6169 - loss: 0.7233 - val_accuracy: 0.5833 - val_loss: 0.8184 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6212 - loss: 0.7176 - val_accuracy: 0.5905 - val_loss: 0.8104 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6194 - loss: 0.7129 - val_accuracy: 0.5934 - val_loss: 0.8184 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6273 - loss: 0.6980 - val_accuracy: 0.5805 - val_loss: 0.8156 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6316 - loss: 0.6919 - val_accuracy: 0.5963 - val_loss: 0.8150 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6258 - loss: 0.6951 - val_accuracy: 0.5833 - val_loss: 0.8184 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6384 - loss: 0.6915 - val_accuracy: 0.6034 - val_loss: 0.8107 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6427 - loss: 0.6747 - val_accuracy: 0.6006 - val_loss: 0.8035 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6420 - loss: 0.6744 - val_accuracy: 0.6092 - val_loss: 0.7843 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6443 - loss: 0.6727 - val_accuracy: 0.5776 - val_loss: 0.8091 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6539 - loss: 0.6702 - val_accuracy: 0.5963 - val_loss: 0.8001 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6450 - loss: 0.6674 - val_accuracy: 0.5862 - val_loss: 0.8046 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6602 - loss: 0.6570 - val_accuracy: 0.5963 - val_loss: 0.8008 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6498 - loss: 0.6630 - val_accuracy: 0.5790 - val_loss: 0.7982 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6569 - loss: 0.6524 - val_accuracy: 0.5776 - val_loss: 0.8234 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6469 - val_accuracy: 0.6034 - val_loss: 0.7924 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6704 - loss: 0.6392 - val_accuracy: 0.6149 - val_loss: 0.8043 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6448 - val_accuracy: 0.5963 - val_loss: 0.7982 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6600 - loss: 0.6440 - val_accuracy: 0.5948 - val_loss: 0.8146 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6643 - loss: 0.6402 - val_accuracy: 0.5991 - val_loss: 0.7927 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6727 - loss: 0.6328 - val_accuracy: 0.6149 - val_loss: 0.7760 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6684 - loss: 0.6310 - val_accuracy: 0.6135 - val_loss: 0.7858 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6717 - loss: 0.6319 - val_accuracy: 0.6034 - val_loss: 0.8021 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6244 - val_accuracy: 0.5934 - val_loss: 0.8059 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6747 - loss: 0.6217 - val_accuracy: 0.5948 - val_loss: 0.7922 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6770 - loss: 0.6220 - val_accuracy: 0.6063 - val_loss: 0.8083 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6291 - val_accuracy: 0.6078 - val_loss: 0.8043 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.6276 - val_accuracy: 0.5891 - val_loss: 0.7990 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.6131 - val_accuracy: 0.5991 - val_loss: 0.7968 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6126 - val_accuracy: 0.6149 - val_loss: 0.7724 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6861 - loss: 0.6119 - val_accuracy: 0.6106 - val_loss: 0.7850 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6213 - val_accuracy: 0.5977 - val_loss: 0.7832 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6818 - loss: 0.6077 - val_accuracy: 0.6034 - val_loss: 0.7845 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6181 - val_accuracy: 0.6092 - val_loss: 0.7743 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6894 - loss: 0.5993 - val_accuracy: 0.6178 - val_loss: 0.7577 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.6052 - val_accuracy: 0.6006 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.5973 - val_accuracy: 0.6221 - val_loss: 0.7733 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.6066 - val_accuracy: 0.6092 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6831 - loss: 0.6020 - val_accuracy: 0.6049 - val_loss: 0.7862 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6025 - val_accuracy: 0.6264 - val_loss: 0.7587 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.6013 - val_accuracy: 0.6135 - val_loss: 0.7657 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.5942 - val_accuracy: 0.6164 - val_loss: 0.7879 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.6020 - val_accuracy: 0.6207 - val_loss: 0.7660 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.5997 - val_accuracy: 0.6063 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.5933 - val_accuracy: 0.6322 - val_loss: 0.7699 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5917 - val_accuracy: 0.6293 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6937 - loss: 0.5849 - val_accuracy: 0.6034 - val_loss: 0.7880 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.5919 - val_accuracy: 0.6264 - val_loss: 0.7480 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5836 - val_accuracy: 0.6121 - val_loss: 0.7686 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5871 - val_accuracy: 0.6063 - val_loss: 0.7859 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6922 - loss: 0.5978 - val_accuracy: 0.6178 - val_loss: 0.7848 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5773 - val_accuracy: 0.6279 - val_loss: 0.7397 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.5914 - val_accuracy: 0.6480 - val_loss: 0.7413 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5816 - val_accuracy: 0.6351 - val_loss: 0.7494 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6973 - loss: 0.5810 - val_accuracy: 0.6264 - val_loss: 0.7480 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.5858 - val_accuracy: 0.6178 - val_loss: 0.7627 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.5856 - val_accuracy: 0.6379 - val_loss: 0.7332 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5746 - val_accuracy: 0.6264 - val_loss: 0.7559 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7059 - loss: 0.5721 - val_accuracy: 0.6135 - val_loss: 0.7855 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5818 - val_accuracy: 0.6178 - val_loss: 0.7673 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7044 - loss: 0.5779 - val_accuracy: 0.6236 - val_loss: 0.7699 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5827 - val_accuracy: 0.6437 - val_loss: 0.7212 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5762 - val_accuracy: 0.6221 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5697 - val_accuracy: 0.6422 - val_loss: 0.7433 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.5843 - val_accuracy: 0.6279 - val_loss: 0.7552 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5682 - val_accuracy: 0.6264 - val_loss: 0.7663 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7061 - loss: 0.5634 - val_accuracy: 0.6379 - val_loss: 0.7631 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5685 - val_accuracy: 0.6394 - val_loss: 0.7429 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5693 - val_accuracy: 0.6279 - val_loss: 0.7511 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7061 - loss: 0.5686 - val_accuracy: 0.6092 - val_loss: 0.7756 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5704 - val_accuracy: 0.6178 - val_loss: 0.7774 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7018 - loss: 0.5709 - val_accuracy: 0.6164 - val_loss: 0.7769 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5655 - val_accuracy: 0.6293 - val_loss: 0.7630 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5705 - val_accuracy: 0.6307 - val_loss: 0.7737 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5584 - val_accuracy: 0.6351 - val_loss: 0.7445 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5676 - val_accuracy: 0.6307 - val_loss: 0.7656 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5672 - val_accuracy: 0.6293 - val_loss: 0.7707 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7110 - loss: 0.5641 - val_accuracy: 0.6221 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5680 - val_accuracy: 0.6149 - val_loss: 0.7762 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5649 - val_accuracy: 0.6193 - val_loss: 0.7619 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5584 - val_accuracy: 0.6178 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 93/500

Epoch 93: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7061 - loss: 0.5695 - val_accuracy: 0.6149 - val_loss: 0.7800 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5413 - val_accuracy: 0.6236 - val_loss: 0.7483 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5335 - val_accuracy: 0.6236 - val_loss: 0.7578 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7388 - loss: 0.5231 - val_accuracy: 0.6193 - val_loss: 0.7449 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7317 - loss: 0.5361 - val_accuracy: 0.6250 - val_loss: 0.7384 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7295 - loss: 0.5305 - val_accuracy: 0.6422 - val_loss: 0.7204 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7366 - loss: 0.5241 - val_accuracy: 0.6322 - val_loss: 0.7397 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7333 - loss: 0.5339 - val_accuracy: 0.6336 - val_loss: 0.7287 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7300 - loss: 0.5237 - val_accuracy: 0.6336 - val_loss: 0.7346 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5250 - val_accuracy: 0.6307 - val_loss: 0.7490 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5177 - val_accuracy: 0.6437 - val_loss: 0.7272 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5282 - val_accuracy: 0.6394 - val_loss: 0.7501 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5199 - val_accuracy: 0.6351 - val_loss: 0.7416 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5173 - val_accuracy: 0.6408 - val_loss: 0.7413 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7320 - loss: 0.5209 - val_accuracy: 0.6437 - val_loss: 0.7402 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7290 - loss: 0.5257 - val_accuracy: 0.6351 - val_loss: 0.7428 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5243 - val_accuracy: 0.6394 - val_loss: 0.7431 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5229 - val_accuracy: 0.6466 - val_loss: 0.7403 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7383 - loss: 0.5217 - val_accuracy: 0.6451 - val_loss: 0.7413 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5211 - val_accuracy: 0.6264 - val_loss: 0.7476 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5159 - val_accuracy: 0.6365 - val_loss: 0.7509 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5162 - val_accuracy: 0.6408 - val_loss: 0.7330 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5252 - val_accuracy: 0.6408 - val_loss: 0.7296 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7378 - loss: 0.5132 - val_accuracy: 0.6307 - val_loss: 0.7453 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5130 - val_accuracy: 0.6322 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 118/500

Epoch 118: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5143 - val_accuracy: 0.6193 - val_loss: 0.7502 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.5043 - val_accuracy: 0.6207 - val_loss: 0.7549 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.5023 - val_accuracy: 0.6365 - val_loss: 0.7529 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.4923 - val_accuracy: 0.6264 - val_loss: 0.7503 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4947 - val_accuracy: 0.6322 - val_loss: 0.7548 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.4960 - val_accuracy: 0.6293 - val_loss: 0.7473 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4917 - val_accuracy: 0.6322 - val_loss: 0.7487 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4930 - val_accuracy: 0.6264 - val_loss: 0.7549 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4973 - val_accuracy: 0.6422 - val_loss: 0.7394 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.4942 - val_accuracy: 0.6322 - val_loss: 0.7579 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4922 - val_accuracy: 0.6336 - val_loss: 0.7576 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4873 - val_accuracy: 0.6351 - val_loss: 0.7560 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.4973 - val_accuracy: 0.6336 - val_loss: 0.7417 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4940 - val_accuracy: 0.6322 - val_loss: 0.7491 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4839 - val_accuracy: 0.6293 - val_loss: 0.7610 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4840 - val_accuracy: 0.6394 - val_loss: 0.7440 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.4965 - val_accuracy: 0.6322 - val_loss: 0.7495 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7515 - loss: 0.4940 - val_accuracy: 0.6279 - val_loss: 0.7464 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.4913 - val_accuracy: 0.6365 - val_loss: 0.7450 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4832 - val_accuracy: 0.6408 - val_loss: 0.7522 - learning_rate: 2.5000e-04
Epoch 138/500

Epoch 138: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4899 - val_accuracy: 0.6336 - val_loss: 0.7546 - learning_rate: 2.5000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7500 - loss: 0.4914 - val_accuracy: 0.6494 - val_loss: 0.7342 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4796 - val_accuracy: 0.6336 - val_loss: 0.7468 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4847 - val_accuracy: 0.6351 - val_loss: 0.7494 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4779 - val_accuracy: 0.6494 - val_loss: 0.7271 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4754 - val_accuracy: 0.6408 - val_loss: 0.7382 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4768 - val_accuracy: 0.6408 - val_loss: 0.7391 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4788 - val_accuracy: 0.6466 - val_loss: 0.7302 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4827 - val_accuracy: 0.6408 - val_loss: 0.7343 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4821 - val_accuracy: 0.6437 - val_loss: 0.7388 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4736 - val_accuracy: 0.6422 - val_loss: 0.7361 - learning_rate: 1.2500e-04
Epoch 148: early stopping
Restoring model weights from the end of the best epoch: 98.
Training complete. Best epoch: 98 of 148. Best val_loss: 0.7204, val_accuracy: 0.6422

========== Evaluation: LOSO fold 9 / held-out EMS0009 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        37         3         0
  intermedia        20        24        36
  max_intens         0         0        40

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.649     0.925     0.763        40
intermediate_intensity      0.889     0.300     0.449        80
         max_intensity      0.526     1.000     0.690        40

              accuracy                          0.631       160
             macro avg      0.688     0.742     0.634       160
          weighted avg      0.738     0.631     0.587       160

Overall accuracy: 0.6312

============================================================
Fold 10 of 30: holding out EMS0011
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.18e-07, 9.67e-07]
  Per-channel std range:  [7.31e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4432 - loss: 1.0214 - val_accuracy: 0.4971 - val_loss: 1.0308 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5299 - loss: 0.9034 - val_accuracy: 0.5345 - val_loss: 0.9427 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5591 - loss: 0.8520 - val_accuracy: 0.5474 - val_loss: 0.9022 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5794 - loss: 0.8193 - val_accuracy: 0.5388 - val_loss: 0.8864 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5816 - loss: 0.8005 - val_accuracy: 0.5287 - val_loss: 0.8727 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5870 - loss: 0.7857 - val_accuracy: 0.5445 - val_loss: 0.8773 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.5994 - loss: 0.7718 - val_accuracy: 0.5431 - val_loss: 0.8602 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6113 - loss: 0.7565 - val_accuracy: 0.5704 - val_loss: 0.8390 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6154 - loss: 0.7545 - val_accuracy: 0.5718 - val_loss: 0.8396 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6154 - loss: 0.7415 - val_accuracy: 0.5761 - val_loss: 0.8313 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6149 - loss: 0.7403 - val_accuracy: 0.5718 - val_loss: 0.8220 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6141 - loss: 0.7263 - val_accuracy: 0.5977 - val_loss: 0.8072 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6303 - loss: 0.7114 - val_accuracy: 0.5833 - val_loss: 0.8044 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6260 - loss: 0.7091 - val_accuracy: 0.5991 - val_loss: 0.7947 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6265 - loss: 0.7043 - val_accuracy: 0.6006 - val_loss: 0.7947 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6354 - loss: 0.6961 - val_accuracy: 0.5848 - val_loss: 0.7908 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6899 - val_accuracy: 0.6135 - val_loss: 0.8030 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6425 - loss: 0.6823 - val_accuracy: 0.6164 - val_loss: 0.7738 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6379 - loss: 0.6890 - val_accuracy: 0.6149 - val_loss: 0.7856 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6354 - loss: 0.6770 - val_accuracy: 0.6149 - val_loss: 0.7711 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6803 - val_accuracy: 0.6049 - val_loss: 0.7922 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6511 - loss: 0.6661 - val_accuracy: 0.6106 - val_loss: 0.7668 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6450 - loss: 0.6690 - val_accuracy: 0.6164 - val_loss: 0.7738 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6647 - val_accuracy: 0.6149 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6613 - val_accuracy: 0.6164 - val_loss: 0.7673 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6503 - val_accuracy: 0.6164 - val_loss: 0.7645 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6618 - loss: 0.6518 - val_accuracy: 0.6236 - val_loss: 0.7724 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6623 - loss: 0.6451 - val_accuracy: 0.6250 - val_loss: 0.7653 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6623 - loss: 0.6423 - val_accuracy: 0.6351 - val_loss: 0.7693 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6656 - loss: 0.6323 - val_accuracy: 0.6250 - val_loss: 0.7655 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6534 - loss: 0.6464 - val_accuracy: 0.6164 - val_loss: 0.7689 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6701 - loss: 0.6357 - val_accuracy: 0.6221 - val_loss: 0.7569 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6347 - val_accuracy: 0.6293 - val_loss: 0.7559 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6727 - loss: 0.6250 - val_accuracy: 0.6336 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6826 - loss: 0.6186 - val_accuracy: 0.6322 - val_loss: 0.7625 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6701 - loss: 0.6270 - val_accuracy: 0.6293 - val_loss: 0.7520 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6727 - loss: 0.6301 - val_accuracy: 0.6293 - val_loss: 0.7693 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6239 - val_accuracy: 0.6336 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6742 - loss: 0.6128 - val_accuracy: 0.6207 - val_loss: 0.7635 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6153 - val_accuracy: 0.6193 - val_loss: 0.7744 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.6161 - val_accuracy: 0.6034 - val_loss: 0.7587 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.6108 - val_accuracy: 0.6221 - val_loss: 0.7637 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.6082 - val_accuracy: 0.6236 - val_loss: 0.7455 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6755 - loss: 0.6105 - val_accuracy: 0.6149 - val_loss: 0.7670 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6831 - loss: 0.6112 - val_accuracy: 0.6279 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6853 - loss: 0.6037 - val_accuracy: 0.6236 - val_loss: 0.7621 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6846 - loss: 0.6042 - val_accuracy: 0.6351 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.6106 - val_accuracy: 0.6221 - val_loss: 0.7525 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.6041 - val_accuracy: 0.6307 - val_loss: 0.7510 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5894 - val_accuracy: 0.6250 - val_loss: 0.7538 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5917 - val_accuracy: 0.6149 - val_loss: 0.7573 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6962 - loss: 0.5907 - val_accuracy: 0.6307 - val_loss: 0.7611 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.5998 - val_accuracy: 0.6236 - val_loss: 0.7673 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7011 - loss: 0.5840 - val_accuracy: 0.6336 - val_loss: 0.7490 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5893 - val_accuracy: 0.6092 - val_loss: 0.7652 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5924 - val_accuracy: 0.6322 - val_loss: 0.7727 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6962 - loss: 0.5885 - val_accuracy: 0.6307 - val_loss: 0.7487 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5834 - val_accuracy: 0.6307 - val_loss: 0.7504 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5887 - val_accuracy: 0.6221 - val_loss: 0.7473 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5778 - val_accuracy: 0.6164 - val_loss: 0.7556 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5768 - val_accuracy: 0.6336 - val_loss: 0.7484 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5784 - val_accuracy: 0.6279 - val_loss: 0.7593 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5866 - val_accuracy: 0.6293 - val_loss: 0.7620 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5775 - val_accuracy: 0.6250 - val_loss: 0.7544 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5824 - val_accuracy: 0.6264 - val_loss: 0.7615 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5827 - val_accuracy: 0.6322 - val_loss: 0.7550 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7145 - loss: 0.5718 - val_accuracy: 0.6394 - val_loss: 0.7355 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5722 - val_accuracy: 0.6121 - val_loss: 0.7602 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5744 - val_accuracy: 0.6379 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7074 - loss: 0.5793 - val_accuracy: 0.6365 - val_loss: 0.7369 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7001 - loss: 0.5760 - val_accuracy: 0.6293 - val_loss: 0.7634 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5680 - val_accuracy: 0.6451 - val_loss: 0.7425 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5695 - val_accuracy: 0.6351 - val_loss: 0.7350 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7155 - loss: 0.5652 - val_accuracy: 0.6279 - val_loss: 0.7578 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5729 - val_accuracy: 0.6336 - val_loss: 0.7402 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5548 - val_accuracy: 0.6221 - val_loss: 0.7705 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7226 - loss: 0.5583 - val_accuracy: 0.6509 - val_loss: 0.7258 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7110 - loss: 0.5595 - val_accuracy: 0.6236 - val_loss: 0.7618 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5679 - val_accuracy: 0.6365 - val_loss: 0.7579 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5692 - val_accuracy: 0.6193 - val_loss: 0.7662 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7120 - loss: 0.5576 - val_accuracy: 0.6293 - val_loss: 0.7576 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7142 - loss: 0.5601 - val_accuracy: 0.6264 - val_loss: 0.7460 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5613 - val_accuracy: 0.6279 - val_loss: 0.7494 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7153 - loss: 0.5634 - val_accuracy: 0.6365 - val_loss: 0.7473 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5578 - val_accuracy: 0.6307 - val_loss: 0.7466 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5597 - val_accuracy: 0.6351 - val_loss: 0.7481 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7241 - loss: 0.5506 - val_accuracy: 0.6307 - val_loss: 0.7701 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5674 - val_accuracy: 0.6279 - val_loss: 0.7767 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5508 - val_accuracy: 0.6480 - val_loss: 0.7371 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5574 - val_accuracy: 0.6537 - val_loss: 0.7402 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5528 - val_accuracy: 0.6523 - val_loss: 0.7492 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7130 - loss: 0.5582 - val_accuracy: 0.6293 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7229 - loss: 0.5553 - val_accuracy: 0.6379 - val_loss: 0.7686 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7183 - loss: 0.5515 - val_accuracy: 0.6580 - val_loss: 0.7342 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7269 - loss: 0.5505 - val_accuracy: 0.6394 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5560 - val_accuracy: 0.6566 - val_loss: 0.7509 - learning_rate: 0.0010
Epoch 97/500

Epoch 97: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7181 - loss: 0.5555 - val_accuracy: 0.6279 - val_loss: 0.7708 - learning_rate: 0.0010
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7404 - loss: 0.5215 - val_accuracy: 0.6523 - val_loss: 0.7322 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5172 - val_accuracy: 0.6422 - val_loss: 0.7361 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7340 - loss: 0.5210 - val_accuracy: 0.6609 - val_loss: 0.7163 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5242 - val_accuracy: 0.6595 - val_loss: 0.7377 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7282 - loss: 0.5271 - val_accuracy: 0.6279 - val_loss: 0.7500 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5149 - val_accuracy: 0.6422 - val_loss: 0.7564 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.5107 - val_accuracy: 0.6552 - val_loss: 0.7341 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7396 - loss: 0.5114 - val_accuracy: 0.6408 - val_loss: 0.7389 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5185 - val_accuracy: 0.6379 - val_loss: 0.7284 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5120 - val_accuracy: 0.6437 - val_loss: 0.7418 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5191 - val_accuracy: 0.6494 - val_loss: 0.7175 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7447 - loss: 0.5137 - val_accuracy: 0.6437 - val_loss: 0.7491 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5143 - val_accuracy: 0.6437 - val_loss: 0.7193 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.5074 - val_accuracy: 0.6451 - val_loss: 0.7181 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5204 - val_accuracy: 0.6566 - val_loss: 0.7279 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.4997 - val_accuracy: 0.6537 - val_loss: 0.7223 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5192 - val_accuracy: 0.6466 - val_loss: 0.7487 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5125 - val_accuracy: 0.6422 - val_loss: 0.7364 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5099 - val_accuracy: 0.6351 - val_loss: 0.7464 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5138 - val_accuracy: 0.6379 - val_loss: 0.7277 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5122 - val_accuracy: 0.6351 - val_loss: 0.7570 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5045 - val_accuracy: 0.6466 - val_loss: 0.7409 - learning_rate: 5.0000e-04
Epoch 120/500

Epoch 120: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.5001 - val_accuracy: 0.6422 - val_loss: 0.7303 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4910 - val_accuracy: 0.6394 - val_loss: 0.7298 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4866 - val_accuracy: 0.6422 - val_loss: 0.7323 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.4980 - val_accuracy: 0.6437 - val_loss: 0.7252 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7568 - loss: 0.4879 - val_accuracy: 0.6451 - val_loss: 0.7216 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7612 - loss: 0.4860 - val_accuracy: 0.6408 - val_loss: 0.7437 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4851 - val_accuracy: 0.6480 - val_loss: 0.7442 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4870 - val_accuracy: 0.6537 - val_loss: 0.7455 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4796 - val_accuracy: 0.6408 - val_loss: 0.7412 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4871 - val_accuracy: 0.6379 - val_loss: 0.7424 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4868 - val_accuracy: 0.6466 - val_loss: 0.7303 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4878 - val_accuracy: 0.6379 - val_loss: 0.7411 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7558 - loss: 0.4837 - val_accuracy: 0.6365 - val_loss: 0.7448 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.4931 - val_accuracy: 0.6494 - val_loss: 0.7417 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4845 - val_accuracy: 0.6509 - val_loss: 0.7455 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4844 - val_accuracy: 0.6466 - val_loss: 0.7405 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4789 - val_accuracy: 0.6408 - val_loss: 0.7404 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4813 - val_accuracy: 0.6408 - val_loss: 0.7491 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7594 - loss: 0.4821 - val_accuracy: 0.6394 - val_loss: 0.7395 - learning_rate: 2.5000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4795 - val_accuracy: 0.6451 - val_loss: 0.7410 - learning_rate: 2.5000e-04
Epoch 140/500

Epoch 140: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4866 - val_accuracy: 0.6437 - val_loss: 0.7297 - learning_rate: 2.5000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4713 - val_accuracy: 0.6523 - val_loss: 0.7227 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4693 - val_accuracy: 0.6552 - val_loss: 0.7269 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7703 - loss: 0.4676 - val_accuracy: 0.6422 - val_loss: 0.7330 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7675 - loss: 0.4682 - val_accuracy: 0.6480 - val_loss: 0.7239 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4756 - val_accuracy: 0.6523 - val_loss: 0.7228 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4699 - val_accuracy: 0.6394 - val_loss: 0.7320 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4657 - val_accuracy: 0.6480 - val_loss: 0.7244 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4728 - val_accuracy: 0.6451 - val_loss: 0.7317 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4725 - val_accuracy: 0.6466 - val_loss: 0.7355 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4822 - val_accuracy: 0.6509 - val_loss: 0.7248 - learning_rate: 1.2500e-04
Epoch 150: early stopping
Restoring model weights from the end of the best epoch: 100.
Training complete. Best epoch: 100 of 150. Best val_loss: 0.7163, val_accuracy: 0.6609

========== Evaluation: LOSO fold 10 / held-out EMS0011 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        36         4         0
  intermedia        46        28         6
  max_intens         0        22        18

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.439     0.900     0.590        40
intermediate_intensity      0.519     0.350     0.418        80
         max_intensity      0.750     0.450     0.562        40

              accuracy                          0.512       160
             macro avg      0.569     0.567     0.524       160
          weighted avg      0.557     0.512     0.497       160

Overall accuracy: 0.5125

============================================================
Fold 11 of 30: holding out EMS0012
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.42e-07, 9.59e-07]
  Per-channel std range:  [7.07e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4838 - loss: 1.0089 - val_accuracy: 0.4526 - val_loss: 1.0317 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5241 - loss: 0.9019 - val_accuracy: 0.4986 - val_loss: 0.9506 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5609 - loss: 0.8512 - val_accuracy: 0.5503 - val_loss: 0.8950 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5766 - loss: 0.8179 - val_accuracy: 0.5733 - val_loss: 0.8673 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5844 - loss: 0.7900 - val_accuracy: 0.5589 - val_loss: 0.8521 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.6037 - loss: 0.7740 - val_accuracy: 0.5905 - val_loss: 0.8309 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.6169 - loss: 0.7497 - val_accuracy: 0.5963 - val_loss: 0.8119 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6230 - loss: 0.7435 - val_accuracy: 0.5948 - val_loss: 0.8170 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6316 - loss: 0.7253 - val_accuracy: 0.6034 - val_loss: 0.8122 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6260 - loss: 0.7169 - val_accuracy: 0.6078 - val_loss: 0.7897 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6422 - loss: 0.7015 - val_accuracy: 0.6049 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6377 - loss: 0.7017 - val_accuracy: 0.6149 - val_loss: 0.7823 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6405 - loss: 0.6917 - val_accuracy: 0.6365 - val_loss: 0.7712 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6453 - loss: 0.6834 - val_accuracy: 0.5991 - val_loss: 0.7846 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6478 - loss: 0.6792 - val_accuracy: 0.6307 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6554 - loss: 0.6681 - val_accuracy: 0.6135 - val_loss: 0.7763 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6483 - loss: 0.6694 - val_accuracy: 0.6279 - val_loss: 0.7548 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6511 - loss: 0.6715 - val_accuracy: 0.6336 - val_loss: 0.7492 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6534 - loss: 0.6563 - val_accuracy: 0.6236 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6577 - loss: 0.6602 - val_accuracy: 0.6293 - val_loss: 0.7652 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6559 - loss: 0.6544 - val_accuracy: 0.6293 - val_loss: 0.7497 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6653 - loss: 0.6480 - val_accuracy: 0.6351 - val_loss: 0.7487 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6648 - loss: 0.6456 - val_accuracy: 0.6264 - val_loss: 0.7654 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6638 - loss: 0.6409 - val_accuracy: 0.6365 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6706 - loss: 0.6385 - val_accuracy: 0.6250 - val_loss: 0.7656 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6676 - loss: 0.6418 - val_accuracy: 0.6236 - val_loss: 0.7436 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6696 - loss: 0.6333 - val_accuracy: 0.6322 - val_loss: 0.7480 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6706 - loss: 0.6291 - val_accuracy: 0.6178 - val_loss: 0.7501 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6795 - loss: 0.6247 - val_accuracy: 0.6135 - val_loss: 0.7502 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6734 - loss: 0.6239 - val_accuracy: 0.6264 - val_loss: 0.7495 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6673 - loss: 0.6285 - val_accuracy: 0.6279 - val_loss: 0.7400 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6184 - val_accuracy: 0.6236 - val_loss: 0.7425 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6161 - val_accuracy: 0.6221 - val_loss: 0.7458 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6739 - loss: 0.6169 - val_accuracy: 0.6307 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6190 - val_accuracy: 0.6466 - val_loss: 0.7290 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6838 - loss: 0.6068 - val_accuracy: 0.6121 - val_loss: 0.7429 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6111 - val_accuracy: 0.6451 - val_loss: 0.7456 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6106 - val_accuracy: 0.6264 - val_loss: 0.7602 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6859 - loss: 0.6089 - val_accuracy: 0.6365 - val_loss: 0.7423 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6090 - val_accuracy: 0.6336 - val_loss: 0.7281 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.6035 - val_accuracy: 0.6293 - val_loss: 0.7375 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.6049 - val_accuracy: 0.6293 - val_loss: 0.7520 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5952 - val_accuracy: 0.6408 - val_loss: 0.7187 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.5963 - val_accuracy: 0.6351 - val_loss: 0.7126 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5973 - val_accuracy: 0.6437 - val_loss: 0.7289 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.5945 - val_accuracy: 0.6379 - val_loss: 0.7392 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6785 - loss: 0.6069 - val_accuracy: 0.6494 - val_loss: 0.7183 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5928 - val_accuracy: 0.6351 - val_loss: 0.7325 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6894 - loss: 0.5975 - val_accuracy: 0.6379 - val_loss: 0.7540 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.5923 - val_accuracy: 0.6408 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5824 - val_accuracy: 0.6437 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7074 - loss: 0.5800 - val_accuracy: 0.6336 - val_loss: 0.7329 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5825 - val_accuracy: 0.6451 - val_loss: 0.7297 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5765 - val_accuracy: 0.6523 - val_loss: 0.7132 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5801 - val_accuracy: 0.6494 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6998 - loss: 0.5776 - val_accuracy: 0.6494 - val_loss: 0.7128 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.5861 - val_accuracy: 0.6580 - val_loss: 0.7092 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5761 - val_accuracy: 0.6250 - val_loss: 0.7619 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5826 - val_accuracy: 0.6279 - val_loss: 0.7460 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7150 - loss: 0.5694 - val_accuracy: 0.6408 - val_loss: 0.7370 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5830 - val_accuracy: 0.6552 - val_loss: 0.7134 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5779 - val_accuracy: 0.6437 - val_loss: 0.7253 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5707 - val_accuracy: 0.6509 - val_loss: 0.7289 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5727 - val_accuracy: 0.6451 - val_loss: 0.7267 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5717 - val_accuracy: 0.6322 - val_loss: 0.7358 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5733 - val_accuracy: 0.6537 - val_loss: 0.7165 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5658 - val_accuracy: 0.6580 - val_loss: 0.7170 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5661 - val_accuracy: 0.6595 - val_loss: 0.7226 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5778 - val_accuracy: 0.6552 - val_loss: 0.7333 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5694 - val_accuracy: 0.6322 - val_loss: 0.7298 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7170 - loss: 0.5636 - val_accuracy: 0.6480 - val_loss: 0.7208 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.6973 - loss: 0.5666 - val_accuracy: 0.6624 - val_loss: 0.7104 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5633 - val_accuracy: 0.6379 - val_loss: 0.7403 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7112 - loss: 0.5614 - val_accuracy: 0.6293 - val_loss: 0.7577 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5614 - val_accuracy: 0.6552 - val_loss: 0.6969 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7120 - loss: 0.5533 - val_accuracy: 0.6466 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5637 - val_accuracy: 0.6307 - val_loss: 0.7303 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5655 - val_accuracy: 0.6422 - val_loss: 0.7259 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5559 - val_accuracy: 0.6422 - val_loss: 0.7226 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5627 - val_accuracy: 0.6451 - val_loss: 0.7364 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5560 - val_accuracy: 0.6595 - val_loss: 0.7160 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7150 - loss: 0.5599 - val_accuracy: 0.6480 - val_loss: 0.7460 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7107 - loss: 0.5629 - val_accuracy: 0.6164 - val_loss: 0.7308 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7196 - loss: 0.5619 - val_accuracy: 0.6466 - val_loss: 0.7522 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5489 - val_accuracy: 0.6279 - val_loss: 0.7601 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5436 - val_accuracy: 0.6523 - val_loss: 0.7067 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5450 - val_accuracy: 0.6494 - val_loss: 0.7080 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7110 - loss: 0.5524 - val_accuracy: 0.6580 - val_loss: 0.7075 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7252 - loss: 0.5473 - val_accuracy: 0.6351 - val_loss: 0.7489 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7142 - loss: 0.5518 - val_accuracy: 0.6451 - val_loss: 0.7291 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7130 - loss: 0.5545 - val_accuracy: 0.6523 - val_loss: 0.7360 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7224 - loss: 0.5459 - val_accuracy: 0.6279 - val_loss: 0.7585 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5470 - val_accuracy: 0.6322 - val_loss: 0.7502 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5491 - val_accuracy: 0.6336 - val_loss: 0.7461 - learning_rate: 0.0010
Epoch 95/500

Epoch 95: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7203 - loss: 0.5493 - val_accuracy: 0.6422 - val_loss: 0.7391 - learning_rate: 0.0010
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5149 - val_accuracy: 0.6624 - val_loss: 0.7105 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7343 - loss: 0.5161 - val_accuracy: 0.6652 - val_loss: 0.7042 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5190 - val_accuracy: 0.6638 - val_loss: 0.6913 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7470 - loss: 0.5056 - val_accuracy: 0.6580 - val_loss: 0.7085 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5106 - val_accuracy: 0.6566 - val_loss: 0.6914 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5167 - val_accuracy: 0.6667 - val_loss: 0.6903 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7490 - loss: 0.5091 - val_accuracy: 0.6710 - val_loss: 0.6942 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5191 - val_accuracy: 0.6724 - val_loss: 0.7016 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7500 - loss: 0.5069 - val_accuracy: 0.6595 - val_loss: 0.7070 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.5118 - val_accuracy: 0.6652 - val_loss: 0.7005 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5028 - val_accuracy: 0.6552 - val_loss: 0.7217 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5087 - val_accuracy: 0.6480 - val_loss: 0.7075 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5038 - val_accuracy: 0.6739 - val_loss: 0.6934 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 22ms/step - accuracy: 0.7437 - loss: 0.5076 - val_accuracy: 0.6537 - val_loss: 0.7062 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5102 - val_accuracy: 0.6652 - val_loss: 0.7040 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7470 - loss: 0.5085 - val_accuracy: 0.6667 - val_loss: 0.7115 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4983 - val_accuracy: 0.6523 - val_loss: 0.7150 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.5041 - val_accuracy: 0.6695 - val_loss: 0.6897 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5002 - val_accuracy: 0.6767 - val_loss: 0.6815 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5079 - val_accuracy: 0.6681 - val_loss: 0.6960 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.5047 - val_accuracy: 0.6652 - val_loss: 0.7171 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7505 - loss: 0.5009 - val_accuracy: 0.6580 - val_loss: 0.7170 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5029 - val_accuracy: 0.6695 - val_loss: 0.7063 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.4952 - val_accuracy: 0.6566 - val_loss: 0.6951 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7538 - loss: 0.4978 - val_accuracy: 0.6566 - val_loss: 0.7243 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7396 - loss: 0.5067 - val_accuracy: 0.6782 - val_loss: 0.7039 - learning_rate: 5.0000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7503 - loss: 0.4987 - val_accuracy: 0.6638 - val_loss: 0.7030 - learning_rate: 5.0000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7500 - loss: 0.5055 - val_accuracy: 0.6710 - val_loss: 0.7095 - learning_rate: 5.0000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7523 - loss: 0.4990 - val_accuracy: 0.6652 - val_loss: 0.7107 - learning_rate: 5.0000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5037 - val_accuracy: 0.6480 - val_loss: 0.7189 - learning_rate: 5.0000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.4948 - val_accuracy: 0.6509 - val_loss: 0.7171 - learning_rate: 5.0000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4976 - val_accuracy: 0.6552 - val_loss: 0.7103 - learning_rate: 5.0000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4898 - val_accuracy: 0.6667 - val_loss: 0.6977 - learning_rate: 5.0000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7533 - loss: 0.4956 - val_accuracy: 0.6537 - val_loss: 0.7247 - learning_rate: 5.0000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7543 - loss: 0.4929 - val_accuracy: 0.6681 - val_loss: 0.6923 - learning_rate: 5.0000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4964 - val_accuracy: 0.6638 - val_loss: 0.7100 - learning_rate: 5.0000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4962 - val_accuracy: 0.6652 - val_loss: 0.7164 - learning_rate: 5.0000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7533 - loss: 0.4932 - val_accuracy: 0.6595 - val_loss: 0.7266 - learning_rate: 5.0000e-04
Epoch 134/500

Epoch 134: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5000 - val_accuracy: 0.6681 - val_loss: 0.7214 - learning_rate: 5.0000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4667 - val_accuracy: 0.6767 - val_loss: 0.7044 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4654 - val_accuracy: 0.6724 - val_loss: 0.7077 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4772 - val_accuracy: 0.6624 - val_loss: 0.7131 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4614 - val_accuracy: 0.6609 - val_loss: 0.7223 - learning_rate: 2.5000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4695 - val_accuracy: 0.6695 - val_loss: 0.7142 - learning_rate: 2.5000e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4671 - val_accuracy: 0.6695 - val_loss: 0.7113 - learning_rate: 2.5000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4675 - val_accuracy: 0.6767 - val_loss: 0.6974 - learning_rate: 2.5000e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4749 - val_accuracy: 0.6667 - val_loss: 0.7012 - learning_rate: 2.5000e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4710 - val_accuracy: 0.6652 - val_loss: 0.7011 - learning_rate: 2.5000e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4698 - val_accuracy: 0.6695 - val_loss: 0.7064 - learning_rate: 2.5000e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4593 - val_accuracy: 0.6652 - val_loss: 0.7059 - learning_rate: 2.5000e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7751 - loss: 0.4627 - val_accuracy: 0.6825 - val_loss: 0.6902 - learning_rate: 2.5000e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4715 - val_accuracy: 0.6739 - val_loss: 0.6937 - learning_rate: 2.5000e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4633 - val_accuracy: 0.6609 - val_loss: 0.7071 - learning_rate: 2.5000e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4612 - val_accuracy: 0.6609 - val_loss: 0.7131 - learning_rate: 2.5000e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4614 - val_accuracy: 0.6753 - val_loss: 0.6982 - learning_rate: 2.5000e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4671 - val_accuracy: 0.6710 - val_loss: 0.7178 - learning_rate: 2.5000e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4711 - val_accuracy: 0.6624 - val_loss: 0.7116 - learning_rate: 2.5000e-04
Epoch 153/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4697 - val_accuracy: 0.6624 - val_loss: 0.7090 - learning_rate: 2.5000e-04
Epoch 154/500

Epoch 154: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4740 - val_accuracy: 0.6652 - val_loss: 0.7302 - learning_rate: 2.5000e-04
Epoch 155/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4635 - val_accuracy: 0.6724 - val_loss: 0.7086 - learning_rate: 1.2500e-04
Epoch 156/500
124/124 - 3s - 23ms/step - accuracy: 0.7792 - loss: 0.4600 - val_accuracy: 0.6810 - val_loss: 0.7031 - learning_rate: 1.2500e-04
Epoch 157/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4588 - val_accuracy: 0.6681 - val_loss: 0.7060 - learning_rate: 1.2500e-04
Epoch 158/500
124/124 - 3s - 23ms/step - accuracy: 0.7812 - loss: 0.4526 - val_accuracy: 0.6767 - val_loss: 0.7010 - learning_rate: 1.2500e-04
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7809 - loss: 0.4546 - val_accuracy: 0.6796 - val_loss: 0.7062 - learning_rate: 1.2500e-04
Epoch 160/500
124/124 - 3s - 23ms/step - accuracy: 0.7852 - loss: 0.4559 - val_accuracy: 0.6868 - val_loss: 0.6977 - learning_rate: 1.2500e-04
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7827 - loss: 0.4522 - val_accuracy: 0.6796 - val_loss: 0.6985 - learning_rate: 1.2500e-04
Epoch 162/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4527 - val_accuracy: 0.6796 - val_loss: 0.7021 - learning_rate: 1.2500e-04
Epoch 163/500
124/124 - 3s - 23ms/step - accuracy: 0.7787 - loss: 0.4564 - val_accuracy: 0.6753 - val_loss: 0.7045 - learning_rate: 1.2500e-04
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4538 - val_accuracy: 0.6839 - val_loss: 0.6901 - learning_rate: 1.2500e-04
Epoch 164: early stopping
Restoring model weights from the end of the best epoch: 114.
Training complete. Best epoch: 114 of 164. Best val_loss: 0.6815, val_accuracy: 0.6767

========== Evaluation: LOSO fold 11 / held-out EMS0012 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        25        15         0
  intermedia        18        58         4
  max_intens         5        20        15

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.521     0.625     0.568        40
intermediate_intensity      0.624     0.725     0.671        80
         max_intensity      0.789     0.375     0.508        40

              accuracy                          0.613       160
             macro avg      0.645     0.575     0.582       160
          weighted avg      0.639     0.613     0.604       160

Overall accuracy: 0.6125

============================================================
Fold 12 of 30: holding out EMS0013
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.08e-07, 9.63e-07]
  Per-channel std range:  [7.11e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4528 - loss: 1.0325 - val_accuracy: 0.4828 - val_loss: 1.0387 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5157 - loss: 0.9240 - val_accuracy: 0.5201 - val_loss: 0.9614 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5581 - loss: 0.8691 - val_accuracy: 0.5374 - val_loss: 0.9160 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5603 - loss: 0.8443 - val_accuracy: 0.5402 - val_loss: 0.8877 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5776 - loss: 0.8187 - val_accuracy: 0.5603 - val_loss: 0.8818 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5938 - loss: 0.7977 - val_accuracy: 0.5776 - val_loss: 0.8578 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.5969 - loss: 0.7801 - val_accuracy: 0.5876 - val_loss: 0.8549 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6098 - loss: 0.7619 - val_accuracy: 0.6106 - val_loss: 0.8317 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6027 - loss: 0.7545 - val_accuracy: 0.6034 - val_loss: 0.8244 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6156 - loss: 0.7423 - val_accuracy: 0.6049 - val_loss: 0.8090 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6230 - loss: 0.7317 - val_accuracy: 0.6121 - val_loss: 0.8143 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6225 - loss: 0.7290 - val_accuracy: 0.6149 - val_loss: 0.7987 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6235 - loss: 0.7175 - val_accuracy: 0.6078 - val_loss: 0.8042 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6298 - loss: 0.7113 - val_accuracy: 0.5991 - val_loss: 0.8036 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6356 - loss: 0.7027 - val_accuracy: 0.6034 - val_loss: 0.7879 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6412 - loss: 0.6977 - val_accuracy: 0.6049 - val_loss: 0.7928 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6412 - loss: 0.6916 - val_accuracy: 0.5905 - val_loss: 0.7983 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6448 - loss: 0.6850 - val_accuracy: 0.5934 - val_loss: 0.8031 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6471 - loss: 0.6815 - val_accuracy: 0.6121 - val_loss: 0.7960 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6443 - loss: 0.6795 - val_accuracy: 0.6092 - val_loss: 0.7839 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6405 - loss: 0.6740 - val_accuracy: 0.6092 - val_loss: 0.7881 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6501 - loss: 0.6660 - val_accuracy: 0.6178 - val_loss: 0.7829 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6531 - loss: 0.6654 - val_accuracy: 0.6221 - val_loss: 0.7831 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6501 - loss: 0.6637 - val_accuracy: 0.6106 - val_loss: 0.7911 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6537 - val_accuracy: 0.6106 - val_loss: 0.7761 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6504 - loss: 0.6594 - val_accuracy: 0.6092 - val_loss: 0.7889 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6443 - loss: 0.6594 - val_accuracy: 0.6020 - val_loss: 0.7974 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6559 - loss: 0.6551 - val_accuracy: 0.6178 - val_loss: 0.7738 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6608 - loss: 0.6464 - val_accuracy: 0.6135 - val_loss: 0.7734 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6643 - loss: 0.6444 - val_accuracy: 0.6020 - val_loss: 0.7865 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6580 - loss: 0.6496 - val_accuracy: 0.6193 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6625 - loss: 0.6369 - val_accuracy: 0.6049 - val_loss: 0.7788 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6661 - loss: 0.6336 - val_accuracy: 0.6336 - val_loss: 0.7674 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6595 - loss: 0.6265 - val_accuracy: 0.6063 - val_loss: 0.7693 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6772 - loss: 0.6276 - val_accuracy: 0.5920 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6289 - val_accuracy: 0.6193 - val_loss: 0.7801 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6752 - loss: 0.6200 - val_accuracy: 0.6149 - val_loss: 0.7741 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6197 - val_accuracy: 0.6164 - val_loss: 0.7825 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6133 - val_accuracy: 0.6135 - val_loss: 0.7719 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6704 - loss: 0.6235 - val_accuracy: 0.6106 - val_loss: 0.8010 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6749 - loss: 0.6198 - val_accuracy: 0.6178 - val_loss: 0.7655 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6119 - val_accuracy: 0.6092 - val_loss: 0.7852 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6173 - val_accuracy: 0.6264 - val_loss: 0.7756 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6891 - loss: 0.6166 - val_accuracy: 0.6221 - val_loss: 0.7743 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6739 - loss: 0.6153 - val_accuracy: 0.6322 - val_loss: 0.7591 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.6123 - val_accuracy: 0.6092 - val_loss: 0.7788 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6158 - val_accuracy: 0.6092 - val_loss: 0.7723 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6075 - val_accuracy: 0.6293 - val_loss: 0.7589 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6853 - loss: 0.6020 - val_accuracy: 0.6293 - val_loss: 0.7653 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5934 - val_accuracy: 0.6336 - val_loss: 0.7707 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.6059 - val_accuracy: 0.6322 - val_loss: 0.7829 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6894 - loss: 0.6028 - val_accuracy: 0.6207 - val_loss: 0.7822 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6032 - val_accuracy: 0.6164 - val_loss: 0.7621 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.6016 - val_accuracy: 0.6264 - val_loss: 0.7769 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5968 - val_accuracy: 0.6336 - val_loss: 0.7720 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5964 - val_accuracy: 0.6193 - val_loss: 0.7869 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5970 - val_accuracy: 0.6307 - val_loss: 0.7574 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5986 - val_accuracy: 0.6264 - val_loss: 0.7792 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6047 - val_accuracy: 0.6135 - val_loss: 0.7714 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6016 - val_accuracy: 0.6164 - val_loss: 0.7765 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5964 - val_accuracy: 0.6092 - val_loss: 0.7770 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6922 - loss: 0.5962 - val_accuracy: 0.6149 - val_loss: 0.7809 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.6970 - loss: 0.5841 - val_accuracy: 0.6365 - val_loss: 0.7435 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.5867 - val_accuracy: 0.6365 - val_loss: 0.7661 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5843 - val_accuracy: 0.6092 - val_loss: 0.8075 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.5911 - val_accuracy: 0.6322 - val_loss: 0.7835 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5897 - val_accuracy: 0.6293 - val_loss: 0.7811 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5852 - val_accuracy: 0.6351 - val_loss: 0.7611 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5818 - val_accuracy: 0.6221 - val_loss: 0.7714 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.5815 - val_accuracy: 0.6236 - val_loss: 0.7690 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5780 - val_accuracy: 0.6307 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5750 - val_accuracy: 0.6264 - val_loss: 0.7718 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6932 - loss: 0.5843 - val_accuracy: 0.6149 - val_loss: 0.7783 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5793 - val_accuracy: 0.6322 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5717 - val_accuracy: 0.6106 - val_loss: 0.7674 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5769 - val_accuracy: 0.6307 - val_loss: 0.7679 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.6922 - loss: 0.5843 - val_accuracy: 0.6121 - val_loss: 0.7900 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5752 - val_accuracy: 0.6221 - val_loss: 0.7612 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.6932 - loss: 0.5826 - val_accuracy: 0.6236 - val_loss: 0.7697 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5791 - val_accuracy: 0.6207 - val_loss: 0.7622 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5688 - val_accuracy: 0.6279 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.5815 - val_accuracy: 0.6207 - val_loss: 0.7674 - learning_rate: 0.0010
Epoch 83/500

Epoch 83: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5765 - val_accuracy: 0.6193 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7287 - loss: 0.5472 - val_accuracy: 0.6379 - val_loss: 0.7577 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7213 - loss: 0.5448 - val_accuracy: 0.6307 - val_loss: 0.7414 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5380 - val_accuracy: 0.6351 - val_loss: 0.7594 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7274 - loss: 0.5412 - val_accuracy: 0.6250 - val_loss: 0.7564 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7348 - loss: 0.5347 - val_accuracy: 0.6336 - val_loss: 0.7316 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7262 - loss: 0.5401 - val_accuracy: 0.6379 - val_loss: 0.7447 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7246 - loss: 0.5344 - val_accuracy: 0.6279 - val_loss: 0.7549 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5292 - val_accuracy: 0.6193 - val_loss: 0.7659 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7320 - loss: 0.5297 - val_accuracy: 0.6451 - val_loss: 0.7360 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7254 - loss: 0.5307 - val_accuracy: 0.6437 - val_loss: 0.7547 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7295 - loss: 0.5346 - val_accuracy: 0.6394 - val_loss: 0.7576 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5360 - val_accuracy: 0.6394 - val_loss: 0.7342 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5341 - val_accuracy: 0.6365 - val_loss: 0.7524 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7338 - loss: 0.5255 - val_accuracy: 0.6437 - val_loss: 0.7451 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7269 - loss: 0.5255 - val_accuracy: 0.6394 - val_loss: 0.7393 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7312 - loss: 0.5284 - val_accuracy: 0.6580 - val_loss: 0.7416 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7317 - loss: 0.5276 - val_accuracy: 0.6336 - val_loss: 0.7470 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5345 - val_accuracy: 0.6408 - val_loss: 0.7389 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7277 - loss: 0.5306 - val_accuracy: 0.6437 - val_loss: 0.7540 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7287 - loss: 0.5288 - val_accuracy: 0.6379 - val_loss: 0.7502 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7290 - loss: 0.5251 - val_accuracy: 0.6307 - val_loss: 0.7445 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5244 - val_accuracy: 0.6566 - val_loss: 0.7316 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5225 - val_accuracy: 0.6394 - val_loss: 0.7511 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5278 - val_accuracy: 0.6379 - val_loss: 0.7524 - learning_rate: 5.0000e-04
Epoch 108/500

Epoch 108: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7348 - loss: 0.5222 - val_accuracy: 0.6566 - val_loss: 0.7336 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5166 - val_accuracy: 0.6437 - val_loss: 0.7408 - learning_rate: 2.5000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5085 - val_accuracy: 0.6437 - val_loss: 0.7459 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5058 - val_accuracy: 0.6466 - val_loss: 0.7443 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7470 - loss: 0.5034 - val_accuracy: 0.6509 - val_loss: 0.7380 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7404 - loss: 0.5090 - val_accuracy: 0.6451 - val_loss: 0.7408 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.5000 - val_accuracy: 0.6466 - val_loss: 0.7367 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7563 - loss: 0.5039 - val_accuracy: 0.6422 - val_loss: 0.7359 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4970 - val_accuracy: 0.6466 - val_loss: 0.7298 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5011 - val_accuracy: 0.6422 - val_loss: 0.7395 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4984 - val_accuracy: 0.6451 - val_loss: 0.7476 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.4958 - val_accuracy: 0.6494 - val_loss: 0.7511 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7541 - loss: 0.4946 - val_accuracy: 0.6480 - val_loss: 0.7377 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5031 - val_accuracy: 0.6451 - val_loss: 0.7422 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7563 - loss: 0.4963 - val_accuracy: 0.6466 - val_loss: 0.7427 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5105 - val_accuracy: 0.6552 - val_loss: 0.7365 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7467 - loss: 0.4985 - val_accuracy: 0.6494 - val_loss: 0.7332 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5091 - val_accuracy: 0.6494 - val_loss: 0.7395 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5040 - val_accuracy: 0.6408 - val_loss: 0.7437 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5006 - val_accuracy: 0.6451 - val_loss: 0.7468 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5051 - val_accuracy: 0.6480 - val_loss: 0.7449 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.4971 - val_accuracy: 0.6523 - val_loss: 0.7338 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4990 - val_accuracy: 0.6451 - val_loss: 0.7442 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5059 - val_accuracy: 0.6451 - val_loss: 0.7470 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7548 - loss: 0.4997 - val_accuracy: 0.6451 - val_loss: 0.7390 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.4950 - val_accuracy: 0.6351 - val_loss: 0.7542 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.4940 - val_accuracy: 0.6480 - val_loss: 0.7442 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7525 - loss: 0.4991 - val_accuracy: 0.6307 - val_loss: 0.7423 - learning_rate: 2.5000e-04
Epoch 136/500

Epoch 136: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7515 - loss: 0.5017 - val_accuracy: 0.6394 - val_loss: 0.7434 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4871 - val_accuracy: 0.6523 - val_loss: 0.7294 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4870 - val_accuracy: 0.6466 - val_loss: 0.7313 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 24ms/step - accuracy: 0.7538 - loss: 0.4856 - val_accuracy: 0.6595 - val_loss: 0.7237 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4908 - val_accuracy: 0.6523 - val_loss: 0.7359 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4811 - val_accuracy: 0.6537 - val_loss: 0.7309 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4800 - val_accuracy: 0.6537 - val_loss: 0.7356 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7558 - loss: 0.4900 - val_accuracy: 0.6624 - val_loss: 0.7334 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4861 - val_accuracy: 0.6580 - val_loss: 0.7347 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7568 - loss: 0.4824 - val_accuracy: 0.6595 - val_loss: 0.7302 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4786 - val_accuracy: 0.6552 - val_loss: 0.7353 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4821 - val_accuracy: 0.6580 - val_loss: 0.7309 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4760 - val_accuracy: 0.6580 - val_loss: 0.7282 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4806 - val_accuracy: 0.6609 - val_loss: 0.7205 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7632 - loss: 0.4836 - val_accuracy: 0.6566 - val_loss: 0.7291 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4817 - val_accuracy: 0.6537 - val_loss: 0.7310 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4872 - val_accuracy: 0.6537 - val_loss: 0.7300 - learning_rate: 1.2500e-04
Epoch 153/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4773 - val_accuracy: 0.6509 - val_loss: 0.7356 - learning_rate: 1.2500e-04
Epoch 154/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4775 - val_accuracy: 0.6552 - val_loss: 0.7421 - learning_rate: 1.2500e-04
Epoch 155/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4857 - val_accuracy: 0.6509 - val_loss: 0.7346 - learning_rate: 1.2500e-04
Epoch 156/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4828 - val_accuracy: 0.6609 - val_loss: 0.7301 - learning_rate: 1.2500e-04
Epoch 157/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4801 - val_accuracy: 0.6523 - val_loss: 0.7309 - learning_rate: 1.2500e-04
Epoch 158/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4874 - val_accuracy: 0.6523 - val_loss: 0.7311 - learning_rate: 1.2500e-04
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4778 - val_accuracy: 0.6609 - val_loss: 0.7334 - learning_rate: 1.2500e-04
Epoch 160/500
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4702 - val_accuracy: 0.6638 - val_loss: 0.7363 - learning_rate: 1.2500e-04
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4796 - val_accuracy: 0.6523 - val_loss: 0.7435 - learning_rate: 1.2500e-04
Epoch 162/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4838 - val_accuracy: 0.6580 - val_loss: 0.7368 - learning_rate: 1.2500e-04
Epoch 163/500
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4844 - val_accuracy: 0.6580 - val_loss: 0.7319 - learning_rate: 1.2500e-04
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7599 - loss: 0.4846 - val_accuracy: 0.6638 - val_loss: 0.7269 - learning_rate: 1.2500e-04
Epoch 165/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4812 - val_accuracy: 0.6595 - val_loss: 0.7280 - learning_rate: 1.2500e-04
Epoch 166/500
124/124 - 3s - 23ms/step - accuracy: 0.7561 - loss: 0.4814 - val_accuracy: 0.6566 - val_loss: 0.7347 - learning_rate: 1.2500e-04
Epoch 167/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4882 - val_accuracy: 0.6624 - val_loss: 0.7319 - learning_rate: 1.2500e-04
Epoch 168/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4814 - val_accuracy: 0.6537 - val_loss: 0.7377 - learning_rate: 1.2500e-04
Epoch 169/500

Epoch 169: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7558 - loss: 0.4798 - val_accuracy: 0.6681 - val_loss: 0.7302 - learning_rate: 1.2500e-04
Epoch 170/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4744 - val_accuracy: 0.6667 - val_loss: 0.7289 - learning_rate: 6.2500e-05
Epoch 171/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4797 - val_accuracy: 0.6624 - val_loss: 0.7337 - learning_rate: 6.2500e-05
Epoch 172/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4742 - val_accuracy: 0.6652 - val_loss: 0.7332 - learning_rate: 6.2500e-05
Epoch 173/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4730 - val_accuracy: 0.6638 - val_loss: 0.7321 - learning_rate: 6.2500e-05
Epoch 174/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4748 - val_accuracy: 0.6652 - val_loss: 0.7352 - learning_rate: 6.2500e-05
Epoch 175/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4672 - val_accuracy: 0.6609 - val_loss: 0.7357 - learning_rate: 6.2500e-05
Epoch 176/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4816 - val_accuracy: 0.6566 - val_loss: 0.7348 - learning_rate: 6.2500e-05
Epoch 177/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4742 - val_accuracy: 0.6523 - val_loss: 0.7355 - learning_rate: 6.2500e-05
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4724 - val_accuracy: 0.6523 - val_loss: 0.7342 - learning_rate: 6.2500e-05
Epoch 179/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4823 - val_accuracy: 0.6552 - val_loss: 0.7373 - learning_rate: 6.2500e-05
Epoch 180/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4787 - val_accuracy: 0.6537 - val_loss: 0.7364 - learning_rate: 6.2500e-05
Epoch 181/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4710 - val_accuracy: 0.6595 - val_loss: 0.7314 - learning_rate: 6.2500e-05
Epoch 182/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4772 - val_accuracy: 0.6523 - val_loss: 0.7352 - learning_rate: 6.2500e-05
Epoch 183/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4745 - val_accuracy: 0.6552 - val_loss: 0.7349 - learning_rate: 6.2500e-05
Epoch 184/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4800 - val_accuracy: 0.6624 - val_loss: 0.7358 - learning_rate: 6.2500e-05
Epoch 185/500
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4717 - val_accuracy: 0.6537 - val_loss: 0.7400 - learning_rate: 6.2500e-05
Epoch 186/500
124/124 - 3s - 23ms/step - accuracy: 0.7667 - loss: 0.4740 - val_accuracy: 0.6624 - val_loss: 0.7365 - learning_rate: 6.2500e-05
Epoch 187/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4720 - val_accuracy: 0.6609 - val_loss: 0.7346 - learning_rate: 6.2500e-05
Epoch 188/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4687 - val_accuracy: 0.6566 - val_loss: 0.7356 - learning_rate: 6.2500e-05
Epoch 189/500

Epoch 189: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4747 - val_accuracy: 0.6552 - val_loss: 0.7402 - learning_rate: 6.2500e-05
Epoch 190/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4720 - val_accuracy: 0.6609 - val_loss: 0.7340 - learning_rate: 3.1250e-05
Epoch 191/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4714 - val_accuracy: 0.6609 - val_loss: 0.7360 - learning_rate: 3.1250e-05
Epoch 192/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4729 - val_accuracy: 0.6609 - val_loss: 0.7344 - learning_rate: 3.1250e-05
Epoch 193/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4687 - val_accuracy: 0.6580 - val_loss: 0.7360 - learning_rate: 3.1250e-05
Epoch 194/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4727 - val_accuracy: 0.6580 - val_loss: 0.7362 - learning_rate: 3.1250e-05
Epoch 195/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4682 - val_accuracy: 0.6609 - val_loss: 0.7348 - learning_rate: 3.1250e-05
Epoch 196/500
124/124 - 3s - 23ms/step - accuracy: 0.7736 - loss: 0.4715 - val_accuracy: 0.6624 - val_loss: 0.7351 - learning_rate: 3.1250e-05
Epoch 197/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4694 - val_accuracy: 0.6580 - val_loss: 0.7391 - learning_rate: 3.1250e-05
Epoch 198/500
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4630 - val_accuracy: 0.6595 - val_loss: 0.7346 - learning_rate: 3.1250e-05
Epoch 199/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4698 - val_accuracy: 0.6609 - val_loss: 0.7330 - learning_rate: 3.1250e-05
Epoch 199: early stopping
Restoring model weights from the end of the best epoch: 149.
Training complete. Best epoch: 149 of 199. Best val_loss: 0.7205, val_accuracy: 0.6609

========== Evaluation: LOSO fold 12 / held-out EMS0013 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        30         9         1
  intermedia        11        40        29
  max_intens         0         0        40

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.732     0.750     0.741        40
intermediate_intensity      0.816     0.500     0.620        80
         max_intensity      0.571     1.000     0.727        40

              accuracy                          0.688       160
             macro avg      0.706     0.750     0.696       160
          weighted avg      0.734     0.688     0.677       160

Overall accuracy: 0.6875

============================================================
Fold 13 of 30: holding out EMS0014
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.10e-07, 9.53e-07]
  Per-channel std range:  [7.20e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 116ms/step - accuracy: 0.4721 - loss: 1.0163 - val_accuracy: 0.4871 - val_loss: 1.0322 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5256 - loss: 0.9032 - val_accuracy: 0.5115 - val_loss: 0.9484 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5611 - loss: 0.8491 - val_accuracy: 0.5489 - val_loss: 0.9027 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5796 - loss: 0.8186 - val_accuracy: 0.5647 - val_loss: 0.8599 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5854 - loss: 0.7947 - val_accuracy: 0.5819 - val_loss: 0.8471 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5981 - loss: 0.7714 - val_accuracy: 0.5934 - val_loss: 0.8277 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6057 - loss: 0.7555 - val_accuracy: 0.6063 - val_loss: 0.8169 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6070 - loss: 0.7485 - val_accuracy: 0.6006 - val_loss: 0.8031 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6151 - loss: 0.7367 - val_accuracy: 0.6149 - val_loss: 0.8028 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6349 - loss: 0.7220 - val_accuracy: 0.6034 - val_loss: 0.7940 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6275 - loss: 0.7159 - val_accuracy: 0.6164 - val_loss: 0.7884 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6379 - loss: 0.7115 - val_accuracy: 0.6394 - val_loss: 0.7772 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6346 - loss: 0.7022 - val_accuracy: 0.6092 - val_loss: 0.7836 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6415 - loss: 0.6965 - val_accuracy: 0.6092 - val_loss: 0.7941 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6962 - val_accuracy: 0.6092 - val_loss: 0.7780 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6863 - val_accuracy: 0.5977 - val_loss: 0.7815 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6488 - loss: 0.6801 - val_accuracy: 0.6034 - val_loss: 0.7695 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6486 - loss: 0.6787 - val_accuracy: 0.6078 - val_loss: 0.7964 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6707 - val_accuracy: 0.6078 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6539 - loss: 0.6614 - val_accuracy: 0.6236 - val_loss: 0.7685 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6610 - loss: 0.6632 - val_accuracy: 0.6149 - val_loss: 0.7639 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6572 - loss: 0.6627 - val_accuracy: 0.6121 - val_loss: 0.7689 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6635 - loss: 0.6575 - val_accuracy: 0.6135 - val_loss: 0.7595 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6618 - loss: 0.6591 - val_accuracy: 0.6207 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6684 - loss: 0.6461 - val_accuracy: 0.6106 - val_loss: 0.7679 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6651 - loss: 0.6450 - val_accuracy: 0.6221 - val_loss: 0.7571 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6600 - loss: 0.6518 - val_accuracy: 0.6006 - val_loss: 0.7670 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6373 - val_accuracy: 0.6020 - val_loss: 0.7689 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6691 - loss: 0.6388 - val_accuracy: 0.6193 - val_loss: 0.7742 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6666 - loss: 0.6305 - val_accuracy: 0.6207 - val_loss: 0.7623 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6744 - loss: 0.6330 - val_accuracy: 0.6236 - val_loss: 0.7694 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6278 - val_accuracy: 0.6034 - val_loss: 0.7721 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6284 - val_accuracy: 0.6193 - val_loss: 0.7670 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6866 - loss: 0.6241 - val_accuracy: 0.6063 - val_loss: 0.7758 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.6208 - val_accuracy: 0.6078 - val_loss: 0.7613 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6813 - loss: 0.6210 - val_accuracy: 0.6307 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6853 - loss: 0.6188 - val_accuracy: 0.6221 - val_loss: 0.7610 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6099 - val_accuracy: 0.6293 - val_loss: 0.7497 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6856 - loss: 0.6128 - val_accuracy: 0.6149 - val_loss: 0.7616 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6897 - loss: 0.6119 - val_accuracy: 0.6264 - val_loss: 0.7575 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.6157 - val_accuracy: 0.6451 - val_loss: 0.7547 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6970 - loss: 0.6054 - val_accuracy: 0.6293 - val_loss: 0.7585 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.7023 - loss: 0.5987 - val_accuracy: 0.6379 - val_loss: 0.7584 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6894 - loss: 0.6022 - val_accuracy: 0.6394 - val_loss: 0.7644 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6891 - loss: 0.6041 - val_accuracy: 0.6078 - val_loss: 0.7851 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6889 - loss: 0.5965 - val_accuracy: 0.6466 - val_loss: 0.7379 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5967 - val_accuracy: 0.6365 - val_loss: 0.7602 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.5983 - val_accuracy: 0.6451 - val_loss: 0.7424 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5919 - val_accuracy: 0.6408 - val_loss: 0.7543 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5922 - val_accuracy: 0.6336 - val_loss: 0.7454 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5955 - val_accuracy: 0.6221 - val_loss: 0.7591 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5884 - val_accuracy: 0.6509 - val_loss: 0.7424 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5945 - val_accuracy: 0.6322 - val_loss: 0.7653 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6965 - loss: 0.5908 - val_accuracy: 0.6336 - val_loss: 0.7544 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.5907 - val_accuracy: 0.6236 - val_loss: 0.7495 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5879 - val_accuracy: 0.6408 - val_loss: 0.7602 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5794 - val_accuracy: 0.6307 - val_loss: 0.7556 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5851 - val_accuracy: 0.6365 - val_loss: 0.7621 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5907 - val_accuracy: 0.6509 - val_loss: 0.7384 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.7064 - loss: 0.5805 - val_accuracy: 0.6480 - val_loss: 0.7293 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.7028 - loss: 0.5753 - val_accuracy: 0.6624 - val_loss: 0.7234 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.7079 - loss: 0.5833 - val_accuracy: 0.6509 - val_loss: 0.7121 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5841 - val_accuracy: 0.6293 - val_loss: 0.7615 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5811 - val_accuracy: 0.6307 - val_loss: 0.7451 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5732 - val_accuracy: 0.6422 - val_loss: 0.7420 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5788 - val_accuracy: 0.6221 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5794 - val_accuracy: 0.6480 - val_loss: 0.7583 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7001 - loss: 0.5796 - val_accuracy: 0.6580 - val_loss: 0.7254 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5794 - val_accuracy: 0.6351 - val_loss: 0.7679 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5771 - val_accuracy: 0.6509 - val_loss: 0.7374 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5734 - val_accuracy: 0.6293 - val_loss: 0.7448 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5697 - val_accuracy: 0.6480 - val_loss: 0.7406 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7097 - loss: 0.5730 - val_accuracy: 0.6322 - val_loss: 0.7664 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5682 - val_accuracy: 0.6466 - val_loss: 0.7252 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5771 - val_accuracy: 0.6466 - val_loss: 0.7288 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5691 - val_accuracy: 0.6624 - val_loss: 0.7381 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7193 - loss: 0.5669 - val_accuracy: 0.6652 - val_loss: 0.7316 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7203 - loss: 0.5613 - val_accuracy: 0.6408 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7155 - loss: 0.5638 - val_accuracy: 0.6537 - val_loss: 0.7322 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7110 - loss: 0.5654 - val_accuracy: 0.6609 - val_loss: 0.7176 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5611 - val_accuracy: 0.6523 - val_loss: 0.7175 - learning_rate: 0.0010
Epoch 82/500

Epoch 82: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5657 - val_accuracy: 0.6580 - val_loss: 0.7327 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7269 - loss: 0.5391 - val_accuracy: 0.6466 - val_loss: 0.7231 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5348 - val_accuracy: 0.6451 - val_loss: 0.7221 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7335 - loss: 0.5354 - val_accuracy: 0.6236 - val_loss: 0.7543 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5198 - val_accuracy: 0.6494 - val_loss: 0.7376 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5247 - val_accuracy: 0.6322 - val_loss: 0.7370 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5284 - val_accuracy: 0.6422 - val_loss: 0.7382 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7404 - loss: 0.5262 - val_accuracy: 0.6437 - val_loss: 0.7320 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5262 - val_accuracy: 0.6566 - val_loss: 0.7273 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5285 - val_accuracy: 0.6480 - val_loss: 0.7146 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7388 - loss: 0.5272 - val_accuracy: 0.6408 - val_loss: 0.7316 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5214 - val_accuracy: 0.6480 - val_loss: 0.7410 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.5188 - val_accuracy: 0.6279 - val_loss: 0.7559 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7439 - loss: 0.5232 - val_accuracy: 0.6523 - val_loss: 0.7260 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7467 - loss: 0.5115 - val_accuracy: 0.6466 - val_loss: 0.7228 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5157 - val_accuracy: 0.6466 - val_loss: 0.7403 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5165 - val_accuracy: 0.6523 - val_loss: 0.7420 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5171 - val_accuracy: 0.6566 - val_loss: 0.7260 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7429 - loss: 0.5232 - val_accuracy: 0.6451 - val_loss: 0.7362 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7424 - loss: 0.5157 - val_accuracy: 0.6437 - val_loss: 0.7432 - learning_rate: 5.0000e-04
Epoch 102/500

Epoch 102: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7371 - loss: 0.5245 - val_accuracy: 0.6451 - val_loss: 0.7447 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4979 - val_accuracy: 0.6437 - val_loss: 0.7507 - learning_rate: 2.5000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7614 - loss: 0.4960 - val_accuracy: 0.6566 - val_loss: 0.7440 - learning_rate: 2.5000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4926 - val_accuracy: 0.6466 - val_loss: 0.7546 - learning_rate: 2.5000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7546 - loss: 0.4972 - val_accuracy: 0.6580 - val_loss: 0.7493 - learning_rate: 2.5000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4942 - val_accuracy: 0.6437 - val_loss: 0.7471 - learning_rate: 2.5000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4911 - val_accuracy: 0.6437 - val_loss: 0.7534 - learning_rate: 2.5000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4911 - val_accuracy: 0.6466 - val_loss: 0.7461 - learning_rate: 2.5000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7538 - loss: 0.4912 - val_accuracy: 0.6408 - val_loss: 0.7423 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4863 - val_accuracy: 0.6466 - val_loss: 0.7502 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4888 - val_accuracy: 0.6523 - val_loss: 0.7533 - learning_rate: 2.5000e-04
Epoch 112: early stopping
Restoring model weights from the end of the best epoch: 62.
Training complete. Best epoch: 62 of 112. Best val_loss: 0.7121, val_accuracy: 0.6509

========== Evaluation: LOSO fold 13 / held-out EMS0014 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        33         7         0
  intermedia        15        62         3
  max_intens         1        24        15

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.673     0.825     0.742        40
intermediate_intensity      0.667     0.775     0.717        80
         max_intensity      0.833     0.375     0.517        40

              accuracy                          0.688       160
             macro avg      0.724     0.658     0.659       160
          weighted avg      0.710     0.688     0.673       160

Overall accuracy: 0.6875

============================================================
Fold 14 of 30: holding out EMS0015
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.13e-07, 9.46e-07]
  Per-channel std range:  [7.22e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 118ms/step - accuracy: 0.4549 - loss: 1.0240 - val_accuracy: 0.4784 - val_loss: 1.0386 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5449 - loss: 0.9014 - val_accuracy: 0.5144 - val_loss: 0.9542 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5641 - loss: 0.8500 - val_accuracy: 0.5345 - val_loss: 0.9120 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5910 - loss: 0.8108 - val_accuracy: 0.5532 - val_loss: 0.8888 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5971 - loss: 0.7936 - val_accuracy: 0.5647 - val_loss: 0.8634 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.6116 - loss: 0.7706 - val_accuracy: 0.5704 - val_loss: 0.8521 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6052 - loss: 0.7565 - val_accuracy: 0.5632 - val_loss: 0.8457 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 25ms/step - accuracy: 0.6075 - loss: 0.7467 - val_accuracy: 0.5733 - val_loss: 0.8319 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 25ms/step - accuracy: 0.6131 - loss: 0.7321 - val_accuracy: 0.5805 - val_loss: 0.8250 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6268 - loss: 0.7271 - val_accuracy: 0.5948 - val_loss: 0.8304 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6301 - loss: 0.7193 - val_accuracy: 0.5833 - val_loss: 0.8248 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6209 - loss: 0.7108 - val_accuracy: 0.5905 - val_loss: 0.8139 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6372 - loss: 0.7070 - val_accuracy: 0.6106 - val_loss: 0.8019 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6346 - loss: 0.6997 - val_accuracy: 0.5991 - val_loss: 0.8021 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6445 - loss: 0.6936 - val_accuracy: 0.6049 - val_loss: 0.8074 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6460 - loss: 0.6904 - val_accuracy: 0.5963 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6453 - loss: 0.6827 - val_accuracy: 0.6063 - val_loss: 0.7964 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6466 - loss: 0.6798 - val_accuracy: 0.6006 - val_loss: 0.7975 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6501 - loss: 0.6741 - val_accuracy: 0.5948 - val_loss: 0.8161 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6496 - loss: 0.6691 - val_accuracy: 0.6034 - val_loss: 0.8097 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6721 - val_accuracy: 0.6063 - val_loss: 0.7967 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6542 - loss: 0.6653 - val_accuracy: 0.5934 - val_loss: 0.7877 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6645 - val_accuracy: 0.6049 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6595 - loss: 0.6633 - val_accuracy: 0.6121 - val_loss: 0.7758 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6538 - val_accuracy: 0.6020 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6671 - loss: 0.6501 - val_accuracy: 0.5977 - val_loss: 0.7926 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6663 - loss: 0.6432 - val_accuracy: 0.6034 - val_loss: 0.7829 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6602 - loss: 0.6440 - val_accuracy: 0.5963 - val_loss: 0.7981 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6395 - val_accuracy: 0.6164 - val_loss: 0.7703 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6770 - loss: 0.6346 - val_accuracy: 0.5963 - val_loss: 0.7962 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6752 - loss: 0.6323 - val_accuracy: 0.6092 - val_loss: 0.7904 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6332 - val_accuracy: 0.6006 - val_loss: 0.7796 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6676 - loss: 0.6382 - val_accuracy: 0.5819 - val_loss: 0.7848 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6309 - val_accuracy: 0.6034 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6742 - loss: 0.6320 - val_accuracy: 0.6121 - val_loss: 0.7868 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6209 - val_accuracy: 0.6106 - val_loss: 0.7802 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6831 - loss: 0.6209 - val_accuracy: 0.6092 - val_loss: 0.7671 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6205 - val_accuracy: 0.5948 - val_loss: 0.7740 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6230 - val_accuracy: 0.6049 - val_loss: 0.7838 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6175 - val_accuracy: 0.5991 - val_loss: 0.7884 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6818 - loss: 0.6124 - val_accuracy: 0.6034 - val_loss: 0.7749 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6072 - val_accuracy: 0.5948 - val_loss: 0.7837 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6785 - loss: 0.6153 - val_accuracy: 0.6092 - val_loss: 0.7728 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6881 - loss: 0.6082 - val_accuracy: 0.6049 - val_loss: 0.7712 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6907 - loss: 0.6005 - val_accuracy: 0.5948 - val_loss: 0.8069 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6818 - loss: 0.6139 - val_accuracy: 0.6078 - val_loss: 0.7713 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 25ms/step - accuracy: 0.6848 - loss: 0.6055 - val_accuracy: 0.6020 - val_loss: 0.7561 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6932 - loss: 0.5973 - val_accuracy: 0.5862 - val_loss: 0.7983 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.5991 - val_accuracy: 0.5934 - val_loss: 0.7912 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6034 - val_accuracy: 0.6034 - val_loss: 0.7839 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5974 - val_accuracy: 0.6078 - val_loss: 0.7934 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6859 - loss: 0.6007 - val_accuracy: 0.6006 - val_loss: 0.7852 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5822 - val_accuracy: 0.5948 - val_loss: 0.8000 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5988 - val_accuracy: 0.6149 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5878 - val_accuracy: 0.5948 - val_loss: 0.8154 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6932 - loss: 0.5938 - val_accuracy: 0.5934 - val_loss: 0.8122 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5886 - val_accuracy: 0.5920 - val_loss: 0.7925 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5872 - val_accuracy: 0.5991 - val_loss: 0.8085 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5864 - val_accuracy: 0.6063 - val_loss: 0.7756 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5845 - val_accuracy: 0.6106 - val_loss: 0.7856 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5769 - val_accuracy: 0.6121 - val_loss: 0.7914 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.5864 - val_accuracy: 0.5977 - val_loss: 0.8011 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5904 - val_accuracy: 0.5963 - val_loss: 0.7694 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5774 - val_accuracy: 0.6020 - val_loss: 0.7861 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5759 - val_accuracy: 0.6020 - val_loss: 0.7643 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5707 - val_accuracy: 0.5977 - val_loss: 0.7901 - learning_rate: 0.0010
Epoch 67/500

Epoch 67: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5753 - val_accuracy: 0.5977 - val_loss: 0.8066 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7262 - loss: 0.5518 - val_accuracy: 0.6178 - val_loss: 0.7749 - learning_rate: 5.0000e-04
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7355 - loss: 0.5386 - val_accuracy: 0.6078 - val_loss: 0.7732 - learning_rate: 5.0000e-04
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7224 - loss: 0.5448 - val_accuracy: 0.6164 - val_loss: 0.7710 - learning_rate: 5.0000e-04
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7297 - loss: 0.5481 - val_accuracy: 0.6149 - val_loss: 0.7833 - learning_rate: 5.0000e-04
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7381 - loss: 0.5386 - val_accuracy: 0.6149 - val_loss: 0.7707 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7269 - loss: 0.5424 - val_accuracy: 0.6207 - val_loss: 0.7712 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5396 - val_accuracy: 0.6207 - val_loss: 0.7796 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7323 - loss: 0.5304 - val_accuracy: 0.6164 - val_loss: 0.7850 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7290 - loss: 0.5423 - val_accuracy: 0.6264 - val_loss: 0.7681 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7284 - loss: 0.5366 - val_accuracy: 0.6135 - val_loss: 0.7709 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7355 - loss: 0.5311 - val_accuracy: 0.6164 - val_loss: 0.7779 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7300 - loss: 0.5315 - val_accuracy: 0.6135 - val_loss: 0.7788 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7371 - loss: 0.5312 - val_accuracy: 0.6178 - val_loss: 0.7572 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7323 - loss: 0.5313 - val_accuracy: 0.6078 - val_loss: 0.7996 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 24ms/step - accuracy: 0.7305 - loss: 0.5346 - val_accuracy: 0.6207 - val_loss: 0.7690 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7358 - loss: 0.5378 - val_accuracy: 0.6193 - val_loss: 0.7739 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5313 - val_accuracy: 0.6063 - val_loss: 0.7786 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5285 - val_accuracy: 0.6164 - val_loss: 0.7743 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5248 - val_accuracy: 0.6193 - val_loss: 0.7635 - learning_rate: 5.0000e-04
Epoch 87/500

Epoch 87: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7320 - loss: 0.5349 - val_accuracy: 0.6092 - val_loss: 0.7808 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7459 - loss: 0.5181 - val_accuracy: 0.6264 - val_loss: 0.7580 - learning_rate: 2.5000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7419 - loss: 0.5100 - val_accuracy: 0.6264 - val_loss: 0.7656 - learning_rate: 2.5000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7434 - loss: 0.5106 - val_accuracy: 0.6236 - val_loss: 0.7660 - learning_rate: 2.5000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7490 - loss: 0.5057 - val_accuracy: 0.6322 - val_loss: 0.7748 - learning_rate: 2.5000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7434 - loss: 0.5058 - val_accuracy: 0.6322 - val_loss: 0.7767 - learning_rate: 2.5000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7292 - loss: 0.5191 - val_accuracy: 0.6351 - val_loss: 0.7716 - learning_rate: 2.5000e-04
Epoch 94/500
124/124 - 3s - 24ms/step - accuracy: 0.7470 - loss: 0.5055 - val_accuracy: 0.6379 - val_loss: 0.7790 - learning_rate: 2.5000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7457 - loss: 0.5088 - val_accuracy: 0.6336 - val_loss: 0.7668 - learning_rate: 2.5000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7497 - loss: 0.5054 - val_accuracy: 0.6293 - val_loss: 0.7899 - learning_rate: 2.5000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7454 - loss: 0.5051 - val_accuracy: 0.6236 - val_loss: 0.7758 - learning_rate: 2.5000e-04
Epoch 97: early stopping
Restoring model weights from the end of the best epoch: 47.
Training complete. Best epoch: 47 of 97. Best val_loss: 0.7561, val_accuracy: 0.6020

========== Evaluation: LOSO fold 14 / held-out EMS0015 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        39         1         0
  intermedia        52        25         3
  max_intens         2        18        20

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.419     0.975     0.586        40
intermediate_intensity      0.568     0.312     0.403        80
         max_intensity      0.870     0.500     0.635        40

              accuracy                          0.525       160
             macro avg      0.619     0.596     0.542       160
          weighted avg      0.606     0.525     0.507       160

Overall accuracy: 0.5250

============================================================
Fold 15 of 30: holding out EMS0016
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.04e-07, 9.50e-07]
  Per-channel std range:  [7.24e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 120ms/step - accuracy: 0.4521 - loss: 1.0158 - val_accuracy: 0.4569 - val_loss: 1.0314 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5307 - loss: 0.9050 - val_accuracy: 0.5244 - val_loss: 0.9289 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5609 - loss: 0.8442 - val_accuracy: 0.5819 - val_loss: 0.8685 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5811 - loss: 0.8099 - val_accuracy: 0.5862 - val_loss: 0.8506 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 25ms/step - accuracy: 0.5865 - loss: 0.7904 - val_accuracy: 0.5891 - val_loss: 0.8346 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5966 - loss: 0.7736 - val_accuracy: 0.6078 - val_loss: 0.8166 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6002 - loss: 0.7571 - val_accuracy: 0.6149 - val_loss: 0.8074 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6116 - loss: 0.7455 - val_accuracy: 0.5934 - val_loss: 0.8083 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6212 - loss: 0.7331 - val_accuracy: 0.6063 - val_loss: 0.8023 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6245 - loss: 0.7243 - val_accuracy: 0.6307 - val_loss: 0.7858 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6303 - loss: 0.7136 - val_accuracy: 0.6178 - val_loss: 0.7842 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6364 - loss: 0.7091 - val_accuracy: 0.5977 - val_loss: 0.8023 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6359 - loss: 0.7058 - val_accuracy: 0.6063 - val_loss: 0.7889 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6435 - loss: 0.6982 - val_accuracy: 0.6135 - val_loss: 0.7864 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 25ms/step - accuracy: 0.6458 - loss: 0.6862 - val_accuracy: 0.6121 - val_loss: 0.7802 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6468 - loss: 0.6850 - val_accuracy: 0.6078 - val_loss: 0.7775 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6435 - loss: 0.6832 - val_accuracy: 0.6149 - val_loss: 0.7786 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6534 - loss: 0.6741 - val_accuracy: 0.5991 - val_loss: 0.7871 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6509 - loss: 0.6725 - val_accuracy: 0.5934 - val_loss: 0.7790 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 24ms/step - accuracy: 0.6524 - loss: 0.6691 - val_accuracy: 0.6092 - val_loss: 0.7655 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6547 - loss: 0.6698 - val_accuracy: 0.6149 - val_loss: 0.7663 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6597 - loss: 0.6600 - val_accuracy: 0.6049 - val_loss: 0.7735 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6625 - loss: 0.6582 - val_accuracy: 0.6307 - val_loss: 0.7669 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6625 - loss: 0.6533 - val_accuracy: 0.6221 - val_loss: 0.7585 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 24ms/step - accuracy: 0.6668 - loss: 0.6506 - val_accuracy: 0.6034 - val_loss: 0.7670 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 25ms/step - accuracy: 0.6651 - loss: 0.6496 - val_accuracy: 0.6236 - val_loss: 0.7540 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 25ms/step - accuracy: 0.6752 - loss: 0.6451 - val_accuracy: 0.6207 - val_loss: 0.7526 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6755 - loss: 0.6416 - val_accuracy: 0.5948 - val_loss: 0.7633 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6704 - loss: 0.6426 - val_accuracy: 0.6034 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6747 - loss: 0.6366 - val_accuracy: 0.5963 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 24ms/step - accuracy: 0.6853 - loss: 0.6302 - val_accuracy: 0.6020 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 24ms/step - accuracy: 0.6803 - loss: 0.6253 - val_accuracy: 0.6078 - val_loss: 0.7664 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6833 - loss: 0.6265 - val_accuracy: 0.6264 - val_loss: 0.7646 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6848 - loss: 0.6199 - val_accuracy: 0.6149 - val_loss: 0.7657 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6881 - loss: 0.6181 - val_accuracy: 0.6293 - val_loss: 0.7473 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6836 - loss: 0.6236 - val_accuracy: 0.6164 - val_loss: 0.7638 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 24ms/step - accuracy: 0.6940 - loss: 0.6050 - val_accuracy: 0.6236 - val_loss: 0.7597 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6826 - loss: 0.6219 - val_accuracy: 0.6063 - val_loss: 0.7628 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6118 - val_accuracy: 0.6178 - val_loss: 0.7676 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6907 - loss: 0.6131 - val_accuracy: 0.6207 - val_loss: 0.7574 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6902 - loss: 0.6124 - val_accuracy: 0.6121 - val_loss: 0.7799 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6985 - loss: 0.5985 - val_accuracy: 0.6221 - val_loss: 0.7583 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6861 - loss: 0.6104 - val_accuracy: 0.6336 - val_loss: 0.7464 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6902 - loss: 0.6085 - val_accuracy: 0.6236 - val_loss: 0.7650 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6922 - loss: 0.6051 - val_accuracy: 0.6135 - val_loss: 0.7676 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.7031 - loss: 0.5994 - val_accuracy: 0.6164 - val_loss: 0.7708 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.7026 - loss: 0.5973 - val_accuracy: 0.6264 - val_loss: 0.7607 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6973 - loss: 0.5974 - val_accuracy: 0.6250 - val_loss: 0.7794 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6962 - loss: 0.5945 - val_accuracy: 0.6322 - val_loss: 0.7399 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.6975 - loss: 0.5991 - val_accuracy: 0.6221 - val_loss: 0.7736 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.7056 - loss: 0.5927 - val_accuracy: 0.6121 - val_loss: 0.7677 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 24ms/step - accuracy: 0.7044 - loss: 0.5859 - val_accuracy: 0.6121 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.7079 - loss: 0.5928 - val_accuracy: 0.6293 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 24ms/step - accuracy: 0.6965 - loss: 0.5910 - val_accuracy: 0.6063 - val_loss: 0.7654 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 25ms/step - accuracy: 0.7011 - loss: 0.5869 - val_accuracy: 0.6351 - val_loss: 0.7378 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 24ms/step - accuracy: 0.6988 - loss: 0.5865 - val_accuracy: 0.6020 - val_loss: 0.7696 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.7092 - loss: 0.5832 - val_accuracy: 0.6164 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 24ms/step - accuracy: 0.7006 - loss: 0.5870 - val_accuracy: 0.6207 - val_loss: 0.7639 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 24ms/step - accuracy: 0.7028 - loss: 0.5891 - val_accuracy: 0.6106 - val_loss: 0.7926 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.7021 - loss: 0.5862 - val_accuracy: 0.6250 - val_loss: 0.7525 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.7011 - loss: 0.5861 - val_accuracy: 0.6178 - val_loss: 0.7890 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.7115 - loss: 0.5757 - val_accuracy: 0.6164 - val_loss: 0.7690 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.7084 - loss: 0.5860 - val_accuracy: 0.6365 - val_loss: 0.7370 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 24ms/step - accuracy: 0.7120 - loss: 0.5752 - val_accuracy: 0.6164 - val_loss: 0.7683 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.7094 - loss: 0.5764 - val_accuracy: 0.6121 - val_loss: 0.7824 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.6983 - loss: 0.5799 - val_accuracy: 0.6034 - val_loss: 0.7943 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.7077 - loss: 0.5734 - val_accuracy: 0.6264 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.7059 - loss: 0.5753 - val_accuracy: 0.6307 - val_loss: 0.7655 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.7115 - loss: 0.5659 - val_accuracy: 0.6422 - val_loss: 0.7503 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 25ms/step - accuracy: 0.7102 - loss: 0.5706 - val_accuracy: 0.6537 - val_loss: 0.7293 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.7104 - loss: 0.5762 - val_accuracy: 0.6250 - val_loss: 0.7513 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.7196 - loss: 0.5588 - val_accuracy: 0.6336 - val_loss: 0.7355 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7117 - loss: 0.5676 - val_accuracy: 0.6279 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7148 - loss: 0.5686 - val_accuracy: 0.6250 - val_loss: 0.7740 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7130 - loss: 0.5650 - val_accuracy: 0.5991 - val_loss: 0.8024 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7150 - loss: 0.5661 - val_accuracy: 0.6365 - val_loss: 0.7478 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7231 - loss: 0.5512 - val_accuracy: 0.6164 - val_loss: 0.7854 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7145 - loss: 0.5615 - val_accuracy: 0.6307 - val_loss: 0.7674 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7170 - loss: 0.5601 - val_accuracy: 0.6322 - val_loss: 0.7425 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7140 - loss: 0.5594 - val_accuracy: 0.6336 - val_loss: 0.7578 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7249 - loss: 0.5618 - val_accuracy: 0.6264 - val_loss: 0.7726 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 24ms/step - accuracy: 0.7135 - loss: 0.5615 - val_accuracy: 0.6092 - val_loss: 0.7715 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7153 - loss: 0.5657 - val_accuracy: 0.6437 - val_loss: 0.7568 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7163 - loss: 0.5500 - val_accuracy: 0.6293 - val_loss: 0.7611 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7140 - loss: 0.5576 - val_accuracy: 0.6178 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7127 - loss: 0.5612 - val_accuracy: 0.6121 - val_loss: 0.7978 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7229 - loss: 0.5591 - val_accuracy: 0.6322 - val_loss: 0.7579 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7198 - loss: 0.5529 - val_accuracy: 0.6020 - val_loss: 0.7871 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7158 - loss: 0.5589 - val_accuracy: 0.6121 - val_loss: 0.7774 - learning_rate: 0.0010
Epoch 90/500

Epoch 90: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 24ms/step - accuracy: 0.7206 - loss: 0.5551 - val_accuracy: 0.6279 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7203 - loss: 0.5347 - val_accuracy: 0.6236 - val_loss: 0.7525 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7409 - loss: 0.5233 - val_accuracy: 0.6279 - val_loss: 0.7699 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7396 - loss: 0.5218 - val_accuracy: 0.6106 - val_loss: 0.7720 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5156 - val_accuracy: 0.6351 - val_loss: 0.7450 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7419 - loss: 0.5160 - val_accuracy: 0.6221 - val_loss: 0.7591 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7371 - loss: 0.5228 - val_accuracy: 0.6221 - val_loss: 0.7538 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7310 - loss: 0.5177 - val_accuracy: 0.6408 - val_loss: 0.7506 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7394 - loss: 0.5176 - val_accuracy: 0.6437 - val_loss: 0.7462 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7497 - loss: 0.5163 - val_accuracy: 0.6437 - val_loss: 0.7542 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7376 - loss: 0.5244 - val_accuracy: 0.6264 - val_loss: 0.7591 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7475 - loss: 0.5137 - val_accuracy: 0.6351 - val_loss: 0.7676 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 24ms/step - accuracy: 0.7503 - loss: 0.5106 - val_accuracy: 0.6365 - val_loss: 0.7610 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7421 - loss: 0.5158 - val_accuracy: 0.6408 - val_loss: 0.7522 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5155 - val_accuracy: 0.6422 - val_loss: 0.7404 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5211 - val_accuracy: 0.6480 - val_loss: 0.7341 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5209 - val_accuracy: 0.6279 - val_loss: 0.7634 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5137 - val_accuracy: 0.6451 - val_loss: 0.7601 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5139 - val_accuracy: 0.6422 - val_loss: 0.7489 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5169 - val_accuracy: 0.6351 - val_loss: 0.7702 - learning_rate: 5.0000e-04
Epoch 110/500

Epoch 110: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7490 - loss: 0.5095 - val_accuracy: 0.6293 - val_loss: 0.7611 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5107 - val_accuracy: 0.6494 - val_loss: 0.7380 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.4983 - val_accuracy: 0.6494 - val_loss: 0.7368 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4957 - val_accuracy: 0.6595 - val_loss: 0.7342 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4930 - val_accuracy: 0.6509 - val_loss: 0.7458 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4929 - val_accuracy: 0.6451 - val_loss: 0.7402 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7515 - loss: 0.4901 - val_accuracy: 0.6422 - val_loss: 0.7589 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4872 - val_accuracy: 0.6695 - val_loss: 0.7343 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4912 - val_accuracy: 0.6566 - val_loss: 0.7489 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4914 - val_accuracy: 0.6451 - val_loss: 0.7501 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.4876 - val_accuracy: 0.6408 - val_loss: 0.7555 - learning_rate: 2.5000e-04
Epoch 120: early stopping
Restoring model weights from the end of the best epoch: 70.
Training complete. Best epoch: 70 of 120. Best val_loss: 0.7293, val_accuracy: 0.6537

========== Evaluation: LOSO fold 15 / held-out EMS0016 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        31         8         1
  intermedia        54        21         5
  max_intens         9        11        20

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.330     0.775     0.463        40
intermediate_intensity      0.525     0.263     0.350        80
         max_intensity      0.769     0.500     0.606        40

              accuracy                          0.450       160
             macro avg      0.541     0.513     0.473       160
          weighted avg      0.537     0.450     0.442       160

Overall accuracy: 0.4500

============================================================
Fold 16 of 30: holding out EMS0017
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.17e-07, 9.38e-07]
  Per-channel std range:  [7.25e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4455 - loss: 1.0355 - val_accuracy: 0.4670 - val_loss: 1.0475 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5226 - loss: 0.9215 - val_accuracy: 0.5057 - val_loss: 0.9540 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5553 - loss: 0.8615 - val_accuracy: 0.5345 - val_loss: 0.9009 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5799 - loss: 0.8221 - val_accuracy: 0.5302 - val_loss: 0.8862 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5931 - loss: 0.7990 - val_accuracy: 0.5546 - val_loss: 0.8728 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5979 - loss: 0.7742 - val_accuracy: 0.5647 - val_loss: 0.8434 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6065 - loss: 0.7609 - val_accuracy: 0.5819 - val_loss: 0.8333 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6169 - loss: 0.7478 - val_accuracy: 0.5848 - val_loss: 0.8235 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6245 - loss: 0.7373 - val_accuracy: 0.5948 - val_loss: 0.8192 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6306 - loss: 0.7274 - val_accuracy: 0.5934 - val_loss: 0.8149 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6265 - loss: 0.7217 - val_accuracy: 0.6092 - val_loss: 0.8050 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6303 - loss: 0.7101 - val_accuracy: 0.6006 - val_loss: 0.8070 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6354 - loss: 0.7070 - val_accuracy: 0.6149 - val_loss: 0.7827 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6392 - loss: 0.6967 - val_accuracy: 0.6049 - val_loss: 0.7963 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6395 - loss: 0.6936 - val_accuracy: 0.6193 - val_loss: 0.7843 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6468 - loss: 0.6905 - val_accuracy: 0.6121 - val_loss: 0.7857 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6486 - loss: 0.6825 - val_accuracy: 0.6078 - val_loss: 0.7792 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6504 - loss: 0.6726 - val_accuracy: 0.6322 - val_loss: 0.7721 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6534 - loss: 0.6713 - val_accuracy: 0.6250 - val_loss: 0.7736 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 24ms/step - accuracy: 0.6531 - loss: 0.6674 - val_accuracy: 0.6178 - val_loss: 0.7700 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6516 - loss: 0.6707 - val_accuracy: 0.6221 - val_loss: 0.7787 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6592 - loss: 0.6581 - val_accuracy: 0.6293 - val_loss: 0.7707 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6562 - val_accuracy: 0.6207 - val_loss: 0.7876 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6605 - loss: 0.6528 - val_accuracy: 0.6437 - val_loss: 0.7635 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6613 - loss: 0.6497 - val_accuracy: 0.6336 - val_loss: 0.7725 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6633 - loss: 0.6467 - val_accuracy: 0.6279 - val_loss: 0.7734 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6678 - loss: 0.6449 - val_accuracy: 0.6322 - val_loss: 0.7752 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6709 - loss: 0.6462 - val_accuracy: 0.6379 - val_loss: 0.7604 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6749 - loss: 0.6342 - val_accuracy: 0.6365 - val_loss: 0.7672 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6696 - loss: 0.6376 - val_accuracy: 0.6250 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6648 - loss: 0.6385 - val_accuracy: 0.6264 - val_loss: 0.7701 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6714 - loss: 0.6314 - val_accuracy: 0.6379 - val_loss: 0.7713 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6749 - loss: 0.6341 - val_accuracy: 0.6264 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6785 - loss: 0.6259 - val_accuracy: 0.6264 - val_loss: 0.7667 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6760 - loss: 0.6202 - val_accuracy: 0.6394 - val_loss: 0.7501 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6207 - val_accuracy: 0.6336 - val_loss: 0.7613 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6838 - loss: 0.6172 - val_accuracy: 0.6149 - val_loss: 0.7630 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6201 - val_accuracy: 0.6264 - val_loss: 0.7555 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.6141 - val_accuracy: 0.6236 - val_loss: 0.7743 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6195 - val_accuracy: 0.6394 - val_loss: 0.7582 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6126 - val_accuracy: 0.6336 - val_loss: 0.7469 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.6032 - val_accuracy: 0.6293 - val_loss: 0.7564 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.6014 - val_accuracy: 0.6336 - val_loss: 0.7417 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.6053 - val_accuracy: 0.6207 - val_loss: 0.7804 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6823 - loss: 0.6087 - val_accuracy: 0.6422 - val_loss: 0.7593 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5991 - val_accuracy: 0.6437 - val_loss: 0.7495 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5956 - val_accuracy: 0.6307 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6833 - loss: 0.6020 - val_accuracy: 0.6293 - val_loss: 0.7606 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.5887 - val_accuracy: 0.6379 - val_loss: 0.7569 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6952 - loss: 0.5955 - val_accuracy: 0.6466 - val_loss: 0.7398 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5804 - val_accuracy: 0.6595 - val_loss: 0.7344 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5836 - val_accuracy: 0.6207 - val_loss: 0.7760 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5888 - val_accuracy: 0.6451 - val_loss: 0.7395 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5839 - val_accuracy: 0.6408 - val_loss: 0.7502 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5739 - val_accuracy: 0.6494 - val_loss: 0.7354 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5888 - val_accuracy: 0.6580 - val_loss: 0.7382 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5868 - val_accuracy: 0.6609 - val_loss: 0.7335 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5859 - val_accuracy: 0.6566 - val_loss: 0.7297 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5815 - val_accuracy: 0.6480 - val_loss: 0.7343 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5756 - val_accuracy: 0.6710 - val_loss: 0.7240 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5734 - val_accuracy: 0.6580 - val_loss: 0.7377 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5690 - val_accuracy: 0.6609 - val_loss: 0.7404 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5772 - val_accuracy: 0.6652 - val_loss: 0.7381 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7092 - loss: 0.5816 - val_accuracy: 0.6451 - val_loss: 0.7490 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5756 - val_accuracy: 0.6466 - val_loss: 0.7528 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7135 - loss: 0.5723 - val_accuracy: 0.6480 - val_loss: 0.7500 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5778 - val_accuracy: 0.6509 - val_loss: 0.7497 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5701 - val_accuracy: 0.6537 - val_loss: 0.7199 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7056 - loss: 0.5752 - val_accuracy: 0.6509 - val_loss: 0.7255 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5751 - val_accuracy: 0.6422 - val_loss: 0.7269 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5727 - val_accuracy: 0.6336 - val_loss: 0.7327 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5680 - val_accuracy: 0.6595 - val_loss: 0.7201 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5667 - val_accuracy: 0.6695 - val_loss: 0.7267 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7168 - loss: 0.5584 - val_accuracy: 0.6537 - val_loss: 0.7593 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7107 - loss: 0.5727 - val_accuracy: 0.6494 - val_loss: 0.7603 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5748 - val_accuracy: 0.6437 - val_loss: 0.7331 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5687 - val_accuracy: 0.6609 - val_loss: 0.7333 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5682 - val_accuracy: 0.6494 - val_loss: 0.7291 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5563 - val_accuracy: 0.6466 - val_loss: 0.7347 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7135 - loss: 0.5579 - val_accuracy: 0.6437 - val_loss: 0.7610 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7112 - loss: 0.5600 - val_accuracy: 0.6537 - val_loss: 0.7362 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5601 - val_accuracy: 0.6523 - val_loss: 0.7431 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7135 - loss: 0.5602 - val_accuracy: 0.6681 - val_loss: 0.7329 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7193 - loss: 0.5570 - val_accuracy: 0.6652 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7163 - loss: 0.5554 - val_accuracy: 0.6451 - val_loss: 0.7639 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7097 - loss: 0.5637 - val_accuracy: 0.6451 - val_loss: 0.7414 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5661 - val_accuracy: 0.6566 - val_loss: 0.7234 - learning_rate: 0.0010
Epoch 88/500

Epoch 88: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5670 - val_accuracy: 0.6523 - val_loss: 0.7278 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7300 - loss: 0.5316 - val_accuracy: 0.6537 - val_loss: 0.7258 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5337 - val_accuracy: 0.6638 - val_loss: 0.7211 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7444 - loss: 0.5156 - val_accuracy: 0.6580 - val_loss: 0.7276 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5160 - val_accuracy: 0.6509 - val_loss: 0.7409 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5195 - val_accuracy: 0.6537 - val_loss: 0.7303 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7343 - loss: 0.5201 - val_accuracy: 0.6609 - val_loss: 0.7235 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5234 - val_accuracy: 0.6595 - val_loss: 0.7279 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5170 - val_accuracy: 0.6695 - val_loss: 0.7016 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5275 - val_accuracy: 0.6638 - val_loss: 0.7200 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7343 - loss: 0.5210 - val_accuracy: 0.6595 - val_loss: 0.7329 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5182 - val_accuracy: 0.6624 - val_loss: 0.7224 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5151 - val_accuracy: 0.6624 - val_loss: 0.7294 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5057 - val_accuracy: 0.6739 - val_loss: 0.7293 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5079 - val_accuracy: 0.6652 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5108 - val_accuracy: 0.6681 - val_loss: 0.7186 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5179 - val_accuracy: 0.6466 - val_loss: 0.7363 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5241 - val_accuracy: 0.6422 - val_loss: 0.7428 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5153 - val_accuracy: 0.6523 - val_loss: 0.7440 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5180 - val_accuracy: 0.6537 - val_loss: 0.7471 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5109 - val_accuracy: 0.6437 - val_loss: 0.7346 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5090 - val_accuracy: 0.6494 - val_loss: 0.7250 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5066 - val_accuracy: 0.6595 - val_loss: 0.7505 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7396 - loss: 0.5148 - val_accuracy: 0.6624 - val_loss: 0.7284 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5163 - val_accuracy: 0.6638 - val_loss: 0.7282 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.4998 - val_accuracy: 0.6624 - val_loss: 0.7202 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5153 - val_accuracy: 0.6552 - val_loss: 0.7389 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7386 - loss: 0.5136 - val_accuracy: 0.6509 - val_loss: 0.7356 - learning_rate: 5.0000e-04
Epoch 116/500

Epoch 116: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5091 - val_accuracy: 0.6624 - val_loss: 0.7289 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4934 - val_accuracy: 0.6853 - val_loss: 0.7183 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7594 - loss: 0.4888 - val_accuracy: 0.6695 - val_loss: 0.7223 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4931 - val_accuracy: 0.6667 - val_loss: 0.7210 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4926 - val_accuracy: 0.6695 - val_loss: 0.7190 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4952 - val_accuracy: 0.6695 - val_loss: 0.7316 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4885 - val_accuracy: 0.6695 - val_loss: 0.7359 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7553 - loss: 0.4861 - val_accuracy: 0.6609 - val_loss: 0.7347 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7655 - loss: 0.4802 - val_accuracy: 0.6638 - val_loss: 0.7362 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4850 - val_accuracy: 0.6638 - val_loss: 0.7399 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4895 - val_accuracy: 0.6710 - val_loss: 0.7304 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7538 - loss: 0.4845 - val_accuracy: 0.6580 - val_loss: 0.7304 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4863 - val_accuracy: 0.6638 - val_loss: 0.7259 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4860 - val_accuracy: 0.6595 - val_loss: 0.7385 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4806 - val_accuracy: 0.6667 - val_loss: 0.7378 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4864 - val_accuracy: 0.6537 - val_loss: 0.7456 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4887 - val_accuracy: 0.6710 - val_loss: 0.7354 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4865 - val_accuracy: 0.6609 - val_loss: 0.7527 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4893 - val_accuracy: 0.6566 - val_loss: 0.7553 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4806 - val_accuracy: 0.6609 - val_loss: 0.7382 - learning_rate: 2.5000e-04
Epoch 136/500

Epoch 136: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4781 - val_accuracy: 0.6566 - val_loss: 0.7540 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4730 - val_accuracy: 0.6681 - val_loss: 0.7371 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4735 - val_accuracy: 0.6681 - val_loss: 0.7397 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4701 - val_accuracy: 0.6695 - val_loss: 0.7296 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4734 - val_accuracy: 0.6695 - val_loss: 0.7366 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4685 - val_accuracy: 0.6753 - val_loss: 0.7304 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4670 - val_accuracy: 0.6724 - val_loss: 0.7305 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4683 - val_accuracy: 0.6724 - val_loss: 0.7301 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7703 - loss: 0.4687 - val_accuracy: 0.6724 - val_loss: 0.7313 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4692 - val_accuracy: 0.6839 - val_loss: 0.7284 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7594 - loss: 0.4754 - val_accuracy: 0.6739 - val_loss: 0.7379 - learning_rate: 1.2500e-04
Epoch 146: early stopping
Restoring model weights from the end of the best epoch: 96.
Training complete. Best epoch: 96 of 146. Best val_loss: 0.7016, val_accuracy: 0.6695

========== Evaluation: LOSO fold 16 / held-out EMS0017 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        25        14         1
  intermedia        29        48         3
  max_intens         7        20        13

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.410     0.625     0.495        40
intermediate_intensity      0.585     0.600     0.593        80
         max_intensity      0.765     0.325     0.456        40

              accuracy                          0.537       160
             macro avg      0.587     0.517     0.515       160
          weighted avg      0.586     0.537     0.534       160

Overall accuracy: 0.5375

============================================================
Fold 17 of 30: holding out EMS0018
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-3.97e-07, 9.58e-07]
  Per-channel std range:  [7.22e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4546 - loss: 1.0322 - val_accuracy: 0.5029 - val_loss: 1.0381 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5426 - loss: 0.9017 - val_accuracy: 0.5388 - val_loss: 0.9390 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5626 - loss: 0.8513 - val_accuracy: 0.5647 - val_loss: 0.8781 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5806 - loss: 0.8137 - val_accuracy: 0.5661 - val_loss: 0.8528 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5872 - loss: 0.7927 - val_accuracy: 0.5934 - val_loss: 0.8401 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5920 - loss: 0.7760 - val_accuracy: 0.5632 - val_loss: 0.8356 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6055 - loss: 0.7617 - val_accuracy: 0.5934 - val_loss: 0.8264 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6128 - loss: 0.7526 - val_accuracy: 0.5934 - val_loss: 0.8148 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6144 - loss: 0.7434 - val_accuracy: 0.5805 - val_loss: 0.8228 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6192 - loss: 0.7358 - val_accuracy: 0.5991 - val_loss: 0.8032 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6184 - loss: 0.7280 - val_accuracy: 0.6135 - val_loss: 0.8051 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6131 - loss: 0.7223 - val_accuracy: 0.5761 - val_loss: 0.8081 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6242 - loss: 0.7146 - val_accuracy: 0.6078 - val_loss: 0.7956 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6273 - loss: 0.7044 - val_accuracy: 0.5934 - val_loss: 0.7892 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6356 - loss: 0.6983 - val_accuracy: 0.5891 - val_loss: 0.8109 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6349 - loss: 0.6960 - val_accuracy: 0.6049 - val_loss: 0.7888 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6346 - loss: 0.6845 - val_accuracy: 0.6135 - val_loss: 0.7870 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6387 - loss: 0.6796 - val_accuracy: 0.6063 - val_loss: 0.7778 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6384 - loss: 0.6810 - val_accuracy: 0.6063 - val_loss: 0.7866 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6402 - loss: 0.6738 - val_accuracy: 0.6034 - val_loss: 0.7853 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6531 - loss: 0.6669 - val_accuracy: 0.6092 - val_loss: 0.7878 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6516 - loss: 0.6721 - val_accuracy: 0.6221 - val_loss: 0.7718 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6562 - loss: 0.6634 - val_accuracy: 0.6078 - val_loss: 0.7627 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6483 - loss: 0.6616 - val_accuracy: 0.6006 - val_loss: 0.7812 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6453 - loss: 0.6620 - val_accuracy: 0.6006 - val_loss: 0.7917 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6602 - loss: 0.6566 - val_accuracy: 0.6063 - val_loss: 0.7693 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6529 - loss: 0.6488 - val_accuracy: 0.6250 - val_loss: 0.7768 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6597 - loss: 0.6524 - val_accuracy: 0.6034 - val_loss: 0.7780 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6552 - loss: 0.6453 - val_accuracy: 0.6121 - val_loss: 0.7743 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6651 - loss: 0.6419 - val_accuracy: 0.6293 - val_loss: 0.7662 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6344 - val_accuracy: 0.6121 - val_loss: 0.7718 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6595 - loss: 0.6413 - val_accuracy: 0.6221 - val_loss: 0.7702 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6303 - val_accuracy: 0.5991 - val_loss: 0.7885 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6391 - val_accuracy: 0.6063 - val_loss: 0.7834 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6277 - val_accuracy: 0.5991 - val_loss: 0.7817 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6757 - loss: 0.6231 - val_accuracy: 0.6250 - val_loss: 0.7599 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6699 - loss: 0.6213 - val_accuracy: 0.6236 - val_loss: 0.7623 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6691 - loss: 0.6210 - val_accuracy: 0.6034 - val_loss: 0.7777 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6744 - loss: 0.6200 - val_accuracy: 0.6135 - val_loss: 0.7745 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6760 - loss: 0.6177 - val_accuracy: 0.6221 - val_loss: 0.7677 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6752 - loss: 0.6181 - val_accuracy: 0.6106 - val_loss: 0.7671 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6673 - loss: 0.6176 - val_accuracy: 0.6135 - val_loss: 0.7630 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6153 - val_accuracy: 0.6250 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6795 - loss: 0.6144 - val_accuracy: 0.6149 - val_loss: 0.7588 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6123 - val_accuracy: 0.6279 - val_loss: 0.7584 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6062 - val_accuracy: 0.6193 - val_loss: 0.7554 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6823 - loss: 0.6096 - val_accuracy: 0.6149 - val_loss: 0.7621 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6788 - loss: 0.6058 - val_accuracy: 0.6394 - val_loss: 0.7543 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.6009 - val_accuracy: 0.6379 - val_loss: 0.7401 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.5946 - val_accuracy: 0.6336 - val_loss: 0.7557 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6734 - loss: 0.6044 - val_accuracy: 0.6092 - val_loss: 0.7894 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.5930 - val_accuracy: 0.6307 - val_loss: 0.7410 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5966 - val_accuracy: 0.6207 - val_loss: 0.7591 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6772 - loss: 0.6022 - val_accuracy: 0.6193 - val_loss: 0.7686 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6018 - val_accuracy: 0.6379 - val_loss: 0.7467 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6856 - loss: 0.5966 - val_accuracy: 0.6365 - val_loss: 0.7603 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.5921 - val_accuracy: 0.6264 - val_loss: 0.7532 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6046 - val_accuracy: 0.6236 - val_loss: 0.7643 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5857 - val_accuracy: 0.6437 - val_loss: 0.7407 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5806 - val_accuracy: 0.6207 - val_loss: 0.7667 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.6884 - loss: 0.5938 - val_accuracy: 0.6437 - val_loss: 0.7357 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5794 - val_accuracy: 0.6422 - val_loss: 0.7558 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5833 - val_accuracy: 0.6250 - val_loss: 0.7563 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5910 - val_accuracy: 0.6135 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6881 - loss: 0.5856 - val_accuracy: 0.6279 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5783 - val_accuracy: 0.6351 - val_loss: 0.7420 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.5842 - val_accuracy: 0.6250 - val_loss: 0.7640 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5859 - val_accuracy: 0.6279 - val_loss: 0.7382 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5783 - val_accuracy: 0.6322 - val_loss: 0.7474 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5757 - val_accuracy: 0.6279 - val_loss: 0.7380 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5755 - val_accuracy: 0.6207 - val_loss: 0.7661 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5761 - val_accuracy: 0.6221 - val_loss: 0.7699 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5863 - val_accuracy: 0.6236 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.6952 - loss: 0.5787 - val_accuracy: 0.6379 - val_loss: 0.7650 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5688 - val_accuracy: 0.6437 - val_loss: 0.7509 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5748 - val_accuracy: 0.6322 - val_loss: 0.7561 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5650 - val_accuracy: 0.6480 - val_loss: 0.7434 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7011 - loss: 0.5765 - val_accuracy: 0.6394 - val_loss: 0.7346 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5659 - val_accuracy: 0.6422 - val_loss: 0.7338 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5705 - val_accuracy: 0.6494 - val_loss: 0.7360 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5759 - val_accuracy: 0.6236 - val_loss: 0.7654 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5768 - val_accuracy: 0.6437 - val_loss: 0.7399 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7092 - loss: 0.5702 - val_accuracy: 0.6408 - val_loss: 0.7595 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5709 - val_accuracy: 0.6422 - val_loss: 0.7460 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5606 - val_accuracy: 0.6408 - val_loss: 0.7512 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7044 - loss: 0.5664 - val_accuracy: 0.6466 - val_loss: 0.7466 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5656 - val_accuracy: 0.6537 - val_loss: 0.7407 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7163 - loss: 0.5549 - val_accuracy: 0.6322 - val_loss: 0.7680 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5599 - val_accuracy: 0.6351 - val_loss: 0.7625 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5597 - val_accuracy: 0.6523 - val_loss: 0.7332 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5606 - val_accuracy: 0.6537 - val_loss: 0.7344 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5622 - val_accuracy: 0.6552 - val_loss: 0.7399 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5548 - val_accuracy: 0.6422 - val_loss: 0.7537 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5622 - val_accuracy: 0.6307 - val_loss: 0.7453 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7148 - loss: 0.5578 - val_accuracy: 0.6307 - val_loss: 0.7666 - learning_rate: 0.0010
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5559 - val_accuracy: 0.6351 - val_loss: 0.7390 - learning_rate: 0.0010
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7175 - loss: 0.5533 - val_accuracy: 0.6408 - val_loss: 0.7504 - learning_rate: 0.0010
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5615 - val_accuracy: 0.6509 - val_loss: 0.7301 - learning_rate: 0.0010
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5553 - val_accuracy: 0.6466 - val_loss: 0.7385 - learning_rate: 0.0010
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7127 - loss: 0.5534 - val_accuracy: 0.6394 - val_loss: 0.7377 - learning_rate: 0.0010
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7249 - loss: 0.5452 - val_accuracy: 0.6595 - val_loss: 0.7382 - learning_rate: 0.0010
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5533 - val_accuracy: 0.6451 - val_loss: 0.7359 - learning_rate: 0.0010
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7150 - loss: 0.5493 - val_accuracy: 0.6580 - val_loss: 0.7347 - learning_rate: 0.0010
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5481 - val_accuracy: 0.6322 - val_loss: 0.7621 - learning_rate: 0.0010
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5489 - val_accuracy: 0.6336 - val_loss: 0.7468 - learning_rate: 0.0010
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7196 - loss: 0.5529 - val_accuracy: 0.6422 - val_loss: 0.7663 - learning_rate: 0.0010
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7175 - loss: 0.5463 - val_accuracy: 0.6379 - val_loss: 0.7563 - learning_rate: 0.0010
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7160 - loss: 0.5498 - val_accuracy: 0.6494 - val_loss: 0.7454 - learning_rate: 0.0010
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7208 - loss: 0.5504 - val_accuracy: 0.6264 - val_loss: 0.7678 - learning_rate: 0.0010
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7145 - loss: 0.5437 - val_accuracy: 0.6307 - val_loss: 0.7820 - learning_rate: 0.0010
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5587 - val_accuracy: 0.6394 - val_loss: 0.7482 - learning_rate: 0.0010
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5427 - val_accuracy: 0.6379 - val_loss: 0.7437 - learning_rate: 0.0010
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7115 - loss: 0.5517 - val_accuracy: 0.6365 - val_loss: 0.7560 - learning_rate: 0.0010
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7226 - loss: 0.5456 - val_accuracy: 0.6307 - val_loss: 0.7538 - learning_rate: 0.0010
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7208 - loss: 0.5432 - val_accuracy: 0.6437 - val_loss: 0.7493 - learning_rate: 0.0010
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5502 - val_accuracy: 0.6336 - val_loss: 0.7661 - learning_rate: 0.0010
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5410 - val_accuracy: 0.6408 - val_loss: 0.7564 - learning_rate: 0.0010
Epoch 118/500

Epoch 118: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7160 - loss: 0.5456 - val_accuracy: 0.6552 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7363 - loss: 0.5135 - val_accuracy: 0.6466 - val_loss: 0.7275 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7426 - loss: 0.5088 - val_accuracy: 0.6509 - val_loss: 0.7264 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7391 - loss: 0.5137 - val_accuracy: 0.6494 - val_loss: 0.7314 - learning_rate: 5.0000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5038 - val_accuracy: 0.6509 - val_loss: 0.7324 - learning_rate: 5.0000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7518 - loss: 0.5018 - val_accuracy: 0.6394 - val_loss: 0.7459 - learning_rate: 5.0000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.4972 - val_accuracy: 0.6437 - val_loss: 0.7313 - learning_rate: 5.0000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7490 - loss: 0.5053 - val_accuracy: 0.6466 - val_loss: 0.7388 - learning_rate: 5.0000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5108 - val_accuracy: 0.6365 - val_loss: 0.7387 - learning_rate: 5.0000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5093 - val_accuracy: 0.6537 - val_loss: 0.7280 - learning_rate: 5.0000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5115 - val_accuracy: 0.6480 - val_loss: 0.7445 - learning_rate: 5.0000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5061 - val_accuracy: 0.6595 - val_loss: 0.7147 - learning_rate: 5.0000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5032 - val_accuracy: 0.6494 - val_loss: 0.7294 - learning_rate: 5.0000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.5008 - val_accuracy: 0.6451 - val_loss: 0.7321 - learning_rate: 5.0000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4990 - val_accuracy: 0.6652 - val_loss: 0.7402 - learning_rate: 5.0000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7561 - loss: 0.4925 - val_accuracy: 0.6523 - val_loss: 0.7448 - learning_rate: 5.0000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7485 - loss: 0.4931 - val_accuracy: 0.6695 - val_loss: 0.7369 - learning_rate: 5.0000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5045 - val_accuracy: 0.6379 - val_loss: 0.7406 - learning_rate: 5.0000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7538 - loss: 0.4938 - val_accuracy: 0.6552 - val_loss: 0.7448 - learning_rate: 5.0000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4901 - val_accuracy: 0.6480 - val_loss: 0.7476 - learning_rate: 5.0000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7505 - loss: 0.4965 - val_accuracy: 0.6552 - val_loss: 0.7543 - learning_rate: 5.0000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.4941 - val_accuracy: 0.6494 - val_loss: 0.7301 - learning_rate: 5.0000e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.4887 - val_accuracy: 0.6537 - val_loss: 0.7261 - learning_rate: 5.0000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.4971 - val_accuracy: 0.6365 - val_loss: 0.7427 - learning_rate: 5.0000e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5055 - val_accuracy: 0.6466 - val_loss: 0.7554 - learning_rate: 5.0000e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.4948 - val_accuracy: 0.6681 - val_loss: 0.7296 - learning_rate: 5.0000e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.4870 - val_accuracy: 0.6437 - val_loss: 0.7437 - learning_rate: 5.0000e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7492 - loss: 0.4981 - val_accuracy: 0.6580 - val_loss: 0.7267 - learning_rate: 5.0000e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.4967 - val_accuracy: 0.6480 - val_loss: 0.7459 - learning_rate: 5.0000e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.4903 - val_accuracy: 0.6580 - val_loss: 0.7328 - learning_rate: 5.0000e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.4943 - val_accuracy: 0.6566 - val_loss: 0.7401 - learning_rate: 5.0000e-04
Epoch 149/500

Epoch 149: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.4993 - val_accuracy: 0.6667 - val_loss: 0.7280 - learning_rate: 5.0000e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7515 - loss: 0.4903 - val_accuracy: 0.6466 - val_loss: 0.7483 - learning_rate: 2.5000e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7675 - loss: 0.4718 - val_accuracy: 0.6365 - val_loss: 0.7622 - learning_rate: 2.5000e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4719 - val_accuracy: 0.6580 - val_loss: 0.7514 - learning_rate: 2.5000e-04
Epoch 153/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4686 - val_accuracy: 0.6394 - val_loss: 0.7681 - learning_rate: 2.5000e-04
Epoch 154/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4646 - val_accuracy: 0.6523 - val_loss: 0.7529 - learning_rate: 2.5000e-04
Epoch 155/500
124/124 - 3s - 24ms/step - accuracy: 0.7703 - loss: 0.4610 - val_accuracy: 0.6451 - val_loss: 0.7594 - learning_rate: 2.5000e-04
Epoch 156/500
124/124 - 3s - 23ms/step - accuracy: 0.7624 - loss: 0.4721 - val_accuracy: 0.6523 - val_loss: 0.7624 - learning_rate: 2.5000e-04
Epoch 157/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4634 - val_accuracy: 0.6480 - val_loss: 0.7592 - learning_rate: 2.5000e-04
Epoch 158/500
124/124 - 3s - 23ms/step - accuracy: 0.7548 - loss: 0.4816 - val_accuracy: 0.6509 - val_loss: 0.7568 - learning_rate: 2.5000e-04
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4717 - val_accuracy: 0.6422 - val_loss: 0.7805 - learning_rate: 2.5000e-04
Epoch 160/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4616 - val_accuracy: 0.6494 - val_loss: 0.7576 - learning_rate: 2.5000e-04
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4734 - val_accuracy: 0.6365 - val_loss: 0.7740 - learning_rate: 2.5000e-04
Epoch 162/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4633 - val_accuracy: 0.6394 - val_loss: 0.7733 - learning_rate: 2.5000e-04
Epoch 163/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4622 - val_accuracy: 0.6451 - val_loss: 0.7651 - learning_rate: 2.5000e-04
Epoch 164/500
124/124 - 3s - 24ms/step - accuracy: 0.7695 - loss: 0.4638 - val_accuracy: 0.6580 - val_loss: 0.7450 - learning_rate: 2.5000e-04
Epoch 165/500
124/124 - 3s - 24ms/step - accuracy: 0.7733 - loss: 0.4627 - val_accuracy: 0.6580 - val_loss: 0.7496 - learning_rate: 2.5000e-04
Epoch 166/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4719 - val_accuracy: 0.6537 - val_loss: 0.7527 - learning_rate: 2.5000e-04
Epoch 167/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4632 - val_accuracy: 0.6523 - val_loss: 0.7580 - learning_rate: 2.5000e-04
Epoch 168/500
124/124 - 3s - 24ms/step - accuracy: 0.7713 - loss: 0.4620 - val_accuracy: 0.6566 - val_loss: 0.7609 - learning_rate: 2.5000e-04
Epoch 169/500

Epoch 169: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7710 - loss: 0.4610 - val_accuracy: 0.6552 - val_loss: 0.7476 - learning_rate: 2.5000e-04
Epoch 170/500
124/124 - 3s - 24ms/step - accuracy: 0.7705 - loss: 0.4562 - val_accuracy: 0.6451 - val_loss: 0.7567 - learning_rate: 1.2500e-04
Epoch 171/500
124/124 - 3s - 23ms/step - accuracy: 0.7832 - loss: 0.4485 - val_accuracy: 0.6480 - val_loss: 0.7479 - learning_rate: 1.2500e-04
Epoch 172/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4535 - val_accuracy: 0.6595 - val_loss: 0.7470 - learning_rate: 1.2500e-04
Epoch 173/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4522 - val_accuracy: 0.6595 - val_loss: 0.7569 - learning_rate: 1.2500e-04
Epoch 174/500
124/124 - 3s - 23ms/step - accuracy: 0.7837 - loss: 0.4476 - val_accuracy: 0.6566 - val_loss: 0.7507 - learning_rate: 1.2500e-04
Epoch 175/500
124/124 - 3s - 23ms/step - accuracy: 0.7814 - loss: 0.4495 - val_accuracy: 0.6595 - val_loss: 0.7564 - learning_rate: 1.2500e-04
Epoch 176/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4582 - val_accuracy: 0.6537 - val_loss: 0.7537 - learning_rate: 1.2500e-04
Epoch 177/500
124/124 - 3s - 23ms/step - accuracy: 0.7847 - loss: 0.4488 - val_accuracy: 0.6422 - val_loss: 0.7560 - learning_rate: 1.2500e-04
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7680 - loss: 0.4643 - val_accuracy: 0.6580 - val_loss: 0.7559 - learning_rate: 1.2500e-04
Epoch 179/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4547 - val_accuracy: 0.6552 - val_loss: 0.7529 - learning_rate: 1.2500e-04
Epoch 179: early stopping
Restoring model weights from the end of the best epoch: 129.
Training complete. Best epoch: 129 of 179. Best val_loss: 0.7147, val_accuracy: 0.6595

========== Evaluation: LOSO fold 17 / held-out EMS0018 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        35         5         0
  intermedia        23        41        16
  max_intens         0        19        21

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.603     0.875     0.714        40
intermediate_intensity      0.631     0.512     0.566        80
         max_intensity      0.568     0.525     0.545        40

              accuracy                          0.606       160
             macro avg      0.601     0.638     0.608       160
          weighted avg      0.608     0.606     0.598       160

Overall accuracy: 0.6062

============================================================
Fold 18 of 30: holding out EMS0019
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-3.95e-07, 9.57e-07]
  Per-channel std range:  [7.19e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 117ms/step - accuracy: 0.4544 - loss: 1.0409 - val_accuracy: 0.5101 - val_loss: 1.0423 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5261 - loss: 0.9154 - val_accuracy: 0.5402 - val_loss: 0.9298 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5621 - loss: 0.8547 - val_accuracy: 0.5632 - val_loss: 0.8879 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5801 - loss: 0.8182 - val_accuracy: 0.5704 - val_loss: 0.8643 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5951 - loss: 0.7948 - val_accuracy: 0.5833 - val_loss: 0.8467 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5966 - loss: 0.7809 - val_accuracy: 0.5920 - val_loss: 0.8456 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6108 - loss: 0.7616 - val_accuracy: 0.5891 - val_loss: 0.8373 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6103 - loss: 0.7499 - val_accuracy: 0.5934 - val_loss: 0.8282 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6265 - loss: 0.7371 - val_accuracy: 0.5934 - val_loss: 0.8108 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6151 - loss: 0.7326 - val_accuracy: 0.6006 - val_loss: 0.8077 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6303 - loss: 0.7165 - val_accuracy: 0.6221 - val_loss: 0.7902 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6313 - loss: 0.7042 - val_accuracy: 0.6034 - val_loss: 0.7883 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6334 - loss: 0.7011 - val_accuracy: 0.6149 - val_loss: 0.7828 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6326 - loss: 0.6945 - val_accuracy: 0.6149 - val_loss: 0.7858 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6344 - loss: 0.6919 - val_accuracy: 0.6236 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6402 - loss: 0.6843 - val_accuracy: 0.6336 - val_loss: 0.7663 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6511 - loss: 0.6731 - val_accuracy: 0.6307 - val_loss: 0.7654 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6519 - loss: 0.6714 - val_accuracy: 0.6264 - val_loss: 0.7619 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6506 - loss: 0.6683 - val_accuracy: 0.6149 - val_loss: 0.7632 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6547 - loss: 0.6605 - val_accuracy: 0.6236 - val_loss: 0.7692 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6587 - loss: 0.6532 - val_accuracy: 0.6250 - val_loss: 0.7634 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6694 - loss: 0.6486 - val_accuracy: 0.6408 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6590 - loss: 0.6460 - val_accuracy: 0.6322 - val_loss: 0.7510 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6638 - loss: 0.6411 - val_accuracy: 0.6365 - val_loss: 0.7423 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6678 - loss: 0.6452 - val_accuracy: 0.6149 - val_loss: 0.7592 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6628 - loss: 0.6423 - val_accuracy: 0.6394 - val_loss: 0.7545 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6630 - loss: 0.6355 - val_accuracy: 0.6494 - val_loss: 0.7377 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6739 - loss: 0.6256 - val_accuracy: 0.6365 - val_loss: 0.7489 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6747 - loss: 0.6241 - val_accuracy: 0.6264 - val_loss: 0.7528 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6279 - val_accuracy: 0.6365 - val_loss: 0.7496 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6154 - val_accuracy: 0.6135 - val_loss: 0.7735 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6864 - loss: 0.6165 - val_accuracy: 0.6236 - val_loss: 0.7468 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6090 - val_accuracy: 0.6034 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6823 - loss: 0.6124 - val_accuracy: 0.6336 - val_loss: 0.7351 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6838 - loss: 0.6041 - val_accuracy: 0.6236 - val_loss: 0.7520 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6141 - val_accuracy: 0.6307 - val_loss: 0.7413 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6102 - val_accuracy: 0.6149 - val_loss: 0.7505 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6823 - loss: 0.6046 - val_accuracy: 0.6322 - val_loss: 0.7451 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6826 - loss: 0.6038 - val_accuracy: 0.6250 - val_loss: 0.7383 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6940 - loss: 0.5979 - val_accuracy: 0.6193 - val_loss: 0.7607 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6024 - val_accuracy: 0.6379 - val_loss: 0.7284 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6793 - loss: 0.6042 - val_accuracy: 0.6293 - val_loss: 0.7216 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5948 - val_accuracy: 0.6293 - val_loss: 0.7279 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.5930 - val_accuracy: 0.6336 - val_loss: 0.7373 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5928 - val_accuracy: 0.6236 - val_loss: 0.7427 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5871 - val_accuracy: 0.6351 - val_loss: 0.7279 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6876 - loss: 0.5962 - val_accuracy: 0.6351 - val_loss: 0.7407 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6891 - loss: 0.5895 - val_accuracy: 0.6178 - val_loss: 0.7357 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6980 - loss: 0.5917 - val_accuracy: 0.6293 - val_loss: 0.7335 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5920 - val_accuracy: 0.6193 - val_loss: 0.7470 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6988 - loss: 0.5805 - val_accuracy: 0.6322 - val_loss: 0.7110 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5773 - val_accuracy: 0.6494 - val_loss: 0.7192 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6940 - loss: 0.5826 - val_accuracy: 0.6264 - val_loss: 0.7434 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5861 - val_accuracy: 0.6379 - val_loss: 0.7137 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5763 - val_accuracy: 0.6307 - val_loss: 0.7346 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5746 - val_accuracy: 0.6422 - val_loss: 0.7306 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5878 - val_accuracy: 0.6422 - val_loss: 0.7347 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5782 - val_accuracy: 0.6480 - val_loss: 0.7219 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5691 - val_accuracy: 0.6394 - val_loss: 0.7251 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5734 - val_accuracy: 0.6509 - val_loss: 0.7343 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7023 - loss: 0.5681 - val_accuracy: 0.6264 - val_loss: 0.7468 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5690 - val_accuracy: 0.6509 - val_loss: 0.7290 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7115 - loss: 0.5663 - val_accuracy: 0.6451 - val_loss: 0.7246 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5660 - val_accuracy: 0.6422 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7059 - loss: 0.5669 - val_accuracy: 0.6351 - val_loss: 0.7208 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5696 - val_accuracy: 0.6408 - val_loss: 0.7209 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7079 - loss: 0.5619 - val_accuracy: 0.6264 - val_loss: 0.7277 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5670 - val_accuracy: 0.6437 - val_loss: 0.7161 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5700 - val_accuracy: 0.6379 - val_loss: 0.7370 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7226 - loss: 0.5576 - val_accuracy: 0.6250 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 71/500

Epoch 71: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5602 - val_accuracy: 0.6394 - val_loss: 0.7180 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7300 - loss: 0.5335 - val_accuracy: 0.6480 - val_loss: 0.7174 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5200 - val_accuracy: 0.6336 - val_loss: 0.7303 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5264 - val_accuracy: 0.6365 - val_loss: 0.7195 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5241 - val_accuracy: 0.6537 - val_loss: 0.7080 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5191 - val_accuracy: 0.6609 - val_loss: 0.7124 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5265 - val_accuracy: 0.6437 - val_loss: 0.7120 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5214 - val_accuracy: 0.6379 - val_loss: 0.7150 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7432 - loss: 0.5166 - val_accuracy: 0.6466 - val_loss: 0.7036 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7383 - loss: 0.5201 - val_accuracy: 0.6451 - val_loss: 0.7165 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5199 - val_accuracy: 0.6351 - val_loss: 0.7159 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5137 - val_accuracy: 0.6422 - val_loss: 0.7292 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7272 - loss: 0.5266 - val_accuracy: 0.6451 - val_loss: 0.7153 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5150 - val_accuracy: 0.6609 - val_loss: 0.7174 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7386 - loss: 0.5152 - val_accuracy: 0.6595 - val_loss: 0.7132 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7343 - loss: 0.5230 - val_accuracy: 0.6595 - val_loss: 0.7137 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7381 - loss: 0.5178 - val_accuracy: 0.6537 - val_loss: 0.7146 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5119 - val_accuracy: 0.6537 - val_loss: 0.7121 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7447 - loss: 0.5123 - val_accuracy: 0.6307 - val_loss: 0.7123 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5095 - val_accuracy: 0.6379 - val_loss: 0.7273 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5063 - val_accuracy: 0.6494 - val_loss: 0.7058 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5140 - val_accuracy: 0.6509 - val_loss: 0.6971 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5088 - val_accuracy: 0.6552 - val_loss: 0.7198 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.5059 - val_accuracy: 0.6595 - val_loss: 0.7046 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5138 - val_accuracy: 0.6422 - val_loss: 0.7098 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5128 - val_accuracy: 0.6394 - val_loss: 0.7081 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5083 - val_accuracy: 0.6523 - val_loss: 0.7164 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.5013 - val_accuracy: 0.6494 - val_loss: 0.7221 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5069 - val_accuracy: 0.6394 - val_loss: 0.7251 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5040 - val_accuracy: 0.6494 - val_loss: 0.7000 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5003 - val_accuracy: 0.6494 - val_loss: 0.7161 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.5069 - val_accuracy: 0.6451 - val_loss: 0.7323 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5039 - val_accuracy: 0.6437 - val_loss: 0.7230 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5063 - val_accuracy: 0.6537 - val_loss: 0.7079 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5155 - val_accuracy: 0.6509 - val_loss: 0.7157 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5056 - val_accuracy: 0.6480 - val_loss: 0.7227 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.5026 - val_accuracy: 0.6552 - val_loss: 0.7223 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.4968 - val_accuracy: 0.6408 - val_loss: 0.7343 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5119 - val_accuracy: 0.6494 - val_loss: 0.7257 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5055 - val_accuracy: 0.6451 - val_loss: 0.7106 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.4993 - val_accuracy: 0.6652 - val_loss: 0.6994 - learning_rate: 5.0000e-04
Epoch 112/500

Epoch 112: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7386 - loss: 0.5019 - val_accuracy: 0.6480 - val_loss: 0.7244 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7591 - loss: 0.4857 - val_accuracy: 0.6422 - val_loss: 0.7342 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4843 - val_accuracy: 0.6509 - val_loss: 0.7159 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4832 - val_accuracy: 0.6466 - val_loss: 0.7270 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4749 - val_accuracy: 0.6437 - val_loss: 0.7246 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7551 - loss: 0.4778 - val_accuracy: 0.6494 - val_loss: 0.7208 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4724 - val_accuracy: 0.6566 - val_loss: 0.7149 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7541 - loss: 0.4799 - val_accuracy: 0.6552 - val_loss: 0.7188 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4788 - val_accuracy: 0.6566 - val_loss: 0.7237 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7657 - loss: 0.4757 - val_accuracy: 0.6466 - val_loss: 0.7243 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7581 - loss: 0.4779 - val_accuracy: 0.6422 - val_loss: 0.7186 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4744 - val_accuracy: 0.6422 - val_loss: 0.7281 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7624 - loss: 0.4766 - val_accuracy: 0.6379 - val_loss: 0.7245 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7579 - loss: 0.4798 - val_accuracy: 0.6451 - val_loss: 0.7214 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7568 - loss: 0.4806 - val_accuracy: 0.6466 - val_loss: 0.7253 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7612 - loss: 0.4744 - val_accuracy: 0.6437 - val_loss: 0.7324 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4757 - val_accuracy: 0.6422 - val_loss: 0.7268 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4720 - val_accuracy: 0.6408 - val_loss: 0.7314 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.4813 - val_accuracy: 0.6437 - val_loss: 0.7216 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7563 - loss: 0.4794 - val_accuracy: 0.6379 - val_loss: 0.7223 - learning_rate: 2.5000e-04
Epoch 132/500

Epoch 132: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4773 - val_accuracy: 0.6523 - val_loss: 0.7149 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4685 - val_accuracy: 0.6552 - val_loss: 0.6963 - learning_rate: 1.2500e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7629 - loss: 0.4631 - val_accuracy: 0.6523 - val_loss: 0.7006 - learning_rate: 1.2500e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4675 - val_accuracy: 0.6566 - val_loss: 0.7067 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4606 - val_accuracy: 0.6537 - val_loss: 0.6996 - learning_rate: 1.2500e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4580 - val_accuracy: 0.6595 - val_loss: 0.6975 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4698 - val_accuracy: 0.6523 - val_loss: 0.7092 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7665 - loss: 0.4644 - val_accuracy: 0.6523 - val_loss: 0.7050 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4588 - val_accuracy: 0.6451 - val_loss: 0.7115 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4779 - val_accuracy: 0.6624 - val_loss: 0.7103 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7708 - loss: 0.4655 - val_accuracy: 0.6624 - val_loss: 0.7120 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7601 - loss: 0.4632 - val_accuracy: 0.6681 - val_loss: 0.7063 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4530 - val_accuracy: 0.6566 - val_loss: 0.7150 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4630 - val_accuracy: 0.6580 - val_loss: 0.7114 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4614 - val_accuracy: 0.6580 - val_loss: 0.7100 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4555 - val_accuracy: 0.6638 - val_loss: 0.7077 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4610 - val_accuracy: 0.6638 - val_loss: 0.7051 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7764 - loss: 0.4601 - val_accuracy: 0.6552 - val_loss: 0.7147 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4629 - val_accuracy: 0.6509 - val_loss: 0.7121 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4584 - val_accuracy: 0.6580 - val_loss: 0.7079 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4636 - val_accuracy: 0.6652 - val_loss: 0.7095 - learning_rate: 1.2500e-04
Epoch 153/500

Epoch 153: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4691 - val_accuracy: 0.6595 - val_loss: 0.7144 - learning_rate: 1.2500e-04
Epoch 154/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4522 - val_accuracy: 0.6710 - val_loss: 0.7022 - learning_rate: 6.2500e-05
Epoch 155/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4568 - val_accuracy: 0.6609 - val_loss: 0.7026 - learning_rate: 6.2500e-05
Epoch 156/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4608 - val_accuracy: 0.6638 - val_loss: 0.7075 - learning_rate: 6.2500e-05
Epoch 157/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4565 - val_accuracy: 0.6624 - val_loss: 0.7056 - learning_rate: 6.2500e-05
Epoch 158/500
124/124 - 3s - 23ms/step - accuracy: 0.7741 - loss: 0.4554 - val_accuracy: 0.6681 - val_loss: 0.7021 - learning_rate: 6.2500e-05
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4582 - val_accuracy: 0.6681 - val_loss: 0.7014 - learning_rate: 6.2500e-05
Epoch 160/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4598 - val_accuracy: 0.6609 - val_loss: 0.7067 - learning_rate: 6.2500e-05
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4526 - val_accuracy: 0.6710 - val_loss: 0.7019 - learning_rate: 6.2500e-05
Epoch 162/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4603 - val_accuracy: 0.6667 - val_loss: 0.7046 - learning_rate: 6.2500e-05
Epoch 163/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4463 - val_accuracy: 0.6609 - val_loss: 0.7064 - learning_rate: 6.2500e-05
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4530 - val_accuracy: 0.6710 - val_loss: 0.7010 - learning_rate: 6.2500e-05
Epoch 165/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4601 - val_accuracy: 0.6595 - val_loss: 0.7089 - learning_rate: 6.2500e-05
Epoch 166/500
124/124 - 3s - 23ms/step - accuracy: 0.7647 - loss: 0.4573 - val_accuracy: 0.6652 - val_loss: 0.7018 - learning_rate: 6.2500e-05
Epoch 167/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4608 - val_accuracy: 0.6624 - val_loss: 0.7032 - learning_rate: 6.2500e-05
Epoch 168/500
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4530 - val_accuracy: 0.6609 - val_loss: 0.7037 - learning_rate: 6.2500e-05
Epoch 169/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4509 - val_accuracy: 0.6624 - val_loss: 0.6946 - learning_rate: 6.2500e-05
Epoch 170/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4520 - val_accuracy: 0.6652 - val_loss: 0.7011 - learning_rate: 6.2500e-05
Epoch 171/500
124/124 - 3s - 23ms/step - accuracy: 0.7693 - loss: 0.4568 - val_accuracy: 0.6595 - val_loss: 0.7028 - learning_rate: 6.2500e-05
Epoch 172/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4560 - val_accuracy: 0.6609 - val_loss: 0.7023 - learning_rate: 6.2500e-05
Epoch 173/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4546 - val_accuracy: 0.6638 - val_loss: 0.7085 - learning_rate: 6.2500e-05
Epoch 174/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4530 - val_accuracy: 0.6652 - val_loss: 0.6973 - learning_rate: 6.2500e-05
Epoch 175/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4558 - val_accuracy: 0.6595 - val_loss: 0.7095 - learning_rate: 6.2500e-05
Epoch 176/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4531 - val_accuracy: 0.6624 - val_loss: 0.7105 - learning_rate: 6.2500e-05
Epoch 177/500
124/124 - 3s - 23ms/step - accuracy: 0.7693 - loss: 0.4517 - val_accuracy: 0.6652 - val_loss: 0.7001 - learning_rate: 6.2500e-05
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7693 - loss: 0.4536 - val_accuracy: 0.6624 - val_loss: 0.7028 - learning_rate: 6.2500e-05
Epoch 179/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4573 - val_accuracy: 0.6695 - val_loss: 0.7016 - learning_rate: 6.2500e-05
Epoch 180/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4666 - val_accuracy: 0.6609 - val_loss: 0.7039 - learning_rate: 6.2500e-05
Epoch 181/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4574 - val_accuracy: 0.6609 - val_loss: 0.7043 - learning_rate: 6.2500e-05
Epoch 182/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4549 - val_accuracy: 0.6638 - val_loss: 0.7018 - learning_rate: 6.2500e-05
Epoch 183/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4522 - val_accuracy: 0.6638 - val_loss: 0.7044 - learning_rate: 6.2500e-05
Epoch 184/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4464 - val_accuracy: 0.6652 - val_loss: 0.7022 - learning_rate: 6.2500e-05
Epoch 185/500
124/124 - 3s - 23ms/step - accuracy: 0.7789 - loss: 0.4487 - val_accuracy: 0.6681 - val_loss: 0.7061 - learning_rate: 6.2500e-05
Epoch 186/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4537 - val_accuracy: 0.6695 - val_loss: 0.7034 - learning_rate: 6.2500e-05
Epoch 187/500
124/124 - 3s - 23ms/step - accuracy: 0.7802 - loss: 0.4503 - val_accuracy: 0.6652 - val_loss: 0.7002 - learning_rate: 6.2500e-05
Epoch 188/500
124/124 - 3s - 23ms/step - accuracy: 0.7812 - loss: 0.4468 - val_accuracy: 0.6638 - val_loss: 0.7051 - learning_rate: 6.2500e-05
Epoch 189/500

Epoch 189: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7693 - loss: 0.4528 - val_accuracy: 0.6667 - val_loss: 0.6959 - learning_rate: 6.2500e-05
Epoch 190/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4530 - val_accuracy: 0.6767 - val_loss: 0.6944 - learning_rate: 3.1250e-05
Epoch 191/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4459 - val_accuracy: 0.6710 - val_loss: 0.6928 - learning_rate: 3.1250e-05
Epoch 192/500
124/124 - 3s - 23ms/step - accuracy: 0.7832 - loss: 0.4436 - val_accuracy: 0.6724 - val_loss: 0.6931 - learning_rate: 3.1250e-05
Epoch 193/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4486 - val_accuracy: 0.6724 - val_loss: 0.6966 - learning_rate: 3.1250e-05
Epoch 194/500
124/124 - 3s - 23ms/step - accuracy: 0.7809 - loss: 0.4502 - val_accuracy: 0.6767 - val_loss: 0.6917 - learning_rate: 3.1250e-05
Epoch 195/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4455 - val_accuracy: 0.6695 - val_loss: 0.6948 - learning_rate: 3.1250e-05
Epoch 196/500
124/124 - 3s - 23ms/step - accuracy: 0.7804 - loss: 0.4511 - val_accuracy: 0.6710 - val_loss: 0.6972 - learning_rate: 3.1250e-05
Epoch 197/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4575 - val_accuracy: 0.6667 - val_loss: 0.6975 - learning_rate: 3.1250e-05
Epoch 198/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4502 - val_accuracy: 0.6710 - val_loss: 0.6945 - learning_rate: 3.1250e-05
Epoch 199/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4470 - val_accuracy: 0.6767 - val_loss: 0.6956 - learning_rate: 3.1250e-05
Epoch 200/500
124/124 - 3s - 23ms/step - accuracy: 0.7792 - loss: 0.4461 - val_accuracy: 0.6710 - val_loss: 0.6948 - learning_rate: 3.1250e-05
Epoch 201/500
124/124 - 3s - 23ms/step - accuracy: 0.7804 - loss: 0.4457 - val_accuracy: 0.6710 - val_loss: 0.6905 - learning_rate: 3.1250e-05
Epoch 202/500
124/124 - 3s - 23ms/step - accuracy: 0.7837 - loss: 0.4492 - val_accuracy: 0.6739 - val_loss: 0.6934 - learning_rate: 3.1250e-05
Epoch 203/500
124/124 - 3s - 23ms/step - accuracy: 0.7883 - loss: 0.4444 - val_accuracy: 0.6739 - val_loss: 0.6948 - learning_rate: 3.1250e-05
Epoch 204/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4492 - val_accuracy: 0.6739 - val_loss: 0.6930 - learning_rate: 3.1250e-05
Epoch 205/500
124/124 - 3s - 23ms/step - accuracy: 0.7741 - loss: 0.4472 - val_accuracy: 0.6710 - val_loss: 0.6930 - learning_rate: 3.1250e-05
Epoch 206/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4526 - val_accuracy: 0.6695 - val_loss: 0.6922 - learning_rate: 3.1250e-05
Epoch 207/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4507 - val_accuracy: 0.6710 - val_loss: 0.6980 - learning_rate: 3.1250e-05
Epoch 208/500
124/124 - 3s - 23ms/step - accuracy: 0.7817 - loss: 0.4480 - val_accuracy: 0.6710 - val_loss: 0.6958 - learning_rate: 3.1250e-05
Epoch 209/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4541 - val_accuracy: 0.6695 - val_loss: 0.6914 - learning_rate: 3.1250e-05
Epoch 210/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4534 - val_accuracy: 0.6681 - val_loss: 0.6926 - learning_rate: 3.1250e-05
Epoch 211/500
124/124 - 3s - 23ms/step - accuracy: 0.7830 - loss: 0.4434 - val_accuracy: 0.6681 - val_loss: 0.6937 - learning_rate: 3.1250e-05
Epoch 212/500
124/124 - 3s - 23ms/step - accuracy: 0.7822 - loss: 0.4434 - val_accuracy: 0.6652 - val_loss: 0.6906 - learning_rate: 3.1250e-05
Epoch 213/500
124/124 - 3s - 23ms/step - accuracy: 0.7809 - loss: 0.4431 - val_accuracy: 0.6667 - val_loss: 0.6940 - learning_rate: 3.1250e-05
Epoch 214/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4579 - val_accuracy: 0.6695 - val_loss: 0.6954 - learning_rate: 3.1250e-05
Epoch 215/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4470 - val_accuracy: 0.6652 - val_loss: 0.6942 - learning_rate: 3.1250e-05
Epoch 216/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4469 - val_accuracy: 0.6710 - val_loss: 0.6903 - learning_rate: 3.1250e-05
Epoch 217/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4497 - val_accuracy: 0.6710 - val_loss: 0.6860 - learning_rate: 3.1250e-05
Epoch 218/500
124/124 - 3s - 23ms/step - accuracy: 0.7797 - loss: 0.4484 - val_accuracy: 0.6695 - val_loss: 0.6913 - learning_rate: 3.1250e-05
Epoch 219/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4477 - val_accuracy: 0.6739 - val_loss: 0.6919 - learning_rate: 3.1250e-05
Epoch 220/500
124/124 - 3s - 23ms/step - accuracy: 0.7764 - loss: 0.4462 - val_accuracy: 0.6652 - val_loss: 0.6924 - learning_rate: 3.1250e-05
Epoch 221/500
124/124 - 3s - 23ms/step - accuracy: 0.7807 - loss: 0.4484 - val_accuracy: 0.6695 - val_loss: 0.6913 - learning_rate: 3.1250e-05
Epoch 222/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4421 - val_accuracy: 0.6710 - val_loss: 0.6936 - learning_rate: 3.1250e-05
Epoch 223/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4457 - val_accuracy: 0.6724 - val_loss: 0.6950 - learning_rate: 3.1250e-05
Epoch 224/500
124/124 - 3s - 23ms/step - accuracy: 0.7827 - loss: 0.4457 - val_accuracy: 0.6739 - val_loss: 0.6952 - learning_rate: 3.1250e-05
Epoch 225/500
124/124 - 3s - 23ms/step - accuracy: 0.7830 - loss: 0.4473 - val_accuracy: 0.6695 - val_loss: 0.6972 - learning_rate: 3.1250e-05
Epoch 226/500
124/124 - 3s - 23ms/step - accuracy: 0.7789 - loss: 0.4413 - val_accuracy: 0.6710 - val_loss: 0.6967 - learning_rate: 3.1250e-05
Epoch 227/500
124/124 - 3s - 23ms/step - accuracy: 0.7741 - loss: 0.4528 - val_accuracy: 0.6695 - val_loss: 0.6930 - learning_rate: 3.1250e-05
Epoch 228/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4478 - val_accuracy: 0.6739 - val_loss: 0.6927 - learning_rate: 3.1250e-05
Epoch 229/500
124/124 - 3s - 23ms/step - accuracy: 0.7797 - loss: 0.4410 - val_accuracy: 0.6710 - val_loss: 0.6929 - learning_rate: 3.1250e-05
Epoch 230/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4496 - val_accuracy: 0.6710 - val_loss: 0.6906 - learning_rate: 3.1250e-05
Epoch 231/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4451 - val_accuracy: 0.6739 - val_loss: 0.6897 - learning_rate: 3.1250e-05
Epoch 232/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4541 - val_accuracy: 0.6695 - val_loss: 0.6929 - learning_rate: 3.1250e-05
Epoch 233/500
124/124 - 3s - 23ms/step - accuracy: 0.7751 - loss: 0.4526 - val_accuracy: 0.6753 - val_loss: 0.6896 - learning_rate: 3.1250e-05
Epoch 234/500
124/124 - 3s - 23ms/step - accuracy: 0.7789 - loss: 0.4449 - val_accuracy: 0.6753 - val_loss: 0.6928 - learning_rate: 3.1250e-05
Epoch 235/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4510 - val_accuracy: 0.6739 - val_loss: 0.6901 - learning_rate: 3.1250e-05
Epoch 236/500
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4469 - val_accuracy: 0.6724 - val_loss: 0.6937 - learning_rate: 3.1250e-05
Epoch 237/500

Epoch 237: ReduceLROnPlateau reducing learning rate to 1.5625000742147677e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7812 - loss: 0.4396 - val_accuracy: 0.6681 - val_loss: 0.6926 - learning_rate: 3.1250e-05
Epoch 238/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4461 - val_accuracy: 0.6710 - val_loss: 0.6882 - learning_rate: 1.5625e-05
Epoch 239/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4479 - val_accuracy: 0.6710 - val_loss: 0.6885 - learning_rate: 1.5625e-05
Epoch 240/500
124/124 - 3s - 23ms/step - accuracy: 0.7797 - loss: 0.4427 - val_accuracy: 0.6710 - val_loss: 0.6866 - learning_rate: 1.5625e-05
Epoch 241/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4476 - val_accuracy: 0.6710 - val_loss: 0.6854 - learning_rate: 1.5625e-05
Epoch 242/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4503 - val_accuracy: 0.6695 - val_loss: 0.6851 - learning_rate: 1.5625e-05
Epoch 243/500
124/124 - 3s - 23ms/step - accuracy: 0.7751 - loss: 0.4518 - val_accuracy: 0.6695 - val_loss: 0.6845 - learning_rate: 1.5625e-05
Epoch 244/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4426 - val_accuracy: 0.6739 - val_loss: 0.6843 - learning_rate: 1.5625e-05
Epoch 245/500
124/124 - 3s - 23ms/step - accuracy: 0.7837 - loss: 0.4411 - val_accuracy: 0.6739 - val_loss: 0.6853 - learning_rate: 1.5625e-05
Epoch 246/500
124/124 - 3s - 23ms/step - accuracy: 0.7825 - loss: 0.4398 - val_accuracy: 0.6739 - val_loss: 0.6852 - learning_rate: 1.5625e-05
Epoch 247/500
124/124 - 3s - 23ms/step - accuracy: 0.7817 - loss: 0.4391 - val_accuracy: 0.6724 - val_loss: 0.6844 - learning_rate: 1.5625e-05
Epoch 248/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4481 - val_accuracy: 0.6710 - val_loss: 0.6856 - learning_rate: 1.5625e-05
Epoch 249/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4532 - val_accuracy: 0.6695 - val_loss: 0.6885 - learning_rate: 1.5625e-05
Epoch 250/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4507 - val_accuracy: 0.6695 - val_loss: 0.6898 - learning_rate: 1.5625e-05
Epoch 251/500
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4453 - val_accuracy: 0.6710 - val_loss: 0.6860 - learning_rate: 1.5625e-05
Epoch 252/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4479 - val_accuracy: 0.6710 - val_loss: 0.6869 - learning_rate: 1.5625e-05
Epoch 253/500
124/124 - 3s - 23ms/step - accuracy: 0.7797 - loss: 0.4410 - val_accuracy: 0.6753 - val_loss: 0.6868 - learning_rate: 1.5625e-05
Epoch 254/500
124/124 - 3s - 23ms/step - accuracy: 0.7756 - loss: 0.4517 - val_accuracy: 0.6695 - val_loss: 0.6880 - learning_rate: 1.5625e-05
Epoch 255/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4463 - val_accuracy: 0.6710 - val_loss: 0.6891 - learning_rate: 1.5625e-05
Epoch 256/500
124/124 - 3s - 23ms/step - accuracy: 0.7764 - loss: 0.4499 - val_accuracy: 0.6710 - val_loss: 0.6880 - learning_rate: 1.5625e-05
Epoch 257/500
124/124 - 3s - 24ms/step - accuracy: 0.7764 - loss: 0.4480 - val_accuracy: 0.6695 - val_loss: 0.6894 - learning_rate: 1.5625e-05
Epoch 258/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4463 - val_accuracy: 0.6724 - val_loss: 0.6886 - learning_rate: 1.5625e-05
Epoch 259/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4503 - val_accuracy: 0.6724 - val_loss: 0.6886 - learning_rate: 1.5625e-05
Epoch 260/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4478 - val_accuracy: 0.6710 - val_loss: 0.6891 - learning_rate: 1.5625e-05
Epoch 261/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4444 - val_accuracy: 0.6724 - val_loss: 0.6860 - learning_rate: 1.5625e-05
Epoch 262/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4531 - val_accuracy: 0.6767 - val_loss: 0.6889 - learning_rate: 1.5625e-05
Epoch 263/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4433 - val_accuracy: 0.6724 - val_loss: 0.6871 - learning_rate: 1.5625e-05
Epoch 264/500

Epoch 264: ReduceLROnPlateau reducing learning rate to 7.812500371073838e-06.
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4539 - val_accuracy: 0.6695 - val_loss: 0.6858 - learning_rate: 1.5625e-05
Epoch 265/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4443 - val_accuracy: 0.6724 - val_loss: 0.6852 - learning_rate: 7.8125e-06
Epoch 266/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4452 - val_accuracy: 0.6710 - val_loss: 0.6856 - learning_rate: 7.8125e-06
Epoch 267/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4474 - val_accuracy: 0.6710 - val_loss: 0.6863 - learning_rate: 7.8125e-06
Epoch 268/500
124/124 - 3s - 23ms/step - accuracy: 0.7822 - loss: 0.4369 - val_accuracy: 0.6710 - val_loss: 0.6846 - learning_rate: 7.8125e-06
Epoch 269/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4416 - val_accuracy: 0.6724 - val_loss: 0.6846 - learning_rate: 7.8125e-06
Epoch 270/500
124/124 - 3s - 23ms/step - accuracy: 0.7799 - loss: 0.4467 - val_accuracy: 0.6739 - val_loss: 0.6846 - learning_rate: 7.8125e-06
Epoch 271/500
124/124 - 3s - 23ms/step - accuracy: 0.7764 - loss: 0.4457 - val_accuracy: 0.6724 - val_loss: 0.6851 - learning_rate: 7.8125e-06
Epoch 272/500
124/124 - 3s - 24ms/step - accuracy: 0.7754 - loss: 0.4456 - val_accuracy: 0.6724 - val_loss: 0.6838 - learning_rate: 7.8125e-06
Epoch 273/500
124/124 - 3s - 24ms/step - accuracy: 0.7794 - loss: 0.4414 - val_accuracy: 0.6710 - val_loss: 0.6835 - learning_rate: 7.8125e-06
Epoch 274/500
124/124 - 3s - 23ms/step - accuracy: 0.7787 - loss: 0.4469 - val_accuracy: 0.6724 - val_loss: 0.6847 - learning_rate: 7.8125e-06
Epoch 275/500
124/124 - 3s - 23ms/step - accuracy: 0.7792 - loss: 0.4452 - val_accuracy: 0.6681 - val_loss: 0.6848 - learning_rate: 7.8125e-06
Epoch 276/500
124/124 - 3s - 23ms/step - accuracy: 0.7756 - loss: 0.4443 - val_accuracy: 0.6681 - val_loss: 0.6852 - learning_rate: 7.8125e-06
Epoch 277/500
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4441 - val_accuracy: 0.6667 - val_loss: 0.6870 - learning_rate: 7.8125e-06
Epoch 278/500
124/124 - 3s - 23ms/step - accuracy: 0.7764 - loss: 0.4424 - val_accuracy: 0.6710 - val_loss: 0.6858 - learning_rate: 7.8125e-06
Epoch 279/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4470 - val_accuracy: 0.6724 - val_loss: 0.6859 - learning_rate: 7.8125e-06
Epoch 280/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4509 - val_accuracy: 0.6724 - val_loss: 0.6865 - learning_rate: 7.8125e-06
Epoch 281/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4452 - val_accuracy: 0.6710 - val_loss: 0.6843 - learning_rate: 7.8125e-06
Epoch 282/500
124/124 - 3s - 23ms/step - accuracy: 0.7792 - loss: 0.4419 - val_accuracy: 0.6739 - val_loss: 0.6861 - learning_rate: 7.8125e-06
Epoch 283/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4411 - val_accuracy: 0.6724 - val_loss: 0.6869 - learning_rate: 7.8125e-06
Epoch 284/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4517 - val_accuracy: 0.6739 - val_loss: 0.6876 - learning_rate: 7.8125e-06
Epoch 285/500
124/124 - 3s - 23ms/step - accuracy: 0.7787 - loss: 0.4416 - val_accuracy: 0.6724 - val_loss: 0.6882 - learning_rate: 7.8125e-06
Epoch 286/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4439 - val_accuracy: 0.6739 - val_loss: 0.6878 - learning_rate: 7.8125e-06
Epoch 287/500
124/124 - 3s - 23ms/step - accuracy: 0.7827 - loss: 0.4415 - val_accuracy: 0.6753 - val_loss: 0.6881 - learning_rate: 7.8125e-06
Epoch 288/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4487 - val_accuracy: 0.6739 - val_loss: 0.6875 - learning_rate: 7.8125e-06
Epoch 289/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4470 - val_accuracy: 0.6739 - val_loss: 0.6867 - learning_rate: 7.8125e-06
Epoch 290/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4437 - val_accuracy: 0.6724 - val_loss: 0.6869 - learning_rate: 7.8125e-06
Epoch 291/500
124/124 - 3s - 23ms/step - accuracy: 0.7865 - loss: 0.4462 - val_accuracy: 0.6739 - val_loss: 0.6871 - learning_rate: 7.8125e-06
Epoch 292/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4471 - val_accuracy: 0.6753 - val_loss: 0.6865 - learning_rate: 7.8125e-06
Epoch 293/500

Epoch 293: ReduceLROnPlateau reducing learning rate to 3.906250185536919e-06.
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4482 - val_accuracy: 0.6767 - val_loss: 0.6859 - learning_rate: 7.8125e-06
Epoch 294/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4429 - val_accuracy: 0.6753 - val_loss: 0.6854 - learning_rate: 3.9063e-06
Epoch 295/500
124/124 - 3s - 23ms/step - accuracy: 0.7865 - loss: 0.4372 - val_accuracy: 0.6739 - val_loss: 0.6857 - learning_rate: 3.9063e-06
Epoch 296/500
124/124 - 3s - 23ms/step - accuracy: 0.7741 - loss: 0.4459 - val_accuracy: 0.6739 - val_loss: 0.6850 - learning_rate: 3.9063e-06
Epoch 297/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4469 - val_accuracy: 0.6724 - val_loss: 0.6853 - learning_rate: 3.9063e-06
Epoch 298/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4478 - val_accuracy: 0.6724 - val_loss: 0.6848 - learning_rate: 3.9063e-06
Epoch 299/500
124/124 - 3s - 23ms/step - accuracy: 0.7799 - loss: 0.4437 - val_accuracy: 0.6739 - val_loss: 0.6843 - learning_rate: 3.9063e-06
Epoch 300/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4520 - val_accuracy: 0.6739 - val_loss: 0.6852 - learning_rate: 3.9063e-06
Epoch 301/500
124/124 - 3s - 23ms/step - accuracy: 0.7766 - loss: 0.4459 - val_accuracy: 0.6724 - val_loss: 0.6861 - learning_rate: 3.9063e-06
Epoch 302/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4429 - val_accuracy: 0.6710 - val_loss: 0.6860 - learning_rate: 3.9063e-06
Epoch 303/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4515 - val_accuracy: 0.6724 - val_loss: 0.6851 - learning_rate: 3.9063e-06
Epoch 304/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4458 - val_accuracy: 0.6724 - val_loss: 0.6850 - learning_rate: 3.9063e-06
Epoch 305/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4493 - val_accuracy: 0.6724 - val_loss: 0.6848 - learning_rate: 3.9063e-06
Epoch 306/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4399 - val_accuracy: 0.6739 - val_loss: 0.6839 - learning_rate: 3.9063e-06
Epoch 307/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4474 - val_accuracy: 0.6724 - val_loss: 0.6847 - learning_rate: 3.9063e-06
Epoch 308/500
124/124 - 3s - 23ms/step - accuracy: 0.7802 - loss: 0.4398 - val_accuracy: 0.6724 - val_loss: 0.6839 - learning_rate: 3.9063e-06
Epoch 309/500
124/124 - 3s - 23ms/step - accuracy: 0.7850 - loss: 0.4378 - val_accuracy: 0.6724 - val_loss: 0.6846 - learning_rate: 3.9063e-06
Epoch 310/500
124/124 - 3s - 23ms/step - accuracy: 0.7817 - loss: 0.4414 - val_accuracy: 0.6724 - val_loss: 0.6854 - learning_rate: 3.9063e-06
Epoch 311/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4474 - val_accuracy: 0.6724 - val_loss: 0.6850 - learning_rate: 3.9063e-06
Epoch 312/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4415 - val_accuracy: 0.6724 - val_loss: 0.6847 - learning_rate: 3.9063e-06
Epoch 313/500

Epoch 313: ReduceLROnPlateau reducing learning rate to 1.9531250927684596e-06.
124/124 - 3s - 23ms/step - accuracy: 0.7784 - loss: 0.4458 - val_accuracy: 0.6739 - val_loss: 0.6842 - learning_rate: 3.9063e-06
Epoch 314/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4516 - val_accuracy: 0.6739 - val_loss: 0.6841 - learning_rate: 1.9531e-06
Epoch 315/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4425 - val_accuracy: 0.6739 - val_loss: 0.6838 - learning_rate: 1.9531e-06
Epoch 316/500
124/124 - 3s - 23ms/step - accuracy: 0.7708 - loss: 0.4498 - val_accuracy: 0.6739 - val_loss: 0.6846 - learning_rate: 1.9531e-06
Epoch 317/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4404 - val_accuracy: 0.6753 - val_loss: 0.6847 - learning_rate: 1.9531e-06
Epoch 318/500
124/124 - 3s - 23ms/step - accuracy: 0.7840 - loss: 0.4399 - val_accuracy: 0.6753 - val_loss: 0.6846 - learning_rate: 1.9531e-06
Epoch 319/500
124/124 - 3s - 23ms/step - accuracy: 0.7842 - loss: 0.4418 - val_accuracy: 0.6739 - val_loss: 0.6846 - learning_rate: 1.9531e-06
Epoch 320/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4400 - val_accuracy: 0.6739 - val_loss: 0.6843 - learning_rate: 1.9531e-06
Epoch 321/500
124/124 - 3s - 23ms/step - accuracy: 0.7837 - loss: 0.4357 - val_accuracy: 0.6753 - val_loss: 0.6842 - learning_rate: 1.9531e-06
Epoch 322/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4410 - val_accuracy: 0.6753 - val_loss: 0.6841 - learning_rate: 1.9531e-06
Epoch 323/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4419 - val_accuracy: 0.6753 - val_loss: 0.6835 - learning_rate: 1.9531e-06
Epoch 323: early stopping
Restoring model weights from the end of the best epoch: 273.
Training complete. Best epoch: 273 of 323. Best val_loss: 0.6835, val_accuracy: 0.6710

========== Evaluation: LOSO fold 18 / held-out EMS0019 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        33         7         0
  intermedia        37        40         3
  max_intens        13        20         7

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.398     0.825     0.537        40
intermediate_intensity      0.597     0.500     0.544        80
         max_intensity      0.700     0.175     0.280        40

              accuracy                          0.500       160
             macro avg      0.565     0.500     0.454       160
          weighted avg      0.573     0.500     0.476       160

Overall accuracy: 0.5000

============================================================
Fold 19 of 30: holding out EMS0020
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-3.52e-07, 1.01e-06]
  Per-channel std range:  [7.01e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4470 - loss: 1.0201 - val_accuracy: 0.4655 - val_loss: 1.0431 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5228 - loss: 0.9065 - val_accuracy: 0.5345 - val_loss: 0.9533 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5662 - loss: 0.8486 - val_accuracy: 0.5460 - val_loss: 0.8987 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5865 - loss: 0.8151 - val_accuracy: 0.5546 - val_loss: 0.8759 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5910 - loss: 0.7886 - val_accuracy: 0.5690 - val_loss: 0.8532 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5979 - loss: 0.7724 - val_accuracy: 0.5733 - val_loss: 0.8319 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6037 - loss: 0.7594 - val_accuracy: 0.5991 - val_loss: 0.8072 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6146 - loss: 0.7456 - val_accuracy: 0.5876 - val_loss: 0.7994 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6245 - loss: 0.7288 - val_accuracy: 0.5977 - val_loss: 0.8046 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6227 - loss: 0.7263 - val_accuracy: 0.5991 - val_loss: 0.7893 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6275 - loss: 0.7185 - val_accuracy: 0.6078 - val_loss: 0.7886 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6339 - loss: 0.7126 - val_accuracy: 0.5819 - val_loss: 0.7968 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6240 - loss: 0.7027 - val_accuracy: 0.6006 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6329 - loss: 0.6952 - val_accuracy: 0.6063 - val_loss: 0.7912 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6359 - loss: 0.6940 - val_accuracy: 0.5977 - val_loss: 0.7879 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6392 - loss: 0.6894 - val_accuracy: 0.5991 - val_loss: 0.7971 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6473 - loss: 0.6835 - val_accuracy: 0.5805 - val_loss: 0.8028 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6438 - loss: 0.6779 - val_accuracy: 0.6063 - val_loss: 0.7884 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6493 - loss: 0.6810 - val_accuracy: 0.6135 - val_loss: 0.7876 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6519 - loss: 0.6710 - val_accuracy: 0.6178 - val_loss: 0.7885 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6580 - loss: 0.6683 - val_accuracy: 0.5991 - val_loss: 0.8020 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6539 - loss: 0.6599 - val_accuracy: 0.5991 - val_loss: 0.7789 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6628 - val_accuracy: 0.6135 - val_loss: 0.7797 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6575 - loss: 0.6617 - val_accuracy: 0.6063 - val_loss: 0.7839 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6597 - loss: 0.6574 - val_accuracy: 0.6020 - val_loss: 0.7909 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6638 - loss: 0.6514 - val_accuracy: 0.6322 - val_loss: 0.7633 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6689 - loss: 0.6476 - val_accuracy: 0.6006 - val_loss: 0.7965 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6605 - loss: 0.6479 - val_accuracy: 0.6279 - val_loss: 0.7715 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6658 - loss: 0.6421 - val_accuracy: 0.6164 - val_loss: 0.7798 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6600 - loss: 0.6500 - val_accuracy: 0.6106 - val_loss: 0.7766 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6694 - loss: 0.6411 - val_accuracy: 0.6279 - val_loss: 0.7666 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6717 - loss: 0.6336 - val_accuracy: 0.6322 - val_loss: 0.7576 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6732 - loss: 0.6333 - val_accuracy: 0.6193 - val_loss: 0.7597 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6775 - loss: 0.6333 - val_accuracy: 0.6092 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6760 - loss: 0.6282 - val_accuracy: 0.6264 - val_loss: 0.7685 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6747 - loss: 0.6241 - val_accuracy: 0.6063 - val_loss: 0.8022 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6323 - val_accuracy: 0.6351 - val_loss: 0.7558 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6762 - loss: 0.6238 - val_accuracy: 0.5905 - val_loss: 0.8188 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6841 - loss: 0.6196 - val_accuracy: 0.6193 - val_loss: 0.7698 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.6243 - val_accuracy: 0.6121 - val_loss: 0.8014 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6859 - loss: 0.6225 - val_accuracy: 0.6092 - val_loss: 0.7760 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6836 - loss: 0.6066 - val_accuracy: 0.5977 - val_loss: 0.7832 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.6233 - val_accuracy: 0.6164 - val_loss: 0.7931 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6800 - loss: 0.6162 - val_accuracy: 0.6149 - val_loss: 0.7822 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.6093 - val_accuracy: 0.6135 - val_loss: 0.8088 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6092 - val_accuracy: 0.6236 - val_loss: 0.7767 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.6078 - val_accuracy: 0.6336 - val_loss: 0.7665 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.6028 - val_accuracy: 0.5934 - val_loss: 0.8059 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.6064 - val_accuracy: 0.6307 - val_loss: 0.7953 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6843 - loss: 0.6082 - val_accuracy: 0.6121 - val_loss: 0.7649 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.6024 - val_accuracy: 0.6178 - val_loss: 0.7739 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5948 - val_accuracy: 0.6250 - val_loss: 0.7731 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6917 - loss: 0.6081 - val_accuracy: 0.6207 - val_loss: 0.7720 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7011 - loss: 0.5972 - val_accuracy: 0.6236 - val_loss: 0.7686 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6937 - loss: 0.5976 - val_accuracy: 0.6149 - val_loss: 0.7683 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5957 - val_accuracy: 0.6106 - val_loss: 0.7895 - learning_rate: 0.0010
Epoch 57/500

Epoch 57: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.6917 - loss: 0.5971 - val_accuracy: 0.6164 - val_loss: 0.7872 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5686 - val_accuracy: 0.6466 - val_loss: 0.7409 - learning_rate: 5.0000e-04
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5575 - val_accuracy: 0.6178 - val_loss: 0.7665 - learning_rate: 5.0000e-04
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7307 - loss: 0.5488 - val_accuracy: 0.6336 - val_loss: 0.7450 - learning_rate: 5.0000e-04
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7163 - loss: 0.5606 - val_accuracy: 0.6307 - val_loss: 0.7575 - learning_rate: 5.0000e-04
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7239 - loss: 0.5497 - val_accuracy: 0.6379 - val_loss: 0.7438 - learning_rate: 5.0000e-04
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5570 - val_accuracy: 0.6394 - val_loss: 0.7524 - learning_rate: 5.0000e-04
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7193 - loss: 0.5550 - val_accuracy: 0.6336 - val_loss: 0.7719 - learning_rate: 5.0000e-04
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5535 - val_accuracy: 0.6236 - val_loss: 0.7592 - learning_rate: 5.0000e-04
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7186 - loss: 0.5490 - val_accuracy: 0.6379 - val_loss: 0.7608 - learning_rate: 5.0000e-04
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7170 - loss: 0.5468 - val_accuracy: 0.6365 - val_loss: 0.7466 - learning_rate: 5.0000e-04
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5507 - val_accuracy: 0.6178 - val_loss: 0.7575 - learning_rate: 5.0000e-04
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5523 - val_accuracy: 0.6293 - val_loss: 0.7582 - learning_rate: 5.0000e-04
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5475 - val_accuracy: 0.6264 - val_loss: 0.7641 - learning_rate: 5.0000e-04
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7216 - loss: 0.5445 - val_accuracy: 0.6437 - val_loss: 0.7470 - learning_rate: 5.0000e-04
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5429 - val_accuracy: 0.6293 - val_loss: 0.7690 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7196 - loss: 0.5495 - val_accuracy: 0.6322 - val_loss: 0.7678 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5483 - val_accuracy: 0.6307 - val_loss: 0.7693 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7279 - loss: 0.5374 - val_accuracy: 0.6264 - val_loss: 0.7650 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5370 - val_accuracy: 0.6365 - val_loss: 0.7628 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7257 - loss: 0.5418 - val_accuracy: 0.6379 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 78/500

Epoch 78: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7290 - loss: 0.5417 - val_accuracy: 0.6307 - val_loss: 0.7580 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7350 - loss: 0.5259 - val_accuracy: 0.6250 - val_loss: 0.7745 - learning_rate: 2.5000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7350 - loss: 0.5255 - val_accuracy: 0.6307 - val_loss: 0.7713 - learning_rate: 2.5000e-04
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7388 - loss: 0.5236 - val_accuracy: 0.6293 - val_loss: 0.7709 - learning_rate: 2.5000e-04
Epoch 82/500
124/124 - 3s - 24ms/step - accuracy: 0.7457 - loss: 0.5187 - val_accuracy: 0.6336 - val_loss: 0.7788 - learning_rate: 2.5000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5208 - val_accuracy: 0.6466 - val_loss: 0.7535 - learning_rate: 2.5000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7401 - loss: 0.5146 - val_accuracy: 0.6365 - val_loss: 0.7611 - learning_rate: 2.5000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7505 - loss: 0.5102 - val_accuracy: 0.6322 - val_loss: 0.7784 - learning_rate: 2.5000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7513 - loss: 0.5136 - val_accuracy: 0.6408 - val_loss: 0.7651 - learning_rate: 2.5000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7447 - loss: 0.5125 - val_accuracy: 0.6509 - val_loss: 0.7583 - learning_rate: 2.5000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7472 - loss: 0.5113 - val_accuracy: 0.6178 - val_loss: 0.7923 - learning_rate: 2.5000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7419 - loss: 0.5120 - val_accuracy: 0.6394 - val_loss: 0.7629 - learning_rate: 2.5000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7409 - loss: 0.5175 - val_accuracy: 0.6293 - val_loss: 0.7685 - learning_rate: 2.5000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7500 - loss: 0.5084 - val_accuracy: 0.6422 - val_loss: 0.7632 - learning_rate: 2.5000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.5076 - val_accuracy: 0.6480 - val_loss: 0.7608 - learning_rate: 2.5000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7426 - loss: 0.5112 - val_accuracy: 0.6351 - val_loss: 0.7736 - learning_rate: 2.5000e-04
Epoch 94/500
124/124 - 3s - 24ms/step - accuracy: 0.7475 - loss: 0.5109 - val_accuracy: 0.6379 - val_loss: 0.7802 - learning_rate: 2.5000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7411 - loss: 0.5122 - val_accuracy: 0.6422 - val_loss: 0.7734 - learning_rate: 2.5000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7437 - loss: 0.5123 - val_accuracy: 0.6451 - val_loss: 0.7630 - learning_rate: 2.5000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7541 - loss: 0.4973 - val_accuracy: 0.6494 - val_loss: 0.7604 - learning_rate: 2.5000e-04
Epoch 98/500

Epoch 98: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7520 - loss: 0.5043 - val_accuracy: 0.6422 - val_loss: 0.7783 - learning_rate: 2.5000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7515 - loss: 0.4969 - val_accuracy: 0.6566 - val_loss: 0.7404 - learning_rate: 1.2500e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7548 - loss: 0.4876 - val_accuracy: 0.6494 - val_loss: 0.7438 - learning_rate: 1.2500e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7571 - loss: 0.4965 - val_accuracy: 0.6480 - val_loss: 0.7340 - learning_rate: 1.2500e-04
Epoch 102/500
124/124 - 3s - 24ms/step - accuracy: 0.7535 - loss: 0.5023 - val_accuracy: 0.6494 - val_loss: 0.7497 - learning_rate: 1.2500e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7546 - loss: 0.4957 - val_accuracy: 0.6509 - val_loss: 0.7411 - learning_rate: 1.2500e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7586 - loss: 0.4962 - val_accuracy: 0.6451 - val_loss: 0.7538 - learning_rate: 1.2500e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.4915 - val_accuracy: 0.6509 - val_loss: 0.7509 - learning_rate: 1.2500e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7576 - loss: 0.4905 - val_accuracy: 0.6480 - val_loss: 0.7441 - learning_rate: 1.2500e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7533 - loss: 0.5056 - val_accuracy: 0.6394 - val_loss: 0.7520 - learning_rate: 1.2500e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7561 - loss: 0.4890 - val_accuracy: 0.6480 - val_loss: 0.7442 - learning_rate: 1.2500e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.4932 - val_accuracy: 0.6394 - val_loss: 0.7506 - learning_rate: 1.2500e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7571 - loss: 0.4903 - val_accuracy: 0.6408 - val_loss: 0.7519 - learning_rate: 1.2500e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7579 - loss: 0.4922 - val_accuracy: 0.6494 - val_loss: 0.7472 - learning_rate: 1.2500e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4987 - val_accuracy: 0.6451 - val_loss: 0.7463 - learning_rate: 1.2500e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7556 - loss: 0.4905 - val_accuracy: 0.6667 - val_loss: 0.7525 - learning_rate: 1.2500e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4852 - val_accuracy: 0.6552 - val_loss: 0.7482 - learning_rate: 1.2500e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7541 - loss: 0.4933 - val_accuracy: 0.6451 - val_loss: 0.7534 - learning_rate: 1.2500e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7452 - loss: 0.5007 - val_accuracy: 0.6451 - val_loss: 0.7485 - learning_rate: 1.2500e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7505 - loss: 0.4942 - val_accuracy: 0.6609 - val_loss: 0.7396 - learning_rate: 1.2500e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7632 - loss: 0.4923 - val_accuracy: 0.6466 - val_loss: 0.7462 - learning_rate: 1.2500e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4933 - val_accuracy: 0.6480 - val_loss: 0.7555 - learning_rate: 1.2500e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4866 - val_accuracy: 0.6509 - val_loss: 0.7505 - learning_rate: 1.2500e-04
Epoch 121/500

Epoch 121: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4916 - val_accuracy: 0.6408 - val_loss: 0.7501 - learning_rate: 1.2500e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4833 - val_accuracy: 0.6609 - val_loss: 0.7434 - learning_rate: 6.2500e-05
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4898 - val_accuracy: 0.6537 - val_loss: 0.7471 - learning_rate: 6.2500e-05
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4859 - val_accuracy: 0.6595 - val_loss: 0.7415 - learning_rate: 6.2500e-05
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7642 - loss: 0.4833 - val_accuracy: 0.6537 - val_loss: 0.7511 - learning_rate: 6.2500e-05
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4839 - val_accuracy: 0.6509 - val_loss: 0.7476 - learning_rate: 6.2500e-05
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.4885 - val_accuracy: 0.6523 - val_loss: 0.7434 - learning_rate: 6.2500e-05
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4851 - val_accuracy: 0.6566 - val_loss: 0.7376 - learning_rate: 6.2500e-05
Epoch 129/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4839 - val_accuracy: 0.6494 - val_loss: 0.7426 - learning_rate: 6.2500e-05
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.4836 - val_accuracy: 0.6480 - val_loss: 0.7440 - learning_rate: 6.2500e-05
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4847 - val_accuracy: 0.6537 - val_loss: 0.7403 - learning_rate: 6.2500e-05
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7561 - loss: 0.4880 - val_accuracy: 0.6566 - val_loss: 0.7431 - learning_rate: 6.2500e-05
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7551 - loss: 0.4852 - val_accuracy: 0.6566 - val_loss: 0.7410 - learning_rate: 6.2500e-05
Epoch 134/500
124/124 - 3s - 24ms/step - accuracy: 0.7650 - loss: 0.4817 - val_accuracy: 0.6509 - val_loss: 0.7473 - learning_rate: 6.2500e-05
Epoch 135/500
124/124 - 3s - 24ms/step - accuracy: 0.7571 - loss: 0.4846 - val_accuracy: 0.6537 - val_loss: 0.7481 - learning_rate: 6.2500e-05
Epoch 136/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4835 - val_accuracy: 0.6552 - val_loss: 0.7416 - learning_rate: 6.2500e-05
Epoch 137/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4850 - val_accuracy: 0.6595 - val_loss: 0.7465 - learning_rate: 6.2500e-05
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7530 - loss: 0.4915 - val_accuracy: 0.6523 - val_loss: 0.7437 - learning_rate: 6.2500e-05
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7624 - loss: 0.4802 - val_accuracy: 0.6537 - val_loss: 0.7464 - learning_rate: 6.2500e-05
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4789 - val_accuracy: 0.6552 - val_loss: 0.7383 - learning_rate: 6.2500e-05
Epoch 141/500

Epoch 141: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4847 - val_accuracy: 0.6523 - val_loss: 0.7453 - learning_rate: 6.2500e-05
Epoch 142/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4839 - val_accuracy: 0.6552 - val_loss: 0.7389 - learning_rate: 3.1250e-05
Epoch 143/500
124/124 - 3s - 24ms/step - accuracy: 0.7672 - loss: 0.4784 - val_accuracy: 0.6580 - val_loss: 0.7324 - learning_rate: 3.1250e-05
Epoch 144/500
124/124 - 3s - 24ms/step - accuracy: 0.7589 - loss: 0.4867 - val_accuracy: 0.6566 - val_loss: 0.7369 - learning_rate: 3.1250e-05
Epoch 145/500
124/124 - 3s - 24ms/step - accuracy: 0.7728 - loss: 0.4797 - val_accuracy: 0.6609 - val_loss: 0.7351 - learning_rate: 3.1250e-05
Epoch 146/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4791 - val_accuracy: 0.6480 - val_loss: 0.7383 - learning_rate: 3.1250e-05
Epoch 147/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4828 - val_accuracy: 0.6552 - val_loss: 0.7345 - learning_rate: 3.1250e-05
Epoch 148/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4754 - val_accuracy: 0.6494 - val_loss: 0.7347 - learning_rate: 3.1250e-05
Epoch 149/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4775 - val_accuracy: 0.6552 - val_loss: 0.7337 - learning_rate: 3.1250e-05
Epoch 150/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4833 - val_accuracy: 0.6509 - val_loss: 0.7329 - learning_rate: 3.1250e-05
Epoch 151/500
124/124 - 3s - 24ms/step - accuracy: 0.7685 - loss: 0.4748 - val_accuracy: 0.6523 - val_loss: 0.7379 - learning_rate: 3.1250e-05
Epoch 152/500
124/124 - 3s - 24ms/step - accuracy: 0.7627 - loss: 0.4752 - val_accuracy: 0.6552 - val_loss: 0.7346 - learning_rate: 3.1250e-05
Epoch 153/500
124/124 - 3s - 24ms/step - accuracy: 0.7563 - loss: 0.4873 - val_accuracy: 0.6494 - val_loss: 0.7326 - learning_rate: 3.1250e-05
Epoch 154/500
124/124 - 3s - 24ms/step - accuracy: 0.7733 - loss: 0.4746 - val_accuracy: 0.6537 - val_loss: 0.7346 - learning_rate: 3.1250e-05
Epoch 155/500
124/124 - 3s - 24ms/step - accuracy: 0.7662 - loss: 0.4792 - val_accuracy: 0.6566 - val_loss: 0.7321 - learning_rate: 3.1250e-05
Epoch 156/500
124/124 - 3s - 24ms/step - accuracy: 0.7708 - loss: 0.4797 - val_accuracy: 0.6494 - val_loss: 0.7357 - learning_rate: 3.1250e-05
Epoch 157/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4798 - val_accuracy: 0.6509 - val_loss: 0.7331 - learning_rate: 3.1250e-05
Epoch 158/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4816 - val_accuracy: 0.6537 - val_loss: 0.7346 - learning_rate: 3.1250e-05
Epoch 159/500
124/124 - 3s - 24ms/step - accuracy: 0.7586 - loss: 0.4829 - val_accuracy: 0.6537 - val_loss: 0.7324 - learning_rate: 3.1250e-05
Epoch 160/500
124/124 - 3s - 24ms/step - accuracy: 0.7647 - loss: 0.4780 - val_accuracy: 0.6552 - val_loss: 0.7289 - learning_rate: 3.1250e-05
Epoch 161/500
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4842 - val_accuracy: 0.6552 - val_loss: 0.7345 - learning_rate: 3.1250e-05
Epoch 162/500
124/124 - 3s - 24ms/step - accuracy: 0.7652 - loss: 0.4778 - val_accuracy: 0.6580 - val_loss: 0.7341 - learning_rate: 3.1250e-05
Epoch 163/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4759 - val_accuracy: 0.6523 - val_loss: 0.7300 - learning_rate: 3.1250e-05
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4805 - val_accuracy: 0.6509 - val_loss: 0.7318 - learning_rate: 3.1250e-05
Epoch 165/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4776 - val_accuracy: 0.6580 - val_loss: 0.7331 - learning_rate: 3.1250e-05
Epoch 166/500
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.4778 - val_accuracy: 0.6580 - val_loss: 0.7340 - learning_rate: 3.1250e-05
Epoch 167/500
124/124 - 3s - 24ms/step - accuracy: 0.7672 - loss: 0.4778 - val_accuracy: 0.6580 - val_loss: 0.7316 - learning_rate: 3.1250e-05
Epoch 168/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4764 - val_accuracy: 0.6595 - val_loss: 0.7340 - learning_rate: 3.1250e-05
Epoch 169/500
124/124 - 3s - 23ms/step - accuracy: 0.7594 - loss: 0.4814 - val_accuracy: 0.6566 - val_loss: 0.7322 - learning_rate: 3.1250e-05
Epoch 170/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4758 - val_accuracy: 0.6509 - val_loss: 0.7333 - learning_rate: 3.1250e-05
Epoch 171/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4822 - val_accuracy: 0.6509 - val_loss: 0.7362 - learning_rate: 3.1250e-05
Epoch 172/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4745 - val_accuracy: 0.6566 - val_loss: 0.7353 - learning_rate: 3.1250e-05
Epoch 173/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4694 - val_accuracy: 0.6537 - val_loss: 0.7276 - learning_rate: 3.1250e-05
Epoch 174/500
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4811 - val_accuracy: 0.6552 - val_loss: 0.7358 - learning_rate: 3.1250e-05
Epoch 175/500
124/124 - 3s - 24ms/step - accuracy: 0.7606 - loss: 0.4834 - val_accuracy: 0.6523 - val_loss: 0.7327 - learning_rate: 3.1250e-05
Epoch 176/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4805 - val_accuracy: 0.6537 - val_loss: 0.7291 - learning_rate: 3.1250e-05
Epoch 177/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4817 - val_accuracy: 0.6509 - val_loss: 0.7307 - learning_rate: 3.1250e-05
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4791 - val_accuracy: 0.6523 - val_loss: 0.7312 - learning_rate: 3.1250e-05
Epoch 179/500
124/124 - 3s - 24ms/step - accuracy: 0.7617 - loss: 0.4771 - val_accuracy: 0.6595 - val_loss: 0.7313 - learning_rate: 3.1250e-05
Epoch 180/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4779 - val_accuracy: 0.6580 - val_loss: 0.7338 - learning_rate: 3.1250e-05
Epoch 181/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4787 - val_accuracy: 0.6509 - val_loss: 0.7346 - learning_rate: 3.1250e-05
Epoch 182/500
124/124 - 3s - 24ms/step - accuracy: 0.7728 - loss: 0.4680 - val_accuracy: 0.6523 - val_loss: 0.7301 - learning_rate: 3.1250e-05
Epoch 183/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4765 - val_accuracy: 0.6537 - val_loss: 0.7315 - learning_rate: 3.1250e-05
Epoch 184/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4787 - val_accuracy: 0.6537 - val_loss: 0.7364 - learning_rate: 3.1250e-05
Epoch 185/500
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.4820 - val_accuracy: 0.6566 - val_loss: 0.7321 - learning_rate: 3.1250e-05
Epoch 186/500
124/124 - 3s - 24ms/step - accuracy: 0.7685 - loss: 0.4780 - val_accuracy: 0.6552 - val_loss: 0.7342 - learning_rate: 3.1250e-05
Epoch 187/500
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4759 - val_accuracy: 0.6580 - val_loss: 0.7317 - learning_rate: 3.1250e-05
Epoch 188/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4758 - val_accuracy: 0.6523 - val_loss: 0.7360 - learning_rate: 3.1250e-05
Epoch 189/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4767 - val_accuracy: 0.6580 - val_loss: 0.7357 - learning_rate: 3.1250e-05
Epoch 190/500
124/124 - 3s - 24ms/step - accuracy: 0.7627 - loss: 0.4810 - val_accuracy: 0.6595 - val_loss: 0.7270 - learning_rate: 3.1250e-05
Epoch 191/500
124/124 - 3s - 24ms/step - accuracy: 0.7667 - loss: 0.4726 - val_accuracy: 0.6523 - val_loss: 0.7290 - learning_rate: 3.1250e-05
Epoch 192/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4767 - val_accuracy: 0.6552 - val_loss: 0.7301 - learning_rate: 3.1250e-05
Epoch 193/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4756 - val_accuracy: 0.6523 - val_loss: 0.7348 - learning_rate: 3.1250e-05
Epoch 194/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4808 - val_accuracy: 0.6566 - val_loss: 0.7293 - learning_rate: 3.1250e-05
Epoch 195/500
124/124 - 3s - 24ms/step - accuracy: 0.7670 - loss: 0.4796 - val_accuracy: 0.6566 - val_loss: 0.7341 - learning_rate: 3.1250e-05
Epoch 196/500
124/124 - 3s - 24ms/step - accuracy: 0.7662 - loss: 0.4800 - val_accuracy: 0.6609 - val_loss: 0.7312 - learning_rate: 3.1250e-05
Epoch 197/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4815 - val_accuracy: 0.6552 - val_loss: 0.7329 - learning_rate: 3.1250e-05
Epoch 198/500
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4751 - val_accuracy: 0.6566 - val_loss: 0.7315 - learning_rate: 3.1250e-05
Epoch 199/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4727 - val_accuracy: 0.6609 - val_loss: 0.7311 - learning_rate: 3.1250e-05
Epoch 200/500
124/124 - 3s - 23ms/step - accuracy: 0.7700 - loss: 0.4738 - val_accuracy: 0.6580 - val_loss: 0.7333 - learning_rate: 3.1250e-05
Epoch 201/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4788 - val_accuracy: 0.6566 - val_loss: 0.7386 - learning_rate: 3.1250e-05
Epoch 202/500
124/124 - 3s - 24ms/step - accuracy: 0.7561 - loss: 0.4822 - val_accuracy: 0.6595 - val_loss: 0.7327 - learning_rate: 3.1250e-05
Epoch 203/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4749 - val_accuracy: 0.6595 - val_loss: 0.7298 - learning_rate: 3.1250e-05
Epoch 204/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4820 - val_accuracy: 0.6566 - val_loss: 0.7323 - learning_rate: 3.1250e-05
Epoch 205/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4748 - val_accuracy: 0.6609 - val_loss: 0.7273 - learning_rate: 3.1250e-05
Epoch 206/500
124/124 - 3s - 23ms/step - accuracy: 0.7675 - loss: 0.4760 - val_accuracy: 0.6638 - val_loss: 0.7328 - learning_rate: 3.1250e-05
Epoch 207/500
124/124 - 3s - 23ms/step - accuracy: 0.7612 - loss: 0.4793 - val_accuracy: 0.6624 - val_loss: 0.7337 - learning_rate: 3.1250e-05
Epoch 208/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4778 - val_accuracy: 0.6624 - val_loss: 0.7324 - learning_rate: 3.1250e-05
Epoch 209/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4849 - val_accuracy: 0.6566 - val_loss: 0.7344 - learning_rate: 3.1250e-05
Epoch 210/500

Epoch 210: ReduceLROnPlateau reducing learning rate to 1.5625000742147677e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7703 - loss: 0.4797 - val_accuracy: 0.6523 - val_loss: 0.7327 - learning_rate: 3.1250e-05
Epoch 211/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4775 - val_accuracy: 0.6537 - val_loss: 0.7309 - learning_rate: 1.5625e-05
Epoch 212/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4738 - val_accuracy: 0.6609 - val_loss: 0.7272 - learning_rate: 1.5625e-05
Epoch 213/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4656 - val_accuracy: 0.6609 - val_loss: 0.7275 - learning_rate: 1.5625e-05
Epoch 214/500
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4746 - val_accuracy: 0.6580 - val_loss: 0.7298 - learning_rate: 1.5625e-05
Epoch 215/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4804 - val_accuracy: 0.6638 - val_loss: 0.7261 - learning_rate: 1.5625e-05
Epoch 216/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4788 - val_accuracy: 0.6609 - val_loss: 0.7280 - learning_rate: 1.5625e-05
Epoch 217/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4723 - val_accuracy: 0.6580 - val_loss: 0.7288 - learning_rate: 1.5625e-05
Epoch 218/500
124/124 - 3s - 23ms/step - accuracy: 0.7589 - loss: 0.4798 - val_accuracy: 0.6566 - val_loss: 0.7298 - learning_rate: 1.5625e-05
Epoch 219/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4714 - val_accuracy: 0.6609 - val_loss: 0.7270 - learning_rate: 1.5625e-05
Epoch 220/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4782 - val_accuracy: 0.6566 - val_loss: 0.7318 - learning_rate: 1.5625e-05
Epoch 221/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4776 - val_accuracy: 0.6624 - val_loss: 0.7277 - learning_rate: 1.5625e-05
Epoch 222/500
124/124 - 3s - 24ms/step - accuracy: 0.7754 - loss: 0.4710 - val_accuracy: 0.6580 - val_loss: 0.7275 - learning_rate: 1.5625e-05
Epoch 223/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4700 - val_accuracy: 0.6580 - val_loss: 0.7278 - learning_rate: 1.5625e-05
Epoch 224/500
124/124 - 3s - 24ms/step - accuracy: 0.7647 - loss: 0.4679 - val_accuracy: 0.6595 - val_loss: 0.7265 - learning_rate: 1.5625e-05
Epoch 225/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4750 - val_accuracy: 0.6566 - val_loss: 0.7285 - learning_rate: 1.5625e-05
Epoch 226/500
124/124 - 3s - 25ms/step - accuracy: 0.7761 - loss: 0.4629 - val_accuracy: 0.6609 - val_loss: 0.7257 - learning_rate: 1.5625e-05
Epoch 227/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4718 - val_accuracy: 0.6595 - val_loss: 0.7273 - learning_rate: 1.5625e-05
Epoch 228/500
124/124 - 3s - 24ms/step - accuracy: 0.7728 - loss: 0.4681 - val_accuracy: 0.6595 - val_loss: 0.7272 - learning_rate: 1.5625e-05
Epoch 229/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4741 - val_accuracy: 0.6580 - val_loss: 0.7297 - learning_rate: 1.5625e-05
Epoch 230/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4748 - val_accuracy: 0.6566 - val_loss: 0.7303 - learning_rate: 1.5625e-05
Epoch 231/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4716 - val_accuracy: 0.6552 - val_loss: 0.7301 - learning_rate: 1.5625e-05
Epoch 232/500
124/124 - 3s - 23ms/step - accuracy: 0.7667 - loss: 0.4781 - val_accuracy: 0.6580 - val_loss: 0.7275 - learning_rate: 1.5625e-05
Epoch 233/500
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4705 - val_accuracy: 0.6580 - val_loss: 0.7298 - learning_rate: 1.5625e-05
Epoch 234/500
124/124 - 3s - 24ms/step - accuracy: 0.7677 - loss: 0.4729 - val_accuracy: 0.6609 - val_loss: 0.7274 - learning_rate: 1.5625e-05
Epoch 235/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4693 - val_accuracy: 0.6609 - val_loss: 0.7272 - learning_rate: 1.5625e-05
Epoch 236/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4763 - val_accuracy: 0.6580 - val_loss: 0.7312 - learning_rate: 1.5625e-05
Epoch 237/500
124/124 - 3s - 24ms/step - accuracy: 0.7589 - loss: 0.4747 - val_accuracy: 0.6595 - val_loss: 0.7278 - learning_rate: 1.5625e-05
Epoch 238/500
124/124 - 3s - 24ms/step - accuracy: 0.7710 - loss: 0.4738 - val_accuracy: 0.6580 - val_loss: 0.7289 - learning_rate: 1.5625e-05
Epoch 239/500
124/124 - 3s - 24ms/step - accuracy: 0.7718 - loss: 0.4742 - val_accuracy: 0.6595 - val_loss: 0.7272 - learning_rate: 1.5625e-05
Epoch 240/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4728 - val_accuracy: 0.6609 - val_loss: 0.7276 - learning_rate: 1.5625e-05
Epoch 241/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4709 - val_accuracy: 0.6580 - val_loss: 0.7286 - learning_rate: 1.5625e-05
Epoch 242/500
124/124 - 3s - 23ms/step - accuracy: 0.7606 - loss: 0.4798 - val_accuracy: 0.6566 - val_loss: 0.7286 - learning_rate: 1.5625e-05
Epoch 243/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4776 - val_accuracy: 0.6595 - val_loss: 0.7290 - learning_rate: 1.5625e-05
Epoch 244/500
124/124 - 3s - 24ms/step - accuracy: 0.7688 - loss: 0.4702 - val_accuracy: 0.6580 - val_loss: 0.7280 - learning_rate: 1.5625e-05
Epoch 245/500
124/124 - 3s - 24ms/step - accuracy: 0.7642 - loss: 0.4791 - val_accuracy: 0.6609 - val_loss: 0.7272 - learning_rate: 1.5625e-05
Epoch 246/500

Epoch 246: ReduceLROnPlateau reducing learning rate to 7.812500371073838e-06.
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4727 - val_accuracy: 0.6624 - val_loss: 0.7264 - learning_rate: 1.5625e-05
Epoch 247/500
124/124 - 3s - 23ms/step - accuracy: 0.7680 - loss: 0.4764 - val_accuracy: 0.6609 - val_loss: 0.7284 - learning_rate: 7.8125e-06
Epoch 248/500
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4690 - val_accuracy: 0.6609 - val_loss: 0.7279 - learning_rate: 7.8125e-06
Epoch 249/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4790 - val_accuracy: 0.6595 - val_loss: 0.7278 - learning_rate: 7.8125e-06
Epoch 250/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4724 - val_accuracy: 0.6595 - val_loss: 0.7281 - learning_rate: 7.8125e-06
Epoch 251/500
124/124 - 3s - 24ms/step - accuracy: 0.7761 - loss: 0.4680 - val_accuracy: 0.6580 - val_loss: 0.7290 - learning_rate: 7.8125e-06
Epoch 252/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4685 - val_accuracy: 0.6624 - val_loss: 0.7278 - learning_rate: 7.8125e-06
Epoch 253/500
124/124 - 3s - 24ms/step - accuracy: 0.7698 - loss: 0.4762 - val_accuracy: 0.6624 - val_loss: 0.7286 - learning_rate: 7.8125e-06
Epoch 254/500
124/124 - 3s - 24ms/step - accuracy: 0.7718 - loss: 0.4753 - val_accuracy: 0.6652 - val_loss: 0.7274 - learning_rate: 7.8125e-06
Epoch 255/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4706 - val_accuracy: 0.6638 - val_loss: 0.7262 - learning_rate: 7.8125e-06
Epoch 256/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4780 - val_accuracy: 0.6652 - val_loss: 0.7259 - learning_rate: 7.8125e-06
Epoch 257/500
124/124 - 3s - 24ms/step - accuracy: 0.7713 - loss: 0.4737 - val_accuracy: 0.6595 - val_loss: 0.7285 - learning_rate: 7.8125e-06
Epoch 258/500
124/124 - 3s - 24ms/step - accuracy: 0.7645 - loss: 0.4753 - val_accuracy: 0.6652 - val_loss: 0.7268 - learning_rate: 7.8125e-06
Epoch 259/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4762 - val_accuracy: 0.6624 - val_loss: 0.7264 - learning_rate: 7.8125e-06
Epoch 260/500
124/124 - 3s - 24ms/step - accuracy: 0.7677 - loss: 0.4730 - val_accuracy: 0.6624 - val_loss: 0.7267 - learning_rate: 7.8125e-06
Epoch 261/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4767 - val_accuracy: 0.6609 - val_loss: 0.7278 - learning_rate: 7.8125e-06
Epoch 262/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4751 - val_accuracy: 0.6624 - val_loss: 0.7278 - learning_rate: 7.8125e-06
Epoch 263/500
124/124 - 3s - 24ms/step - accuracy: 0.7617 - loss: 0.4796 - val_accuracy: 0.6609 - val_loss: 0.7300 - learning_rate: 7.8125e-06
Epoch 264/500
124/124 - 3s - 24ms/step - accuracy: 0.7672 - loss: 0.4741 - val_accuracy: 0.6609 - val_loss: 0.7279 - learning_rate: 7.8125e-06
Epoch 265/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4749 - val_accuracy: 0.6580 - val_loss: 0.7298 - learning_rate: 7.8125e-06
Epoch 266/500

Epoch 266: ReduceLROnPlateau reducing learning rate to 3.906250185536919e-06.
124/124 - 3s - 24ms/step - accuracy: 0.7652 - loss: 0.4723 - val_accuracy: 0.6580 - val_loss: 0.7289 - learning_rate: 7.8125e-06
Epoch 267/500
124/124 - 3s - 23ms/step - accuracy: 0.7632 - loss: 0.4742 - val_accuracy: 0.6566 - val_loss: 0.7294 - learning_rate: 3.9063e-06
Epoch 268/500
124/124 - 3s - 24ms/step - accuracy: 0.7647 - loss: 0.4761 - val_accuracy: 0.6566 - val_loss: 0.7291 - learning_rate: 3.9063e-06
Epoch 269/500
124/124 - 3s - 24ms/step - accuracy: 0.7792 - loss: 0.4666 - val_accuracy: 0.6595 - val_loss: 0.7279 - learning_rate: 3.9063e-06
Epoch 270/500
124/124 - 3s - 24ms/step - accuracy: 0.7728 - loss: 0.4683 - val_accuracy: 0.6580 - val_loss: 0.7280 - learning_rate: 3.9063e-06
Epoch 271/500
124/124 - 3s - 24ms/step - accuracy: 0.7693 - loss: 0.4716 - val_accuracy: 0.6580 - val_loss: 0.7288 - learning_rate: 3.9063e-06
Epoch 272/500
124/124 - 3s - 24ms/step - accuracy: 0.7814 - loss: 0.4650 - val_accuracy: 0.6609 - val_loss: 0.7269 - learning_rate: 3.9063e-06
Epoch 273/500
124/124 - 3s - 24ms/step - accuracy: 0.7688 - loss: 0.4711 - val_accuracy: 0.6595 - val_loss: 0.7268 - learning_rate: 3.9063e-06
Epoch 274/500
124/124 - 3s - 24ms/step - accuracy: 0.7708 - loss: 0.4679 - val_accuracy: 0.6580 - val_loss: 0.7272 - learning_rate: 3.9063e-06
Epoch 275/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4656 - val_accuracy: 0.6580 - val_loss: 0.7273 - learning_rate: 3.9063e-06
Epoch 276/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4753 - val_accuracy: 0.6580 - val_loss: 0.7279 - learning_rate: 3.9063e-06
Epoch 276: early stopping
Restoring model weights from the end of the best epoch: 226.
Training complete. Best epoch: 226 of 276. Best val_loss: 0.7257, val_accuracy: 0.6609

========== Evaluation: LOSO fold 19 / held-out EMS0020 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        23        17         0
  intermedia         3        30        47
  max_intens         0         1        39

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.885     0.575     0.697        40
intermediate_intensity      0.625     0.375     0.469        80
         max_intensity      0.453     0.975     0.619        40

              accuracy                          0.575       160
             macro avg      0.654     0.642     0.595       160
          weighted avg      0.647     0.575     0.563       160

Overall accuracy: 0.5750

============================================================
Fold 20 of 30: holding out EMS0021
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.10e-07, 9.59e-07]
  Per-channel std range:  [7.25e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 117ms/step - accuracy: 0.4191 - loss: 1.0452 - val_accuracy: 0.5014 - val_loss: 1.0454 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5200 - loss: 0.9298 - val_accuracy: 0.5374 - val_loss: 0.9642 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5451 - loss: 0.8787 - val_accuracy: 0.5503 - val_loss: 0.9216 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5548 - loss: 0.8491 - val_accuracy: 0.5388 - val_loss: 0.9138 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5733 - loss: 0.8199 - val_accuracy: 0.5374 - val_loss: 0.9010 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5814 - loss: 0.7987 - val_accuracy: 0.5431 - val_loss: 0.8879 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.5976 - loss: 0.7785 - val_accuracy: 0.5589 - val_loss: 0.8522 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6062 - loss: 0.7641 - val_accuracy: 0.5819 - val_loss: 0.8476 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6078 - loss: 0.7512 - val_accuracy: 0.5675 - val_loss: 0.8368 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6187 - loss: 0.7381 - val_accuracy: 0.5747 - val_loss: 0.8317 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6212 - loss: 0.7337 - val_accuracy: 0.5920 - val_loss: 0.8212 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6283 - loss: 0.7174 - val_accuracy: 0.5891 - val_loss: 0.8351 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6247 - loss: 0.7125 - val_accuracy: 0.5862 - val_loss: 0.8129 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6326 - loss: 0.7043 - val_accuracy: 0.5819 - val_loss: 0.8249 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6412 - loss: 0.6998 - val_accuracy: 0.5891 - val_loss: 0.8251 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6377 - loss: 0.6985 - val_accuracy: 0.5948 - val_loss: 0.8067 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6280 - loss: 0.6998 - val_accuracy: 0.5948 - val_loss: 0.8078 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6382 - loss: 0.6880 - val_accuracy: 0.6121 - val_loss: 0.8042 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6521 - loss: 0.6813 - val_accuracy: 0.6034 - val_loss: 0.8120 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6595 - loss: 0.6687 - val_accuracy: 0.6164 - val_loss: 0.7844 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6478 - loss: 0.6737 - val_accuracy: 0.6049 - val_loss: 0.7842 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6476 - loss: 0.6765 - val_accuracy: 0.5876 - val_loss: 0.8204 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6498 - loss: 0.6659 - val_accuracy: 0.5934 - val_loss: 0.7998 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6491 - loss: 0.6639 - val_accuracy: 0.6106 - val_loss: 0.7833 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6488 - loss: 0.6592 - val_accuracy: 0.6049 - val_loss: 0.7884 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6582 - loss: 0.6514 - val_accuracy: 0.6164 - val_loss: 0.7911 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6501 - loss: 0.6579 - val_accuracy: 0.6121 - val_loss: 0.7713 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6564 - loss: 0.6468 - val_accuracy: 0.6063 - val_loss: 0.7964 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6658 - loss: 0.6419 - val_accuracy: 0.6164 - val_loss: 0.7835 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6656 - loss: 0.6433 - val_accuracy: 0.6121 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6608 - loss: 0.6460 - val_accuracy: 0.6078 - val_loss: 0.7868 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6651 - loss: 0.6331 - val_accuracy: 0.6279 - val_loss: 0.7766 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6658 - loss: 0.6364 - val_accuracy: 0.6207 - val_loss: 0.7797 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6325 - val_accuracy: 0.6236 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6651 - loss: 0.6318 - val_accuracy: 0.6207 - val_loss: 0.7669 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6673 - loss: 0.6342 - val_accuracy: 0.6221 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6689 - loss: 0.6242 - val_accuracy: 0.6221 - val_loss: 0.7736 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6228 - val_accuracy: 0.6121 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6212 - val_accuracy: 0.5991 - val_loss: 0.7837 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6782 - loss: 0.6106 - val_accuracy: 0.6135 - val_loss: 0.7799 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6689 - loss: 0.6218 - val_accuracy: 0.6164 - val_loss: 0.7824 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6165 - val_accuracy: 0.6020 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6788 - loss: 0.6157 - val_accuracy: 0.6236 - val_loss: 0.7682 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6722 - loss: 0.6151 - val_accuracy: 0.6221 - val_loss: 0.7643 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6747 - loss: 0.6137 - val_accuracy: 0.6293 - val_loss: 0.7558 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6833 - loss: 0.6073 - val_accuracy: 0.6264 - val_loss: 0.7487 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6886 - loss: 0.6130 - val_accuracy: 0.6322 - val_loss: 0.7459 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6909 - loss: 0.6059 - val_accuracy: 0.6006 - val_loss: 0.7749 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6120 - val_accuracy: 0.6092 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6788 - loss: 0.6081 - val_accuracy: 0.6264 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6889 - loss: 0.6008 - val_accuracy: 0.6221 - val_loss: 0.7747 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.5968 - val_accuracy: 0.6307 - val_loss: 0.7702 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.5988 - val_accuracy: 0.6221 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6785 - loss: 0.6065 - val_accuracy: 0.6193 - val_loss: 0.7648 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.5951 - val_accuracy: 0.6236 - val_loss: 0.7682 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5949 - val_accuracy: 0.6250 - val_loss: 0.7547 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.5937 - val_accuracy: 0.6221 - val_loss: 0.7658 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.5997 - val_accuracy: 0.6250 - val_loss: 0.7745 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5978 - val_accuracy: 0.6336 - val_loss: 0.7708 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6962 - loss: 0.5918 - val_accuracy: 0.6336 - val_loss: 0.7542 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5820 - val_accuracy: 0.6351 - val_loss: 0.7583 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6952 - loss: 0.5889 - val_accuracy: 0.6264 - val_loss: 0.7799 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5946 - val_accuracy: 0.6336 - val_loss: 0.7436 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.5943 - val_accuracy: 0.6480 - val_loss: 0.7517 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.5817 - val_accuracy: 0.6193 - val_loss: 0.7945 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5881 - val_accuracy: 0.6293 - val_loss: 0.7617 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5871 - val_accuracy: 0.6207 - val_loss: 0.7817 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5796 - val_accuracy: 0.6379 - val_loss: 0.7533 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7074 - loss: 0.5775 - val_accuracy: 0.6279 - val_loss: 0.7761 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5820 - val_accuracy: 0.6365 - val_loss: 0.7597 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5863 - val_accuracy: 0.6264 - val_loss: 0.7724 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5761 - val_accuracy: 0.6365 - val_loss: 0.7615 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7061 - loss: 0.5762 - val_accuracy: 0.6365 - val_loss: 0.7676 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7018 - loss: 0.5763 - val_accuracy: 0.6365 - val_loss: 0.7481 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5798 - val_accuracy: 0.6451 - val_loss: 0.7345 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5783 - val_accuracy: 0.6437 - val_loss: 0.7639 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5769 - val_accuracy: 0.6437 - val_loss: 0.7574 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5785 - val_accuracy: 0.6322 - val_loss: 0.7587 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5813 - val_accuracy: 0.6379 - val_loss: 0.7637 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5746 - val_accuracy: 0.6494 - val_loss: 0.7504 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5785 - val_accuracy: 0.6422 - val_loss: 0.7636 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5751 - val_accuracy: 0.6408 - val_loss: 0.7626 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5665 - val_accuracy: 0.6322 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7094 - loss: 0.5736 - val_accuracy: 0.6451 - val_loss: 0.7638 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5797 - val_accuracy: 0.6408 - val_loss: 0.7722 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5728 - val_accuracy: 0.6322 - val_loss: 0.7737 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5682 - val_accuracy: 0.6322 - val_loss: 0.7828 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5651 - val_accuracy: 0.6422 - val_loss: 0.7731 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5721 - val_accuracy: 0.6480 - val_loss: 0.7808 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7127 - loss: 0.5666 - val_accuracy: 0.6624 - val_loss: 0.7401 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7127 - loss: 0.5625 - val_accuracy: 0.6480 - val_loss: 0.7359 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7153 - loss: 0.5615 - val_accuracy: 0.6336 - val_loss: 0.7686 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7216 - loss: 0.5535 - val_accuracy: 0.6494 - val_loss: 0.7485 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5615 - val_accuracy: 0.6408 - val_loss: 0.7634 - learning_rate: 0.0010
Epoch 95/500

Epoch 95: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5589 - val_accuracy: 0.6480 - val_loss: 0.7471 - learning_rate: 0.0010
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5464 - val_accuracy: 0.6422 - val_loss: 0.7686 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7201 - loss: 0.5357 - val_accuracy: 0.6365 - val_loss: 0.7665 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7262 - loss: 0.5361 - val_accuracy: 0.6451 - val_loss: 0.7539 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7317 - loss: 0.5281 - val_accuracy: 0.6509 - val_loss: 0.7497 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5224 - val_accuracy: 0.6451 - val_loss: 0.7599 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5300 - val_accuracy: 0.6422 - val_loss: 0.7705 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7287 - loss: 0.5305 - val_accuracy: 0.6609 - val_loss: 0.7453 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5255 - val_accuracy: 0.6422 - val_loss: 0.7634 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7361 - loss: 0.5237 - val_accuracy: 0.6480 - val_loss: 0.7604 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5218 - val_accuracy: 0.6466 - val_loss: 0.7599 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5186 - val_accuracy: 0.6422 - val_loss: 0.7678 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5159 - val_accuracy: 0.6422 - val_loss: 0.7674 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7315 - loss: 0.5243 - val_accuracy: 0.6523 - val_loss: 0.7553 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5166 - val_accuracy: 0.6494 - val_loss: 0.7567 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7307 - loss: 0.5298 - val_accuracy: 0.6422 - val_loss: 0.7704 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5251 - val_accuracy: 0.6609 - val_loss: 0.7616 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7338 - loss: 0.5276 - val_accuracy: 0.6379 - val_loss: 0.7781 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5165 - val_accuracy: 0.6408 - val_loss: 0.7568 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5127 - val_accuracy: 0.6566 - val_loss: 0.7536 - learning_rate: 5.0000e-04
Epoch 115/500

Epoch 115: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5181 - val_accuracy: 0.6437 - val_loss: 0.7611 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7490 - loss: 0.5056 - val_accuracy: 0.6379 - val_loss: 0.7658 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.4994 - val_accuracy: 0.6509 - val_loss: 0.7518 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7566 - loss: 0.4953 - val_accuracy: 0.6466 - val_loss: 0.7721 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7541 - loss: 0.4948 - val_accuracy: 0.6466 - val_loss: 0.7702 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7574 - loss: 0.4874 - val_accuracy: 0.6466 - val_loss: 0.7524 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7543 - loss: 0.4950 - val_accuracy: 0.6365 - val_loss: 0.7723 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7533 - loss: 0.4977 - val_accuracy: 0.6580 - val_loss: 0.7530 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7596 - loss: 0.4872 - val_accuracy: 0.6537 - val_loss: 0.7706 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7543 - loss: 0.4954 - val_accuracy: 0.6523 - val_loss: 0.7625 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4940 - val_accuracy: 0.6566 - val_loss: 0.7658 - learning_rate: 2.5000e-04
Epoch 125: early stopping
Restoring model weights from the end of the best epoch: 75.
Training complete. Best epoch: 75 of 125. Best val_loss: 0.7345, val_accuracy: 0.6451

========== Evaluation: LOSO fold 20 / held-out EMS0021 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        25        15         0
  intermedia        14        42        24
  max_intens         1         4        35

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.625     0.625     0.625        40
intermediate_intensity      0.689     0.525     0.596        80
         max_intensity      0.593     0.875     0.707        40

              accuracy                          0.637       160
             macro avg      0.636     0.675     0.643       160
          weighted avg      0.649     0.637     0.631       160

Overall accuracy: 0.6375

============================================================
Fold 21 of 30: holding out EMS0022
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.25e-07, 9.43e-07]
  Per-channel std range:  [7.26e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 114ms/step - accuracy: 0.4658 - loss: 1.0172 - val_accuracy: 0.4698 - val_loss: 1.0290 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5312 - loss: 0.9082 - val_accuracy: 0.5230 - val_loss: 0.9455 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5543 - loss: 0.8583 - val_accuracy: 0.5316 - val_loss: 0.8978 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5707 - loss: 0.8246 - val_accuracy: 0.5417 - val_loss: 0.8762 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5910 - loss: 0.8056 - val_accuracy: 0.5560 - val_loss: 0.8686 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5963 - loss: 0.7866 - val_accuracy: 0.5546 - val_loss: 0.8596 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.5991 - loss: 0.7729 - val_accuracy: 0.5618 - val_loss: 0.8484 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6009 - loss: 0.7603 - val_accuracy: 0.5690 - val_loss: 0.8335 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6083 - loss: 0.7473 - val_accuracy: 0.5819 - val_loss: 0.8336 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6217 - loss: 0.7368 - val_accuracy: 0.5920 - val_loss: 0.8130 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6247 - loss: 0.7234 - val_accuracy: 0.5920 - val_loss: 0.8139 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6260 - loss: 0.7164 - val_accuracy: 0.5905 - val_loss: 0.8138 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6260 - loss: 0.7134 - val_accuracy: 0.5991 - val_loss: 0.8114 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6296 - loss: 0.7084 - val_accuracy: 0.5934 - val_loss: 0.7935 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6316 - loss: 0.6982 - val_accuracy: 0.5991 - val_loss: 0.8055 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6384 - loss: 0.6945 - val_accuracy: 0.5934 - val_loss: 0.8140 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6466 - loss: 0.6832 - val_accuracy: 0.5833 - val_loss: 0.8070 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6542 - loss: 0.6803 - val_accuracy: 0.5790 - val_loss: 0.8193 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6458 - loss: 0.6758 - val_accuracy: 0.5848 - val_loss: 0.7945 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 24ms/step - accuracy: 0.6569 - loss: 0.6737 - val_accuracy: 0.5920 - val_loss: 0.7877 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6450 - loss: 0.6785 - val_accuracy: 0.5963 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6608 - loss: 0.6666 - val_accuracy: 0.6020 - val_loss: 0.7829 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6559 - loss: 0.6614 - val_accuracy: 0.5905 - val_loss: 0.8012 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6569 - loss: 0.6581 - val_accuracy: 0.5876 - val_loss: 0.8097 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6524 - loss: 0.6589 - val_accuracy: 0.5776 - val_loss: 0.8019 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6638 - loss: 0.6520 - val_accuracy: 0.5991 - val_loss: 0.7873 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6618 - loss: 0.6505 - val_accuracy: 0.6092 - val_loss: 0.7822 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6547 - loss: 0.6572 - val_accuracy: 0.6006 - val_loss: 0.7911 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6681 - loss: 0.6377 - val_accuracy: 0.6078 - val_loss: 0.7937 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6681 - loss: 0.6388 - val_accuracy: 0.6078 - val_loss: 0.7728 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 24ms/step - accuracy: 0.6663 - loss: 0.6402 - val_accuracy: 0.6092 - val_loss: 0.7873 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 24ms/step - accuracy: 0.6706 - loss: 0.6408 - val_accuracy: 0.6106 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6633 - loss: 0.6303 - val_accuracy: 0.5991 - val_loss: 0.7912 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6749 - loss: 0.6304 - val_accuracy: 0.6034 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6689 - loss: 0.6258 - val_accuracy: 0.5977 - val_loss: 0.7818 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6262 - val_accuracy: 0.5963 - val_loss: 0.7848 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 24ms/step - accuracy: 0.6689 - loss: 0.6293 - val_accuracy: 0.5776 - val_loss: 0.8092 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6757 - loss: 0.6231 - val_accuracy: 0.5920 - val_loss: 0.7921 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6767 - loss: 0.6182 - val_accuracy: 0.5948 - val_loss: 0.7917 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6818 - loss: 0.6164 - val_accuracy: 0.6020 - val_loss: 0.7865 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6828 - loss: 0.6099 - val_accuracy: 0.6106 - val_loss: 0.7752 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6770 - loss: 0.6171 - val_accuracy: 0.6207 - val_loss: 0.7606 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6803 - loss: 0.6170 - val_accuracy: 0.5977 - val_loss: 0.8037 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6897 - loss: 0.6123 - val_accuracy: 0.5991 - val_loss: 0.7998 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6808 - loss: 0.6145 - val_accuracy: 0.6049 - val_loss: 0.7963 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6187 - val_accuracy: 0.6034 - val_loss: 0.7967 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6775 - loss: 0.6082 - val_accuracy: 0.6164 - val_loss: 0.7702 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6869 - loss: 0.6034 - val_accuracy: 0.6020 - val_loss: 0.7856 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.5987 - val_accuracy: 0.6164 - val_loss: 0.7826 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.6912 - loss: 0.6080 - val_accuracy: 0.6207 - val_loss: 0.7737 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.6897 - loss: 0.5981 - val_accuracy: 0.6149 - val_loss: 0.7622 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 24ms/step - accuracy: 0.6798 - loss: 0.6042 - val_accuracy: 0.5905 - val_loss: 0.7973 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.6874 - loss: 0.6047 - val_accuracy: 0.5848 - val_loss: 0.8137 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.5919 - val_accuracy: 0.6149 - val_loss: 0.7681 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 25ms/step - accuracy: 0.6968 - loss: 0.5904 - val_accuracy: 0.6279 - val_loss: 0.7558 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 24ms/step - accuracy: 0.6935 - loss: 0.5941 - val_accuracy: 0.6078 - val_loss: 0.7906 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.6983 - loss: 0.5950 - val_accuracy: 0.6149 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5893 - val_accuracy: 0.5805 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 24ms/step - accuracy: 0.6957 - loss: 0.5884 - val_accuracy: 0.5991 - val_loss: 0.7908 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.6957 - loss: 0.5856 - val_accuracy: 0.6063 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.6836 - loss: 0.6009 - val_accuracy: 0.6063 - val_loss: 0.7849 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.6942 - loss: 0.5882 - val_accuracy: 0.6121 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.6993 - loss: 0.5815 - val_accuracy: 0.6193 - val_loss: 0.7876 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7056 - loss: 0.5824 - val_accuracy: 0.6264 - val_loss: 0.7682 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5863 - val_accuracy: 0.6020 - val_loss: 0.7951 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7054 - loss: 0.5866 - val_accuracy: 0.6236 - val_loss: 0.7708 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.7056 - loss: 0.5784 - val_accuracy: 0.6135 - val_loss: 0.7859 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.6965 - loss: 0.5824 - val_accuracy: 0.6264 - val_loss: 0.7693 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.6975 - loss: 0.5827 - val_accuracy: 0.6063 - val_loss: 0.7998 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 24ms/step - accuracy: 0.6983 - loss: 0.5771 - val_accuracy: 0.6250 - val_loss: 0.7848 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.7061 - loss: 0.5699 - val_accuracy: 0.6063 - val_loss: 0.7914 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.6945 - loss: 0.5862 - val_accuracy: 0.6020 - val_loss: 0.7953 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7074 - loss: 0.5770 - val_accuracy: 0.5905 - val_loss: 0.8044 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7031 - loss: 0.5718 - val_accuracy: 0.6221 - val_loss: 0.7428 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7049 - loss: 0.5724 - val_accuracy: 0.6078 - val_loss: 0.8012 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7028 - loss: 0.5716 - val_accuracy: 0.6336 - val_loss: 0.7591 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.6968 - loss: 0.5844 - val_accuracy: 0.5948 - val_loss: 0.7933 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7069 - loss: 0.5700 - val_accuracy: 0.6178 - val_loss: 0.7729 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7110 - loss: 0.5662 - val_accuracy: 0.6063 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7003 - loss: 0.5774 - val_accuracy: 0.6106 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5649 - val_accuracy: 0.6221 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5774 - val_accuracy: 0.6207 - val_loss: 0.7745 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7056 - loss: 0.5663 - val_accuracy: 0.6034 - val_loss: 0.7930 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7135 - loss: 0.5641 - val_accuracy: 0.6221 - val_loss: 0.7823 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7016 - loss: 0.5763 - val_accuracy: 0.6221 - val_loss: 0.7917 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7170 - loss: 0.5613 - val_accuracy: 0.6034 - val_loss: 0.8121 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7089 - loss: 0.5606 - val_accuracy: 0.6092 - val_loss: 0.7779 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7102 - loss: 0.5594 - val_accuracy: 0.6236 - val_loss: 0.7970 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7112 - loss: 0.5537 - val_accuracy: 0.6221 - val_loss: 0.7765 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7066 - loss: 0.5617 - val_accuracy: 0.6049 - val_loss: 0.8318 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7059 - loss: 0.5627 - val_accuracy: 0.6250 - val_loss: 0.7798 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7056 - loss: 0.5591 - val_accuracy: 0.6408 - val_loss: 0.7922 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7097 - loss: 0.5633 - val_accuracy: 0.6193 - val_loss: 0.7956 - learning_rate: 0.0010
Epoch 94/500

Epoch 94: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 24ms/step - accuracy: 0.7198 - loss: 0.5582 - val_accuracy: 0.6207 - val_loss: 0.8036 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7284 - loss: 0.5328 - val_accuracy: 0.6293 - val_loss: 0.7748 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7343 - loss: 0.5222 - val_accuracy: 0.6351 - val_loss: 0.7711 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7350 - loss: 0.5181 - val_accuracy: 0.6322 - val_loss: 0.7745 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7409 - loss: 0.5201 - val_accuracy: 0.6264 - val_loss: 0.7750 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7269 - loss: 0.5217 - val_accuracy: 0.6322 - val_loss: 0.7629 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7340 - loss: 0.5208 - val_accuracy: 0.6207 - val_loss: 0.7829 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7404 - loss: 0.5264 - val_accuracy: 0.6236 - val_loss: 0.7727 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5174 - val_accuracy: 0.6279 - val_loss: 0.7734 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7330 - loss: 0.5173 - val_accuracy: 0.6293 - val_loss: 0.7822 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7394 - loss: 0.5151 - val_accuracy: 0.6293 - val_loss: 0.7703 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7419 - loss: 0.5147 - val_accuracy: 0.6365 - val_loss: 0.7550 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7358 - loss: 0.5119 - val_accuracy: 0.6307 - val_loss: 0.7656 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7426 - loss: 0.5134 - val_accuracy: 0.6408 - val_loss: 0.7880 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7366 - loss: 0.5182 - val_accuracy: 0.6394 - val_loss: 0.7903 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7363 - loss: 0.5229 - val_accuracy: 0.6207 - val_loss: 0.7748 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7406 - loss: 0.5125 - val_accuracy: 0.6293 - val_loss: 0.7978 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7444 - loss: 0.5107 - val_accuracy: 0.6336 - val_loss: 0.7819 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7404 - loss: 0.5169 - val_accuracy: 0.6149 - val_loss: 0.7915 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7358 - loss: 0.5169 - val_accuracy: 0.6307 - val_loss: 0.7920 - learning_rate: 5.0000e-04
Epoch 114/500

Epoch 114: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7371 - loss: 0.5110 - val_accuracy: 0.6250 - val_loss: 0.7652 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7508 - loss: 0.4940 - val_accuracy: 0.6293 - val_loss: 0.7698 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7609 - loss: 0.4951 - val_accuracy: 0.6307 - val_loss: 0.7682 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4962 - val_accuracy: 0.6236 - val_loss: 0.7792 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7571 - loss: 0.4887 - val_accuracy: 0.6279 - val_loss: 0.7704 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7576 - loss: 0.4869 - val_accuracy: 0.6307 - val_loss: 0.7695 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7553 - loss: 0.4949 - val_accuracy: 0.6351 - val_loss: 0.7812 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4896 - val_accuracy: 0.6250 - val_loss: 0.7862 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4842 - val_accuracy: 0.6193 - val_loss: 0.7849 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7574 - loss: 0.4856 - val_accuracy: 0.6293 - val_loss: 0.7805 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4838 - val_accuracy: 0.6264 - val_loss: 0.7988 - learning_rate: 2.5000e-04
Epoch 124: early stopping
Restoring model weights from the end of the best epoch: 74.
Training complete. Best epoch: 74 of 124. Best val_loss: 0.7428, val_accuracy: 0.6221

========== Evaluation: LOSO fold 21 / held-out EMS0022 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        35         5         0
  intermedia        10        50        20
  max_intens         0        12        28

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.778     0.875     0.824        40
intermediate_intensity      0.746     0.625     0.680        80
         max_intensity      0.583     0.700     0.636        40

              accuracy                          0.706       160
             macro avg      0.702     0.733     0.713       160
          weighted avg      0.713     0.706     0.705       160

Overall accuracy: 0.7063

============================================================
Fold 22 of 30: holding out EMS0023
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-3.93e-07, 9.59e-07]
  Per-channel std range:  [6.86e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 124ms/step - accuracy: 0.4452 - loss: 1.0353 - val_accuracy: 0.4727 - val_loss: 1.0420 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5259 - loss: 0.9126 - val_accuracy: 0.5144 - val_loss: 0.9530 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5573 - loss: 0.8528 - val_accuracy: 0.5302 - val_loss: 0.9185 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5783 - loss: 0.8132 - val_accuracy: 0.5287 - val_loss: 0.9013 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5915 - loss: 0.7942 - val_accuracy: 0.5503 - val_loss: 0.8976 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.6014 - loss: 0.7773 - val_accuracy: 0.5460 - val_loss: 0.8786 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.5870 - loss: 0.7666 - val_accuracy: 0.5560 - val_loss: 0.8826 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6050 - loss: 0.7561 - val_accuracy: 0.5661 - val_loss: 0.8591 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6194 - loss: 0.7416 - val_accuracy: 0.5575 - val_loss: 0.8729 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6164 - loss: 0.7364 - val_accuracy: 0.5460 - val_loss: 0.8683 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6161 - loss: 0.7349 - val_accuracy: 0.5733 - val_loss: 0.8452 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6227 - loss: 0.7211 - val_accuracy: 0.5575 - val_loss: 0.8490 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6149 - loss: 0.7239 - val_accuracy: 0.5489 - val_loss: 0.8609 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6237 - loss: 0.7070 - val_accuracy: 0.5560 - val_loss: 0.8472 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6301 - loss: 0.7009 - val_accuracy: 0.5661 - val_loss: 0.8383 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 25ms/step - accuracy: 0.6349 - loss: 0.6988 - val_accuracy: 0.5747 - val_loss: 0.8327 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6387 - loss: 0.6896 - val_accuracy: 0.5718 - val_loss: 0.8457 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6364 - loss: 0.6971 - val_accuracy: 0.5718 - val_loss: 0.8242 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6392 - loss: 0.6854 - val_accuracy: 0.5805 - val_loss: 0.8238 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 24ms/step - accuracy: 0.6504 - loss: 0.6814 - val_accuracy: 0.5819 - val_loss: 0.8314 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6379 - loss: 0.6786 - val_accuracy: 0.5876 - val_loss: 0.8185 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6524 - loss: 0.6784 - val_accuracy: 0.5920 - val_loss: 0.8278 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6569 - loss: 0.6680 - val_accuracy: 0.5704 - val_loss: 0.8329 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6552 - loss: 0.6642 - val_accuracy: 0.5848 - val_loss: 0.8352 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 24ms/step - accuracy: 0.6585 - loss: 0.6681 - val_accuracy: 0.5761 - val_loss: 0.8477 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6602 - loss: 0.6571 - val_accuracy: 0.5776 - val_loss: 0.8461 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6514 - loss: 0.6584 - val_accuracy: 0.5833 - val_loss: 0.8334 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6648 - loss: 0.6473 - val_accuracy: 0.5833 - val_loss: 0.8203 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6618 - loss: 0.6513 - val_accuracy: 0.5704 - val_loss: 0.8245 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6671 - loss: 0.6443 - val_accuracy: 0.5920 - val_loss: 0.8162 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6640 - loss: 0.6429 - val_accuracy: 0.5805 - val_loss: 0.8216 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6615 - loss: 0.6478 - val_accuracy: 0.5819 - val_loss: 0.8347 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6689 - loss: 0.6381 - val_accuracy: 0.5848 - val_loss: 0.8069 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6673 - loss: 0.6421 - val_accuracy: 0.5848 - val_loss: 0.8150 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6719 - loss: 0.6427 - val_accuracy: 0.5920 - val_loss: 0.7975 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6795 - loss: 0.6297 - val_accuracy: 0.5934 - val_loss: 0.8248 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 24ms/step - accuracy: 0.6826 - loss: 0.6241 - val_accuracy: 0.5790 - val_loss: 0.8254 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 25ms/step - accuracy: 0.6762 - loss: 0.6299 - val_accuracy: 0.6006 - val_loss: 0.7974 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6805 - loss: 0.6267 - val_accuracy: 0.5833 - val_loss: 0.8177 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6755 - loss: 0.6292 - val_accuracy: 0.5948 - val_loss: 0.8044 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6790 - loss: 0.6257 - val_accuracy: 0.6006 - val_loss: 0.7929 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6767 - loss: 0.6222 - val_accuracy: 0.5963 - val_loss: 0.7978 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6722 - loss: 0.6290 - val_accuracy: 0.5905 - val_loss: 0.8277 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6841 - loss: 0.6144 - val_accuracy: 0.5833 - val_loss: 0.8110 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6755 - loss: 0.6195 - val_accuracy: 0.5920 - val_loss: 0.8179 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 25ms/step - accuracy: 0.6747 - loss: 0.6169 - val_accuracy: 0.5948 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6767 - loss: 0.6138 - val_accuracy: 0.5977 - val_loss: 0.8160 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6815 - loss: 0.6181 - val_accuracy: 0.5991 - val_loss: 0.7862 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6879 - loss: 0.6069 - val_accuracy: 0.6006 - val_loss: 0.7924 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.6848 - loss: 0.6068 - val_accuracy: 0.6092 - val_loss: 0.7841 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.6869 - loss: 0.6073 - val_accuracy: 0.6034 - val_loss: 0.8057 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 25ms/step - accuracy: 0.6942 - loss: 0.6047 - val_accuracy: 0.6063 - val_loss: 0.7792 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.6917 - loss: 0.6015 - val_accuracy: 0.6063 - val_loss: 0.7992 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 24ms/step - accuracy: 0.6917 - loss: 0.6015 - val_accuracy: 0.5948 - val_loss: 0.8308 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 24ms/step - accuracy: 0.6927 - loss: 0.5968 - val_accuracy: 0.5991 - val_loss: 0.7966 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5955 - val_accuracy: 0.6049 - val_loss: 0.7949 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.6881 - loss: 0.6020 - val_accuracy: 0.6178 - val_loss: 0.7839 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 24ms/step - accuracy: 0.6879 - loss: 0.6047 - val_accuracy: 0.5920 - val_loss: 0.8096 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6002 - val_accuracy: 0.6020 - val_loss: 0.7928 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.6937 - loss: 0.6003 - val_accuracy: 0.6078 - val_loss: 0.8131 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.6990 - loss: 0.5927 - val_accuracy: 0.6092 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.6886 - loss: 0.5993 - val_accuracy: 0.6236 - val_loss: 0.7816 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.6909 - loss: 0.5910 - val_accuracy: 0.6034 - val_loss: 0.8063 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 24ms/step - accuracy: 0.6922 - loss: 0.5999 - val_accuracy: 0.6121 - val_loss: 0.8181 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.6932 - loss: 0.5873 - val_accuracy: 0.6078 - val_loss: 0.7955 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.6960 - loss: 0.5934 - val_accuracy: 0.5991 - val_loss: 0.7856 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.7049 - loss: 0.5891 - val_accuracy: 0.6006 - val_loss: 0.8141 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.6940 - loss: 0.5882 - val_accuracy: 0.6121 - val_loss: 0.7895 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.7006 - loss: 0.5892 - val_accuracy: 0.6164 - val_loss: 0.8010 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 24ms/step - accuracy: 0.7001 - loss: 0.5868 - val_accuracy: 0.6178 - val_loss: 0.8260 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.5916 - val_accuracy: 0.6106 - val_loss: 0.7886 - learning_rate: 0.0010
Epoch 72/500

Epoch 72: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 24ms/step - accuracy: 0.7056 - loss: 0.5771 - val_accuracy: 0.6034 - val_loss: 0.8048 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7104 - loss: 0.5593 - val_accuracy: 0.6322 - val_loss: 0.7599 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7175 - loss: 0.5532 - val_accuracy: 0.6264 - val_loss: 0.7631 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7254 - loss: 0.5446 - val_accuracy: 0.6250 - val_loss: 0.7426 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7315 - loss: 0.5438 - val_accuracy: 0.6322 - val_loss: 0.7527 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7196 - loss: 0.5476 - val_accuracy: 0.6293 - val_loss: 0.7887 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7252 - loss: 0.5422 - val_accuracy: 0.6149 - val_loss: 0.7709 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7254 - loss: 0.5408 - val_accuracy: 0.6178 - val_loss: 0.7712 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7112 - loss: 0.5506 - val_accuracy: 0.6149 - val_loss: 0.7522 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7183 - loss: 0.5466 - val_accuracy: 0.6236 - val_loss: 0.7653 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5451 - val_accuracy: 0.6149 - val_loss: 0.7744 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7305 - loss: 0.5366 - val_accuracy: 0.6279 - val_loss: 0.7687 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7333 - loss: 0.5372 - val_accuracy: 0.6279 - val_loss: 0.7796 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7297 - loss: 0.5368 - val_accuracy: 0.6164 - val_loss: 0.7457 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7292 - loss: 0.5362 - val_accuracy: 0.6279 - val_loss: 0.7651 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7257 - loss: 0.5379 - val_accuracy: 0.6322 - val_loss: 0.7517 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7211 - loss: 0.5480 - val_accuracy: 0.6207 - val_loss: 0.7753 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7264 - loss: 0.5394 - val_accuracy: 0.6221 - val_loss: 0.7441 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7239 - loss: 0.5363 - val_accuracy: 0.6178 - val_loss: 0.7728 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5384 - val_accuracy: 0.6264 - val_loss: 0.7688 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5390 - val_accuracy: 0.6221 - val_loss: 0.7772 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7221 - loss: 0.5421 - val_accuracy: 0.6207 - val_loss: 0.7466 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7246 - loss: 0.5399 - val_accuracy: 0.6164 - val_loss: 0.7617 - learning_rate: 5.0000e-04
Epoch 95/500

Epoch 95: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7323 - loss: 0.5354 - val_accuracy: 0.6164 - val_loss: 0.7645 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7371 - loss: 0.5152 - val_accuracy: 0.6279 - val_loss: 0.7740 - learning_rate: 2.5000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7421 - loss: 0.5158 - val_accuracy: 0.6236 - val_loss: 0.7542 - learning_rate: 2.5000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7467 - loss: 0.5125 - val_accuracy: 0.6221 - val_loss: 0.7580 - learning_rate: 2.5000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7409 - loss: 0.5116 - val_accuracy: 0.6250 - val_loss: 0.7535 - learning_rate: 2.5000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5124 - val_accuracy: 0.6322 - val_loss: 0.7698 - learning_rate: 2.5000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5084 - val_accuracy: 0.6264 - val_loss: 0.7629 - learning_rate: 2.5000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.5111 - val_accuracy: 0.6307 - val_loss: 0.7633 - learning_rate: 2.5000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5135 - val_accuracy: 0.6250 - val_loss: 0.7528 - learning_rate: 2.5000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7452 - loss: 0.5103 - val_accuracy: 0.6250 - val_loss: 0.7752 - learning_rate: 2.5000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5159 - val_accuracy: 0.6307 - val_loss: 0.7706 - learning_rate: 2.5000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5176 - val_accuracy: 0.6351 - val_loss: 0.7594 - learning_rate: 2.5000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5115 - val_accuracy: 0.6408 - val_loss: 0.7497 - learning_rate: 2.5000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7442 - loss: 0.5139 - val_accuracy: 0.6422 - val_loss: 0.7657 - learning_rate: 2.5000e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7490 - loss: 0.5054 - val_accuracy: 0.6307 - val_loss: 0.7464 - learning_rate: 2.5000e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7406 - loss: 0.5130 - val_accuracy: 0.6365 - val_loss: 0.7517 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7495 - loss: 0.5036 - val_accuracy: 0.6351 - val_loss: 0.7544 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7462 - loss: 0.5082 - val_accuracy: 0.6336 - val_loss: 0.7635 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7599 - loss: 0.5037 - val_accuracy: 0.6394 - val_loss: 0.7493 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7437 - loss: 0.5073 - val_accuracy: 0.6279 - val_loss: 0.7479 - learning_rate: 2.5000e-04
Epoch 115/500

Epoch 115: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7492 - loss: 0.5062 - val_accuracy: 0.6394 - val_loss: 0.7502 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7475 - loss: 0.5044 - val_accuracy: 0.6365 - val_loss: 0.7411 - learning_rate: 1.2500e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4914 - val_accuracy: 0.6307 - val_loss: 0.7396 - learning_rate: 1.2500e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7530 - loss: 0.4979 - val_accuracy: 0.6351 - val_loss: 0.7428 - learning_rate: 1.2500e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7485 - loss: 0.4925 - val_accuracy: 0.6394 - val_loss: 0.7405 - learning_rate: 1.2500e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.5002 - val_accuracy: 0.6336 - val_loss: 0.7441 - learning_rate: 1.2500e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7528 - loss: 0.4953 - val_accuracy: 0.6437 - val_loss: 0.7434 - learning_rate: 1.2500e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7541 - loss: 0.4934 - val_accuracy: 0.6408 - val_loss: 0.7445 - learning_rate: 1.2500e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7591 - loss: 0.4954 - val_accuracy: 0.6336 - val_loss: 0.7574 - learning_rate: 1.2500e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7553 - loss: 0.4930 - val_accuracy: 0.6408 - val_loss: 0.7440 - learning_rate: 1.2500e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7601 - loss: 0.4799 - val_accuracy: 0.6408 - val_loss: 0.7505 - learning_rate: 1.2500e-04
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7561 - loss: 0.4925 - val_accuracy: 0.6451 - val_loss: 0.7449 - learning_rate: 1.2500e-04
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7530 - loss: 0.4981 - val_accuracy: 0.6351 - val_loss: 0.7473 - learning_rate: 1.2500e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7558 - loss: 0.4915 - val_accuracy: 0.6422 - val_loss: 0.7440 - learning_rate: 1.2500e-04
Epoch 129/500
124/124 - 3s - 24ms/step - accuracy: 0.7487 - loss: 0.4933 - val_accuracy: 0.6379 - val_loss: 0.7468 - learning_rate: 1.2500e-04
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4906 - val_accuracy: 0.6379 - val_loss: 0.7481 - learning_rate: 1.2500e-04
Epoch 131/500
124/124 - 3s - 24ms/step - accuracy: 0.7510 - loss: 0.4919 - val_accuracy: 0.6336 - val_loss: 0.7460 - learning_rate: 1.2500e-04
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7563 - loss: 0.4945 - val_accuracy: 0.6408 - val_loss: 0.7509 - learning_rate: 1.2500e-04
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7599 - loss: 0.4899 - val_accuracy: 0.6394 - val_loss: 0.7524 - learning_rate: 1.2500e-04
Epoch 134/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4838 - val_accuracy: 0.6451 - val_loss: 0.7455 - learning_rate: 1.2500e-04
Epoch 135/500
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.4913 - val_accuracy: 0.6394 - val_loss: 0.7508 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 24ms/step - accuracy: 0.7485 - loss: 0.4954 - val_accuracy: 0.6422 - val_loss: 0.7566 - learning_rate: 1.2500e-04
Epoch 137/500

Epoch 137: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7513 - loss: 0.4912 - val_accuracy: 0.6351 - val_loss: 0.7458 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4868 - val_accuracy: 0.6351 - val_loss: 0.7483 - learning_rate: 6.2500e-05
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7541 - loss: 0.4905 - val_accuracy: 0.6365 - val_loss: 0.7565 - learning_rate: 6.2500e-05
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4869 - val_accuracy: 0.6379 - val_loss: 0.7539 - learning_rate: 6.2500e-05
Epoch 141/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4861 - val_accuracy: 0.6379 - val_loss: 0.7539 - learning_rate: 6.2500e-05
Epoch 142/500
124/124 - 3s - 24ms/step - accuracy: 0.7546 - loss: 0.4930 - val_accuracy: 0.6336 - val_loss: 0.7506 - learning_rate: 6.2500e-05
Epoch 143/500
124/124 - 3s - 24ms/step - accuracy: 0.7571 - loss: 0.4871 - val_accuracy: 0.6394 - val_loss: 0.7592 - learning_rate: 6.2500e-05
Epoch 144/500
124/124 - 3s - 24ms/step - accuracy: 0.7652 - loss: 0.4792 - val_accuracy: 0.6379 - val_loss: 0.7516 - learning_rate: 6.2500e-05
Epoch 145/500
124/124 - 3s - 24ms/step - accuracy: 0.7660 - loss: 0.4851 - val_accuracy: 0.6394 - val_loss: 0.7568 - learning_rate: 6.2500e-05
Epoch 146/500
124/124 - 3s - 24ms/step - accuracy: 0.7609 - loss: 0.4889 - val_accuracy: 0.6365 - val_loss: 0.7520 - learning_rate: 6.2500e-05
Epoch 147/500
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.4901 - val_accuracy: 0.6351 - val_loss: 0.7546 - learning_rate: 6.2500e-05
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4867 - val_accuracy: 0.6365 - val_loss: 0.7499 - learning_rate: 6.2500e-05
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4814 - val_accuracy: 0.6408 - val_loss: 0.7575 - learning_rate: 6.2500e-05
Epoch 150/500
124/124 - 3s - 24ms/step - accuracy: 0.7614 - loss: 0.4858 - val_accuracy: 0.6394 - val_loss: 0.7533 - learning_rate: 6.2500e-05
Epoch 151/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4795 - val_accuracy: 0.6379 - val_loss: 0.7512 - learning_rate: 6.2500e-05
Epoch 152/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4841 - val_accuracy: 0.6379 - val_loss: 0.7512 - learning_rate: 6.2500e-05
Epoch 153/500
124/124 - 3s - 24ms/step - accuracy: 0.7586 - loss: 0.4850 - val_accuracy: 0.6437 - val_loss: 0.7550 - learning_rate: 6.2500e-05
Epoch 154/500
124/124 - 3s - 24ms/step - accuracy: 0.7586 - loss: 0.4867 - val_accuracy: 0.6394 - val_loss: 0.7545 - learning_rate: 6.2500e-05
Epoch 155/500
124/124 - 3s - 24ms/step - accuracy: 0.7606 - loss: 0.4820 - val_accuracy: 0.6351 - val_loss: 0.7525 - learning_rate: 6.2500e-05
Epoch 156/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4891 - val_accuracy: 0.6336 - val_loss: 0.7480 - learning_rate: 6.2500e-05
Epoch 157/500

Epoch 157: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4837 - val_accuracy: 0.6408 - val_loss: 0.7480 - learning_rate: 6.2500e-05
Epoch 158/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4744 - val_accuracy: 0.6379 - val_loss: 0.7440 - learning_rate: 3.1250e-05
Epoch 159/500
124/124 - 3s - 24ms/step - accuracy: 0.7579 - loss: 0.4844 - val_accuracy: 0.6336 - val_loss: 0.7459 - learning_rate: 3.1250e-05
Epoch 160/500
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4798 - val_accuracy: 0.6408 - val_loss: 0.7444 - learning_rate: 3.1250e-05
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7586 - loss: 0.4807 - val_accuracy: 0.6437 - val_loss: 0.7430 - learning_rate: 3.1250e-05
Epoch 162/500
124/124 - 3s - 24ms/step - accuracy: 0.7576 - loss: 0.4890 - val_accuracy: 0.6408 - val_loss: 0.7464 - learning_rate: 3.1250e-05
Epoch 163/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4798 - val_accuracy: 0.6422 - val_loss: 0.7424 - learning_rate: 3.1250e-05
Epoch 164/500
124/124 - 3s - 24ms/step - accuracy: 0.7599 - loss: 0.4795 - val_accuracy: 0.6437 - val_loss: 0.7425 - learning_rate: 3.1250e-05
Epoch 165/500
124/124 - 3s - 24ms/step - accuracy: 0.7520 - loss: 0.4868 - val_accuracy: 0.6394 - val_loss: 0.7468 - learning_rate: 3.1250e-05
Epoch 166/500
124/124 - 3s - 24ms/step - accuracy: 0.7599 - loss: 0.4785 - val_accuracy: 0.6394 - val_loss: 0.7447 - learning_rate: 3.1250e-05
Epoch 167/500
124/124 - 3s - 24ms/step - accuracy: 0.7639 - loss: 0.4819 - val_accuracy: 0.6365 - val_loss: 0.7436 - learning_rate: 3.1250e-05
Epoch 167: early stopping
Restoring model weights from the end of the best epoch: 117.
Training complete. Best epoch: 117 of 167. Best val_loss: 0.7396, val_accuracy: 0.6307

========== Evaluation: LOSO fold 22 / held-out EMS0023 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        30         9         1
  intermedia         3        47        30
  max_intens         0         4        36

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.909     0.750     0.822        40
intermediate_intensity      0.783     0.588     0.671        80
         max_intensity      0.537     0.900     0.673        40

              accuracy                          0.706       160
             macro avg      0.743     0.746     0.722       160
          weighted avg      0.753     0.706     0.709       160

Overall accuracy: 0.7063

============================================================
Fold 23 of 30: holding out EMS0024
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.04e-07, 9.55e-07]
  Per-channel std range:  [7.15e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4341 - loss: 1.0371 - val_accuracy: 0.5144 - val_loss: 1.0329 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5193 - loss: 0.9278 - val_accuracy: 0.5316 - val_loss: 0.9436 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5484 - loss: 0.8753 - val_accuracy: 0.5273 - val_loss: 0.9079 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5631 - loss: 0.8406 - val_accuracy: 0.5632 - val_loss: 0.8735 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5809 - loss: 0.8145 - val_accuracy: 0.5704 - val_loss: 0.8653 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5905 - loss: 0.7954 - val_accuracy: 0.5761 - val_loss: 0.8455 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.5918 - loss: 0.7775 - val_accuracy: 0.5963 - val_loss: 0.8248 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 23ms/step - accuracy: 0.6007 - loss: 0.7652 - val_accuracy: 0.6006 - val_loss: 0.8194 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6070 - loss: 0.7496 - val_accuracy: 0.6049 - val_loss: 0.8087 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6098 - loss: 0.7426 - val_accuracy: 0.5991 - val_loss: 0.8084 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6265 - loss: 0.7282 - val_accuracy: 0.5819 - val_loss: 0.8003 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6285 - loss: 0.7194 - val_accuracy: 0.5948 - val_loss: 0.7871 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6197 - loss: 0.7174 - val_accuracy: 0.5805 - val_loss: 0.8053 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6296 - loss: 0.7104 - val_accuracy: 0.6063 - val_loss: 0.7830 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6364 - loss: 0.7000 - val_accuracy: 0.6063 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6397 - loss: 0.6951 - val_accuracy: 0.6049 - val_loss: 0.7821 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6863 - val_accuracy: 0.5991 - val_loss: 0.7826 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6420 - loss: 0.6862 - val_accuracy: 0.6207 - val_loss: 0.7730 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6433 - loss: 0.6782 - val_accuracy: 0.6106 - val_loss: 0.7786 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6521 - loss: 0.6686 - val_accuracy: 0.6034 - val_loss: 0.7685 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6402 - loss: 0.6737 - val_accuracy: 0.6092 - val_loss: 0.7647 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6621 - val_accuracy: 0.6135 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6491 - loss: 0.6661 - val_accuracy: 0.6236 - val_loss: 0.7596 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6658 - loss: 0.6527 - val_accuracy: 0.6135 - val_loss: 0.7721 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6498 - loss: 0.6602 - val_accuracy: 0.6207 - val_loss: 0.7514 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6549 - loss: 0.6529 - val_accuracy: 0.6178 - val_loss: 0.7535 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6575 - loss: 0.6496 - val_accuracy: 0.6149 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6592 - loss: 0.6510 - val_accuracy: 0.6264 - val_loss: 0.7475 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6409 - val_accuracy: 0.6106 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6575 - loss: 0.6491 - val_accuracy: 0.6149 - val_loss: 0.7679 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6689 - loss: 0.6352 - val_accuracy: 0.6149 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6334 - val_accuracy: 0.6236 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6613 - loss: 0.6336 - val_accuracy: 0.6264 - val_loss: 0.7515 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6623 - loss: 0.6365 - val_accuracy: 0.6020 - val_loss: 0.7604 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6691 - loss: 0.6291 - val_accuracy: 0.6322 - val_loss: 0.7442 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6272 - val_accuracy: 0.6135 - val_loss: 0.7546 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6737 - loss: 0.6303 - val_accuracy: 0.6106 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6237 - val_accuracy: 0.6178 - val_loss: 0.7449 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6770 - loss: 0.6267 - val_accuracy: 0.6293 - val_loss: 0.7398 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6808 - loss: 0.6159 - val_accuracy: 0.6193 - val_loss: 0.7438 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6176 - val_accuracy: 0.6264 - val_loss: 0.7478 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6150 - val_accuracy: 0.6193 - val_loss: 0.7462 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6719 - loss: 0.6237 - val_accuracy: 0.6135 - val_loss: 0.7582 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.6122 - val_accuracy: 0.6279 - val_loss: 0.7545 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6793 - loss: 0.6116 - val_accuracy: 0.6293 - val_loss: 0.7394 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6810 - loss: 0.6134 - val_accuracy: 0.6264 - val_loss: 0.7438 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6101 - val_accuracy: 0.6293 - val_loss: 0.7438 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6093 - val_accuracy: 0.6078 - val_loss: 0.7368 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6061 - val_accuracy: 0.6149 - val_loss: 0.7424 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6795 - loss: 0.6099 - val_accuracy: 0.6236 - val_loss: 0.7469 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5969 - val_accuracy: 0.6279 - val_loss: 0.7342 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6767 - loss: 0.6101 - val_accuracy: 0.6178 - val_loss: 0.7530 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6803 - loss: 0.6026 - val_accuracy: 0.6236 - val_loss: 0.7384 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6019 - val_accuracy: 0.6236 - val_loss: 0.7362 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.5976 - val_accuracy: 0.6293 - val_loss: 0.7420 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.5981 - val_accuracy: 0.6078 - val_loss: 0.7556 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.5901 - val_accuracy: 0.6250 - val_loss: 0.7389 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6955 - loss: 0.5942 - val_accuracy: 0.6379 - val_loss: 0.7358 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.5980 - val_accuracy: 0.6193 - val_loss: 0.7674 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6962 - loss: 0.5943 - val_accuracy: 0.6480 - val_loss: 0.7204 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5950 - val_accuracy: 0.6264 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5885 - val_accuracy: 0.6207 - val_loss: 0.7352 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.5949 - val_accuracy: 0.6307 - val_loss: 0.7521 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6930 - loss: 0.5857 - val_accuracy: 0.6408 - val_loss: 0.7229 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6973 - loss: 0.5913 - val_accuracy: 0.6092 - val_loss: 0.7393 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5952 - val_accuracy: 0.6078 - val_loss: 0.7616 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.5869 - val_accuracy: 0.6293 - val_loss: 0.7539 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.5862 - val_accuracy: 0.6336 - val_loss: 0.7548 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6990 - loss: 0.5765 - val_accuracy: 0.6322 - val_loss: 0.7239 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5794 - val_accuracy: 0.6451 - val_loss: 0.7366 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7001 - loss: 0.5810 - val_accuracy: 0.6365 - val_loss: 0.7252 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.6879 - loss: 0.5844 - val_accuracy: 0.6279 - val_loss: 0.7405 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5814 - val_accuracy: 0.6236 - val_loss: 0.7361 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5731 - val_accuracy: 0.6250 - val_loss: 0.7396 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5813 - val_accuracy: 0.6178 - val_loss: 0.7511 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5777 - val_accuracy: 0.6250 - val_loss: 0.7343 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5778 - val_accuracy: 0.6293 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5695 - val_accuracy: 0.6264 - val_loss: 0.7396 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7056 - loss: 0.5711 - val_accuracy: 0.6250 - val_loss: 0.7352 - learning_rate: 0.0010
Epoch 80/500

Epoch 80: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5619 - val_accuracy: 0.6178 - val_loss: 0.7507 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7229 - loss: 0.5406 - val_accuracy: 0.6293 - val_loss: 0.7389 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5375 - val_accuracy: 0.6307 - val_loss: 0.7330 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7208 - loss: 0.5365 - val_accuracy: 0.6379 - val_loss: 0.7226 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5292 - val_accuracy: 0.6351 - val_loss: 0.7187 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5345 - val_accuracy: 0.6250 - val_loss: 0.7399 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7206 - loss: 0.5414 - val_accuracy: 0.6351 - val_loss: 0.7372 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7312 - loss: 0.5291 - val_accuracy: 0.6379 - val_loss: 0.7295 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7292 - loss: 0.5297 - val_accuracy: 0.6264 - val_loss: 0.7286 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7325 - loss: 0.5316 - val_accuracy: 0.6307 - val_loss: 0.7398 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7284 - loss: 0.5249 - val_accuracy: 0.6351 - val_loss: 0.7321 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5243 - val_accuracy: 0.6322 - val_loss: 0.7427 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7307 - loss: 0.5265 - val_accuracy: 0.6336 - val_loss: 0.7205 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7284 - loss: 0.5330 - val_accuracy: 0.6307 - val_loss: 0.7380 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 24ms/step - accuracy: 0.7350 - loss: 0.5203 - val_accuracy: 0.6379 - val_loss: 0.7251 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7315 - loss: 0.5271 - val_accuracy: 0.6394 - val_loss: 0.7124 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7363 - loss: 0.5213 - val_accuracy: 0.6293 - val_loss: 0.7421 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7328 - loss: 0.5169 - val_accuracy: 0.6379 - val_loss: 0.7180 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7297 - loss: 0.5300 - val_accuracy: 0.6379 - val_loss: 0.7218 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7330 - loss: 0.5249 - val_accuracy: 0.6322 - val_loss: 0.7249 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7328 - loss: 0.5273 - val_accuracy: 0.6307 - val_loss: 0.7328 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7325 - loss: 0.5192 - val_accuracy: 0.6279 - val_loss: 0.7486 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5198 - val_accuracy: 0.6365 - val_loss: 0.7227 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7287 - loss: 0.5204 - val_accuracy: 0.6307 - val_loss: 0.7292 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5117 - val_accuracy: 0.6293 - val_loss: 0.7253 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7267 - loss: 0.5230 - val_accuracy: 0.6250 - val_loss: 0.7359 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7373 - loss: 0.5131 - val_accuracy: 0.6322 - val_loss: 0.7156 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5190 - val_accuracy: 0.6379 - val_loss: 0.7336 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7353 - loss: 0.5217 - val_accuracy: 0.6322 - val_loss: 0.7263 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7388 - loss: 0.5175 - val_accuracy: 0.6351 - val_loss: 0.7487 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7399 - loss: 0.5177 - val_accuracy: 0.6494 - val_loss: 0.7179 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7345 - loss: 0.5185 - val_accuracy: 0.6351 - val_loss: 0.7348 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7343 - loss: 0.5226 - val_accuracy: 0.6451 - val_loss: 0.7205 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7335 - loss: 0.5270 - val_accuracy: 0.6365 - val_loss: 0.7300 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7421 - loss: 0.5179 - val_accuracy: 0.6379 - val_loss: 0.7259 - learning_rate: 5.0000e-04
Epoch 115/500

Epoch 115: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7444 - loss: 0.5117 - val_accuracy: 0.6322 - val_loss: 0.7522 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7558 - loss: 0.5012 - val_accuracy: 0.6279 - val_loss: 0.7309 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7614 - loss: 0.4860 - val_accuracy: 0.6307 - val_loss: 0.7201 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4912 - val_accuracy: 0.6451 - val_loss: 0.7203 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7535 - loss: 0.4953 - val_accuracy: 0.6279 - val_loss: 0.7250 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.4865 - val_accuracy: 0.6379 - val_loss: 0.7290 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7518 - loss: 0.4941 - val_accuracy: 0.6379 - val_loss: 0.7277 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7515 - loss: 0.4896 - val_accuracy: 0.6408 - val_loss: 0.7131 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.4977 - val_accuracy: 0.6379 - val_loss: 0.7313 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.4959 - val_accuracy: 0.6466 - val_loss: 0.7220 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.4888 - val_accuracy: 0.6394 - val_loss: 0.7242 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7533 - loss: 0.4938 - val_accuracy: 0.6351 - val_loss: 0.7257 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4901 - val_accuracy: 0.6307 - val_loss: 0.7376 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4837 - val_accuracy: 0.6293 - val_loss: 0.7263 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7530 - loss: 0.4897 - val_accuracy: 0.6307 - val_loss: 0.7307 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4870 - val_accuracy: 0.6307 - val_loss: 0.7453 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 24ms/step - accuracy: 0.7508 - loss: 0.4935 - val_accuracy: 0.6279 - val_loss: 0.7386 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7574 - loss: 0.4864 - val_accuracy: 0.6279 - val_loss: 0.7420 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4834 - val_accuracy: 0.6422 - val_loss: 0.7240 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 24ms/step - accuracy: 0.7548 - loss: 0.4921 - val_accuracy: 0.6336 - val_loss: 0.7422 - learning_rate: 2.5000e-04
Epoch 135/500

Epoch 135: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.4827 - val_accuracy: 0.6437 - val_loss: 0.7292 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4795 - val_accuracy: 0.6379 - val_loss: 0.7105 - learning_rate: 1.2500e-04
Epoch 137/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4782 - val_accuracy: 0.6351 - val_loss: 0.7099 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7726 - loss: 0.4759 - val_accuracy: 0.6365 - val_loss: 0.7115 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 24ms/step - accuracy: 0.7551 - loss: 0.4810 - val_accuracy: 0.6293 - val_loss: 0.7287 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 24ms/step - accuracy: 0.7606 - loss: 0.4733 - val_accuracy: 0.6451 - val_loss: 0.7119 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 24ms/step - accuracy: 0.7660 - loss: 0.4768 - val_accuracy: 0.6336 - val_loss: 0.7193 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4802 - val_accuracy: 0.6365 - val_loss: 0.7155 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4782 - val_accuracy: 0.6466 - val_loss: 0.7214 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4785 - val_accuracy: 0.6351 - val_loss: 0.7220 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 24ms/step - accuracy: 0.7614 - loss: 0.4773 - val_accuracy: 0.6408 - val_loss: 0.7181 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 24ms/step - accuracy: 0.7677 - loss: 0.4765 - val_accuracy: 0.6451 - val_loss: 0.7169 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4712 - val_accuracy: 0.6365 - val_loss: 0.7208 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 24ms/step - accuracy: 0.7718 - loss: 0.4672 - val_accuracy: 0.6466 - val_loss: 0.7178 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 24ms/step - accuracy: 0.7606 - loss: 0.4775 - val_accuracy: 0.6351 - val_loss: 0.7241 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4803 - val_accuracy: 0.6437 - val_loss: 0.7244 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4755 - val_accuracy: 0.6466 - val_loss: 0.7197 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4730 - val_accuracy: 0.6480 - val_loss: 0.7159 - learning_rate: 1.2500e-04
Epoch 153/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4809 - val_accuracy: 0.6437 - val_loss: 0.7265 - learning_rate: 1.2500e-04
Epoch 154/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4688 - val_accuracy: 0.6379 - val_loss: 0.7281 - learning_rate: 1.2500e-04
Epoch 155/500
124/124 - 3s - 24ms/step - accuracy: 0.7690 - loss: 0.4645 - val_accuracy: 0.6494 - val_loss: 0.7160 - learning_rate: 1.2500e-04
Epoch 156/500
124/124 - 3s - 24ms/step - accuracy: 0.7698 - loss: 0.4708 - val_accuracy: 0.6494 - val_loss: 0.7195 - learning_rate: 1.2500e-04
Epoch 157/500

Epoch 157: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4740 - val_accuracy: 0.6394 - val_loss: 0.7227 - learning_rate: 1.2500e-04
Epoch 158/500
124/124 - 3s - 24ms/step - accuracy: 0.7759 - loss: 0.4620 - val_accuracy: 0.6394 - val_loss: 0.7176 - learning_rate: 6.2500e-05
Epoch 159/500
124/124 - 3s - 24ms/step - accuracy: 0.7634 - loss: 0.4747 - val_accuracy: 0.6394 - val_loss: 0.7132 - learning_rate: 6.2500e-05
Epoch 160/500
124/124 - 3s - 24ms/step - accuracy: 0.7748 - loss: 0.4655 - val_accuracy: 0.6379 - val_loss: 0.7246 - learning_rate: 6.2500e-05
Epoch 161/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4678 - val_accuracy: 0.6408 - val_loss: 0.7230 - learning_rate: 6.2500e-05
Epoch 162/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4680 - val_accuracy: 0.6351 - val_loss: 0.7174 - learning_rate: 6.2500e-05
Epoch 163/500
124/124 - 3s - 24ms/step - accuracy: 0.7672 - loss: 0.4717 - val_accuracy: 0.6351 - val_loss: 0.7178 - learning_rate: 6.2500e-05
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4575 - val_accuracy: 0.6365 - val_loss: 0.7186 - learning_rate: 6.2500e-05
Epoch 165/500
124/124 - 3s - 23ms/step - accuracy: 0.7672 - loss: 0.4686 - val_accuracy: 0.6336 - val_loss: 0.7219 - learning_rate: 6.2500e-05
Epoch 166/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4662 - val_accuracy: 0.6379 - val_loss: 0.7225 - learning_rate: 6.2500e-05
Epoch 167/500
124/124 - 3s - 24ms/step - accuracy: 0.7721 - loss: 0.4613 - val_accuracy: 0.6394 - val_loss: 0.7200 - learning_rate: 6.2500e-05
Epoch 168/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4674 - val_accuracy: 0.6307 - val_loss: 0.7179 - learning_rate: 6.2500e-05
Epoch 169/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4758 - val_accuracy: 0.6394 - val_loss: 0.7187 - learning_rate: 6.2500e-05
Epoch 170/500
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.4710 - val_accuracy: 0.6322 - val_loss: 0.7195 - learning_rate: 6.2500e-05
Epoch 171/500
124/124 - 3s - 24ms/step - accuracy: 0.7797 - loss: 0.4618 - val_accuracy: 0.6336 - val_loss: 0.7217 - learning_rate: 6.2500e-05
Epoch 172/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4595 - val_accuracy: 0.6480 - val_loss: 0.7176 - learning_rate: 6.2500e-05
Epoch 173/500
124/124 - 3s - 24ms/step - accuracy: 0.7703 - loss: 0.4653 - val_accuracy: 0.6365 - val_loss: 0.7249 - learning_rate: 6.2500e-05
Epoch 174/500
124/124 - 3s - 24ms/step - accuracy: 0.7642 - loss: 0.4711 - val_accuracy: 0.6336 - val_loss: 0.7211 - learning_rate: 6.2500e-05
Epoch 175/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4631 - val_accuracy: 0.6466 - val_loss: 0.7154 - learning_rate: 6.2500e-05
Epoch 176/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4662 - val_accuracy: 0.6365 - val_loss: 0.7200 - learning_rate: 6.2500e-05
Epoch 177/500

Epoch 177: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4698 - val_accuracy: 0.6466 - val_loss: 0.7153 - learning_rate: 6.2500e-05
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4610 - val_accuracy: 0.6466 - val_loss: 0.7139 - learning_rate: 3.1250e-05
Epoch 179/500
124/124 - 3s - 24ms/step - accuracy: 0.7721 - loss: 0.4683 - val_accuracy: 0.6451 - val_loss: 0.7163 - learning_rate: 3.1250e-05
Epoch 180/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4724 - val_accuracy: 0.6437 - val_loss: 0.7144 - learning_rate: 3.1250e-05
Epoch 181/500
124/124 - 3s - 24ms/step - accuracy: 0.7718 - loss: 0.4603 - val_accuracy: 0.6466 - val_loss: 0.7105 - learning_rate: 3.1250e-05
Epoch 182/500
124/124 - 3s - 24ms/step - accuracy: 0.7759 - loss: 0.4586 - val_accuracy: 0.6466 - val_loss: 0.7138 - learning_rate: 3.1250e-05
Epoch 183/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4583 - val_accuracy: 0.6509 - val_loss: 0.7153 - learning_rate: 3.1250e-05
Epoch 184/500
124/124 - 3s - 24ms/step - accuracy: 0.7695 - loss: 0.4611 - val_accuracy: 0.6509 - val_loss: 0.7123 - learning_rate: 3.1250e-05
Epoch 185/500
124/124 - 3s - 24ms/step - accuracy: 0.7756 - loss: 0.4604 - val_accuracy: 0.6466 - val_loss: 0.7122 - learning_rate: 3.1250e-05
Epoch 186/500
124/124 - 3s - 24ms/step - accuracy: 0.7776 - loss: 0.4627 - val_accuracy: 0.6509 - val_loss: 0.7133 - learning_rate: 3.1250e-05
Epoch 187/500
124/124 - 3s - 24ms/step - accuracy: 0.7804 - loss: 0.4607 - val_accuracy: 0.6509 - val_loss: 0.7120 - learning_rate: 3.1250e-05
Epoch 187: early stopping
Restoring model weights from the end of the best epoch: 137.
Training complete. Best epoch: 137 of 187. Best val_loss: 0.7099, val_accuracy: 0.6351

========== Evaluation: LOSO fold 23 / held-out EMS0024 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        31         8         1
  intermedia        31        38        11
  max_intens         0         6        34

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.500     0.775     0.608        40
intermediate_intensity      0.731     0.475     0.576        80
         max_intensity      0.739     0.850     0.791        40

              accuracy                          0.644       160
             macro avg      0.657     0.700     0.658       160
          weighted avg      0.675     0.644     0.638       160

Overall accuracy: 0.6438

============================================================
Fold 24 of 30: holding out EMS0025
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.28e-07, 9.59e-07]
  Per-channel std range:  [7.27e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 121ms/step - accuracy: 0.4533 - loss: 1.0289 - val_accuracy: 0.4511 - val_loss: 1.0435 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5325 - loss: 0.9009 - val_accuracy: 0.5014 - val_loss: 0.9568 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5659 - loss: 0.8392 - val_accuracy: 0.5374 - val_loss: 0.9055 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5827 - loss: 0.8089 - val_accuracy: 0.5575 - val_loss: 0.8794 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5898 - loss: 0.7883 - val_accuracy: 0.5675 - val_loss: 0.8495 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.6085 - loss: 0.7720 - val_accuracy: 0.5747 - val_loss: 0.8394 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 25ms/step - accuracy: 0.6133 - loss: 0.7595 - val_accuracy: 0.6078 - val_loss: 0.8361 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 25ms/step - accuracy: 0.6159 - loss: 0.7462 - val_accuracy: 0.5963 - val_loss: 0.8233 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 25ms/step - accuracy: 0.6131 - loss: 0.7375 - val_accuracy: 0.5848 - val_loss: 0.8219 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6258 - loss: 0.7251 - val_accuracy: 0.5948 - val_loss: 0.8155 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6311 - loss: 0.7128 - val_accuracy: 0.5920 - val_loss: 0.8123 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 25ms/step - accuracy: 0.6301 - loss: 0.7112 - val_accuracy: 0.6049 - val_loss: 0.8034 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 25ms/step - accuracy: 0.6395 - loss: 0.7037 - val_accuracy: 0.6020 - val_loss: 0.8004 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6468 - loss: 0.6917 - val_accuracy: 0.6149 - val_loss: 0.7898 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6417 - loss: 0.6915 - val_accuracy: 0.5948 - val_loss: 0.7962 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6491 - loss: 0.6861 - val_accuracy: 0.6135 - val_loss: 0.7869 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6509 - loss: 0.6824 - val_accuracy: 0.6121 - val_loss: 0.8005 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6481 - loss: 0.6788 - val_accuracy: 0.6063 - val_loss: 0.7880 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6450 - loss: 0.6720 - val_accuracy: 0.6092 - val_loss: 0.7753 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6521 - loss: 0.6703 - val_accuracy: 0.6164 - val_loss: 0.7810 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6625 - loss: 0.6644 - val_accuracy: 0.6034 - val_loss: 0.7905 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6552 - loss: 0.6597 - val_accuracy: 0.6250 - val_loss: 0.7671 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6613 - loss: 0.6587 - val_accuracy: 0.6149 - val_loss: 0.7850 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6600 - loss: 0.6553 - val_accuracy: 0.6336 - val_loss: 0.7650 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 24ms/step - accuracy: 0.6686 - loss: 0.6436 - val_accuracy: 0.6178 - val_loss: 0.7844 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6691 - loss: 0.6427 - val_accuracy: 0.6207 - val_loss: 0.7675 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6661 - loss: 0.6465 - val_accuracy: 0.6178 - val_loss: 0.7753 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6666 - loss: 0.6429 - val_accuracy: 0.6322 - val_loss: 0.7732 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6747 - loss: 0.6326 - val_accuracy: 0.6365 - val_loss: 0.7677 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6696 - loss: 0.6393 - val_accuracy: 0.6365 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 24ms/step - accuracy: 0.6701 - loss: 0.6387 - val_accuracy: 0.6106 - val_loss: 0.7746 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 24ms/step - accuracy: 0.6666 - loss: 0.6369 - val_accuracy: 0.6322 - val_loss: 0.7617 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6694 - loss: 0.6303 - val_accuracy: 0.6279 - val_loss: 0.7538 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6760 - loss: 0.6237 - val_accuracy: 0.6264 - val_loss: 0.7569 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6760 - loss: 0.6312 - val_accuracy: 0.6408 - val_loss: 0.7533 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6749 - loss: 0.6245 - val_accuracy: 0.6422 - val_loss: 0.7449 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 25ms/step - accuracy: 0.6782 - loss: 0.6217 - val_accuracy: 0.6494 - val_loss: 0.7433 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.6169 - val_accuracy: 0.6394 - val_loss: 0.7490 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6755 - loss: 0.6132 - val_accuracy: 0.6365 - val_loss: 0.7465 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6793 - loss: 0.6191 - val_accuracy: 0.6480 - val_loss: 0.7358 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6914 - loss: 0.6094 - val_accuracy: 0.6336 - val_loss: 0.7670 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.6169 - val_accuracy: 0.6164 - val_loss: 0.7650 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6800 - loss: 0.6169 - val_accuracy: 0.6566 - val_loss: 0.7410 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6803 - loss: 0.6091 - val_accuracy: 0.6379 - val_loss: 0.7559 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.6089 - val_accuracy: 0.6279 - val_loss: 0.7564 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6902 - loss: 0.6057 - val_accuracy: 0.6193 - val_loss: 0.7563 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6940 - loss: 0.5968 - val_accuracy: 0.6408 - val_loss: 0.7642 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6813 - loss: 0.6077 - val_accuracy: 0.6365 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6955 - loss: 0.5985 - val_accuracy: 0.6178 - val_loss: 0.7637 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.6044 - val_accuracy: 0.6121 - val_loss: 0.7622 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.6930 - loss: 0.6032 - val_accuracy: 0.6078 - val_loss: 0.7587 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 24ms/step - accuracy: 0.6973 - loss: 0.6026 - val_accuracy: 0.6422 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6940 - loss: 0.6033 - val_accuracy: 0.6164 - val_loss: 0.7700 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6927 - loss: 0.5894 - val_accuracy: 0.6264 - val_loss: 0.7626 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 24ms/step - accuracy: 0.6924 - loss: 0.5961 - val_accuracy: 0.6394 - val_loss: 0.7445 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 24ms/step - accuracy: 0.6940 - loss: 0.5991 - val_accuracy: 0.6236 - val_loss: 0.7556 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.6950 - loss: 0.5914 - val_accuracy: 0.6379 - val_loss: 0.7476 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 24ms/step - accuracy: 0.7018 - loss: 0.5930 - val_accuracy: 0.6422 - val_loss: 0.7482 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 24ms/step - accuracy: 0.6927 - loss: 0.5850 - val_accuracy: 0.6193 - val_loss: 0.7683 - learning_rate: 0.0010
Epoch 60/500

Epoch 60: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 24ms/step - accuracy: 0.7001 - loss: 0.5949 - val_accuracy: 0.6379 - val_loss: 0.7515 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.7173 - loss: 0.5622 - val_accuracy: 0.6149 - val_loss: 0.7665 - learning_rate: 5.0000e-04
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.7282 - loss: 0.5448 - val_accuracy: 0.6121 - val_loss: 0.7554 - learning_rate: 5.0000e-04
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.7216 - loss: 0.5500 - val_accuracy: 0.6250 - val_loss: 0.7526 - learning_rate: 5.0000e-04
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7188 - loss: 0.5523 - val_accuracy: 0.6365 - val_loss: 0.7484 - learning_rate: 5.0000e-04
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.7198 - loss: 0.5444 - val_accuracy: 0.6307 - val_loss: 0.7620 - learning_rate: 5.0000e-04
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.7264 - loss: 0.5488 - val_accuracy: 0.6351 - val_loss: 0.7455 - learning_rate: 5.0000e-04
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.7249 - loss: 0.5476 - val_accuracy: 0.6264 - val_loss: 0.7476 - learning_rate: 5.0000e-04
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.7193 - loss: 0.5506 - val_accuracy: 0.6063 - val_loss: 0.7765 - learning_rate: 5.0000e-04
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.7231 - loss: 0.5439 - val_accuracy: 0.6135 - val_loss: 0.7729 - learning_rate: 5.0000e-04
Epoch 70/500
124/124 - 3s - 24ms/step - accuracy: 0.7305 - loss: 0.5449 - val_accuracy: 0.6221 - val_loss: 0.7596 - learning_rate: 5.0000e-04
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.7170 - loss: 0.5480 - val_accuracy: 0.6307 - val_loss: 0.7414 - learning_rate: 5.0000e-04
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.7236 - loss: 0.5423 - val_accuracy: 0.6394 - val_loss: 0.7374 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7269 - loss: 0.5359 - val_accuracy: 0.6264 - val_loss: 0.7480 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7203 - loss: 0.5436 - val_accuracy: 0.6121 - val_loss: 0.7739 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7302 - loss: 0.5395 - val_accuracy: 0.6365 - val_loss: 0.7456 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7246 - loss: 0.5381 - val_accuracy: 0.6264 - val_loss: 0.7510 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7246 - loss: 0.5375 - val_accuracy: 0.6351 - val_loss: 0.7371 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7244 - loss: 0.5405 - val_accuracy: 0.6279 - val_loss: 0.7562 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7295 - loss: 0.5378 - val_accuracy: 0.6422 - val_loss: 0.7342 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7272 - loss: 0.5359 - val_accuracy: 0.6221 - val_loss: 0.7555 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5396 - val_accuracy: 0.6437 - val_loss: 0.7414 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7219 - loss: 0.5339 - val_accuracy: 0.6236 - val_loss: 0.7511 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5281 - val_accuracy: 0.6351 - val_loss: 0.7452 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7305 - loss: 0.5402 - val_accuracy: 0.6236 - val_loss: 0.7648 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7368 - loss: 0.5305 - val_accuracy: 0.6379 - val_loss: 0.7392 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7274 - loss: 0.5281 - val_accuracy: 0.6307 - val_loss: 0.7460 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7358 - loss: 0.5306 - val_accuracy: 0.6379 - val_loss: 0.7379 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7366 - loss: 0.5265 - val_accuracy: 0.6279 - val_loss: 0.7475 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7320 - loss: 0.5267 - val_accuracy: 0.6307 - val_loss: 0.7430 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7317 - loss: 0.5320 - val_accuracy: 0.6236 - val_loss: 0.7567 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7277 - loss: 0.5362 - val_accuracy: 0.6336 - val_loss: 0.7466 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7401 - loss: 0.5287 - val_accuracy: 0.6351 - val_loss: 0.7427 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7348 - loss: 0.5278 - val_accuracy: 0.6379 - val_loss: 0.7377 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7297 - loss: 0.5280 - val_accuracy: 0.6552 - val_loss: 0.7279 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7343 - loss: 0.5253 - val_accuracy: 0.6307 - val_loss: 0.7397 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7305 - loss: 0.5299 - val_accuracy: 0.6408 - val_loss: 0.7386 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7257 - loss: 0.5292 - val_accuracy: 0.6149 - val_loss: 0.7638 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5356 - val_accuracy: 0.6336 - val_loss: 0.7393 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5173 - val_accuracy: 0.6408 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5235 - val_accuracy: 0.6307 - val_loss: 0.7400 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5230 - val_accuracy: 0.6379 - val_loss: 0.7377 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7338 - loss: 0.5274 - val_accuracy: 0.6394 - val_loss: 0.7380 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7406 - loss: 0.5190 - val_accuracy: 0.6336 - val_loss: 0.7487 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5242 - val_accuracy: 0.6523 - val_loss: 0.7363 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7361 - loss: 0.5216 - val_accuracy: 0.6322 - val_loss: 0.7414 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5222 - val_accuracy: 0.6178 - val_loss: 0.7644 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5265 - val_accuracy: 0.6437 - val_loss: 0.7317 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.5218 - val_accuracy: 0.6408 - val_loss: 0.7389 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5143 - val_accuracy: 0.6480 - val_loss: 0.7360 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5141 - val_accuracy: 0.6523 - val_loss: 0.7407 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5205 - val_accuracy: 0.6221 - val_loss: 0.7629 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7338 - loss: 0.5273 - val_accuracy: 0.6221 - val_loss: 0.7547 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7409 - loss: 0.5170 - val_accuracy: 0.6351 - val_loss: 0.7555 - learning_rate: 5.0000e-04
Epoch 114/500

Epoch 114: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7376 - loss: 0.5144 - val_accuracy: 0.6322 - val_loss: 0.7374 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7480 - loss: 0.5036 - val_accuracy: 0.6322 - val_loss: 0.7426 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.4927 - val_accuracy: 0.6279 - val_loss: 0.7457 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.4969 - val_accuracy: 0.6250 - val_loss: 0.7473 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7563 - loss: 0.4893 - val_accuracy: 0.6408 - val_loss: 0.7483 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.4965 - val_accuracy: 0.6178 - val_loss: 0.7514 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7647 - loss: 0.4935 - val_accuracy: 0.6365 - val_loss: 0.7449 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7563 - loss: 0.4959 - val_accuracy: 0.6408 - val_loss: 0.7409 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7558 - loss: 0.4927 - val_accuracy: 0.6307 - val_loss: 0.7510 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.4903 - val_accuracy: 0.6264 - val_loss: 0.7439 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7520 - loss: 0.4963 - val_accuracy: 0.6336 - val_loss: 0.7457 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7543 - loss: 0.4938 - val_accuracy: 0.6221 - val_loss: 0.7585 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7510 - loss: 0.4937 - val_accuracy: 0.6322 - val_loss: 0.7440 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7538 - loss: 0.4964 - val_accuracy: 0.6307 - val_loss: 0.7506 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7528 - loss: 0.4909 - val_accuracy: 0.6322 - val_loss: 0.7434 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 24ms/step - accuracy: 0.7601 - loss: 0.4872 - val_accuracy: 0.6307 - val_loss: 0.7468 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7551 - loss: 0.4890 - val_accuracy: 0.6250 - val_loss: 0.7516 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 24ms/step - accuracy: 0.7650 - loss: 0.4856 - val_accuracy: 0.6408 - val_loss: 0.7415 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7574 - loss: 0.4929 - val_accuracy: 0.6379 - val_loss: 0.7380 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7561 - loss: 0.4925 - val_accuracy: 0.6236 - val_loss: 0.7452 - learning_rate: 2.5000e-04
Epoch 134/500

Epoch 134: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7563 - loss: 0.4904 - val_accuracy: 0.6322 - val_loss: 0.7472 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4865 - val_accuracy: 0.6451 - val_loss: 0.7305 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4840 - val_accuracy: 0.6451 - val_loss: 0.7328 - learning_rate: 1.2500e-04
Epoch 137/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4770 - val_accuracy: 0.6351 - val_loss: 0.7345 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7708 - loss: 0.4737 - val_accuracy: 0.6509 - val_loss: 0.7320 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4712 - val_accuracy: 0.6408 - val_loss: 0.7320 - learning_rate: 1.2500e-04
Epoch 140/500
124/124 - 3s - 24ms/step - accuracy: 0.7761 - loss: 0.4686 - val_accuracy: 0.6624 - val_loss: 0.7240 - learning_rate: 1.2500e-04
Epoch 141/500
124/124 - 3s - 24ms/step - accuracy: 0.7710 - loss: 0.4674 - val_accuracy: 0.6480 - val_loss: 0.7314 - learning_rate: 1.2500e-04
Epoch 142/500
124/124 - 3s - 24ms/step - accuracy: 0.7667 - loss: 0.4729 - val_accuracy: 0.6566 - val_loss: 0.7238 - learning_rate: 1.2500e-04
Epoch 143/500
124/124 - 3s - 24ms/step - accuracy: 0.7642 - loss: 0.4778 - val_accuracy: 0.6523 - val_loss: 0.7277 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4775 - val_accuracy: 0.6351 - val_loss: 0.7433 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4704 - val_accuracy: 0.6566 - val_loss: 0.7245 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 24ms/step - accuracy: 0.7642 - loss: 0.4777 - val_accuracy: 0.6394 - val_loss: 0.7353 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 24ms/step - accuracy: 0.7680 - loss: 0.4733 - val_accuracy: 0.6494 - val_loss: 0.7294 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4736 - val_accuracy: 0.6451 - val_loss: 0.7408 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4766 - val_accuracy: 0.6394 - val_loss: 0.7360 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 24ms/step - accuracy: 0.7645 - loss: 0.4766 - val_accuracy: 0.6408 - val_loss: 0.7326 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4740 - val_accuracy: 0.6480 - val_loss: 0.7300 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 24ms/step - accuracy: 0.7594 - loss: 0.4817 - val_accuracy: 0.6394 - val_loss: 0.7396 - learning_rate: 1.2500e-04
Epoch 153/500
124/124 - 3s - 24ms/step - accuracy: 0.7639 - loss: 0.4814 - val_accuracy: 0.6451 - val_loss: 0.7341 - learning_rate: 1.2500e-04
Epoch 154/500
124/124 - 3s - 24ms/step - accuracy: 0.7685 - loss: 0.4769 - val_accuracy: 0.6537 - val_loss: 0.7310 - learning_rate: 1.2500e-04
Epoch 155/500
124/124 - 3s - 24ms/step - accuracy: 0.7703 - loss: 0.4762 - val_accuracy: 0.6509 - val_loss: 0.7276 - learning_rate: 1.2500e-04
Epoch 156/500
124/124 - 3s - 24ms/step - accuracy: 0.7708 - loss: 0.4768 - val_accuracy: 0.6394 - val_loss: 0.7379 - learning_rate: 1.2500e-04
Epoch 157/500
124/124 - 3s - 24ms/step - accuracy: 0.7617 - loss: 0.4757 - val_accuracy: 0.6537 - val_loss: 0.7273 - learning_rate: 1.2500e-04
Epoch 158/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4795 - val_accuracy: 0.6437 - val_loss: 0.7329 - learning_rate: 1.2500e-04
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4689 - val_accuracy: 0.6394 - val_loss: 0.7377 - learning_rate: 1.2500e-04
Epoch 160/500
124/124 - 3s - 24ms/step - accuracy: 0.7703 - loss: 0.4709 - val_accuracy: 0.6566 - val_loss: 0.7292 - learning_rate: 1.2500e-04
Epoch 161/500
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4778 - val_accuracy: 0.6351 - val_loss: 0.7433 - learning_rate: 1.2500e-04
Epoch 162/500

Epoch 162: ReduceLROnPlateau reducing learning rate to 6.25000029685907e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4724 - val_accuracy: 0.6537 - val_loss: 0.7322 - learning_rate: 1.2500e-04
Epoch 163/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4679 - val_accuracy: 0.6566 - val_loss: 0.7298 - learning_rate: 6.2500e-05
Epoch 164/500
124/124 - 3s - 24ms/step - accuracy: 0.7685 - loss: 0.4666 - val_accuracy: 0.6667 - val_loss: 0.7242 - learning_rate: 6.2500e-05
Epoch 165/500
124/124 - 3s - 24ms/step - accuracy: 0.7748 - loss: 0.4660 - val_accuracy: 0.6638 - val_loss: 0.7283 - learning_rate: 6.2500e-05
Epoch 166/500
124/124 - 3s - 24ms/step - accuracy: 0.7787 - loss: 0.4644 - val_accuracy: 0.6609 - val_loss: 0.7291 - learning_rate: 6.2500e-05
Epoch 167/500
124/124 - 3s - 24ms/step - accuracy: 0.7713 - loss: 0.4724 - val_accuracy: 0.6566 - val_loss: 0.7282 - learning_rate: 6.2500e-05
Epoch 168/500
124/124 - 3s - 24ms/step - accuracy: 0.7741 - loss: 0.4627 - val_accuracy: 0.6580 - val_loss: 0.7292 - learning_rate: 6.2500e-05
Epoch 169/500
124/124 - 3s - 24ms/step - accuracy: 0.7708 - loss: 0.4664 - val_accuracy: 0.6595 - val_loss: 0.7312 - learning_rate: 6.2500e-05
Epoch 170/500
124/124 - 3s - 24ms/step - accuracy: 0.7713 - loss: 0.4615 - val_accuracy: 0.6480 - val_loss: 0.7355 - learning_rate: 6.2500e-05
Epoch 171/500
124/124 - 3s - 24ms/step - accuracy: 0.7705 - loss: 0.4697 - val_accuracy: 0.6595 - val_loss: 0.7262 - learning_rate: 6.2500e-05
Epoch 172/500
124/124 - 3s - 24ms/step - accuracy: 0.7721 - loss: 0.4657 - val_accuracy: 0.6523 - val_loss: 0.7296 - learning_rate: 6.2500e-05
Epoch 173/500
124/124 - 3s - 24ms/step - accuracy: 0.7650 - loss: 0.4701 - val_accuracy: 0.6580 - val_loss: 0.7299 - learning_rate: 6.2500e-05
Epoch 174/500
124/124 - 3s - 24ms/step - accuracy: 0.7660 - loss: 0.4706 - val_accuracy: 0.6624 - val_loss: 0.7277 - learning_rate: 6.2500e-05
Epoch 175/500
124/124 - 3s - 24ms/step - accuracy: 0.7710 - loss: 0.4627 - val_accuracy: 0.6652 - val_loss: 0.7294 - learning_rate: 6.2500e-05
Epoch 176/500
124/124 - 3s - 24ms/step - accuracy: 0.7769 - loss: 0.4568 - val_accuracy: 0.6638 - val_loss: 0.7275 - learning_rate: 6.2500e-05
Epoch 177/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4702 - val_accuracy: 0.6451 - val_loss: 0.7368 - learning_rate: 6.2500e-05
Epoch 178/500
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4617 - val_accuracy: 0.6537 - val_loss: 0.7336 - learning_rate: 6.2500e-05
Epoch 179/500
124/124 - 3s - 23ms/step - accuracy: 0.7685 - loss: 0.4727 - val_accuracy: 0.6552 - val_loss: 0.7370 - learning_rate: 6.2500e-05
Epoch 180/500
124/124 - 3s - 24ms/step - accuracy: 0.7660 - loss: 0.4676 - val_accuracy: 0.6609 - val_loss: 0.7313 - learning_rate: 6.2500e-05
Epoch 181/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4745 - val_accuracy: 0.6609 - val_loss: 0.7245 - learning_rate: 6.2500e-05
Epoch 182/500

Epoch 182: ReduceLROnPlateau reducing learning rate to 3.125000148429535e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7705 - loss: 0.4668 - val_accuracy: 0.6552 - val_loss: 0.7336 - learning_rate: 6.2500e-05
Epoch 183/500
124/124 - 3s - 24ms/step - accuracy: 0.7645 - loss: 0.4703 - val_accuracy: 0.6595 - val_loss: 0.7269 - learning_rate: 3.1250e-05
Epoch 184/500
124/124 - 3s - 24ms/step - accuracy: 0.7837 - loss: 0.4578 - val_accuracy: 0.6624 - val_loss: 0.7247 - learning_rate: 3.1250e-05
Epoch 185/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4654 - val_accuracy: 0.6537 - val_loss: 0.7271 - learning_rate: 3.1250e-05
Epoch 186/500
124/124 - 3s - 24ms/step - accuracy: 0.7703 - loss: 0.4689 - val_accuracy: 0.6624 - val_loss: 0.7263 - learning_rate: 3.1250e-05
Epoch 187/500
124/124 - 3s - 24ms/step - accuracy: 0.7721 - loss: 0.4672 - val_accuracy: 0.6624 - val_loss: 0.7259 - learning_rate: 3.1250e-05
Epoch 188/500
124/124 - 3s - 24ms/step - accuracy: 0.7693 - loss: 0.4691 - val_accuracy: 0.6624 - val_loss: 0.7255 - learning_rate: 3.1250e-05
Epoch 189/500
124/124 - 3s - 24ms/step - accuracy: 0.7705 - loss: 0.4701 - val_accuracy: 0.6638 - val_loss: 0.7190 - learning_rate: 3.1250e-05
Epoch 190/500
124/124 - 3s - 24ms/step - accuracy: 0.7670 - loss: 0.4726 - val_accuracy: 0.6609 - val_loss: 0.7237 - learning_rate: 3.1250e-05
Epoch 191/500
124/124 - 3s - 24ms/step - accuracy: 0.7738 - loss: 0.4625 - val_accuracy: 0.6595 - val_loss: 0.7259 - learning_rate: 3.1250e-05
Epoch 192/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4632 - val_accuracy: 0.6537 - val_loss: 0.7279 - learning_rate: 3.1250e-05
Epoch 193/500
124/124 - 3s - 24ms/step - accuracy: 0.7695 - loss: 0.4649 - val_accuracy: 0.6609 - val_loss: 0.7240 - learning_rate: 3.1250e-05
Epoch 194/500
124/124 - 3s - 24ms/step - accuracy: 0.7695 - loss: 0.4617 - val_accuracy: 0.6609 - val_loss: 0.7214 - learning_rate: 3.1250e-05
Epoch 195/500
124/124 - 3s - 24ms/step - accuracy: 0.7685 - loss: 0.4600 - val_accuracy: 0.6624 - val_loss: 0.7215 - learning_rate: 3.1250e-05
Epoch 196/500
124/124 - 3s - 24ms/step - accuracy: 0.7733 - loss: 0.4684 - val_accuracy: 0.6609 - val_loss: 0.7231 - learning_rate: 3.1250e-05
Epoch 197/500
124/124 - 3s - 24ms/step - accuracy: 0.7655 - loss: 0.4675 - val_accuracy: 0.6638 - val_loss: 0.7211 - learning_rate: 3.1250e-05
Epoch 198/500
124/124 - 3s - 24ms/step - accuracy: 0.7743 - loss: 0.4711 - val_accuracy: 0.6624 - val_loss: 0.7257 - learning_rate: 3.1250e-05
Epoch 199/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4629 - val_accuracy: 0.6595 - val_loss: 0.7234 - learning_rate: 3.1250e-05
Epoch 200/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4691 - val_accuracy: 0.6624 - val_loss: 0.7264 - learning_rate: 3.1250e-05
Epoch 201/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4624 - val_accuracy: 0.6638 - val_loss: 0.7211 - learning_rate: 3.1250e-05
Epoch 202/500
124/124 - 3s - 24ms/step - accuracy: 0.7670 - loss: 0.4641 - val_accuracy: 0.6652 - val_loss: 0.7224 - learning_rate: 3.1250e-05
Epoch 203/500
124/124 - 3s - 24ms/step - accuracy: 0.7764 - loss: 0.4632 - val_accuracy: 0.6624 - val_loss: 0.7256 - learning_rate: 3.1250e-05
Epoch 204/500
124/124 - 3s - 24ms/step - accuracy: 0.7787 - loss: 0.4594 - val_accuracy: 0.6667 - val_loss: 0.7238 - learning_rate: 3.1250e-05
Epoch 205/500
124/124 - 3s - 24ms/step - accuracy: 0.7781 - loss: 0.4642 - val_accuracy: 0.6638 - val_loss: 0.7248 - learning_rate: 3.1250e-05
Epoch 206/500
124/124 - 3s - 24ms/step - accuracy: 0.7751 - loss: 0.4660 - val_accuracy: 0.6652 - val_loss: 0.7252 - learning_rate: 3.1250e-05
Epoch 207/500
124/124 - 3s - 23ms/step - accuracy: 0.7733 - loss: 0.4733 - val_accuracy: 0.6609 - val_loss: 0.7244 - learning_rate: 3.1250e-05
Epoch 208/500
124/124 - 3s - 24ms/step - accuracy: 0.7733 - loss: 0.4615 - val_accuracy: 0.6609 - val_loss: 0.7262 - learning_rate: 3.1250e-05
Epoch 209/500

Epoch 209: ReduceLROnPlateau reducing learning rate to 1.5625000742147677e-05.
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4648 - val_accuracy: 0.6652 - val_loss: 0.7247 - learning_rate: 3.1250e-05
Epoch 210/500
124/124 - 3s - 25ms/step - accuracy: 0.7741 - loss: 0.4605 - val_accuracy: 0.6652 - val_loss: 0.7179 - learning_rate: 1.5625e-05
Epoch 211/500
124/124 - 3s - 24ms/step - accuracy: 0.7716 - loss: 0.4655 - val_accuracy: 0.6652 - val_loss: 0.7209 - learning_rate: 1.5625e-05
Epoch 212/500
124/124 - 3s - 24ms/step - accuracy: 0.7723 - loss: 0.4539 - val_accuracy: 0.6609 - val_loss: 0.7202 - learning_rate: 1.5625e-05
Epoch 213/500
124/124 - 3s - 24ms/step - accuracy: 0.7731 - loss: 0.4606 - val_accuracy: 0.6652 - val_loss: 0.7182 - learning_rate: 1.5625e-05
Epoch 214/500
124/124 - 3s - 24ms/step - accuracy: 0.7705 - loss: 0.4703 - val_accuracy: 0.6652 - val_loss: 0.7193 - learning_rate: 1.5625e-05
Epoch 215/500
124/124 - 3s - 24ms/step - accuracy: 0.7688 - loss: 0.4600 - val_accuracy: 0.6667 - val_loss: 0.7193 - learning_rate: 1.5625e-05
Epoch 216/500
124/124 - 3s - 24ms/step - accuracy: 0.7792 - loss: 0.4551 - val_accuracy: 0.6638 - val_loss: 0.7185 - learning_rate: 1.5625e-05
Epoch 217/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4578 - val_accuracy: 0.6609 - val_loss: 0.7213 - learning_rate: 1.5625e-05
Epoch 218/500
124/124 - 3s - 24ms/step - accuracy: 0.7731 - loss: 0.4620 - val_accuracy: 0.6638 - val_loss: 0.7202 - learning_rate: 1.5625e-05
Epoch 219/500
124/124 - 3s - 24ms/step - accuracy: 0.7776 - loss: 0.4627 - val_accuracy: 0.6652 - val_loss: 0.7196 - learning_rate: 1.5625e-05
Epoch 220/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4658 - val_accuracy: 0.6609 - val_loss: 0.7228 - learning_rate: 1.5625e-05
Epoch 221/500
124/124 - 3s - 24ms/step - accuracy: 0.7769 - loss: 0.4568 - val_accuracy: 0.6652 - val_loss: 0.7205 - learning_rate: 1.5625e-05
Epoch 222/500
124/124 - 3s - 24ms/step - accuracy: 0.7748 - loss: 0.4566 - val_accuracy: 0.6609 - val_loss: 0.7203 - learning_rate: 1.5625e-05
Epoch 223/500
124/124 - 3s - 24ms/step - accuracy: 0.7789 - loss: 0.4579 - val_accuracy: 0.6652 - val_loss: 0.7203 - learning_rate: 1.5625e-05
Epoch 224/500
124/124 - 3s - 24ms/step - accuracy: 0.7660 - loss: 0.4655 - val_accuracy: 0.6638 - val_loss: 0.7213 - learning_rate: 1.5625e-05
Epoch 225/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4577 - val_accuracy: 0.6624 - val_loss: 0.7219 - learning_rate: 1.5625e-05
Epoch 226/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4638 - val_accuracy: 0.6667 - val_loss: 0.7231 - learning_rate: 1.5625e-05
Epoch 227/500
124/124 - 3s - 24ms/step - accuracy: 0.7779 - loss: 0.4585 - val_accuracy: 0.6667 - val_loss: 0.7176 - learning_rate: 1.5625e-05
Epoch 228/500
124/124 - 3s - 24ms/step - accuracy: 0.7776 - loss: 0.4549 - val_accuracy: 0.6681 - val_loss: 0.7206 - learning_rate: 1.5625e-05
Epoch 229/500
124/124 - 3s - 24ms/step - accuracy: 0.7807 - loss: 0.4555 - val_accuracy: 0.6638 - val_loss: 0.7209 - learning_rate: 1.5625e-05
Epoch 230/500
124/124 - 3s - 24ms/step - accuracy: 0.7756 - loss: 0.4547 - val_accuracy: 0.6624 - val_loss: 0.7198 - learning_rate: 1.5625e-05
Epoch 231/500
124/124 - 3s - 24ms/step - accuracy: 0.7794 - loss: 0.4636 - val_accuracy: 0.6609 - val_loss: 0.7201 - learning_rate: 1.5625e-05
Epoch 232/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4631 - val_accuracy: 0.6609 - val_loss: 0.7217 - learning_rate: 1.5625e-05
Epoch 233/500
124/124 - 3s - 24ms/step - accuracy: 0.7751 - loss: 0.4618 - val_accuracy: 0.6624 - val_loss: 0.7210 - learning_rate: 1.5625e-05
Epoch 234/500
124/124 - 3s - 24ms/step - accuracy: 0.7751 - loss: 0.4540 - val_accuracy: 0.6667 - val_loss: 0.7180 - learning_rate: 1.5625e-05
Epoch 235/500
124/124 - 3s - 24ms/step - accuracy: 0.7748 - loss: 0.4591 - val_accuracy: 0.6638 - val_loss: 0.7193 - learning_rate: 1.5625e-05
Epoch 236/500
124/124 - 3s - 24ms/step - accuracy: 0.7746 - loss: 0.4678 - val_accuracy: 0.6667 - val_loss: 0.7214 - learning_rate: 1.5625e-05
Epoch 237/500
124/124 - 3s - 23ms/step - accuracy: 0.7814 - loss: 0.4572 - val_accuracy: 0.6667 - val_loss: 0.7186 - learning_rate: 1.5625e-05
Epoch 238/500
124/124 - 3s - 23ms/step - accuracy: 0.7624 - loss: 0.4662 - val_accuracy: 0.6695 - val_loss: 0.7189 - learning_rate: 1.5625e-05
Epoch 239/500
124/124 - 3s - 23ms/step - accuracy: 0.7748 - loss: 0.4654 - val_accuracy: 0.6695 - val_loss: 0.7196 - learning_rate: 1.5625e-05
Epoch 240/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4671 - val_accuracy: 0.6681 - val_loss: 0.7210 - learning_rate: 1.5625e-05
Epoch 241/500
124/124 - 3s - 23ms/step - accuracy: 0.7807 - loss: 0.4533 - val_accuracy: 0.6695 - val_loss: 0.7208 - learning_rate: 1.5625e-05
Epoch 242/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4667 - val_accuracy: 0.6667 - val_loss: 0.7233 - learning_rate: 1.5625e-05
Epoch 243/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4622 - val_accuracy: 0.6724 - val_loss: 0.7191 - learning_rate: 1.5625e-05
Epoch 244/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4595 - val_accuracy: 0.6724 - val_loss: 0.7189 - learning_rate: 1.5625e-05
Epoch 245/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4597 - val_accuracy: 0.6695 - val_loss: 0.7201 - learning_rate: 1.5625e-05
Epoch 246/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4588 - val_accuracy: 0.6681 - val_loss: 0.7179 - learning_rate: 1.5625e-05
Epoch 247/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4596 - val_accuracy: 0.6710 - val_loss: 0.7163 - learning_rate: 1.5625e-05
Epoch 248/500
124/124 - 3s - 23ms/step - accuracy: 0.7751 - loss: 0.4637 - val_accuracy: 0.6667 - val_loss: 0.7209 - learning_rate: 1.5625e-05
Epoch 249/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4641 - val_accuracy: 0.6667 - val_loss: 0.7197 - learning_rate: 1.5625e-05
Epoch 250/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4564 - val_accuracy: 0.6681 - val_loss: 0.7191 - learning_rate: 1.5625e-05
Epoch 251/500
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4640 - val_accuracy: 0.6652 - val_loss: 0.7207 - learning_rate: 1.5625e-05
Epoch 252/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4588 - val_accuracy: 0.6652 - val_loss: 0.7211 - learning_rate: 1.5625e-05
Epoch 253/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4626 - val_accuracy: 0.6667 - val_loss: 0.7216 - learning_rate: 1.5625e-05
Epoch 254/500
124/124 - 3s - 23ms/step - accuracy: 0.7799 - loss: 0.4609 - val_accuracy: 0.6638 - val_loss: 0.7203 - learning_rate: 1.5625e-05
Epoch 255/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4619 - val_accuracy: 0.6638 - val_loss: 0.7196 - learning_rate: 1.5625e-05
Epoch 256/500
124/124 - 3s - 23ms/step - accuracy: 0.7703 - loss: 0.4631 - val_accuracy: 0.6695 - val_loss: 0.7161 - learning_rate: 1.5625e-05
Epoch 257/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4664 - val_accuracy: 0.6681 - val_loss: 0.7198 - learning_rate: 1.5625e-05
Epoch 258/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4585 - val_accuracy: 0.6681 - val_loss: 0.7172 - learning_rate: 1.5625e-05
Epoch 259/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4586 - val_accuracy: 0.6667 - val_loss: 0.7211 - learning_rate: 1.5625e-05
Epoch 260/500
124/124 - 3s - 23ms/step - accuracy: 0.7809 - loss: 0.4543 - val_accuracy: 0.6595 - val_loss: 0.7218 - learning_rate: 1.5625e-05
Epoch 261/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4599 - val_accuracy: 0.6624 - val_loss: 0.7227 - learning_rate: 1.5625e-05
Epoch 262/500
124/124 - 3s - 23ms/step - accuracy: 0.7670 - loss: 0.4624 - val_accuracy: 0.6624 - val_loss: 0.7217 - learning_rate: 1.5625e-05
Epoch 263/500
124/124 - 3s - 23ms/step - accuracy: 0.7787 - loss: 0.4617 - val_accuracy: 0.6667 - val_loss: 0.7179 - learning_rate: 1.5625e-05
Epoch 264/500
124/124 - 3s - 23ms/step - accuracy: 0.7855 - loss: 0.4584 - val_accuracy: 0.6652 - val_loss: 0.7197 - learning_rate: 1.5625e-05
Epoch 265/500
124/124 - 3s - 23ms/step - accuracy: 0.7769 - loss: 0.4559 - val_accuracy: 0.6652 - val_loss: 0.7199 - learning_rate: 1.5625e-05
Epoch 266/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4581 - val_accuracy: 0.6595 - val_loss: 0.7215 - learning_rate: 1.5625e-05
Epoch 267/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4643 - val_accuracy: 0.6624 - val_loss: 0.7197 - learning_rate: 1.5625e-05
Epoch 268/500
124/124 - 3s - 23ms/step - accuracy: 0.7825 - loss: 0.4574 - val_accuracy: 0.6624 - val_loss: 0.7208 - learning_rate: 1.5625e-05
Epoch 269/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4615 - val_accuracy: 0.6609 - val_loss: 0.7189 - learning_rate: 1.5625e-05
Epoch 270/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4642 - val_accuracy: 0.6638 - val_loss: 0.7213 - learning_rate: 1.5625e-05
Epoch 271/500
124/124 - 3s - 23ms/step - accuracy: 0.7759 - loss: 0.4608 - val_accuracy: 0.6609 - val_loss: 0.7217 - learning_rate: 1.5625e-05
Epoch 272/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4604 - val_accuracy: 0.6638 - val_loss: 0.7195 - learning_rate: 1.5625e-05
Epoch 273/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4608 - val_accuracy: 0.6638 - val_loss: 0.7199 - learning_rate: 1.5625e-05
Epoch 274/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4622 - val_accuracy: 0.6609 - val_loss: 0.7236 - learning_rate: 1.5625e-05
Epoch 275/500
124/124 - 3s - 23ms/step - accuracy: 0.7680 - loss: 0.4632 - val_accuracy: 0.6624 - val_loss: 0.7198 - learning_rate: 1.5625e-05
Epoch 276/500

Epoch 276: ReduceLROnPlateau reducing learning rate to 7.812500371073838e-06.
124/124 - 3s - 23ms/step - accuracy: 0.7883 - loss: 0.4515 - val_accuracy: 0.6624 - val_loss: 0.7205 - learning_rate: 1.5625e-05
Epoch 277/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4590 - val_accuracy: 0.6624 - val_loss: 0.7175 - learning_rate: 7.8125e-06
Epoch 278/500
124/124 - 3s - 23ms/step - accuracy: 0.7743 - loss: 0.4608 - val_accuracy: 0.6652 - val_loss: 0.7164 - learning_rate: 7.8125e-06
Epoch 279/500
124/124 - 3s - 23ms/step - accuracy: 0.7761 - loss: 0.4575 - val_accuracy: 0.6652 - val_loss: 0.7175 - learning_rate: 7.8125e-06
Epoch 280/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4654 - val_accuracy: 0.6624 - val_loss: 0.7191 - learning_rate: 7.8125e-06
Epoch 281/500
124/124 - 3s - 23ms/step - accuracy: 0.7830 - loss: 0.4601 - val_accuracy: 0.6638 - val_loss: 0.7181 - learning_rate: 7.8125e-06
Epoch 282/500
124/124 - 3s - 23ms/step - accuracy: 0.7657 - loss: 0.4637 - val_accuracy: 0.6667 - val_loss: 0.7162 - learning_rate: 7.8125e-06
Epoch 283/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4583 - val_accuracy: 0.6667 - val_loss: 0.7178 - learning_rate: 7.8125e-06
Epoch 284/500
124/124 - 3s - 23ms/step - accuracy: 0.7771 - loss: 0.4561 - val_accuracy: 0.6652 - val_loss: 0.7183 - learning_rate: 7.8125e-06
Epoch 285/500
124/124 - 3s - 23ms/step - accuracy: 0.7746 - loss: 0.4614 - val_accuracy: 0.6652 - val_loss: 0.7190 - learning_rate: 7.8125e-06
Epoch 286/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4625 - val_accuracy: 0.6652 - val_loss: 0.7194 - learning_rate: 7.8125e-06
Epoch 287/500
124/124 - 3s - 23ms/step - accuracy: 0.7756 - loss: 0.4587 - val_accuracy: 0.6667 - val_loss: 0.7180 - learning_rate: 7.8125e-06
Epoch 288/500
124/124 - 3s - 23ms/step - accuracy: 0.7776 - loss: 0.4547 - val_accuracy: 0.6652 - val_loss: 0.7166 - learning_rate: 7.8125e-06
Epoch 289/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4570 - val_accuracy: 0.6638 - val_loss: 0.7192 - learning_rate: 7.8125e-06
Epoch 290/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4613 - val_accuracy: 0.6638 - val_loss: 0.7179 - learning_rate: 7.8125e-06
Epoch 291/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4589 - val_accuracy: 0.6638 - val_loss: 0.7181 - learning_rate: 7.8125e-06
Epoch 292/500
124/124 - 3s - 23ms/step - accuracy: 0.7814 - loss: 0.4549 - val_accuracy: 0.6638 - val_loss: 0.7178 - learning_rate: 7.8125e-06
Epoch 293/500
124/124 - 3s - 23ms/step - accuracy: 0.7779 - loss: 0.4571 - val_accuracy: 0.6609 - val_loss: 0.7169 - learning_rate: 7.8125e-06
Epoch 294/500
124/124 - 3s - 23ms/step - accuracy: 0.7794 - loss: 0.4518 - val_accuracy: 0.6667 - val_loss: 0.7164 - learning_rate: 7.8125e-06
Epoch 295/500
124/124 - 3s - 23ms/step - accuracy: 0.7781 - loss: 0.4634 - val_accuracy: 0.6652 - val_loss: 0.7176 - learning_rate: 7.8125e-06
Epoch 296/500

Epoch 296: ReduceLROnPlateau reducing learning rate to 3.906250185536919e-06.
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4686 - val_accuracy: 0.6638 - val_loss: 0.7196 - learning_rate: 7.8125e-06
Epoch 297/500
124/124 - 3s - 23ms/step - accuracy: 0.7774 - loss: 0.4576 - val_accuracy: 0.6638 - val_loss: 0.7181 - learning_rate: 3.9063e-06
Epoch 298/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4614 - val_accuracy: 0.6652 - val_loss: 0.7183 - learning_rate: 3.9063e-06
Epoch 299/500
124/124 - 3s - 23ms/step - accuracy: 0.7738 - loss: 0.4550 - val_accuracy: 0.6638 - val_loss: 0.7180 - learning_rate: 3.9063e-06
Epoch 300/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4657 - val_accuracy: 0.6638 - val_loss: 0.7184 - learning_rate: 3.9063e-06
Epoch 301/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4602 - val_accuracy: 0.6652 - val_loss: 0.7174 - learning_rate: 3.9063e-06
Epoch 302/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4567 - val_accuracy: 0.6667 - val_loss: 0.7163 - learning_rate: 3.9063e-06
Epoch 303/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4630 - val_accuracy: 0.6681 - val_loss: 0.7172 - learning_rate: 3.9063e-06
Epoch 304/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4635 - val_accuracy: 0.6681 - val_loss: 0.7176 - learning_rate: 3.9063e-06
Epoch 305/500
124/124 - 3s - 23ms/step - accuracy: 0.7792 - loss: 0.4522 - val_accuracy: 0.6681 - val_loss: 0.7178 - learning_rate: 3.9063e-06
Epoch 306/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4616 - val_accuracy: 0.6652 - val_loss: 0.7184 - learning_rate: 3.9063e-06
Epoch 306: early stopping
Restoring model weights from the end of the best epoch: 256.
Training complete. Best epoch: 256 of 306. Best val_loss: 0.7161, val_accuracy: 0.6695

========== Evaluation: LOSO fold 24 / held-out EMS0025 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        34         6         0
  intermedia        35        39         6
  max_intens         0        10        30

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.493     0.850     0.624        40
intermediate_intensity      0.709     0.487     0.578        80
         max_intensity      0.833     0.750     0.789        40

              accuracy                          0.644       160
             macro avg      0.678     0.696     0.664       160
          weighted avg      0.686     0.644     0.642       160

Overall accuracy: 0.6438

============================================================
Fold 25 of 30: holding out EMS0026
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.20e-07, 9.56e-07]
  Per-channel std range:  [7.28e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4660 - loss: 1.0227 - val_accuracy: 0.4842 - val_loss: 1.0367 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5350 - loss: 0.8992 - val_accuracy: 0.5259 - val_loss: 0.9335 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5718 - loss: 0.8380 - val_accuracy: 0.5517 - val_loss: 0.8788 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5923 - loss: 0.8076 - val_accuracy: 0.5618 - val_loss: 0.8513 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5953 - loss: 0.7815 - val_accuracy: 0.5747 - val_loss: 0.8427 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.6019 - loss: 0.7710 - val_accuracy: 0.5761 - val_loss: 0.8327 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6062 - loss: 0.7519 - val_accuracy: 0.5747 - val_loss: 0.8175 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6204 - loss: 0.7354 - val_accuracy: 0.5833 - val_loss: 0.8140 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6105 - loss: 0.7317 - val_accuracy: 0.6063 - val_loss: 0.7977 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6260 - loss: 0.7205 - val_accuracy: 0.6020 - val_loss: 0.7984 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6232 - loss: 0.7107 - val_accuracy: 0.5790 - val_loss: 0.8001 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6308 - loss: 0.7045 - val_accuracy: 0.5948 - val_loss: 0.7901 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6402 - loss: 0.6936 - val_accuracy: 0.5991 - val_loss: 0.7741 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6422 - loss: 0.6881 - val_accuracy: 0.5934 - val_loss: 0.7900 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6382 - loss: 0.6873 - val_accuracy: 0.6006 - val_loss: 0.7828 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6443 - loss: 0.6798 - val_accuracy: 0.6135 - val_loss: 0.7563 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6504 - loss: 0.6721 - val_accuracy: 0.6149 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6552 - loss: 0.6645 - val_accuracy: 0.5934 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6514 - loss: 0.6677 - val_accuracy: 0.6063 - val_loss: 0.7606 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6547 - loss: 0.6588 - val_accuracy: 0.6207 - val_loss: 0.7638 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6572 - loss: 0.6565 - val_accuracy: 0.6106 - val_loss: 0.7566 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6580 - loss: 0.6500 - val_accuracy: 0.6121 - val_loss: 0.7590 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6557 - loss: 0.6426 - val_accuracy: 0.6264 - val_loss: 0.7494 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6608 - loss: 0.6419 - val_accuracy: 0.6049 - val_loss: 0.7553 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6691 - loss: 0.6349 - val_accuracy: 0.6250 - val_loss: 0.7417 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6727 - loss: 0.6366 - val_accuracy: 0.6250 - val_loss: 0.7501 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6678 - loss: 0.6363 - val_accuracy: 0.6336 - val_loss: 0.7449 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6671 - loss: 0.6283 - val_accuracy: 0.6221 - val_loss: 0.7368 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6757 - loss: 0.6306 - val_accuracy: 0.6106 - val_loss: 0.7544 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6765 - loss: 0.6184 - val_accuracy: 0.6236 - val_loss: 0.7499 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6800 - loss: 0.6232 - val_accuracy: 0.6264 - val_loss: 0.7533 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6788 - loss: 0.6195 - val_accuracy: 0.6236 - val_loss: 0.7399 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6719 - loss: 0.6273 - val_accuracy: 0.6250 - val_loss: 0.7546 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6841 - loss: 0.6121 - val_accuracy: 0.6149 - val_loss: 0.7531 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6770 - loss: 0.6165 - val_accuracy: 0.6279 - val_loss: 0.7470 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6848 - loss: 0.6176 - val_accuracy: 0.6279 - val_loss: 0.7336 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6891 - loss: 0.6152 - val_accuracy: 0.6336 - val_loss: 0.7418 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6869 - loss: 0.6121 - val_accuracy: 0.6466 - val_loss: 0.7310 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6805 - loss: 0.6103 - val_accuracy: 0.6494 - val_loss: 0.7321 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.7023 - loss: 0.5989 - val_accuracy: 0.6365 - val_loss: 0.7484 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6853 - loss: 0.6136 - val_accuracy: 0.6451 - val_loss: 0.7350 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6891 - loss: 0.6059 - val_accuracy: 0.6221 - val_loss: 0.7572 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6042 - val_accuracy: 0.6351 - val_loss: 0.7522 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6808 - loss: 0.6031 - val_accuracy: 0.6466 - val_loss: 0.7241 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6952 - loss: 0.5956 - val_accuracy: 0.6437 - val_loss: 0.7419 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6907 - loss: 0.5950 - val_accuracy: 0.6264 - val_loss: 0.7507 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.7003 - loss: 0.5879 - val_accuracy: 0.6451 - val_loss: 0.7357 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.7006 - loss: 0.5873 - val_accuracy: 0.6408 - val_loss: 0.7367 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6922 - loss: 0.5947 - val_accuracy: 0.6351 - val_loss: 0.7452 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.7028 - loss: 0.5830 - val_accuracy: 0.6322 - val_loss: 0.7390 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 25ms/step - accuracy: 0.7003 - loss: 0.5851 - val_accuracy: 0.6480 - val_loss: 0.7016 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 24ms/step - accuracy: 0.7039 - loss: 0.5879 - val_accuracy: 0.6379 - val_loss: 0.7203 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.6846 - loss: 0.5886 - val_accuracy: 0.6365 - val_loss: 0.7299 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 24ms/step - accuracy: 0.6922 - loss: 0.5874 - val_accuracy: 0.6494 - val_loss: 0.7132 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 24ms/step - accuracy: 0.6907 - loss: 0.5806 - val_accuracy: 0.6379 - val_loss: 0.7187 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 24ms/step - accuracy: 0.6975 - loss: 0.5877 - val_accuracy: 0.6351 - val_loss: 0.7322 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.7039 - loss: 0.5796 - val_accuracy: 0.6379 - val_loss: 0.7455 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 24ms/step - accuracy: 0.7026 - loss: 0.5692 - val_accuracy: 0.6523 - val_loss: 0.7150 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6942 - loss: 0.5828 - val_accuracy: 0.6279 - val_loss: 0.7343 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.7044 - loss: 0.5759 - val_accuracy: 0.6394 - val_loss: 0.7183 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.6998 - loss: 0.5843 - val_accuracy: 0.6523 - val_loss: 0.7103 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.7064 - loss: 0.5690 - val_accuracy: 0.6466 - val_loss: 0.7163 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.6978 - loss: 0.5706 - val_accuracy: 0.6509 - val_loss: 0.7187 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 24ms/step - accuracy: 0.7059 - loss: 0.5783 - val_accuracy: 0.6480 - val_loss: 0.7233 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.6952 - loss: 0.5716 - val_accuracy: 0.6552 - val_loss: 0.7179 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.7132 - loss: 0.5626 - val_accuracy: 0.6437 - val_loss: 0.7034 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.7066 - loss: 0.5679 - val_accuracy: 0.6379 - val_loss: 0.7258 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.6998 - loss: 0.5794 - val_accuracy: 0.6480 - val_loss: 0.7209 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.6955 - loss: 0.5714 - val_accuracy: 0.6379 - val_loss: 0.7276 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 24ms/step - accuracy: 0.7046 - loss: 0.5668 - val_accuracy: 0.6422 - val_loss: 0.7350 - learning_rate: 0.0010
Epoch 71/500

Epoch 71: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5668 - val_accuracy: 0.6365 - val_loss: 0.7253 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.7153 - loss: 0.5504 - val_accuracy: 0.6609 - val_loss: 0.7092 - learning_rate: 5.0000e-04
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7302 - loss: 0.5327 - val_accuracy: 0.6681 - val_loss: 0.6995 - learning_rate: 5.0000e-04
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7269 - loss: 0.5328 - val_accuracy: 0.6537 - val_loss: 0.6918 - learning_rate: 5.0000e-04
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7315 - loss: 0.5258 - val_accuracy: 0.6595 - val_loss: 0.7010 - learning_rate: 5.0000e-04
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7300 - loss: 0.5260 - val_accuracy: 0.6566 - val_loss: 0.6979 - learning_rate: 5.0000e-04
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7312 - loss: 0.5280 - val_accuracy: 0.6681 - val_loss: 0.7040 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7383 - loss: 0.5246 - val_accuracy: 0.6609 - val_loss: 0.6938 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7355 - loss: 0.5217 - val_accuracy: 0.6580 - val_loss: 0.7043 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7424 - loss: 0.5158 - val_accuracy: 0.6523 - val_loss: 0.7036 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7328 - loss: 0.5255 - val_accuracy: 0.6552 - val_loss: 0.7033 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 24ms/step - accuracy: 0.7376 - loss: 0.5204 - val_accuracy: 0.6624 - val_loss: 0.7022 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7302 - loss: 0.5283 - val_accuracy: 0.6595 - val_loss: 0.6890 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7234 - loss: 0.5337 - val_accuracy: 0.6739 - val_loss: 0.6957 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7345 - loss: 0.5234 - val_accuracy: 0.6638 - val_loss: 0.7178 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7328 - loss: 0.5223 - val_accuracy: 0.6595 - val_loss: 0.7064 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7335 - loss: 0.5195 - val_accuracy: 0.6681 - val_loss: 0.6936 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7330 - loss: 0.5170 - val_accuracy: 0.6695 - val_loss: 0.6821 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7406 - loss: 0.5151 - val_accuracy: 0.6466 - val_loss: 0.6938 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7414 - loss: 0.5146 - val_accuracy: 0.6609 - val_loss: 0.7018 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7244 - loss: 0.5231 - val_accuracy: 0.6552 - val_loss: 0.7044 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7317 - loss: 0.5221 - val_accuracy: 0.6652 - val_loss: 0.6852 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7333 - loss: 0.5163 - val_accuracy: 0.6667 - val_loss: 0.6919 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7340 - loss: 0.5189 - val_accuracy: 0.6609 - val_loss: 0.7065 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 24ms/step - accuracy: 0.7459 - loss: 0.5149 - val_accuracy: 0.6667 - val_loss: 0.6982 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7305 - loss: 0.5178 - val_accuracy: 0.6739 - val_loss: 0.6892 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7348 - loss: 0.5139 - val_accuracy: 0.6595 - val_loss: 0.7100 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7358 - loss: 0.5214 - val_accuracy: 0.6710 - val_loss: 0.6944 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7338 - loss: 0.5121 - val_accuracy: 0.6595 - val_loss: 0.6976 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7302 - loss: 0.5130 - val_accuracy: 0.6739 - val_loss: 0.6925 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7363 - loss: 0.5089 - val_accuracy: 0.6681 - val_loss: 0.6996 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 24ms/step - accuracy: 0.7399 - loss: 0.5090 - val_accuracy: 0.6681 - val_loss: 0.6901 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7366 - loss: 0.5174 - val_accuracy: 0.6638 - val_loss: 0.6780 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7312 - loss: 0.5211 - val_accuracy: 0.6580 - val_loss: 0.6970 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7320 - loss: 0.5134 - val_accuracy: 0.6537 - val_loss: 0.7020 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7414 - loss: 0.5104 - val_accuracy: 0.6566 - val_loss: 0.7144 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7320 - loss: 0.5139 - val_accuracy: 0.6580 - val_loss: 0.7050 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7368 - loss: 0.5198 - val_accuracy: 0.6753 - val_loss: 0.6942 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7442 - loss: 0.5023 - val_accuracy: 0.6566 - val_loss: 0.7079 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7421 - loss: 0.5051 - val_accuracy: 0.6681 - val_loss: 0.7037 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7475 - loss: 0.5042 - val_accuracy: 0.6624 - val_loss: 0.7079 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7373 - loss: 0.5133 - val_accuracy: 0.6624 - val_loss: 0.6995 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7292 - loss: 0.5160 - val_accuracy: 0.6710 - val_loss: 0.6986 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7396 - loss: 0.5162 - val_accuracy: 0.6652 - val_loss: 0.6888 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5086 - val_accuracy: 0.6638 - val_loss: 0.7036 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7444 - loss: 0.5015 - val_accuracy: 0.6537 - val_loss: 0.7032 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7470 - loss: 0.5059 - val_accuracy: 0.6609 - val_loss: 0.6949 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7386 - loss: 0.5097 - val_accuracy: 0.6609 - val_loss: 0.6884 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7414 - loss: 0.5114 - val_accuracy: 0.6695 - val_loss: 0.6995 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7381 - loss: 0.5090 - val_accuracy: 0.6652 - val_loss: 0.7033 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7409 - loss: 0.5016 - val_accuracy: 0.6695 - val_loss: 0.7077 - learning_rate: 5.0000e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7426 - loss: 0.5140 - val_accuracy: 0.6595 - val_loss: 0.7065 - learning_rate: 5.0000e-04
Epoch 123/500

Epoch 123: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7447 - loss: 0.5024 - val_accuracy: 0.6537 - val_loss: 0.7262 - learning_rate: 5.0000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.4839 - val_accuracy: 0.6624 - val_loss: 0.7070 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7541 - loss: 0.4884 - val_accuracy: 0.6552 - val_loss: 0.7138 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7619 - loss: 0.4785 - val_accuracy: 0.6494 - val_loss: 0.7162 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7609 - loss: 0.4824 - val_accuracy: 0.6494 - val_loss: 0.7244 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7541 - loss: 0.4816 - val_accuracy: 0.6552 - val_loss: 0.7172 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7624 - loss: 0.4734 - val_accuracy: 0.6537 - val_loss: 0.7063 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7500 - loss: 0.4784 - val_accuracy: 0.6552 - val_loss: 0.7039 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.4833 - val_accuracy: 0.6552 - val_loss: 0.7076 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7594 - loss: 0.4840 - val_accuracy: 0.6580 - val_loss: 0.7013 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4749 - val_accuracy: 0.6552 - val_loss: 0.7041 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7617 - loss: 0.4789 - val_accuracy: 0.6552 - val_loss: 0.7105 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7538 - loss: 0.4854 - val_accuracy: 0.6566 - val_loss: 0.7136 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4841 - val_accuracy: 0.6580 - val_loss: 0.7037 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4773 - val_accuracy: 0.6509 - val_loss: 0.7203 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.4815 - val_accuracy: 0.6509 - val_loss: 0.7238 - learning_rate: 2.5000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.4789 - val_accuracy: 0.6595 - val_loss: 0.7079 - learning_rate: 2.5000e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7639 - loss: 0.4778 - val_accuracy: 0.6566 - val_loss: 0.7135 - learning_rate: 2.5000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7523 - loss: 0.4825 - val_accuracy: 0.6595 - val_loss: 0.7089 - learning_rate: 2.5000e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.4788 - val_accuracy: 0.6595 - val_loss: 0.7061 - learning_rate: 2.5000e-04
Epoch 143/500

Epoch 143: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7665 - loss: 0.4674 - val_accuracy: 0.6624 - val_loss: 0.7001 - learning_rate: 2.5000e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4682 - val_accuracy: 0.6710 - val_loss: 0.6955 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4624 - val_accuracy: 0.6724 - val_loss: 0.6961 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 24ms/step - accuracy: 0.7614 - loss: 0.4688 - val_accuracy: 0.6681 - val_loss: 0.6912 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 24ms/step - accuracy: 0.7672 - loss: 0.4645 - val_accuracy: 0.6595 - val_loss: 0.6988 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 24ms/step - accuracy: 0.7627 - loss: 0.4645 - val_accuracy: 0.6652 - val_loss: 0.6946 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4638 - val_accuracy: 0.6681 - val_loss: 0.6932 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4618 - val_accuracy: 0.6595 - val_loss: 0.6919 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4615 - val_accuracy: 0.6624 - val_loss: 0.7021 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 24ms/step - accuracy: 0.7721 - loss: 0.4626 - val_accuracy: 0.6609 - val_loss: 0.6954 - learning_rate: 1.2500e-04
Epoch 153/500
124/124 - 3s - 24ms/step - accuracy: 0.7754 - loss: 0.4638 - val_accuracy: 0.6595 - val_loss: 0.6957 - learning_rate: 1.2500e-04
Epoch 153: early stopping
Restoring model weights from the end of the best epoch: 103.
Training complete. Best epoch: 103 of 153. Best val_loss: 0.6780, val_accuracy: 0.6638

========== Evaluation: LOSO fold 25 / held-out EMS0026 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        32         8         0
  intermedia        43        28         9
  max_intens         9        23         8

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.381     0.800     0.516        40
intermediate_intensity      0.475     0.350     0.403        80
         max_intensity      0.471     0.200     0.281        40

              accuracy                          0.425       160
             macro avg      0.442     0.450     0.400       160
          weighted avg      0.450     0.425     0.401       160

Overall accuracy: 0.4250

============================================================
Fold 26 of 30: holding out EMS0027
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.28e-07, 9.55e-07]
  Per-channel std range:  [7.25e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 117ms/step - accuracy: 0.4630 - loss: 1.0075 - val_accuracy: 0.4799 - val_loss: 1.0311 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5335 - loss: 0.8928 - val_accuracy: 0.5216 - val_loss: 0.9545 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5591 - loss: 0.8474 - val_accuracy: 0.5388 - val_loss: 0.9031 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5822 - loss: 0.8135 - val_accuracy: 0.5747 - val_loss: 0.8801 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5892 - loss: 0.7934 - val_accuracy: 0.5747 - val_loss: 0.8608 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5991 - loss: 0.7747 - val_accuracy: 0.5891 - val_loss: 0.8468 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6022 - loss: 0.7613 - val_accuracy: 0.5934 - val_loss: 0.8420 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6078 - loss: 0.7519 - val_accuracy: 0.5948 - val_loss: 0.8278 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6090 - loss: 0.7425 - val_accuracy: 0.5876 - val_loss: 0.8359 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6121 - loss: 0.7384 - val_accuracy: 0.6135 - val_loss: 0.8230 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6235 - loss: 0.7265 - val_accuracy: 0.6092 - val_loss: 0.8086 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6237 - loss: 0.7194 - val_accuracy: 0.5848 - val_loss: 0.8205 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6265 - loss: 0.7174 - val_accuracy: 0.5905 - val_loss: 0.8193 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6270 - loss: 0.7102 - val_accuracy: 0.6135 - val_loss: 0.8038 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 23ms/step - accuracy: 0.6324 - loss: 0.7033 - val_accuracy: 0.6020 - val_loss: 0.8040 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6438 - loss: 0.6972 - val_accuracy: 0.6049 - val_loss: 0.7850 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6389 - loss: 0.6963 - val_accuracy: 0.6049 - val_loss: 0.7862 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6407 - loss: 0.6897 - val_accuracy: 0.6092 - val_loss: 0.7795 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6356 - loss: 0.6937 - val_accuracy: 0.6020 - val_loss: 0.8002 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6450 - loss: 0.6847 - val_accuracy: 0.6106 - val_loss: 0.7991 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6450 - loss: 0.6748 - val_accuracy: 0.6193 - val_loss: 0.7785 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6575 - loss: 0.6654 - val_accuracy: 0.6049 - val_loss: 0.7892 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6580 - loss: 0.6619 - val_accuracy: 0.5977 - val_loss: 0.8052 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6539 - loss: 0.6633 - val_accuracy: 0.6279 - val_loss: 0.7637 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6547 - loss: 0.6586 - val_accuracy: 0.6063 - val_loss: 0.7892 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6577 - loss: 0.6554 - val_accuracy: 0.5876 - val_loss: 0.7959 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6613 - loss: 0.6555 - val_accuracy: 0.6034 - val_loss: 0.7789 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6704 - loss: 0.6447 - val_accuracy: 0.5963 - val_loss: 0.7892 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6666 - loss: 0.6487 - val_accuracy: 0.5905 - val_loss: 0.8042 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6577 - loss: 0.6457 - val_accuracy: 0.6250 - val_loss: 0.7632 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 24ms/step - accuracy: 0.6651 - loss: 0.6434 - val_accuracy: 0.6221 - val_loss: 0.7748 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 24ms/step - accuracy: 0.6646 - loss: 0.6385 - val_accuracy: 0.6149 - val_loss: 0.7599 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6742 - loss: 0.6268 - val_accuracy: 0.6236 - val_loss: 0.7566 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6749 - loss: 0.6327 - val_accuracy: 0.6149 - val_loss: 0.7591 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 24ms/step - accuracy: 0.6752 - loss: 0.6355 - val_accuracy: 0.6279 - val_loss: 0.7548 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6676 - loss: 0.6341 - val_accuracy: 0.6221 - val_loss: 0.7592 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6828 - loss: 0.6232 - val_accuracy: 0.6193 - val_loss: 0.7521 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6749 - loss: 0.6310 - val_accuracy: 0.6250 - val_loss: 0.7503 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6711 - loss: 0.6227 - val_accuracy: 0.6250 - val_loss: 0.7704 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6757 - loss: 0.6204 - val_accuracy: 0.6293 - val_loss: 0.7517 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6755 - loss: 0.6283 - val_accuracy: 0.6178 - val_loss: 0.7581 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6788 - loss: 0.6174 - val_accuracy: 0.6236 - val_loss: 0.7512 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6889 - loss: 0.6106 - val_accuracy: 0.6293 - val_loss: 0.7560 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6848 - loss: 0.6066 - val_accuracy: 0.6293 - val_loss: 0.7526 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.6902 - loss: 0.6044 - val_accuracy: 0.6092 - val_loss: 0.7806 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6884 - loss: 0.6060 - val_accuracy: 0.6149 - val_loss: 0.7571 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6777 - loss: 0.6187 - val_accuracy: 0.6351 - val_loss: 0.7502 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6874 - loss: 0.6058 - val_accuracy: 0.6365 - val_loss: 0.7351 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6856 - loss: 0.6110 - val_accuracy: 0.6264 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.6891 - loss: 0.5998 - val_accuracy: 0.6121 - val_loss: 0.7612 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6866 - loss: 0.6003 - val_accuracy: 0.6379 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.5970 - val_accuracy: 0.6365 - val_loss: 0.7416 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6820 - loss: 0.5992 - val_accuracy: 0.6336 - val_loss: 0.7383 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5991 - val_accuracy: 0.6236 - val_loss: 0.7542 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.6017 - val_accuracy: 0.6307 - val_loss: 0.7538 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.5926 - val_accuracy: 0.6466 - val_loss: 0.7351 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6935 - loss: 0.6035 - val_accuracy: 0.6221 - val_loss: 0.7484 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.6002 - val_accuracy: 0.6279 - val_loss: 0.7593 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6957 - loss: 0.5994 - val_accuracy: 0.6193 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5885 - val_accuracy: 0.6293 - val_loss: 0.7497 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6904 - loss: 0.5974 - val_accuracy: 0.6379 - val_loss: 0.7505 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.6952 - loss: 0.5920 - val_accuracy: 0.6250 - val_loss: 0.7566 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7011 - loss: 0.5818 - val_accuracy: 0.6394 - val_loss: 0.7373 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7018 - loss: 0.5864 - val_accuracy: 0.6523 - val_loss: 0.7406 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.6917 - loss: 0.5889 - val_accuracy: 0.6351 - val_loss: 0.7491 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5835 - val_accuracy: 0.6365 - val_loss: 0.7444 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5934 - val_accuracy: 0.6466 - val_loss: 0.7362 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6922 - loss: 0.5807 - val_accuracy: 0.6566 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.7003 - loss: 0.5851 - val_accuracy: 0.6365 - val_loss: 0.7472 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5795 - val_accuracy: 0.6523 - val_loss: 0.7360 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.6962 - loss: 0.5828 - val_accuracy: 0.6379 - val_loss: 0.7254 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5708 - val_accuracy: 0.6408 - val_loss: 0.7357 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5822 - val_accuracy: 0.6422 - val_loss: 0.7294 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5765 - val_accuracy: 0.6566 - val_loss: 0.7026 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5743 - val_accuracy: 0.6466 - val_loss: 0.7473 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7150 - loss: 0.5624 - val_accuracy: 0.6566 - val_loss: 0.7365 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7011 - loss: 0.5783 - val_accuracy: 0.6351 - val_loss: 0.7473 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5787 - val_accuracy: 0.6408 - val_loss: 0.7375 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5720 - val_accuracy: 0.6437 - val_loss: 0.7520 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5795 - val_accuracy: 0.6422 - val_loss: 0.7446 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7097 - loss: 0.5734 - val_accuracy: 0.6422 - val_loss: 0.7383 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5731 - val_accuracy: 0.6279 - val_loss: 0.7530 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5760 - val_accuracy: 0.6494 - val_loss: 0.7288 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7056 - loss: 0.5713 - val_accuracy: 0.6552 - val_loss: 0.7219 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7059 - loss: 0.5747 - val_accuracy: 0.6221 - val_loss: 0.7543 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5736 - val_accuracy: 0.6379 - val_loss: 0.7672 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7072 - loss: 0.5645 - val_accuracy: 0.6552 - val_loss: 0.7162 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5729 - val_accuracy: 0.6264 - val_loss: 0.7538 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7089 - loss: 0.5608 - val_accuracy: 0.6523 - val_loss: 0.7375 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5625 - val_accuracy: 0.6609 - val_loss: 0.7246 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5622 - val_accuracy: 0.6681 - val_loss: 0.7045 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7112 - loss: 0.5583 - val_accuracy: 0.6537 - val_loss: 0.7463 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5619 - val_accuracy: 0.6552 - val_loss: 0.7395 - learning_rate: 0.0010
Epoch 94/500

Epoch 94: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5574 - val_accuracy: 0.6293 - val_loss: 0.7461 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7226 - loss: 0.5438 - val_accuracy: 0.6509 - val_loss: 0.7296 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5262 - val_accuracy: 0.6595 - val_loss: 0.7334 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5187 - val_accuracy: 0.6537 - val_loss: 0.7346 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5205 - val_accuracy: 0.6681 - val_loss: 0.7259 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7355 - loss: 0.5254 - val_accuracy: 0.6580 - val_loss: 0.7251 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7378 - loss: 0.5227 - val_accuracy: 0.6667 - val_loss: 0.7417 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7454 - loss: 0.5205 - val_accuracy: 0.6494 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5184 - val_accuracy: 0.6667 - val_loss: 0.7332 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5223 - val_accuracy: 0.6767 - val_loss: 0.7125 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7348 - loss: 0.5200 - val_accuracy: 0.6652 - val_loss: 0.7240 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7371 - loss: 0.5211 - val_accuracy: 0.6753 - val_loss: 0.7179 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5191 - val_accuracy: 0.6552 - val_loss: 0.7429 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5129 - val_accuracy: 0.6652 - val_loss: 0.7376 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5167 - val_accuracy: 0.6638 - val_loss: 0.7132 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5166 - val_accuracy: 0.6552 - val_loss: 0.7337 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5166 - val_accuracy: 0.6652 - val_loss: 0.7264 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5127 - val_accuracy: 0.6638 - val_loss: 0.7252 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7366 - loss: 0.5204 - val_accuracy: 0.6537 - val_loss: 0.7234 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7553 - loss: 0.5093 - val_accuracy: 0.6552 - val_loss: 0.7226 - learning_rate: 5.0000e-04
Epoch 114/500

Epoch 114: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7411 - loss: 0.5154 - val_accuracy: 0.6681 - val_loss: 0.7140 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7543 - loss: 0.5031 - val_accuracy: 0.6739 - val_loss: 0.7197 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.4930 - val_accuracy: 0.6652 - val_loss: 0.7050 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7568 - loss: 0.4952 - val_accuracy: 0.6681 - val_loss: 0.7150 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4877 - val_accuracy: 0.6695 - val_loss: 0.7223 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4888 - val_accuracy: 0.6724 - val_loss: 0.7184 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7601 - loss: 0.4939 - val_accuracy: 0.6724 - val_loss: 0.7107 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7553 - loss: 0.4988 - val_accuracy: 0.6609 - val_loss: 0.7313 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 24ms/step - accuracy: 0.7612 - loss: 0.4925 - val_accuracy: 0.6724 - val_loss: 0.7215 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7693 - loss: 0.4876 - val_accuracy: 0.6695 - val_loss: 0.7192 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4887 - val_accuracy: 0.6652 - val_loss: 0.7200 - learning_rate: 2.5000e-04
Epoch 124: early stopping
Restoring model weights from the end of the best epoch: 74.
Training complete. Best epoch: 74 of 124. Best val_loss: 0.7026, val_accuracy: 0.6566

========== Evaluation: LOSO fold 26 / held-out EMS0027 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        29        11         0
  intermedia        27        47         6
  max_intens         6        29         5

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.468     0.725     0.569        40
intermediate_intensity      0.540     0.588     0.563        80
         max_intensity      0.455     0.125     0.196        40

              accuracy                          0.506       160
             macro avg      0.488     0.479     0.443       160
          weighted avg      0.501     0.506     0.473       160

Overall accuracy: 0.5062

============================================================
Fold 27 of 30: holding out EMS0028
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.03e-07, 9.52e-07]
  Per-channel std range:  [7.23e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 119ms/step - accuracy: 0.4473 - loss: 1.0369 - val_accuracy: 0.4741 - val_loss: 1.0501 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5330 - loss: 0.9095 - val_accuracy: 0.5144 - val_loss: 0.9676 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5522 - loss: 0.8540 - val_accuracy: 0.5618 - val_loss: 0.9069 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5725 - loss: 0.8235 - val_accuracy: 0.5560 - val_loss: 0.8717 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 24ms/step - accuracy: 0.5834 - loss: 0.8024 - val_accuracy: 0.5532 - val_loss: 0.8612 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 24ms/step - accuracy: 0.5862 - loss: 0.7852 - val_accuracy: 0.5632 - val_loss: 0.8452 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 25ms/step - accuracy: 0.6040 - loss: 0.7691 - val_accuracy: 0.5718 - val_loss: 0.8317 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.5966 - loss: 0.7602 - val_accuracy: 0.5876 - val_loss: 0.8164 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6138 - loss: 0.7436 - val_accuracy: 0.5905 - val_loss: 0.8077 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6179 - loss: 0.7381 - val_accuracy: 0.5948 - val_loss: 0.8048 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6204 - loss: 0.7336 - val_accuracy: 0.6006 - val_loss: 0.8019 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 25ms/step - accuracy: 0.6263 - loss: 0.7257 - val_accuracy: 0.5934 - val_loss: 0.7889 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 25ms/step - accuracy: 0.6334 - loss: 0.7096 - val_accuracy: 0.6221 - val_loss: 0.7852 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 25ms/step - accuracy: 0.6326 - loss: 0.7066 - val_accuracy: 0.6178 - val_loss: 0.7820 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 25ms/step - accuracy: 0.6253 - loss: 0.7079 - val_accuracy: 0.6221 - val_loss: 0.7726 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 25ms/step - accuracy: 0.6247 - loss: 0.7033 - val_accuracy: 0.6221 - val_loss: 0.7725 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6402 - loss: 0.6933 - val_accuracy: 0.6106 - val_loss: 0.7697 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6407 - loss: 0.6801 - val_accuracy: 0.6164 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6463 - loss: 0.6787 - val_accuracy: 0.6307 - val_loss: 0.7651 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 25ms/step - accuracy: 0.6493 - loss: 0.6812 - val_accuracy: 0.6207 - val_loss: 0.7620 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6509 - loss: 0.6764 - val_accuracy: 0.6236 - val_loss: 0.7560 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6476 - loss: 0.6715 - val_accuracy: 0.6106 - val_loss: 0.7513 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6511 - loss: 0.6691 - val_accuracy: 0.6178 - val_loss: 0.7625 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6544 - loss: 0.6611 - val_accuracy: 0.6078 - val_loss: 0.7594 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 24ms/step - accuracy: 0.6567 - loss: 0.6643 - val_accuracy: 0.6178 - val_loss: 0.7573 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6539 - loss: 0.6630 - val_accuracy: 0.6236 - val_loss: 0.7569 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 25ms/step - accuracy: 0.6575 - loss: 0.6542 - val_accuracy: 0.6193 - val_loss: 0.7451 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6549 - loss: 0.6556 - val_accuracy: 0.6351 - val_loss: 0.7467 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6620 - loss: 0.6515 - val_accuracy: 0.6135 - val_loss: 0.7488 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 25ms/step - accuracy: 0.6623 - loss: 0.6444 - val_accuracy: 0.6293 - val_loss: 0.7395 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6620 - loss: 0.6477 - val_accuracy: 0.6221 - val_loss: 0.7514 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 24ms/step - accuracy: 0.6656 - loss: 0.6467 - val_accuracy: 0.6279 - val_loss: 0.7540 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6704 - loss: 0.6356 - val_accuracy: 0.6221 - val_loss: 0.7479 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 24ms/step - accuracy: 0.6600 - loss: 0.6423 - val_accuracy: 0.6293 - val_loss: 0.7469 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 25ms/step - accuracy: 0.6772 - loss: 0.6379 - val_accuracy: 0.6322 - val_loss: 0.7305 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6775 - loss: 0.6293 - val_accuracy: 0.6365 - val_loss: 0.7346 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 24ms/step - accuracy: 0.6803 - loss: 0.6260 - val_accuracy: 0.6365 - val_loss: 0.7376 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6623 - loss: 0.6385 - val_accuracy: 0.6394 - val_loss: 0.7300 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6749 - loss: 0.6248 - val_accuracy: 0.6422 - val_loss: 0.7283 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6676 - loss: 0.6234 - val_accuracy: 0.6279 - val_loss: 0.7443 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6767 - loss: 0.6194 - val_accuracy: 0.6322 - val_loss: 0.7388 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6744 - loss: 0.6171 - val_accuracy: 0.6609 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6724 - loss: 0.6254 - val_accuracy: 0.6580 - val_loss: 0.7158 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6856 - loss: 0.6162 - val_accuracy: 0.6494 - val_loss: 0.7228 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6851 - loss: 0.6131 - val_accuracy: 0.6408 - val_loss: 0.7351 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.6108 - val_accuracy: 0.6437 - val_loss: 0.7301 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6800 - loss: 0.6163 - val_accuracy: 0.6494 - val_loss: 0.7141 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6833 - loss: 0.6095 - val_accuracy: 0.6494 - val_loss: 0.7278 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.6052 - val_accuracy: 0.6336 - val_loss: 0.7325 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.6023 - val_accuracy: 0.6250 - val_loss: 0.7384 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6831 - loss: 0.6086 - val_accuracy: 0.6509 - val_loss: 0.7269 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5984 - val_accuracy: 0.6408 - val_loss: 0.7295 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6914 - loss: 0.6071 - val_accuracy: 0.6595 - val_loss: 0.7145 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6874 - loss: 0.6008 - val_accuracy: 0.6264 - val_loss: 0.7427 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5856 - val_accuracy: 0.6250 - val_loss: 0.7337 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6950 - loss: 0.5932 - val_accuracy: 0.6466 - val_loss: 0.7233 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.7018 - loss: 0.5885 - val_accuracy: 0.6408 - val_loss: 0.7179 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5972 - val_accuracy: 0.6351 - val_loss: 0.7263 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6912 - loss: 0.5892 - val_accuracy: 0.6580 - val_loss: 0.7139 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.5926 - val_accuracy: 0.6408 - val_loss: 0.7287 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6978 - loss: 0.5865 - val_accuracy: 0.6379 - val_loss: 0.7260 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5875 - val_accuracy: 0.6408 - val_loss: 0.7146 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7028 - loss: 0.5851 - val_accuracy: 0.6322 - val_loss: 0.7249 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 24ms/step - accuracy: 0.6960 - loss: 0.5896 - val_accuracy: 0.6552 - val_loss: 0.7133 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7001 - loss: 0.5866 - val_accuracy: 0.6466 - val_loss: 0.7207 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5835 - val_accuracy: 0.6121 - val_loss: 0.7447 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7066 - loss: 0.5826 - val_accuracy: 0.6351 - val_loss: 0.7300 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7117 - loss: 0.5729 - val_accuracy: 0.6336 - val_loss: 0.7260 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5798 - val_accuracy: 0.6264 - val_loss: 0.7208 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7031 - loss: 0.5744 - val_accuracy: 0.6437 - val_loss: 0.7207 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5724 - val_accuracy: 0.6408 - val_loss: 0.7204 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5759 - val_accuracy: 0.6279 - val_loss: 0.7160 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5809 - val_accuracy: 0.6293 - val_loss: 0.7251 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7125 - loss: 0.5684 - val_accuracy: 0.6509 - val_loss: 0.7137 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5737 - val_accuracy: 0.6408 - val_loss: 0.7104 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5814 - val_accuracy: 0.6480 - val_loss: 0.7177 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5668 - val_accuracy: 0.6250 - val_loss: 0.7277 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.7132 - loss: 0.5698 - val_accuracy: 0.6293 - val_loss: 0.7250 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5734 - val_accuracy: 0.6322 - val_loss: 0.7302 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7102 - loss: 0.5681 - val_accuracy: 0.6523 - val_loss: 0.7087 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7104 - loss: 0.5731 - val_accuracy: 0.6408 - val_loss: 0.7364 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7122 - loss: 0.5669 - val_accuracy: 0.6250 - val_loss: 0.7301 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7183 - loss: 0.5545 - val_accuracy: 0.6250 - val_loss: 0.7349 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7140 - loss: 0.5738 - val_accuracy: 0.6250 - val_loss: 0.7332 - learning_rate: 0.0010
Epoch 85/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5665 - val_accuracy: 0.6494 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7110 - loss: 0.5601 - val_accuracy: 0.6523 - val_loss: 0.7123 - learning_rate: 0.0010
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7125 - loss: 0.5579 - val_accuracy: 0.6422 - val_loss: 0.7030 - learning_rate: 0.0010
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7087 - loss: 0.5648 - val_accuracy: 0.6365 - val_loss: 0.7289 - learning_rate: 0.0010
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7173 - loss: 0.5624 - val_accuracy: 0.6580 - val_loss: 0.7271 - learning_rate: 0.0010
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7196 - loss: 0.5569 - val_accuracy: 0.6451 - val_loss: 0.7179 - learning_rate: 0.0010
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7191 - loss: 0.5551 - val_accuracy: 0.6365 - val_loss: 0.7240 - learning_rate: 0.0010
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7165 - loss: 0.5574 - val_accuracy: 0.6379 - val_loss: 0.7141 - learning_rate: 0.0010
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7102 - loss: 0.5577 - val_accuracy: 0.6451 - val_loss: 0.7035 - learning_rate: 0.0010
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7178 - loss: 0.5583 - val_accuracy: 0.6466 - val_loss: 0.7173 - learning_rate: 0.0010
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7082 - loss: 0.5532 - val_accuracy: 0.6365 - val_loss: 0.7306 - learning_rate: 0.0010
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7092 - loss: 0.5569 - val_accuracy: 0.6480 - val_loss: 0.7157 - learning_rate: 0.0010
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7244 - loss: 0.5569 - val_accuracy: 0.6408 - val_loss: 0.7314 - learning_rate: 0.0010
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7158 - loss: 0.5584 - val_accuracy: 0.6480 - val_loss: 0.7184 - learning_rate: 0.0010
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7084 - loss: 0.5580 - val_accuracy: 0.6422 - val_loss: 0.7260 - learning_rate: 0.0010
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5530 - val_accuracy: 0.6466 - val_loss: 0.7367 - learning_rate: 0.0010
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7198 - loss: 0.5540 - val_accuracy: 0.6480 - val_loss: 0.7199 - learning_rate: 0.0010
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7203 - loss: 0.5538 - val_accuracy: 0.6437 - val_loss: 0.7380 - learning_rate: 0.0010
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7249 - loss: 0.5472 - val_accuracy: 0.6451 - val_loss: 0.7221 - learning_rate: 0.0010
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7236 - loss: 0.5523 - val_accuracy: 0.6408 - val_loss: 0.7162 - learning_rate: 0.0010
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7127 - loss: 0.5530 - val_accuracy: 0.6451 - val_loss: 0.7272 - learning_rate: 0.0010
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7259 - loss: 0.5465 - val_accuracy: 0.6408 - val_loss: 0.7171 - learning_rate: 0.0010
Epoch 107/500

Epoch 107: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7234 - loss: 0.5477 - val_accuracy: 0.6595 - val_loss: 0.7189 - learning_rate: 0.0010
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5178 - val_accuracy: 0.6451 - val_loss: 0.7278 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5177 - val_accuracy: 0.6408 - val_loss: 0.7167 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7487 - loss: 0.5123 - val_accuracy: 0.6451 - val_loss: 0.7246 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5065 - val_accuracy: 0.6451 - val_loss: 0.7197 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5097 - val_accuracy: 0.6523 - val_loss: 0.7032 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7416 - loss: 0.5122 - val_accuracy: 0.6537 - val_loss: 0.7083 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7386 - loss: 0.5188 - val_accuracy: 0.6638 - val_loss: 0.7104 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7475 - loss: 0.5059 - val_accuracy: 0.6307 - val_loss: 0.7330 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.5130 - val_accuracy: 0.6351 - val_loss: 0.7126 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.5101 - val_accuracy: 0.6494 - val_loss: 0.7161 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.5096 - val_accuracy: 0.6437 - val_loss: 0.7235 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7548 - loss: 0.5005 - val_accuracy: 0.6437 - val_loss: 0.7178 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5026 - val_accuracy: 0.6494 - val_loss: 0.7148 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5116 - val_accuracy: 0.6609 - val_loss: 0.7213 - learning_rate: 5.0000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5050 - val_accuracy: 0.6523 - val_loss: 0.7227 - learning_rate: 5.0000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5063 - val_accuracy: 0.6609 - val_loss: 0.7166 - learning_rate: 5.0000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7485 - loss: 0.5121 - val_accuracy: 0.6509 - val_loss: 0.7055 - learning_rate: 5.0000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5092 - val_accuracy: 0.6437 - val_loss: 0.7204 - learning_rate: 5.0000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.4984 - val_accuracy: 0.6523 - val_loss: 0.7134 - learning_rate: 5.0000e-04
Epoch 127/500

Epoch 127: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4915 - val_accuracy: 0.6580 - val_loss: 0.7172 - learning_rate: 5.0000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7571 - loss: 0.4868 - val_accuracy: 0.6480 - val_loss: 0.7265 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7718 - loss: 0.4737 - val_accuracy: 0.6509 - val_loss: 0.7309 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7622 - loss: 0.4863 - val_accuracy: 0.6566 - val_loss: 0.7287 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7652 - loss: 0.4813 - val_accuracy: 0.6537 - val_loss: 0.7247 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7667 - loss: 0.4775 - val_accuracy: 0.6451 - val_loss: 0.7319 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7693 - loss: 0.4757 - val_accuracy: 0.6394 - val_loss: 0.7257 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7716 - loss: 0.4763 - val_accuracy: 0.6451 - val_loss: 0.7220 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7662 - loss: 0.4781 - val_accuracy: 0.6480 - val_loss: 0.7326 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7604 - loss: 0.4830 - val_accuracy: 0.6379 - val_loss: 0.7342 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7703 - loss: 0.4743 - val_accuracy: 0.6408 - val_loss: 0.7326 - learning_rate: 2.5000e-04
Epoch 137: early stopping
Restoring model weights from the end of the best epoch: 87.
Training complete. Best epoch: 87 of 137. Best val_loss: 0.7030, val_accuracy: 0.6422

========== Evaluation: LOSO fold 27 / held-out EMS0028 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        33         6         1
  intermedia        21        36        23
  max_intens         0         3        37

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.611     0.825     0.702        40
intermediate_intensity      0.800     0.450     0.576        80
         max_intensity      0.607     0.925     0.733        40

              accuracy                          0.662       160
             macro avg      0.673     0.733     0.670       160
          weighted avg      0.704     0.662     0.647       160

Overall accuracy: 0.6625

============================================================
Fold 28 of 30: holding out EMS0029
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.19e-07, 9.66e-07]
  Per-channel std range:  [7.25e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 116ms/step - accuracy: 0.4561 - loss: 1.0319 - val_accuracy: 0.4713 - val_loss: 1.0415 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5134 - loss: 0.9286 - val_accuracy: 0.5086 - val_loss: 0.9626 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5423 - loss: 0.8674 - val_accuracy: 0.5359 - val_loss: 0.9139 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5634 - loss: 0.8346 - val_accuracy: 0.5388 - val_loss: 0.8926 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5682 - loss: 0.8135 - val_accuracy: 0.5546 - val_loss: 0.8713 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5865 - loss: 0.7893 - val_accuracy: 0.5647 - val_loss: 0.8547 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.5963 - loss: 0.7783 - val_accuracy: 0.5733 - val_loss: 0.8461 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.5951 - loss: 0.7667 - val_accuracy: 0.5661 - val_loss: 0.8389 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 23ms/step - accuracy: 0.6002 - loss: 0.7605 - val_accuracy: 0.5848 - val_loss: 0.8321 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 23ms/step - accuracy: 0.6080 - loss: 0.7488 - val_accuracy: 0.6063 - val_loss: 0.8155 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6136 - loss: 0.7394 - val_accuracy: 0.5891 - val_loss: 0.8243 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 23ms/step - accuracy: 0.6227 - loss: 0.7284 - val_accuracy: 0.5920 - val_loss: 0.8180 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6194 - loss: 0.7251 - val_accuracy: 0.5948 - val_loss: 0.8164 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6369 - loss: 0.7170 - val_accuracy: 0.5905 - val_loss: 0.8161 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6316 - loss: 0.7137 - val_accuracy: 0.5819 - val_loss: 0.8115 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6334 - loss: 0.7105 - val_accuracy: 0.5934 - val_loss: 0.8063 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6359 - loss: 0.7067 - val_accuracy: 0.6006 - val_loss: 0.8097 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6318 - loss: 0.6981 - val_accuracy: 0.5819 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6445 - loss: 0.6916 - val_accuracy: 0.6034 - val_loss: 0.7947 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6455 - loss: 0.6855 - val_accuracy: 0.5934 - val_loss: 0.7963 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6509 - loss: 0.6850 - val_accuracy: 0.6092 - val_loss: 0.7819 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6415 - loss: 0.6767 - val_accuracy: 0.6049 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6552 - loss: 0.6726 - val_accuracy: 0.6221 - val_loss: 0.7751 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 23ms/step - accuracy: 0.6544 - loss: 0.6707 - val_accuracy: 0.6164 - val_loss: 0.7725 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6557 - loss: 0.6661 - val_accuracy: 0.6020 - val_loss: 0.7921 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6610 - loss: 0.6622 - val_accuracy: 0.6049 - val_loss: 0.7778 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 23ms/step - accuracy: 0.6552 - loss: 0.6620 - val_accuracy: 0.6264 - val_loss: 0.7744 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6585 - loss: 0.6635 - val_accuracy: 0.6207 - val_loss: 0.7676 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6592 - loss: 0.6603 - val_accuracy: 0.6049 - val_loss: 0.7710 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6628 - loss: 0.6524 - val_accuracy: 0.6293 - val_loss: 0.7581 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6691 - loss: 0.6554 - val_accuracy: 0.6006 - val_loss: 0.7819 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6752 - loss: 0.6409 - val_accuracy: 0.6164 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 23ms/step - accuracy: 0.6694 - loss: 0.6440 - val_accuracy: 0.5948 - val_loss: 0.7716 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6676 - loss: 0.6515 - val_accuracy: 0.6264 - val_loss: 0.7544 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6686 - loss: 0.6450 - val_accuracy: 0.6307 - val_loss: 0.7509 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6661 - loss: 0.6506 - val_accuracy: 0.6293 - val_loss: 0.7616 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6777 - loss: 0.6355 - val_accuracy: 0.6236 - val_loss: 0.7459 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6722 - loss: 0.6363 - val_accuracy: 0.6121 - val_loss: 0.7685 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6760 - loss: 0.6332 - val_accuracy: 0.6394 - val_loss: 0.7464 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6785 - loss: 0.6292 - val_accuracy: 0.6063 - val_loss: 0.7557 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6737 - loss: 0.6381 - val_accuracy: 0.6250 - val_loss: 0.7565 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6808 - loss: 0.6222 - val_accuracy: 0.6236 - val_loss: 0.7528 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.6287 - val_accuracy: 0.6193 - val_loss: 0.7676 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.6861 - loss: 0.6181 - val_accuracy: 0.6322 - val_loss: 0.7416 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6907 - loss: 0.6243 - val_accuracy: 0.6293 - val_loss: 0.7442 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.6879 - loss: 0.6165 - val_accuracy: 0.6264 - val_loss: 0.7558 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6869 - loss: 0.6173 - val_accuracy: 0.6250 - val_loss: 0.7415 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6884 - loss: 0.6159 - val_accuracy: 0.6351 - val_loss: 0.7449 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6899 - loss: 0.6124 - val_accuracy: 0.6221 - val_loss: 0.7620 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.6120 - val_accuracy: 0.6264 - val_loss: 0.7496 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6856 - loss: 0.6199 - val_accuracy: 0.6149 - val_loss: 0.7682 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 24ms/step - accuracy: 0.6904 - loss: 0.6102 - val_accuracy: 0.6408 - val_loss: 0.7383 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 24ms/step - accuracy: 0.6859 - loss: 0.6172 - val_accuracy: 0.6293 - val_loss: 0.7507 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 24ms/step - accuracy: 0.6912 - loss: 0.6085 - val_accuracy: 0.6264 - val_loss: 0.7364 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 25ms/step - accuracy: 0.6861 - loss: 0.6145 - val_accuracy: 0.6494 - val_loss: 0.7286 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 25ms/step - accuracy: 0.6998 - loss: 0.6006 - val_accuracy: 0.6451 - val_loss: 0.7220 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.7013 - loss: 0.6026 - val_accuracy: 0.6293 - val_loss: 0.7480 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 24ms/step - accuracy: 0.6995 - loss: 0.6064 - val_accuracy: 0.6408 - val_loss: 0.7338 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 24ms/step - accuracy: 0.6876 - loss: 0.6057 - val_accuracy: 0.6466 - val_loss: 0.7409 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.6990 - loss: 0.6018 - val_accuracy: 0.6307 - val_loss: 0.7476 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.6978 - loss: 0.6026 - val_accuracy: 0.6422 - val_loss: 0.7356 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6085 - val_accuracy: 0.6451 - val_loss: 0.7261 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.6957 - loss: 0.6007 - val_accuracy: 0.6365 - val_loss: 0.7379 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.6983 - loss: 0.5870 - val_accuracy: 0.6394 - val_loss: 0.7309 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.7013 - loss: 0.5986 - val_accuracy: 0.6466 - val_loss: 0.7272 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.7021 - loss: 0.5896 - val_accuracy: 0.6624 - val_loss: 0.7366 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 24ms/step - accuracy: 0.6932 - loss: 0.5966 - val_accuracy: 0.6422 - val_loss: 0.7382 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5923 - val_accuracy: 0.6207 - val_loss: 0.7587 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5964 - val_accuracy: 0.6193 - val_loss: 0.7750 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.6995 - loss: 0.5945 - val_accuracy: 0.6509 - val_loss: 0.7372 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.6980 - loss: 0.5906 - val_accuracy: 0.6365 - val_loss: 0.7457 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.7006 - loss: 0.5845 - val_accuracy: 0.6221 - val_loss: 0.7682 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7031 - loss: 0.5893 - val_accuracy: 0.6351 - val_loss: 0.7562 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7066 - loss: 0.5868 - val_accuracy: 0.6394 - val_loss: 0.7332 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7033 - loss: 0.5838 - val_accuracy: 0.6365 - val_loss: 0.7425 - learning_rate: 0.0010
Epoch 76/500

Epoch 76: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7016 - loss: 0.5897 - val_accuracy: 0.6566 - val_loss: 0.7336 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 24ms/step - accuracy: 0.7191 - loss: 0.5651 - val_accuracy: 0.6494 - val_loss: 0.7215 - learning_rate: 5.0000e-04
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7300 - loss: 0.5475 - val_accuracy: 0.6552 - val_loss: 0.7183 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 25ms/step - accuracy: 0.7269 - loss: 0.5505 - val_accuracy: 0.6509 - val_loss: 0.7145 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7350 - loss: 0.5447 - val_accuracy: 0.6394 - val_loss: 0.7238 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 24ms/step - accuracy: 0.7292 - loss: 0.5536 - val_accuracy: 0.6537 - val_loss: 0.7168 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 24ms/step - accuracy: 0.7262 - loss: 0.5416 - val_accuracy: 0.6509 - val_loss: 0.7122 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5487 - val_accuracy: 0.6580 - val_loss: 0.7237 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7269 - loss: 0.5476 - val_accuracy: 0.6523 - val_loss: 0.7094 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7386 - loss: 0.5432 - val_accuracy: 0.6537 - val_loss: 0.7143 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7353 - loss: 0.5406 - val_accuracy: 0.6552 - val_loss: 0.7129 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7284 - loss: 0.5406 - val_accuracy: 0.6566 - val_loss: 0.7127 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5435 - val_accuracy: 0.6537 - val_loss: 0.7178 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7295 - loss: 0.5464 - val_accuracy: 0.6509 - val_loss: 0.7001 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7388 - loss: 0.5364 - val_accuracy: 0.6466 - val_loss: 0.7184 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7345 - loss: 0.5347 - val_accuracy: 0.6494 - val_loss: 0.7170 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5387 - val_accuracy: 0.6437 - val_loss: 0.7204 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7399 - loss: 0.5324 - val_accuracy: 0.6480 - val_loss: 0.7244 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7328 - loss: 0.5335 - val_accuracy: 0.6595 - val_loss: 0.7143 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5373 - val_accuracy: 0.6509 - val_loss: 0.7160 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5359 - val_accuracy: 0.6466 - val_loss: 0.7237 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7330 - loss: 0.5364 - val_accuracy: 0.6422 - val_loss: 0.7138 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7409 - loss: 0.5344 - val_accuracy: 0.6494 - val_loss: 0.7263 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7386 - loss: 0.5367 - val_accuracy: 0.6595 - val_loss: 0.7200 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5277 - val_accuracy: 0.6494 - val_loss: 0.7332 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7297 - loss: 0.5348 - val_accuracy: 0.6422 - val_loss: 0.7336 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 24ms/step - accuracy: 0.7373 - loss: 0.5278 - val_accuracy: 0.6451 - val_loss: 0.7094 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7421 - loss: 0.5312 - val_accuracy: 0.6537 - val_loss: 0.7142 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7439 - loss: 0.5289 - val_accuracy: 0.6624 - val_loss: 0.7112 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7396 - loss: 0.5242 - val_accuracy: 0.6494 - val_loss: 0.7195 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7378 - loss: 0.5265 - val_accuracy: 0.6552 - val_loss: 0.7075 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7414 - loss: 0.5270 - val_accuracy: 0.6494 - val_loss: 0.7093 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7279 - loss: 0.5330 - val_accuracy: 0.6466 - val_loss: 0.7215 - learning_rate: 5.0000e-04
Epoch 109/500

Epoch 109: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7432 - loss: 0.5222 - val_accuracy: 0.6466 - val_loss: 0.7159 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7477 - loss: 0.5103 - val_accuracy: 0.6509 - val_loss: 0.7120 - learning_rate: 2.5000e-04
Epoch 111/500
124/124 - 3s - 24ms/step - accuracy: 0.7553 - loss: 0.5073 - val_accuracy: 0.6351 - val_loss: 0.7323 - learning_rate: 2.5000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7533 - loss: 0.5065 - val_accuracy: 0.6365 - val_loss: 0.7287 - learning_rate: 2.5000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7500 - loss: 0.5032 - val_accuracy: 0.6537 - val_loss: 0.7193 - learning_rate: 2.5000e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.5029 - val_accuracy: 0.6624 - val_loss: 0.7187 - learning_rate: 2.5000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.5032 - val_accuracy: 0.6351 - val_loss: 0.7361 - learning_rate: 2.5000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7459 - loss: 0.5033 - val_accuracy: 0.6580 - val_loss: 0.7328 - learning_rate: 2.5000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7515 - loss: 0.5106 - val_accuracy: 0.6509 - val_loss: 0.7273 - learning_rate: 2.5000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4944 - val_accuracy: 0.6494 - val_loss: 0.7249 - learning_rate: 2.5000e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.4974 - val_accuracy: 0.6537 - val_loss: 0.7138 - learning_rate: 2.5000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7462 - loss: 0.5089 - val_accuracy: 0.6537 - val_loss: 0.7182 - learning_rate: 2.5000e-04
Epoch 121/500
124/124 - 3s - 24ms/step - accuracy: 0.7457 - loss: 0.5115 - val_accuracy: 0.6537 - val_loss: 0.7176 - learning_rate: 2.5000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7495 - loss: 0.5004 - val_accuracy: 0.6523 - val_loss: 0.7192 - learning_rate: 2.5000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7513 - loss: 0.5036 - val_accuracy: 0.6494 - val_loss: 0.7205 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7508 - loss: 0.5018 - val_accuracy: 0.6466 - val_loss: 0.7281 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.4989 - val_accuracy: 0.6552 - val_loss: 0.7104 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7574 - loss: 0.4942 - val_accuracy: 0.6451 - val_loss: 0.7206 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.4990 - val_accuracy: 0.6379 - val_loss: 0.7299 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7596 - loss: 0.5012 - val_accuracy: 0.6509 - val_loss: 0.7218 - learning_rate: 2.5000e-04
Epoch 129/500

Epoch 129: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 24ms/step - accuracy: 0.7566 - loss: 0.5004 - val_accuracy: 0.6451 - val_loss: 0.7240 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7639 - loss: 0.4899 - val_accuracy: 0.6451 - val_loss: 0.7269 - learning_rate: 1.2500e-04
Epoch 131/500
124/124 - 3s - 24ms/step - accuracy: 0.7581 - loss: 0.4873 - val_accuracy: 0.6537 - val_loss: 0.7162 - learning_rate: 1.2500e-04
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7665 - loss: 0.4821 - val_accuracy: 0.6466 - val_loss: 0.7198 - learning_rate: 1.2500e-04
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7622 - loss: 0.4862 - val_accuracy: 0.6537 - val_loss: 0.7117 - learning_rate: 1.2500e-04
Epoch 134/500
124/124 - 3s - 24ms/step - accuracy: 0.7624 - loss: 0.4870 - val_accuracy: 0.6480 - val_loss: 0.7224 - learning_rate: 1.2500e-04
Epoch 135/500
124/124 - 3s - 24ms/step - accuracy: 0.7599 - loss: 0.4880 - val_accuracy: 0.6466 - val_loss: 0.7234 - learning_rate: 1.2500e-04
Epoch 136/500
124/124 - 3s - 24ms/step - accuracy: 0.7574 - loss: 0.4944 - val_accuracy: 0.6466 - val_loss: 0.7174 - learning_rate: 1.2500e-04
Epoch 137/500
124/124 - 3s - 24ms/step - accuracy: 0.7604 - loss: 0.4870 - val_accuracy: 0.6537 - val_loss: 0.7179 - learning_rate: 1.2500e-04
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7584 - loss: 0.4934 - val_accuracy: 0.6523 - val_loss: 0.7197 - learning_rate: 1.2500e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7627 - loss: 0.4837 - val_accuracy: 0.6537 - val_loss: 0.7185 - learning_rate: 1.2500e-04
Epoch 139: early stopping
Restoring model weights from the end of the best epoch: 89.
Training complete. Best epoch: 89 of 139. Best val_loss: 0.7001, val_accuracy: 0.6509

========== Evaluation: LOSO fold 28 / held-out EMS0029 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        30         9         1
  intermedia        12        48        20
  max_intens         0         3        37

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.714     0.750     0.732        40
intermediate_intensity      0.800     0.600     0.686        80
         max_intensity      0.638     0.925     0.755        40

              accuracy                          0.719       160
             macro avg      0.717     0.758     0.724       160
          weighted avg      0.738     0.719     0.715       160

Overall accuracy: 0.7188

============================================================
Fold 29 of 30: holding out EMS0030
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.17e-07, 9.65e-07]
  Per-channel std range:  [7.22e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 15s - 121ms/step - accuracy: 0.4653 - loss: 1.0199 - val_accuracy: 0.4914 - val_loss: 1.0304 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 25ms/step - accuracy: 0.5385 - loss: 0.8944 - val_accuracy: 0.5330 - val_loss: 0.9406 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 24ms/step - accuracy: 0.5631 - loss: 0.8494 - val_accuracy: 0.5532 - val_loss: 0.8938 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 24ms/step - accuracy: 0.5786 - loss: 0.8158 - val_accuracy: 0.5848 - val_loss: 0.8609 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 25ms/step - accuracy: 0.5931 - loss: 0.7920 - val_accuracy: 0.5848 - val_loss: 0.8380 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 25ms/step - accuracy: 0.5946 - loss: 0.7728 - val_accuracy: 0.5848 - val_loss: 0.8370 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 24ms/step - accuracy: 0.6032 - loss: 0.7610 - val_accuracy: 0.5905 - val_loss: 0.8160 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6126 - loss: 0.7466 - val_accuracy: 0.6034 - val_loss: 0.8002 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6136 - loss: 0.7377 - val_accuracy: 0.5920 - val_loss: 0.8026 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6159 - loss: 0.7283 - val_accuracy: 0.6092 - val_loss: 0.7898 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 24ms/step - accuracy: 0.6199 - loss: 0.7169 - val_accuracy: 0.6063 - val_loss: 0.7854 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6242 - loss: 0.7120 - val_accuracy: 0.6020 - val_loss: 0.8027 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 24ms/step - accuracy: 0.6336 - loss: 0.7011 - val_accuracy: 0.6264 - val_loss: 0.7781 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 24ms/step - accuracy: 0.6324 - loss: 0.6982 - val_accuracy: 0.6264 - val_loss: 0.7838 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6415 - loss: 0.6919 - val_accuracy: 0.6250 - val_loss: 0.7737 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 24ms/step - accuracy: 0.6468 - loss: 0.6832 - val_accuracy: 0.6351 - val_loss: 0.7727 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 24ms/step - accuracy: 0.6453 - loss: 0.6801 - val_accuracy: 0.6193 - val_loss: 0.7758 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 24ms/step - accuracy: 0.6498 - loss: 0.6762 - val_accuracy: 0.6264 - val_loss: 0.7664 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 24ms/step - accuracy: 0.6496 - loss: 0.6710 - val_accuracy: 0.6307 - val_loss: 0.7659 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 24ms/step - accuracy: 0.6539 - loss: 0.6691 - val_accuracy: 0.6437 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 24ms/step - accuracy: 0.6590 - loss: 0.6635 - val_accuracy: 0.6236 - val_loss: 0.7787 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 24ms/step - accuracy: 0.6519 - loss: 0.6599 - val_accuracy: 0.6379 - val_loss: 0.7476 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 24ms/step - accuracy: 0.6635 - loss: 0.6545 - val_accuracy: 0.6408 - val_loss: 0.7586 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6620 - loss: 0.6556 - val_accuracy: 0.6422 - val_loss: 0.7515 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 24ms/step - accuracy: 0.6684 - loss: 0.6475 - val_accuracy: 0.6408 - val_loss: 0.7629 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 24ms/step - accuracy: 0.6678 - loss: 0.6444 - val_accuracy: 0.6523 - val_loss: 0.7423 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6737 - loss: 0.6405 - val_accuracy: 0.6595 - val_loss: 0.7425 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 24ms/step - accuracy: 0.6722 - loss: 0.6386 - val_accuracy: 0.6580 - val_loss: 0.7315 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 24ms/step - accuracy: 0.6724 - loss: 0.6303 - val_accuracy: 0.6609 - val_loss: 0.7371 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 24ms/step - accuracy: 0.6724 - loss: 0.6344 - val_accuracy: 0.6480 - val_loss: 0.7464 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 24ms/step - accuracy: 0.6785 - loss: 0.6289 - val_accuracy: 0.6609 - val_loss: 0.7347 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 25ms/step - accuracy: 0.6663 - loss: 0.6338 - val_accuracy: 0.6624 - val_loss: 0.7220 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6856 - loss: 0.6195 - val_accuracy: 0.6595 - val_loss: 0.7329 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6864 - loss: 0.6199 - val_accuracy: 0.6609 - val_loss: 0.7302 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6848 - loss: 0.6258 - val_accuracy: 0.6537 - val_loss: 0.7510 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 24ms/step - accuracy: 0.6874 - loss: 0.6182 - val_accuracy: 0.6437 - val_loss: 0.7471 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 24ms/step - accuracy: 0.6864 - loss: 0.6141 - val_accuracy: 0.6624 - val_loss: 0.7259 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 24ms/step - accuracy: 0.6914 - loss: 0.6067 - val_accuracy: 0.6552 - val_loss: 0.7381 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6079 - val_accuracy: 0.6365 - val_loss: 0.7463 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 24ms/step - accuracy: 0.6945 - loss: 0.6149 - val_accuracy: 0.6509 - val_loss: 0.7336 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 24ms/step - accuracy: 0.6899 - loss: 0.6060 - val_accuracy: 0.6667 - val_loss: 0.7169 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 24ms/step - accuracy: 0.6894 - loss: 0.6085 - val_accuracy: 0.6595 - val_loss: 0.7397 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 24ms/step - accuracy: 0.6935 - loss: 0.6098 - val_accuracy: 0.6566 - val_loss: 0.7317 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 24ms/step - accuracy: 0.7036 - loss: 0.6032 - val_accuracy: 0.6681 - val_loss: 0.7266 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 24ms/step - accuracy: 0.7021 - loss: 0.6000 - val_accuracy: 0.6480 - val_loss: 0.7432 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 24ms/step - accuracy: 0.7089 - loss: 0.5882 - val_accuracy: 0.6480 - val_loss: 0.7277 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 24ms/step - accuracy: 0.6945 - loss: 0.5925 - val_accuracy: 0.6480 - val_loss: 0.7234 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 24ms/step - accuracy: 0.6945 - loss: 0.6001 - val_accuracy: 0.6609 - val_loss: 0.7159 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 24ms/step - accuracy: 0.6932 - loss: 0.5901 - val_accuracy: 0.6537 - val_loss: 0.7220 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 24ms/step - accuracy: 0.7044 - loss: 0.5963 - val_accuracy: 0.6523 - val_loss: 0.7316 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 24ms/step - accuracy: 0.7077 - loss: 0.5869 - val_accuracy: 0.6609 - val_loss: 0.7308 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.7039 - loss: 0.5906 - val_accuracy: 0.6494 - val_loss: 0.7356 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.7013 - loss: 0.5867 - val_accuracy: 0.6552 - val_loss: 0.7374 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.7077 - loss: 0.5869 - val_accuracy: 0.6537 - val_loss: 0.7359 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5823 - val_accuracy: 0.6624 - val_loss: 0.7317 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.7021 - loss: 0.5897 - val_accuracy: 0.6537 - val_loss: 0.7470 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 24ms/step - accuracy: 0.7008 - loss: 0.5837 - val_accuracy: 0.6724 - val_loss: 0.7089 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.7099 - loss: 0.5781 - val_accuracy: 0.6580 - val_loss: 0.7219 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5876 - val_accuracy: 0.6552 - val_loss: 0.7296 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 24ms/step - accuracy: 0.7011 - loss: 0.5800 - val_accuracy: 0.6509 - val_loss: 0.7254 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 24ms/step - accuracy: 0.7104 - loss: 0.5712 - val_accuracy: 0.6523 - val_loss: 0.7397 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 24ms/step - accuracy: 0.7059 - loss: 0.5745 - val_accuracy: 0.6595 - val_loss: 0.7360 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 24ms/step - accuracy: 0.7066 - loss: 0.5778 - val_accuracy: 0.6681 - val_loss: 0.7184 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 24ms/step - accuracy: 0.7069 - loss: 0.5816 - val_accuracy: 0.6552 - val_loss: 0.7368 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 24ms/step - accuracy: 0.7181 - loss: 0.5720 - val_accuracy: 0.6523 - val_loss: 0.7223 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 24ms/step - accuracy: 0.7153 - loss: 0.5740 - val_accuracy: 0.6624 - val_loss: 0.7186 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7145 - loss: 0.5678 - val_accuracy: 0.6394 - val_loss: 0.7312 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 24ms/step - accuracy: 0.7150 - loss: 0.5597 - val_accuracy: 0.6667 - val_loss: 0.7203 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 24ms/step - accuracy: 0.7142 - loss: 0.5653 - val_accuracy: 0.6523 - val_loss: 0.7387 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 24ms/step - accuracy: 0.7137 - loss: 0.5675 - val_accuracy: 0.6509 - val_loss: 0.7299 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 24ms/step - accuracy: 0.7003 - loss: 0.5834 - val_accuracy: 0.6523 - val_loss: 0.7236 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 24ms/step - accuracy: 0.7104 - loss: 0.5759 - val_accuracy: 0.6494 - val_loss: 0.7246 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 24ms/step - accuracy: 0.7244 - loss: 0.5539 - val_accuracy: 0.6480 - val_loss: 0.7367 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 24ms/step - accuracy: 0.7059 - loss: 0.5736 - val_accuracy: 0.6710 - val_loss: 0.7109 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 24ms/step - accuracy: 0.7094 - loss: 0.5716 - val_accuracy: 0.6494 - val_loss: 0.7235 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 24ms/step - accuracy: 0.7117 - loss: 0.5658 - val_accuracy: 0.6566 - val_loss: 0.7216 - learning_rate: 0.0010
Epoch 77/500

Epoch 77: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 24ms/step - accuracy: 0.7137 - loss: 0.5637 - val_accuracy: 0.6624 - val_loss: 0.7291 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 24ms/step - accuracy: 0.7252 - loss: 0.5390 - val_accuracy: 0.6638 - val_loss: 0.7137 - learning_rate: 5.0000e-04
Epoch 79/500
124/124 - 3s - 24ms/step - accuracy: 0.7383 - loss: 0.5331 - val_accuracy: 0.6652 - val_loss: 0.6920 - learning_rate: 5.0000e-04
Epoch 80/500
124/124 - 3s - 24ms/step - accuracy: 0.7444 - loss: 0.5285 - val_accuracy: 0.6509 - val_loss: 0.7100 - learning_rate: 5.0000e-04
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5284 - val_accuracy: 0.6566 - val_loss: 0.7095 - learning_rate: 5.0000e-04
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5268 - val_accuracy: 0.6509 - val_loss: 0.7108 - learning_rate: 5.0000e-04
Epoch 83/500
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.5220 - val_accuracy: 0.6509 - val_loss: 0.7117 - learning_rate: 5.0000e-04
Epoch 84/500
124/124 - 3s - 24ms/step - accuracy: 0.7452 - loss: 0.5228 - val_accuracy: 0.6422 - val_loss: 0.7074 - learning_rate: 5.0000e-04
Epoch 85/500
124/124 - 3s - 24ms/step - accuracy: 0.7338 - loss: 0.5300 - val_accuracy: 0.6466 - val_loss: 0.7145 - learning_rate: 5.0000e-04
Epoch 86/500
124/124 - 3s - 24ms/step - accuracy: 0.7437 - loss: 0.5252 - val_accuracy: 0.6523 - val_loss: 0.7111 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 24ms/step - accuracy: 0.7388 - loss: 0.5241 - val_accuracy: 0.6580 - val_loss: 0.7076 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 24ms/step - accuracy: 0.7437 - loss: 0.5245 - val_accuracy: 0.6552 - val_loss: 0.7047 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 24ms/step - accuracy: 0.7406 - loss: 0.5216 - val_accuracy: 0.6422 - val_loss: 0.7011 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 24ms/step - accuracy: 0.7518 - loss: 0.5171 - val_accuracy: 0.6552 - val_loss: 0.6946 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 24ms/step - accuracy: 0.7366 - loss: 0.5204 - val_accuracy: 0.6580 - val_loss: 0.6982 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 24ms/step - accuracy: 0.7429 - loss: 0.5179 - val_accuracy: 0.6480 - val_loss: 0.6943 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 24ms/step - accuracy: 0.7503 - loss: 0.5156 - val_accuracy: 0.6537 - val_loss: 0.6963 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5291 - val_accuracy: 0.6580 - val_loss: 0.7008 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5158 - val_accuracy: 0.6537 - val_loss: 0.7045 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 24ms/step - accuracy: 0.7467 - loss: 0.5162 - val_accuracy: 0.6494 - val_loss: 0.6953 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 24ms/step - accuracy: 0.7429 - loss: 0.5173 - val_accuracy: 0.6624 - val_loss: 0.6899 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 24ms/step - accuracy: 0.7490 - loss: 0.5151 - val_accuracy: 0.6580 - val_loss: 0.6903 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 24ms/step - accuracy: 0.7386 - loss: 0.5182 - val_accuracy: 0.6580 - val_loss: 0.6960 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 24ms/step - accuracy: 0.7523 - loss: 0.5164 - val_accuracy: 0.6552 - val_loss: 0.6899 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 24ms/step - accuracy: 0.7452 - loss: 0.5193 - val_accuracy: 0.6566 - val_loss: 0.7043 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 24ms/step - accuracy: 0.7551 - loss: 0.5092 - val_accuracy: 0.6710 - val_loss: 0.6830 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 24ms/step - accuracy: 0.7452 - loss: 0.5200 - val_accuracy: 0.6494 - val_loss: 0.6977 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 24ms/step - accuracy: 0.7404 - loss: 0.5167 - val_accuracy: 0.6595 - val_loss: 0.6952 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 24ms/step - accuracy: 0.7447 - loss: 0.5138 - val_accuracy: 0.6652 - val_loss: 0.7054 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 24ms/step - accuracy: 0.7424 - loss: 0.5085 - val_accuracy: 0.6552 - val_loss: 0.6994 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 24ms/step - accuracy: 0.7551 - loss: 0.5074 - val_accuracy: 0.6537 - val_loss: 0.7097 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 24ms/step - accuracy: 0.7470 - loss: 0.5111 - val_accuracy: 0.6652 - val_loss: 0.6882 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 24ms/step - accuracy: 0.7523 - loss: 0.5105 - val_accuracy: 0.6652 - val_loss: 0.6875 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 24ms/step - accuracy: 0.7487 - loss: 0.5089 - val_accuracy: 0.6537 - val_loss: 0.7014 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7523 - loss: 0.5132 - val_accuracy: 0.6537 - val_loss: 0.7056 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 24ms/step - accuracy: 0.7556 - loss: 0.4968 - val_accuracy: 0.6624 - val_loss: 0.7032 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 24ms/step - accuracy: 0.7495 - loss: 0.5026 - val_accuracy: 0.6580 - val_loss: 0.6982 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 24ms/step - accuracy: 0.7467 - loss: 0.5094 - val_accuracy: 0.6595 - val_loss: 0.7045 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 24ms/step - accuracy: 0.7480 - loss: 0.5127 - val_accuracy: 0.6695 - val_loss: 0.7006 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 24ms/step - accuracy: 0.7444 - loss: 0.5134 - val_accuracy: 0.6566 - val_loss: 0.7071 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 24ms/step - accuracy: 0.7459 - loss: 0.5049 - val_accuracy: 0.6638 - val_loss: 0.6972 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 24ms/step - accuracy: 0.7497 - loss: 0.5025 - val_accuracy: 0.6580 - val_loss: 0.6962 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 24ms/step - accuracy: 0.7467 - loss: 0.5138 - val_accuracy: 0.6595 - val_loss: 0.7049 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 24ms/step - accuracy: 0.7490 - loss: 0.5116 - val_accuracy: 0.6810 - val_loss: 0.6919 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7543 - loss: 0.5029 - val_accuracy: 0.6624 - val_loss: 0.6928 - learning_rate: 5.0000e-04
Epoch 122/500

Epoch 122: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 24ms/step - accuracy: 0.7477 - loss: 0.5018 - val_accuracy: 0.6695 - val_loss: 0.6955 - learning_rate: 5.0000e-04
Epoch 123/500
124/124 - 3s - 24ms/step - accuracy: 0.7523 - loss: 0.4980 - val_accuracy: 0.6509 - val_loss: 0.7060 - learning_rate: 2.5000e-04
Epoch 124/500
124/124 - 3s - 24ms/step - accuracy: 0.7675 - loss: 0.4862 - val_accuracy: 0.6537 - val_loss: 0.7032 - learning_rate: 2.5000e-04
Epoch 125/500
124/124 - 3s - 24ms/step - accuracy: 0.7589 - loss: 0.4864 - val_accuracy: 0.6595 - val_loss: 0.7003 - learning_rate: 2.5000e-04
Epoch 126/500
124/124 - 3s - 24ms/step - accuracy: 0.7700 - loss: 0.4782 - val_accuracy: 0.6566 - val_loss: 0.6993 - learning_rate: 2.5000e-04
Epoch 127/500
124/124 - 3s - 24ms/step - accuracy: 0.7657 - loss: 0.4798 - val_accuracy: 0.6681 - val_loss: 0.6954 - learning_rate: 2.5000e-04
Epoch 128/500
124/124 - 3s - 24ms/step - accuracy: 0.7576 - loss: 0.4807 - val_accuracy: 0.6580 - val_loss: 0.6931 - learning_rate: 2.5000e-04
Epoch 129/500
124/124 - 3s - 24ms/step - accuracy: 0.7652 - loss: 0.4824 - val_accuracy: 0.6537 - val_loss: 0.7050 - learning_rate: 2.5000e-04
Epoch 130/500
124/124 - 3s - 24ms/step - accuracy: 0.7677 - loss: 0.4806 - val_accuracy: 0.6523 - val_loss: 0.7057 - learning_rate: 2.5000e-04
Epoch 131/500
124/124 - 3s - 24ms/step - accuracy: 0.7647 - loss: 0.4828 - val_accuracy: 0.6595 - val_loss: 0.6963 - learning_rate: 2.5000e-04
Epoch 132/500
124/124 - 3s - 24ms/step - accuracy: 0.7726 - loss: 0.4797 - val_accuracy: 0.6552 - val_loss: 0.6947 - learning_rate: 2.5000e-04
Epoch 133/500
124/124 - 3s - 24ms/step - accuracy: 0.7629 - loss: 0.4858 - val_accuracy: 0.6652 - val_loss: 0.6922 - learning_rate: 2.5000e-04
Epoch 134/500
124/124 - 3s - 24ms/step - accuracy: 0.7637 - loss: 0.4912 - val_accuracy: 0.6566 - val_loss: 0.6935 - learning_rate: 2.5000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4827 - val_accuracy: 0.6552 - val_loss: 0.7108 - learning_rate: 2.5000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7561 - loss: 0.4855 - val_accuracy: 0.6552 - val_loss: 0.6957 - learning_rate: 2.5000e-04
Epoch 137/500
124/124 - 3s - 24ms/step - accuracy: 0.7695 - loss: 0.4743 - val_accuracy: 0.6652 - val_loss: 0.6983 - learning_rate: 2.5000e-04
Epoch 138/500
124/124 - 3s - 24ms/step - accuracy: 0.7683 - loss: 0.4794 - val_accuracy: 0.6681 - val_loss: 0.6996 - learning_rate: 2.5000e-04
Epoch 139/500
124/124 - 3s - 24ms/step - accuracy: 0.7698 - loss: 0.4757 - val_accuracy: 0.6566 - val_loss: 0.7096 - learning_rate: 2.5000e-04
Epoch 140/500
124/124 - 3s - 24ms/step - accuracy: 0.7736 - loss: 0.4741 - val_accuracy: 0.6724 - val_loss: 0.6927 - learning_rate: 2.5000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7634 - loss: 0.4762 - val_accuracy: 0.6509 - val_loss: 0.7019 - learning_rate: 2.5000e-04
Epoch 142/500

Epoch 142: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7683 - loss: 0.4771 - val_accuracy: 0.6624 - val_loss: 0.7028 - learning_rate: 2.5000e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4742 - val_accuracy: 0.6695 - val_loss: 0.6931 - learning_rate: 1.2500e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7645 - loss: 0.4709 - val_accuracy: 0.6739 - val_loss: 0.6878 - learning_rate: 1.2500e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7754 - loss: 0.4648 - val_accuracy: 0.6566 - val_loss: 0.7030 - learning_rate: 1.2500e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4698 - val_accuracy: 0.6609 - val_loss: 0.6990 - learning_rate: 1.2500e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7708 - loss: 0.4695 - val_accuracy: 0.6609 - val_loss: 0.6982 - learning_rate: 1.2500e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7723 - loss: 0.4722 - val_accuracy: 0.6609 - val_loss: 0.6909 - learning_rate: 1.2500e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7799 - loss: 0.4647 - val_accuracy: 0.6624 - val_loss: 0.6989 - learning_rate: 1.2500e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4690 - val_accuracy: 0.6523 - val_loss: 0.7009 - learning_rate: 1.2500e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4720 - val_accuracy: 0.6595 - val_loss: 0.6990 - learning_rate: 1.2500e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4695 - val_accuracy: 0.6566 - val_loss: 0.6952 - learning_rate: 1.2500e-04
Epoch 152: early stopping
Restoring model weights from the end of the best epoch: 102.
Training complete. Best epoch: 102 of 152. Best val_loss: 0.6830, val_accuracy: 0.6710

========== Evaluation: LOSO fold 29 / held-out EMS0030 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        30        10         0
  intermedia        40        26        14
  max_intens         2         7        31

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.417     0.750     0.536        40
intermediate_intensity      0.605     0.325     0.423        80
         max_intensity      0.689     0.775     0.729        40

              accuracy                          0.544       160
             macro avg      0.570     0.617     0.563       160
          weighted avg      0.579     0.544     0.528       160

Overall accuracy: 0.5437

============================================================
Fold 30 of 30: holding out EMS0031
============================================================
Fitted scaler on 3944 epochs, 60 channels.
  Per-channel mean range: [-4.16e-07, 9.75e-07]
  Per-channel std range:  [7.27e-06, 1.13e-04]
Class weights: {0: 1.3333333333333333, 1: 0.6666666666666666, 2: 1.3333333333333333}
Building EEGNet: C=60, T=876, kernLength=125
/usr/local/lib/python3.12/dist-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/500
124/124 - 14s - 115ms/step - accuracy: 0.4559 - loss: 1.0221 - val_accuracy: 0.4971 - val_loss: 1.0354 - learning_rate: 0.0010
Epoch 2/500
124/124 - 3s - 24ms/step - accuracy: 0.5198 - loss: 0.9255 - val_accuracy: 0.5345 - val_loss: 0.9593 - learning_rate: 0.0010
Epoch 3/500
124/124 - 3s - 23ms/step - accuracy: 0.5368 - loss: 0.8699 - val_accuracy: 0.5359 - val_loss: 0.8974 - learning_rate: 0.0010
Epoch 4/500
124/124 - 3s - 23ms/step - accuracy: 0.5667 - loss: 0.8287 - val_accuracy: 0.5474 - val_loss: 0.8747 - learning_rate: 0.0010
Epoch 5/500
124/124 - 3s - 23ms/step - accuracy: 0.5697 - loss: 0.8082 - val_accuracy: 0.5589 - val_loss: 0.8524 - learning_rate: 0.0010
Epoch 6/500
124/124 - 3s - 23ms/step - accuracy: 0.5806 - loss: 0.7904 - val_accuracy: 0.5503 - val_loss: 0.8501 - learning_rate: 0.0010
Epoch 7/500
124/124 - 3s - 23ms/step - accuracy: 0.5854 - loss: 0.7777 - val_accuracy: 0.5704 - val_loss: 0.8329 - learning_rate: 0.0010
Epoch 8/500
124/124 - 3s - 24ms/step - accuracy: 0.6027 - loss: 0.7597 - val_accuracy: 0.5876 - val_loss: 0.8277 - learning_rate: 0.0010
Epoch 9/500
124/124 - 3s - 24ms/step - accuracy: 0.6070 - loss: 0.7459 - val_accuracy: 0.5776 - val_loss: 0.8242 - learning_rate: 0.0010
Epoch 10/500
124/124 - 3s - 24ms/step - accuracy: 0.6131 - loss: 0.7412 - val_accuracy: 0.5891 - val_loss: 0.8161 - learning_rate: 0.0010
Epoch 11/500
124/124 - 3s - 23ms/step - accuracy: 0.6151 - loss: 0.7324 - val_accuracy: 0.5747 - val_loss: 0.8165 - learning_rate: 0.0010
Epoch 12/500
124/124 - 3s - 24ms/step - accuracy: 0.6171 - loss: 0.7195 - val_accuracy: 0.5862 - val_loss: 0.8048 - learning_rate: 0.0010
Epoch 13/500
124/124 - 3s - 23ms/step - accuracy: 0.6275 - loss: 0.7136 - val_accuracy: 0.5833 - val_loss: 0.8103 - learning_rate: 0.0010
Epoch 14/500
124/124 - 3s - 23ms/step - accuracy: 0.6258 - loss: 0.7066 - val_accuracy: 0.6063 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 15/500
124/124 - 3s - 24ms/step - accuracy: 0.6351 - loss: 0.7018 - val_accuracy: 0.6135 - val_loss: 0.7803 - learning_rate: 0.0010
Epoch 16/500
124/124 - 3s - 23ms/step - accuracy: 0.6369 - loss: 0.6969 - val_accuracy: 0.6092 - val_loss: 0.7980 - learning_rate: 0.0010
Epoch 17/500
124/124 - 3s - 23ms/step - accuracy: 0.6410 - loss: 0.6873 - val_accuracy: 0.6049 - val_loss: 0.8045 - learning_rate: 0.0010
Epoch 18/500
124/124 - 3s - 23ms/step - accuracy: 0.6288 - loss: 0.6966 - val_accuracy: 0.6049 - val_loss: 0.7840 - learning_rate: 0.0010
Epoch 19/500
124/124 - 3s - 23ms/step - accuracy: 0.6438 - loss: 0.6749 - val_accuracy: 0.6106 - val_loss: 0.7813 - learning_rate: 0.0010
Epoch 20/500
124/124 - 3s - 23ms/step - accuracy: 0.6405 - loss: 0.6775 - val_accuracy: 0.6149 - val_loss: 0.7866 - learning_rate: 0.0010
Epoch 21/500
124/124 - 3s - 23ms/step - accuracy: 0.6395 - loss: 0.6765 - val_accuracy: 0.6207 - val_loss: 0.7872 - learning_rate: 0.0010
Epoch 22/500
124/124 - 3s - 23ms/step - accuracy: 0.6529 - loss: 0.6685 - val_accuracy: 0.6063 - val_loss: 0.7867 - learning_rate: 0.0010
Epoch 23/500
124/124 - 3s - 23ms/step - accuracy: 0.6537 - loss: 0.6600 - val_accuracy: 0.6063 - val_loss: 0.7771 - learning_rate: 0.0010
Epoch 24/500
124/124 - 3s - 24ms/step - accuracy: 0.6557 - loss: 0.6592 - val_accuracy: 0.6149 - val_loss: 0.7733 - learning_rate: 0.0010
Epoch 25/500
124/124 - 3s - 23ms/step - accuracy: 0.6504 - loss: 0.6643 - val_accuracy: 0.6164 - val_loss: 0.7730 - learning_rate: 0.0010
Epoch 26/500
124/124 - 3s - 23ms/step - accuracy: 0.6567 - loss: 0.6540 - val_accuracy: 0.6149 - val_loss: 0.7714 - learning_rate: 0.0010
Epoch 27/500
124/124 - 3s - 24ms/step - accuracy: 0.6623 - loss: 0.6529 - val_accuracy: 0.6149 - val_loss: 0.7684 - learning_rate: 0.0010
Epoch 28/500
124/124 - 3s - 23ms/step - accuracy: 0.6714 - loss: 0.6469 - val_accuracy: 0.6049 - val_loss: 0.7687 - learning_rate: 0.0010
Epoch 29/500
124/124 - 3s - 23ms/step - accuracy: 0.6722 - loss: 0.6365 - val_accuracy: 0.6092 - val_loss: 0.7781 - learning_rate: 0.0010
Epoch 30/500
124/124 - 3s - 23ms/step - accuracy: 0.6610 - loss: 0.6439 - val_accuracy: 0.6178 - val_loss: 0.7688 - learning_rate: 0.0010
Epoch 31/500
124/124 - 3s - 23ms/step - accuracy: 0.6684 - loss: 0.6406 - val_accuracy: 0.6121 - val_loss: 0.7712 - learning_rate: 0.0010
Epoch 32/500
124/124 - 3s - 23ms/step - accuracy: 0.6699 - loss: 0.6405 - val_accuracy: 0.6135 - val_loss: 0.7720 - learning_rate: 0.0010
Epoch 33/500
124/124 - 3s - 24ms/step - accuracy: 0.6734 - loss: 0.6304 - val_accuracy: 0.6336 - val_loss: 0.7580 - learning_rate: 0.0010
Epoch 34/500
124/124 - 3s - 23ms/step - accuracy: 0.6640 - loss: 0.6416 - val_accuracy: 0.6164 - val_loss: 0.7729 - learning_rate: 0.0010
Epoch 35/500
124/124 - 3s - 23ms/step - accuracy: 0.6595 - loss: 0.6328 - val_accuracy: 0.6092 - val_loss: 0.7645 - learning_rate: 0.0010
Epoch 36/500
124/124 - 3s - 23ms/step - accuracy: 0.6744 - loss: 0.6334 - val_accuracy: 0.6020 - val_loss: 0.7738 - learning_rate: 0.0010
Epoch 37/500
124/124 - 3s - 23ms/step - accuracy: 0.6729 - loss: 0.6234 - val_accuracy: 0.6063 - val_loss: 0.7826 - learning_rate: 0.0010
Epoch 38/500
124/124 - 3s - 23ms/step - accuracy: 0.6709 - loss: 0.6330 - val_accuracy: 0.6250 - val_loss: 0.7736 - learning_rate: 0.0010
Epoch 39/500
124/124 - 3s - 23ms/step - accuracy: 0.6765 - loss: 0.6192 - val_accuracy: 0.6221 - val_loss: 0.7584 - learning_rate: 0.0010
Epoch 40/500
124/124 - 3s - 23ms/step - accuracy: 0.6790 - loss: 0.6209 - val_accuracy: 0.6106 - val_loss: 0.7793 - learning_rate: 0.0010
Epoch 41/500
124/124 - 3s - 23ms/step - accuracy: 0.6813 - loss: 0.6125 - val_accuracy: 0.6322 - val_loss: 0.7522 - learning_rate: 0.0010
Epoch 42/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6213 - val_accuracy: 0.6307 - val_loss: 0.7599 - learning_rate: 0.0010
Epoch 43/500
124/124 - 3s - 23ms/step - accuracy: 0.6798 - loss: 0.6184 - val_accuracy: 0.6149 - val_loss: 0.7631 - learning_rate: 0.0010
Epoch 44/500
124/124 - 3s - 23ms/step - accuracy: 0.6846 - loss: 0.6154 - val_accuracy: 0.6178 - val_loss: 0.7773 - learning_rate: 0.0010
Epoch 45/500
124/124 - 3s - 23ms/step - accuracy: 0.6869 - loss: 0.6078 - val_accuracy: 0.6279 - val_loss: 0.7579 - learning_rate: 0.0010
Epoch 46/500
124/124 - 3s - 23ms/step - accuracy: 0.6815 - loss: 0.6111 - val_accuracy: 0.6236 - val_loss: 0.7590 - learning_rate: 0.0010
Epoch 47/500
124/124 - 3s - 23ms/step - accuracy: 0.6859 - loss: 0.6157 - val_accuracy: 0.6336 - val_loss: 0.7600 - learning_rate: 0.0010
Epoch 48/500
124/124 - 3s - 23ms/step - accuracy: 0.6894 - loss: 0.6008 - val_accuracy: 0.6322 - val_loss: 0.7706 - learning_rate: 0.0010
Epoch 49/500
124/124 - 3s - 23ms/step - accuracy: 0.6945 - loss: 0.5986 - val_accuracy: 0.6322 - val_loss: 0.7407 - learning_rate: 0.0010
Epoch 50/500
124/124 - 3s - 23ms/step - accuracy: 0.6871 - loss: 0.6028 - val_accuracy: 0.6365 - val_loss: 0.7458 - learning_rate: 0.0010
Epoch 51/500
124/124 - 3s - 23ms/step - accuracy: 0.6902 - loss: 0.6065 - val_accuracy: 0.6437 - val_loss: 0.7560 - learning_rate: 0.0010
Epoch 52/500
124/124 - 3s - 23ms/step - accuracy: 0.6960 - loss: 0.5939 - val_accuracy: 0.6293 - val_loss: 0.7614 - learning_rate: 0.0010
Epoch 53/500
124/124 - 3s - 23ms/step - accuracy: 0.6897 - loss: 0.5974 - val_accuracy: 0.6193 - val_loss: 0.7624 - learning_rate: 0.0010
Epoch 54/500
124/124 - 3s - 23ms/step - accuracy: 0.6924 - loss: 0.5945 - val_accuracy: 0.6322 - val_loss: 0.7559 - learning_rate: 0.0010
Epoch 55/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.6008 - val_accuracy: 0.6408 - val_loss: 0.7467 - learning_rate: 0.0010
Epoch 56/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5995 - val_accuracy: 0.6250 - val_loss: 0.7668 - learning_rate: 0.0010
Epoch 57/500
124/124 - 3s - 23ms/step - accuracy: 0.6940 - loss: 0.5948 - val_accuracy: 0.6250 - val_loss: 0.7620 - learning_rate: 0.0010
Epoch 58/500
124/124 - 3s - 23ms/step - accuracy: 0.6919 - loss: 0.5916 - val_accuracy: 0.6351 - val_loss: 0.7521 - learning_rate: 0.0010
Epoch 59/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5914 - val_accuracy: 0.6236 - val_loss: 0.7372 - learning_rate: 0.0010
Epoch 60/500
124/124 - 3s - 23ms/step - accuracy: 0.6891 - loss: 0.5938 - val_accuracy: 0.6250 - val_loss: 0.7623 - learning_rate: 0.0010
Epoch 61/500
124/124 - 3s - 23ms/step - accuracy: 0.6866 - loss: 0.5980 - val_accuracy: 0.6279 - val_loss: 0.7567 - learning_rate: 0.0010
Epoch 62/500
124/124 - 3s - 23ms/step - accuracy: 0.7069 - loss: 0.5845 - val_accuracy: 0.6307 - val_loss: 0.7509 - learning_rate: 0.0010
Epoch 63/500
124/124 - 3s - 23ms/step - accuracy: 0.7036 - loss: 0.5865 - val_accuracy: 0.6336 - val_loss: 0.7525 - learning_rate: 0.0010
Epoch 64/500
124/124 - 3s - 23ms/step - accuracy: 0.7026 - loss: 0.5801 - val_accuracy: 0.6264 - val_loss: 0.7414 - learning_rate: 0.0010
Epoch 65/500
124/124 - 3s - 23ms/step - accuracy: 0.7008 - loss: 0.5781 - val_accuracy: 0.6293 - val_loss: 0.7244 - learning_rate: 0.0010
Epoch 66/500
124/124 - 3s - 23ms/step - accuracy: 0.6993 - loss: 0.5810 - val_accuracy: 0.6293 - val_loss: 0.7400 - learning_rate: 0.0010
Epoch 67/500
124/124 - 3s - 23ms/step - accuracy: 0.7049 - loss: 0.5837 - val_accuracy: 0.6322 - val_loss: 0.7479 - learning_rate: 0.0010
Epoch 68/500
124/124 - 3s - 23ms/step - accuracy: 0.6975 - loss: 0.5893 - val_accuracy: 0.6422 - val_loss: 0.7359 - learning_rate: 0.0010
Epoch 69/500
124/124 - 3s - 23ms/step - accuracy: 0.6985 - loss: 0.5794 - val_accuracy: 0.6250 - val_loss: 0.7459 - learning_rate: 0.0010
Epoch 70/500
124/124 - 3s - 23ms/step - accuracy: 0.7044 - loss: 0.5784 - val_accuracy: 0.6250 - val_loss: 0.7716 - learning_rate: 0.0010
Epoch 71/500
124/124 - 3s - 23ms/step - accuracy: 0.7001 - loss: 0.5796 - val_accuracy: 0.6164 - val_loss: 0.7549 - learning_rate: 0.0010
Epoch 72/500
124/124 - 3s - 23ms/step - accuracy: 0.6968 - loss: 0.5809 - val_accuracy: 0.6221 - val_loss: 0.7456 - learning_rate: 0.0010
Epoch 73/500
124/124 - 3s - 23ms/step - accuracy: 0.6970 - loss: 0.5963 - val_accuracy: 0.6394 - val_loss: 0.7467 - learning_rate: 0.0010
Epoch 74/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5811 - val_accuracy: 0.6351 - val_loss: 0.7362 - learning_rate: 0.0010
Epoch 75/500
124/124 - 3s - 23ms/step - accuracy: 0.7006 - loss: 0.5786 - val_accuracy: 0.6149 - val_loss: 0.7627 - learning_rate: 0.0010
Epoch 76/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5775 - val_accuracy: 0.6566 - val_loss: 0.7331 - learning_rate: 0.0010
Epoch 77/500
124/124 - 3s - 23ms/step - accuracy: 0.7051 - loss: 0.5764 - val_accuracy: 0.6379 - val_loss: 0.7481 - learning_rate: 0.0010
Epoch 78/500
124/124 - 3s - 23ms/step - accuracy: 0.6947 - loss: 0.5791 - val_accuracy: 0.6394 - val_loss: 0.7455 - learning_rate: 0.0010
Epoch 79/500
124/124 - 3s - 23ms/step - accuracy: 0.7041 - loss: 0.5752 - val_accuracy: 0.6336 - val_loss: 0.7450 - learning_rate: 0.0010
Epoch 80/500
124/124 - 3s - 23ms/step - accuracy: 0.7137 - loss: 0.5700 - val_accuracy: 0.6351 - val_loss: 0.7495 - learning_rate: 0.0010
Epoch 81/500
124/124 - 3s - 23ms/step - accuracy: 0.7107 - loss: 0.5701 - val_accuracy: 0.6379 - val_loss: 0.7307 - learning_rate: 0.0010
Epoch 82/500
124/124 - 3s - 23ms/step - accuracy: 0.7064 - loss: 0.5679 - val_accuracy: 0.6379 - val_loss: 0.7458 - learning_rate: 0.0010
Epoch 83/500
124/124 - 3s - 23ms/step - accuracy: 0.7061 - loss: 0.5754 - val_accuracy: 0.6422 - val_loss: 0.7288 - learning_rate: 0.0010
Epoch 84/500
124/124 - 3s - 23ms/step - accuracy: 0.7046 - loss: 0.5703 - val_accuracy: 0.6351 - val_loss: 0.7508 - learning_rate: 0.0010
Epoch 85/500

Epoch 85: ReduceLROnPlateau reducing learning rate to 0.0005000000237487257.
124/124 - 3s - 23ms/step - accuracy: 0.7107 - loss: 0.5685 - val_accuracy: 0.6537 - val_loss: 0.7335 - learning_rate: 0.0010
Epoch 86/500
124/124 - 3s - 23ms/step - accuracy: 0.7201 - loss: 0.5463 - val_accuracy: 0.6523 - val_loss: 0.7254 - learning_rate: 5.0000e-04
Epoch 87/500
124/124 - 3s - 23ms/step - accuracy: 0.7302 - loss: 0.5354 - val_accuracy: 0.6451 - val_loss: 0.7304 - learning_rate: 5.0000e-04
Epoch 88/500
124/124 - 3s - 23ms/step - accuracy: 0.7411 - loss: 0.5342 - val_accuracy: 0.6480 - val_loss: 0.7296 - learning_rate: 5.0000e-04
Epoch 89/500
124/124 - 3s - 23ms/step - accuracy: 0.7388 - loss: 0.5302 - val_accuracy: 0.6466 - val_loss: 0.7237 - learning_rate: 5.0000e-04
Epoch 90/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5270 - val_accuracy: 0.6351 - val_loss: 0.7375 - learning_rate: 5.0000e-04
Epoch 91/500
124/124 - 3s - 23ms/step - accuracy: 0.7264 - loss: 0.5363 - val_accuracy: 0.6379 - val_loss: 0.7350 - learning_rate: 5.0000e-04
Epoch 92/500
124/124 - 3s - 23ms/step - accuracy: 0.7325 - loss: 0.5267 - val_accuracy: 0.6437 - val_loss: 0.7257 - learning_rate: 5.0000e-04
Epoch 93/500
124/124 - 3s - 23ms/step - accuracy: 0.7267 - loss: 0.5353 - val_accuracy: 0.6466 - val_loss: 0.7229 - learning_rate: 5.0000e-04
Epoch 94/500
124/124 - 3s - 23ms/step - accuracy: 0.7401 - loss: 0.5230 - val_accuracy: 0.6494 - val_loss: 0.7368 - learning_rate: 5.0000e-04
Epoch 95/500
124/124 - 3s - 23ms/step - accuracy: 0.7323 - loss: 0.5310 - val_accuracy: 0.6365 - val_loss: 0.7196 - learning_rate: 5.0000e-04
Epoch 96/500
124/124 - 3s - 23ms/step - accuracy: 0.7330 - loss: 0.5195 - val_accuracy: 0.6394 - val_loss: 0.7250 - learning_rate: 5.0000e-04
Epoch 97/500
124/124 - 3s - 23ms/step - accuracy: 0.7333 - loss: 0.5283 - val_accuracy: 0.6293 - val_loss: 0.7301 - learning_rate: 5.0000e-04
Epoch 98/500
124/124 - 3s - 23ms/step - accuracy: 0.7373 - loss: 0.5236 - val_accuracy: 0.6480 - val_loss: 0.7151 - learning_rate: 5.0000e-04
Epoch 99/500
124/124 - 3s - 23ms/step - accuracy: 0.7355 - loss: 0.5247 - val_accuracy: 0.6322 - val_loss: 0.7453 - learning_rate: 5.0000e-04
Epoch 100/500
124/124 - 3s - 23ms/step - accuracy: 0.7414 - loss: 0.5217 - val_accuracy: 0.6250 - val_loss: 0.7411 - learning_rate: 5.0000e-04
Epoch 101/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5214 - val_accuracy: 0.6437 - val_loss: 0.7236 - learning_rate: 5.0000e-04
Epoch 102/500
124/124 - 3s - 23ms/step - accuracy: 0.7394 - loss: 0.5136 - val_accuracy: 0.6351 - val_loss: 0.7315 - learning_rate: 5.0000e-04
Epoch 103/500
124/124 - 3s - 23ms/step - accuracy: 0.7381 - loss: 0.5194 - val_accuracy: 0.6451 - val_loss: 0.7280 - learning_rate: 5.0000e-04
Epoch 104/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5188 - val_accuracy: 0.6552 - val_loss: 0.7310 - learning_rate: 5.0000e-04
Epoch 105/500
124/124 - 3s - 23ms/step - accuracy: 0.7345 - loss: 0.5288 - val_accuracy: 0.6394 - val_loss: 0.7369 - learning_rate: 5.0000e-04
Epoch 106/500
124/124 - 3s - 23ms/step - accuracy: 0.7485 - loss: 0.5129 - val_accuracy: 0.6523 - val_loss: 0.7095 - learning_rate: 5.0000e-04
Epoch 107/500
124/124 - 3s - 23ms/step - accuracy: 0.7350 - loss: 0.5272 - val_accuracy: 0.6552 - val_loss: 0.7146 - learning_rate: 5.0000e-04
Epoch 108/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5193 - val_accuracy: 0.6652 - val_loss: 0.7088 - learning_rate: 5.0000e-04
Epoch 109/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.5182 - val_accuracy: 0.6494 - val_loss: 0.7195 - learning_rate: 5.0000e-04
Epoch 110/500
124/124 - 3s - 23ms/step - accuracy: 0.7361 - loss: 0.5206 - val_accuracy: 0.6451 - val_loss: 0.7188 - learning_rate: 5.0000e-04
Epoch 111/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5100 - val_accuracy: 0.6394 - val_loss: 0.7420 - learning_rate: 5.0000e-04
Epoch 112/500
124/124 - 3s - 23ms/step - accuracy: 0.7358 - loss: 0.5218 - val_accuracy: 0.6422 - val_loss: 0.7262 - learning_rate: 5.0000e-04
Epoch 113/500
124/124 - 3s - 23ms/step - accuracy: 0.7449 - loss: 0.5100 - val_accuracy: 0.6480 - val_loss: 0.7298 - learning_rate: 5.0000e-04
Epoch 114/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5149 - val_accuracy: 0.6552 - val_loss: 0.7323 - learning_rate: 5.0000e-04
Epoch 115/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5028 - val_accuracy: 0.6437 - val_loss: 0.7209 - learning_rate: 5.0000e-04
Epoch 116/500
124/124 - 3s - 23ms/step - accuracy: 0.7292 - loss: 0.5310 - val_accuracy: 0.6336 - val_loss: 0.7363 - learning_rate: 5.0000e-04
Epoch 117/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5151 - val_accuracy: 0.6264 - val_loss: 0.7508 - learning_rate: 5.0000e-04
Epoch 118/500
124/124 - 3s - 23ms/step - accuracy: 0.7444 - loss: 0.5147 - val_accuracy: 0.6379 - val_loss: 0.7403 - learning_rate: 5.0000e-04
Epoch 119/500
124/124 - 3s - 23ms/step - accuracy: 0.7510 - loss: 0.5080 - val_accuracy: 0.6480 - val_loss: 0.7232 - learning_rate: 5.0000e-04
Epoch 120/500
124/124 - 3s - 23ms/step - accuracy: 0.7434 - loss: 0.5167 - val_accuracy: 0.6494 - val_loss: 0.7155 - learning_rate: 5.0000e-04
Epoch 121/500
124/124 - 3s - 23ms/step - accuracy: 0.7429 - loss: 0.5105 - val_accuracy: 0.6408 - val_loss: 0.7386 - learning_rate: 5.0000e-04
Epoch 122/500
124/124 - 3s - 23ms/step - accuracy: 0.7424 - loss: 0.5104 - val_accuracy: 0.6494 - val_loss: 0.7104 - learning_rate: 5.0000e-04
Epoch 123/500
124/124 - 3s - 23ms/step - accuracy: 0.7437 - loss: 0.5123 - val_accuracy: 0.6609 - val_loss: 0.7084 - learning_rate: 5.0000e-04
Epoch 124/500
124/124 - 3s - 23ms/step - accuracy: 0.7368 - loss: 0.5194 - val_accuracy: 0.6537 - val_loss: 0.7162 - learning_rate: 5.0000e-04
Epoch 125/500
124/124 - 3s - 23ms/step - accuracy: 0.7457 - loss: 0.5075 - val_accuracy: 0.6437 - val_loss: 0.7270 - learning_rate: 5.0000e-04
Epoch 126/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.5069 - val_accuracy: 0.6437 - val_loss: 0.7151 - learning_rate: 5.0000e-04
Epoch 127/500
124/124 - 3s - 23ms/step - accuracy: 0.7467 - loss: 0.5076 - val_accuracy: 0.6609 - val_loss: 0.7162 - learning_rate: 5.0000e-04
Epoch 128/500
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5105 - val_accuracy: 0.6580 - val_loss: 0.7132 - learning_rate: 5.0000e-04
Epoch 129/500
124/124 - 3s - 23ms/step - accuracy: 0.7353 - loss: 0.5186 - val_accuracy: 0.6394 - val_loss: 0.7294 - learning_rate: 5.0000e-04
Epoch 130/500
124/124 - 3s - 23ms/step - accuracy: 0.7528 - loss: 0.5040 - val_accuracy: 0.6451 - val_loss: 0.7234 - learning_rate: 5.0000e-04
Epoch 131/500
124/124 - 3s - 23ms/step - accuracy: 0.7419 - loss: 0.5111 - val_accuracy: 0.6394 - val_loss: 0.7346 - learning_rate: 5.0000e-04
Epoch 132/500
124/124 - 3s - 23ms/step - accuracy: 0.7386 - loss: 0.5149 - val_accuracy: 0.6537 - val_loss: 0.7036 - learning_rate: 5.0000e-04
Epoch 133/500
124/124 - 3s - 23ms/step - accuracy: 0.7333 - loss: 0.5184 - val_accuracy: 0.6408 - val_loss: 0.7382 - learning_rate: 5.0000e-04
Epoch 134/500
124/124 - 3s - 23ms/step - accuracy: 0.7363 - loss: 0.5131 - val_accuracy: 0.6379 - val_loss: 0.7231 - learning_rate: 5.0000e-04
Epoch 135/500
124/124 - 3s - 23ms/step - accuracy: 0.7518 - loss: 0.5031 - val_accuracy: 0.6595 - val_loss: 0.7019 - learning_rate: 5.0000e-04
Epoch 136/500
124/124 - 3s - 23ms/step - accuracy: 0.7482 - loss: 0.5090 - val_accuracy: 0.6609 - val_loss: 0.7185 - learning_rate: 5.0000e-04
Epoch 137/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.5001 - val_accuracy: 0.6480 - val_loss: 0.7356 - learning_rate: 5.0000e-04
Epoch 138/500
124/124 - 3s - 23ms/step - accuracy: 0.7426 - loss: 0.5081 - val_accuracy: 0.6394 - val_loss: 0.7299 - learning_rate: 5.0000e-04
Epoch 139/500
124/124 - 3s - 23ms/step - accuracy: 0.7442 - loss: 0.5049 - val_accuracy: 0.6552 - val_loss: 0.7295 - learning_rate: 5.0000e-04
Epoch 140/500
124/124 - 3s - 23ms/step - accuracy: 0.7409 - loss: 0.5047 - val_accuracy: 0.6523 - val_loss: 0.7218 - learning_rate: 5.0000e-04
Epoch 141/500
124/124 - 3s - 23ms/step - accuracy: 0.7465 - loss: 0.5076 - val_accuracy: 0.6408 - val_loss: 0.7254 - learning_rate: 5.0000e-04
Epoch 142/500
124/124 - 3s - 23ms/step - accuracy: 0.7503 - loss: 0.4970 - val_accuracy: 0.6509 - val_loss: 0.7255 - learning_rate: 5.0000e-04
Epoch 143/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.5017 - val_accuracy: 0.6537 - val_loss: 0.7322 - learning_rate: 5.0000e-04
Epoch 144/500
124/124 - 3s - 23ms/step - accuracy: 0.7513 - loss: 0.5052 - val_accuracy: 0.6422 - val_loss: 0.7212 - learning_rate: 5.0000e-04
Epoch 145/500
124/124 - 3s - 23ms/step - accuracy: 0.7480 - loss: 0.4971 - val_accuracy: 0.6422 - val_loss: 0.7181 - learning_rate: 5.0000e-04
Epoch 146/500
124/124 - 3s - 23ms/step - accuracy: 0.7472 - loss: 0.4948 - val_accuracy: 0.6537 - val_loss: 0.7205 - learning_rate: 5.0000e-04
Epoch 147/500
124/124 - 3s - 23ms/step - accuracy: 0.7515 - loss: 0.5018 - val_accuracy: 0.6523 - val_loss: 0.7208 - learning_rate: 5.0000e-04
Epoch 148/500
124/124 - 3s - 23ms/step - accuracy: 0.7462 - loss: 0.5096 - val_accuracy: 0.6336 - val_loss: 0.7493 - learning_rate: 5.0000e-04
Epoch 149/500
124/124 - 3s - 23ms/step - accuracy: 0.7470 - loss: 0.5034 - val_accuracy: 0.6379 - val_loss: 0.7239 - learning_rate: 5.0000e-04
Epoch 150/500
124/124 - 3s - 23ms/step - accuracy: 0.7439 - loss: 0.5031 - val_accuracy: 0.6552 - val_loss: 0.7175 - learning_rate: 5.0000e-04
Epoch 151/500
124/124 - 3s - 23ms/step - accuracy: 0.7459 - loss: 0.4965 - val_accuracy: 0.6509 - val_loss: 0.7196 - learning_rate: 5.0000e-04
Epoch 152/500
124/124 - 3s - 23ms/step - accuracy: 0.7520 - loss: 0.4987 - val_accuracy: 0.6566 - val_loss: 0.7114 - learning_rate: 5.0000e-04
Epoch 153/500
124/124 - 3s - 23ms/step - accuracy: 0.7497 - loss: 0.5018 - val_accuracy: 0.6523 - val_loss: 0.7253 - learning_rate: 5.0000e-04
Epoch 154/500
124/124 - 3s - 23ms/step - accuracy: 0.7546 - loss: 0.5027 - val_accuracy: 0.6466 - val_loss: 0.7422 - learning_rate: 5.0000e-04
Epoch 155/500

Epoch 155: ReduceLROnPlateau reducing learning rate to 0.0002500000118743628.
124/124 - 3s - 23ms/step - accuracy: 0.7421 - loss: 0.5098 - val_accuracy: 0.6466 - val_loss: 0.7264 - learning_rate: 5.0000e-04
Epoch 156/500
124/124 - 3s - 23ms/step - accuracy: 0.7619 - loss: 0.4861 - val_accuracy: 0.6466 - val_loss: 0.7237 - learning_rate: 2.5000e-04
Epoch 157/500
124/124 - 3s - 23ms/step - accuracy: 0.7713 - loss: 0.4734 - val_accuracy: 0.6509 - val_loss: 0.7240 - learning_rate: 2.5000e-04
Epoch 158/500
124/124 - 3s - 23ms/step - accuracy: 0.7731 - loss: 0.4780 - val_accuracy: 0.6552 - val_loss: 0.7131 - learning_rate: 2.5000e-04
Epoch 159/500
124/124 - 3s - 23ms/step - accuracy: 0.7614 - loss: 0.4767 - val_accuracy: 0.6494 - val_loss: 0.7260 - learning_rate: 2.5000e-04
Epoch 160/500
124/124 - 3s - 23ms/step - accuracy: 0.7655 - loss: 0.4842 - val_accuracy: 0.6566 - val_loss: 0.7185 - learning_rate: 2.5000e-04
Epoch 161/500
124/124 - 3s - 23ms/step - accuracy: 0.7614 - loss: 0.4819 - val_accuracy: 0.6437 - val_loss: 0.7341 - learning_rate: 2.5000e-04
Epoch 162/500
124/124 - 3s - 23ms/step - accuracy: 0.7677 - loss: 0.4740 - val_accuracy: 0.6451 - val_loss: 0.7268 - learning_rate: 2.5000e-04
Epoch 163/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4705 - val_accuracy: 0.6652 - val_loss: 0.7229 - learning_rate: 2.5000e-04
Epoch 164/500
124/124 - 3s - 23ms/step - accuracy: 0.7728 - loss: 0.4652 - val_accuracy: 0.6580 - val_loss: 0.7186 - learning_rate: 2.5000e-04
Epoch 165/500
124/124 - 3s - 23ms/step - accuracy: 0.7660 - loss: 0.4749 - val_accuracy: 0.6566 - val_loss: 0.7171 - learning_rate: 2.5000e-04
Epoch 166/500
124/124 - 3s - 23ms/step - accuracy: 0.7632 - loss: 0.4768 - val_accuracy: 0.6566 - val_loss: 0.7133 - learning_rate: 2.5000e-04
Epoch 167/500
124/124 - 3s - 23ms/step - accuracy: 0.7642 - loss: 0.4771 - val_accuracy: 0.6523 - val_loss: 0.7217 - learning_rate: 2.5000e-04
Epoch 168/500
124/124 - 3s - 23ms/step - accuracy: 0.7576 - loss: 0.4783 - val_accuracy: 0.6480 - val_loss: 0.7257 - learning_rate: 2.5000e-04
Epoch 169/500
124/124 - 3s - 23ms/step - accuracy: 0.7584 - loss: 0.4842 - val_accuracy: 0.6451 - val_loss: 0.7205 - learning_rate: 2.5000e-04
Epoch 170/500
124/124 - 3s - 23ms/step - accuracy: 0.7726 - loss: 0.4718 - val_accuracy: 0.6509 - val_loss: 0.7306 - learning_rate: 2.5000e-04
Epoch 171/500
124/124 - 3s - 23ms/step - accuracy: 0.7650 - loss: 0.4677 - val_accuracy: 0.6580 - val_loss: 0.7193 - learning_rate: 2.5000e-04
Epoch 172/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4728 - val_accuracy: 0.6509 - val_loss: 0.7253 - learning_rate: 2.5000e-04
Epoch 173/500
124/124 - 3s - 23ms/step - accuracy: 0.7650 - loss: 0.4707 - val_accuracy: 0.6667 - val_loss: 0.7090 - learning_rate: 2.5000e-04
Epoch 174/500
124/124 - 3s - 23ms/step - accuracy: 0.7637 - loss: 0.4753 - val_accuracy: 0.6580 - val_loss: 0.7195 - learning_rate: 2.5000e-04
Epoch 175/500

Epoch 175: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4738 - val_accuracy: 0.6509 - val_loss: 0.7282 - learning_rate: 2.5000e-04
Epoch 176/500
124/124 - 3s - 23ms/step - accuracy: 0.7695 - loss: 0.4659 - val_accuracy: 0.6609 - val_loss: 0.7192 - learning_rate: 1.2500e-04
Epoch 177/500
124/124 - 3s - 23ms/step - accuracy: 0.7710 - loss: 0.4656 - val_accuracy: 0.6566 - val_loss: 0.7192 - learning_rate: 1.2500e-04
Epoch 178/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4670 - val_accuracy: 0.6652 - val_loss: 0.7166 - learning_rate: 1.2500e-04
Epoch 179/500
124/124 - 3s - 23ms/step - accuracy: 0.7698 - loss: 0.4638 - val_accuracy: 0.6595 - val_loss: 0.7161 - learning_rate: 1.2500e-04
Epoch 180/500
124/124 - 3s - 23ms/step - accuracy: 0.7819 - loss: 0.4571 - val_accuracy: 0.6667 - val_loss: 0.7085 - learning_rate: 1.2500e-04
Epoch 181/500
124/124 - 3s - 23ms/step - accuracy: 0.7817 - loss: 0.4583 - val_accuracy: 0.6494 - val_loss: 0.7230 - learning_rate: 1.2500e-04
Epoch 182/500
124/124 - 3s - 23ms/step - accuracy: 0.7688 - loss: 0.4612 - val_accuracy: 0.6566 - val_loss: 0.7183 - learning_rate: 1.2500e-04
Epoch 183/500
124/124 - 3s - 23ms/step - accuracy: 0.7705 - loss: 0.4711 - val_accuracy: 0.6480 - val_loss: 0.7237 - learning_rate: 1.2500e-04
Epoch 184/500
124/124 - 3s - 23ms/step - accuracy: 0.7690 - loss: 0.4651 - val_accuracy: 0.6494 - val_loss: 0.7207 - learning_rate: 1.2500e-04
Epoch 185/500
124/124 - 3s - 23ms/step - accuracy: 0.7721 - loss: 0.4610 - val_accuracy: 0.6580 - val_loss: 0.7147 - learning_rate: 1.2500e-04
Epoch 185: early stopping
Restoring model weights from the end of the best epoch: 135.
Training complete. Best epoch: 135 of 185. Best val_loss: 0.7019, val_accuracy: 0.6595

========== Evaluation: LOSO fold 30 / held-out EMS0031 ==========

Confusion matrix (rows = true class, cols = predicted class):
             no_stimu  intermed  max_inte
  no_stimula        31         9         0
  intermedia        11        34        35
  max_intens         0         0        40

Classification report:
                        precision    recall  f1-score   support

        no_stimulation      0.738     0.775     0.756        40
intermediate_intensity      0.791     0.425     0.553        80
         max_intensity      0.533     1.000     0.696        40

              accuracy                          0.656       160
             macro avg      0.687     0.733     0.668       160
          weighted avg      0.713     0.656     0.639       160

Overall accuracy: 0.6562

============================================================
LOSO Summary
============================================================
Mean accuracy: 0.5910 ± 0.0956
Range: [0.3750, 0.7250]
Per-fold accuracies: ['0.700', '0.637', '0.725', '0.600', '0.375', '0.512', '0.419', '0.588', '0.631', '0.512', '0.613', '0.688', '0.688', '0.525', '0.450', '0.537', '0.606', '0.500', '0.575', '0.637', '0.706', '0.706', '0.644', '0.644', '0.425', '0.506', '0.662', '0.719', '0.544', '0.656']

Aggregated confusion matrix across all 30 folds:
[[ 917  263   20]
 [ 781 1194  425]
 [  86  388  726]]

Per-class recall: {'no_stimulation': np.float64(0.7641666666666667), 'intermediate_intensity': np.float64(0.4975), 'max_intensity': np.float64(0.605)}