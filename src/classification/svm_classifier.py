"""
Support Vector Machine (SVM) Classifier for Land Use / Land Cover and Crop Extraction
"""

from typing import Tuple, Dict
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report

class CropSVMClassifier:
    """
    Supervised Support Vector Machine Classifier tailored for multispectral remote sensing.
    Classifies 6 land cover classes:
        1: Rice Crop (Paddy)
        2: Vegetation and Other Crops
        3: Fallow Land and Barren Land
        4: Built-up
        5: Waterbodies
        6: Sandbar
    """

    def __init__(self, kernel: str = "rbf", C: float = 10.0, gamma: str = "scale"):
        self.classifier = SVC(kernel=kernel, C=C, gamma=gamma, class_weight="balanced")
        self.is_trained = False

    def fit(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Trains the SVM classifier on spectral samples.
        X_train shape: (num_samples, num_spectral_bands)
        y_train shape: (num_samples,)
        """
        self.classifier.fit(X_train, y_train)
        self.is_trained = True
        return self

    def predict_raster(self, raster_stack: np.ndarray) -> np.ndarray:
        """
        Applies trained SVM across a 3D raster stack of shape (bands, rows, cols).
        Returns a 2D classified map (rows, cols) of class IDs (1 to 6).
        """
        if not self.is_trained:
            raise RuntimeError("Classifier has not been trained yet. Call .fit() first.")

        bands, rows, cols = raster_stack.shape
        flat_pixels = raster_stack.reshape(bands, -1).T  # Shape: (rows*cols, bands)

        # Handle NaNs or zeros
        valid_mask = ~np.isnan(flat_pixels).any(axis=1)
        classified_flat = np.zeros(rows * cols, dtype=np.int32)

        if np.any(valid_mask):
            classified_flat[valid_mask] = self.classifier.predict(flat_pixels[valid_mask])

        return classified_flat.reshape(rows, cols)

    @staticmethod
    def calculate_class_areas(
        classified_map: np.ndarray,
        pixel_size_meters: float = 30.0,
        rice_class_id: int = 1
    ) -> Dict[str, float]:
        """
        Calculates pixel count and area (in Hectares) for rice and total classes.
        Area (m2) = count * (pixel_size ^ 2)
        Area (Ha) = Area (m2) / 10,000
        """
        pixel_area_m2 = pixel_size_meters * pixel_size_meters
        rice_pixel_count = int(np.sum(classified_map == rice_class_id))
        rice_area_m2 = rice_pixel_count * pixel_area_m2
        rice_area_ha = rice_area_m2 / 10000.0

        return {
            "rice_pixel_count": rice_pixel_count,
            "rice_area_m2": rice_area_m2,
            "rice_area_ha": rice_area_ha,
        }
