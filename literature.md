# **Best Models To Use:**

- EEGNet:
    - Compact CNN explicitly designed to generalize across multiple BCI paradigms (P300, ErrPs, MRCP, SMR) with limited data and minimal preprocessing
    - Uses 1D temporal convolution plus depthwise spatial convolution to mimic standard EEG filtering and spatial patterns, and performs competitively with larger CNNs and traditional pipelines across tasks
    - In MI BCI with CSP + classical classifiers, 1–2 s windows are suggested as an optimal compromise between classification accuracy and responsiveness
    - EEGNet and many MI/emotion CNNs take raw (or band‑pass filtered) EEG segments as C×T matrices, avoiding explicit time–frequency conversion
        - This avoids information loss and extra compute; specifically recommended for real-time emotion recognition due to time–frequency conversion overhead
    - 1D‑CNN on band‑pass time-domain EEG slightly outperformed PSD‑based sequences for MI classification 
    - **Shape**:
        Input: shape **(C, T)** where C = channels, T = time samples (e.g., 32–64 chans, 128 Hz)  (Lawhern et al., 2016).

        **Block 1 (temporal + spatial filters)**  (Lawhern et al., 2016):  
        - Reshape → (1, C, T)  
        - **Conv2D**: F1 filters, kernel **(1, 64)** (for 128 Hz, 64 ≈ 0.5 s), `padding='same'`, linear activation, no bias  
        - BatchNorm (2·F1 params)  
        - **DepthwiseConv2D**: depth multiplier **D**, kernel **(C, 1)**, `padding='valid'`, linear, max-norm=1  
        - BatchNorm (2·D·F1)  
        - ELU  
        - AveragePool2D: size (1, 4) → downsample to 32 Hz  
        - Dropout: p = 0.5 (within‑subject) or 0.25 (cross‑subject)  (Lawhern et al., 2016)
        
        **Block 2 (separable conv)**  (Lawhern et al., 2016):  
        - SeparableConv2D: depthwise kernel **(1, 16)** (≈500 ms at 32 Hz), pointwise with **F2** filters  
        - Params: `16*D*F1 + F2*(D*F1)`  
        - BatchNorm (2·F2)  
        - ELU  
        - AveragePool2D: size (1, 8) → downsample T by 32 overall  
        - Dropout: same p as Block 1  
        - Flatten → Dense(**N**, softmax), max‑norm=0.25  (Lawhern et al., 2016)
        
        **Hyperparameter template** (used in the paper)  (Lawhern et al., 2016):  
        - Typical configs: **EEGNet‑4,2** or **EEGNet‑8,2**  
        - F1 = 4 or 8  
        - D = 2  
        - F2 = D·F1 (i.e., 8 or 16)  
        - Optimizer: **Adam**, default params  ()- Loss: categorical cross‑entropy  
        - Epochs: **500**, early stopping on validation loss; save best weights  (Lawhern et al., 2016)- No biases in conv layers; BatchNorm everywhere instead  (Lawhern et al., 2016)- Dropout as above; max‑norm constraints on spatial and Dense layer weights  (Lawhern et al., 2016)Parameter count: order of **1k–2k params** for T≈1–1.5 s at 128 Hz (EEGNet‑4,2 or 8,2), vs >100k for DeepConvNet  (Lawhern et al., 2016)[Table 3].

        **Adapting to EMS EEG**

        - **Sampling rate**: in the paper T is based on 128 Hz; if you use a different rate, scale the first temporal kernel length to about **0.5 s** (e.g., at 250 Hz → kernel length ≈125 samples instead of 64)  (Lawhern et al., 2016).  
        - **Epoch window**: choose T to cover your EMS response (e.g., 1–2 s). EEGNet just takes whatever T you give; internal pooling shrinks it by a factor of 32 in time  (Lawhern et al., 2016).  
        - **Channels**: C is whatever your montage provides; DepthwiseConv2D’s kernel is (C,1) so spatial filters always span all channels  (Lawhern et al., 2016).

        **Practical recipe**

        For your 3‑class EMS tolerability task, a concrete, paper-faithful setup is:

        - **Input**: band‑limited EEG, shape (C, T), e.g., C=8–32, T = samples for 1–2 s post‑EMS.  
        - **Model**: EEGNet‑4,2 or EEGNet‑8,2 exactly as in Table 2 with scaled temporal kernel if fs≠128 Hz  (Lawhern et al., 2016).  
        - **Training**: Adam, 500 epochs with early stopping on validation loss, dropout 0.5 within‑subject, inverse‑frequency class weights if imbalanced  (Lawhern et al., 2016).

        This gives you a compact, real‑time‑friendly CNN whose architecture and hyperparameters are fully specified and validated across multiple BCI paradigms.

Brain Decode
Kaggle for training