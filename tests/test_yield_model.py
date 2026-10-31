"""
Unit Tests for Exponential Crop Yield Model
"""

import unittest
import numpy as np
from src.modeling.yield_model import (
    estimate_yield_from_ndvi,
    calculate_yield_statistics,
    compute_percentage_accuracy
)

class TestYieldModel(unittest.TestCase):

    def test_exponential_yield_min_max(self):
        # Values from Table 4.5 & Table 4.6 in the thesis
        min_ndvi = 0.285720
        max_ndvi = 0.531192

        min_yield = estimate_yield_from_ndvi(min_ndvi)
        max_yield = estimate_yield_from_ndvi(max_ndvi)

        # Thesis observed values: min = 3790.21, max = 7046.50
        self.assertTrue(np.isclose(min_yield, 3790.21, atol=0.1))
        self.assertTrue(np.isclose(max_yield, 7046.51, atol=0.1))

    def test_percentage_accuracy(self):
        # East Godavari: observed = 5418.36, actual = 5333.551 -> Pa = 98.41%
        pa_eg = compute_percentage_accuracy(5418.36, 5333.551)
        self.assertTrue(np.isclose(pa_eg, 98.41, atol=0.01))

        # West Godavari: observed = 5379.22, actual = 5394.66 -> Pa = 99.71%
        pa_wg = compute_percentage_accuracy(5379.22, 5394.66)
        self.assertTrue(np.isclose(pa_wg, 99.71, atol=0.01))

    def test_yield_statistics(self):
        yield_arr = np.array([3000.0, 5000.0, 7000.0, np.nan])
        stats = calculate_yield_statistics(yield_arr)

        self.assertEqual(stats["min_yield"], 3000.0)
        self.assertEqual(stats["max_yield"], 7000.0)
        self.assertEqual(stats["mean_yield"], 5000.0)
        self.assertEqual(stats["valid_pixels"], 3)

if __name__ == "__main__":
    unittest.main()
