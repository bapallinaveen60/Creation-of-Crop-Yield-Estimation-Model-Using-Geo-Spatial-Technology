"""
Unit Tests for NDVI Calculation and Masking
"""

import unittest
import numpy as np
from src.indices.ndvi_calculator import calculate_ndvi, extract_crop_ndvi

class TestNDVICalculator(unittest.TestCase):

    def test_calculate_ndvi_basic(self):
        nir = np.array([0.8, 0.5, 0.2])
        red = np.array([0.2, 0.5, 0.8])
        ndvi = calculate_ndvi(nir, red)
        
        # Expected: (0.8 - 0.2) / (0.8 + 0.2) = 0.6 / 1.0 = 0.6
        self.assertTrue(np.isclose(ndvi[0], 0.6))
        # Expected: (0.5 - 0.5) / 1.0 = 0.0
        self.assertTrue(np.isclose(ndvi[1], 0.0))
        # Expected: (0.2 - 0.8) / 1.0 = -0.6
        self.assertTrue(np.isclose(ndvi[2], -0.6))

    def test_calculate_ndvi_bounds(self):
        nir = np.array([1.0, 0.0])
        red = np.array([0.0, 1.0])
        ndvi = calculate_ndvi(nir, red)
        self.assertTrue(np.all(ndvi >= -1.0))
        self.assertTrue(np.all(ndvi <= 1.0))

    def test_extract_crop_ndvi(self):
        ndvi = np.array([[0.5, 0.3], [0.8, 0.1]])
        classes = np.array([[1, 2], [1, 4]])
        
        masked = extract_crop_ndvi(ndvi, classes, crop_class_id=1, nodata_value=np.nan)
        self.assertTrue(np.isclose(masked[0, 0], 0.5))
        self.assertTrue(np.isclose(masked[1, 0], 0.8))
        self.assertTrue(np.isnan(masked[0, 1]))
        self.assertTrue(np.isnan(masked[1, 1]))

if __name__ == "__main__":
    unittest.main()
