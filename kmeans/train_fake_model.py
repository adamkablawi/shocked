import glob
import numpy as np
from scipy.signal import welch
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pickle

DATA_DIR = "trials_20260602_152823"
FS = 250  # Hz
N_CLUSTERS = 4

BANDS = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta":  (13, 30),
    "gamma": (30, 100),
}


def band_power(psd, freqs, fmin, fmax):
    mask = (freqs >= fmin) & (freqs <= fmax)
    return np.trapz(psd[mask], freqs[mask])


def extract_features(window):
    """window: (n_channels, n_samples) -> 1D feature vector of band powers per channel."""
    n_channels = window.shape[0]
    features = []
    for ch in range(n_channels):
        freqs, psd = welch(window[ch], fs=FS, nperseg=min(128, window.shape[1]))
        for fmin, fmax in BANDS.values():
            features.append(band_power(psd, freqs, fmin, fmax))
    return np.array(features)


def load_data():
    paths = sorted(glob.glob(f"{DATA_DIR}/window_*.npz"),
                   key=lambda p: int(p.split("_")[-1].split(".")[0]))
    X, names = [], []
    for path in paths:
        window = np.load(path)["data"]   # (11, 300)
        X.append(extract_features(window))
        names.append(path)
    return np.array(X), names


def main():
    print("Loading windows and extracting band-power features...")
    X, names = load_data()
    print(f"  Feature matrix: {X.shape}  ({X.shape[0]} windows, {X.shape[1]} features)")

    # Standardise
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Elbow scan to help pick k
    inertias = []
    for k in range(2, 9):
        km = KMeans(n_clusters=k, n_init=20, random_state=42)
        km.fit(X_scaled)
        inertias.append((k, km.inertia_))
    print("\nElbow (inertia by k):")
    for k, inert in inertias:
        print(f"  k={k}  inertia={inert:.1f}")

    # Fit final model
    print(f"\nFitting KMeans with k={N_CLUSTERS}...")
    model = KMeans(n_clusters=N_CLUSTERS, n_init=50, random_state=42)
    labels = model.fit_predict(X_scaled)

    # PCA for a 2-D summary
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    var = pca.explained_variance_ratio_
    print(f"PCA variance explained: PC1={var[0]:.1%}  PC2={var[1]:.1%}")

    print(f"\nCluster assignments (window → cluster):")
    for name, label, (pc1, pc2) in zip(names, labels, X_pca):
        tag = name.split("/")[-1].replace(".npz", "")
        print(f"  {tag:12s}  cluster={label}  PC1={pc1:+.2f}  PC2={pc2:+.2f}")

    counts = np.bincount(labels)
    print(f"\nCluster sizes: {dict(enumerate(counts))}")

    # Save
    artifact = {"model": model, "scaler": scaler, "pca": pca, "labels": labels, "names": names}
    with open("eeg_kmeans_model.pkl", "wb") as f:
        pickle.dump(artifact, f)
    print("\nSaved → eeg_kmeans_model.pkl")


if __name__ == "__main__":
    main()
