"""
Empirical Exponential Crop Yield Estimation Model
==================================================
Based on research findings from Andhra University B.Tech Thesis:
"Creation of Crop Yield Estimation Model Using Geo-Spatial Technology"

Model Formulation:
    Yield (kg/ha) = a * exp(b * NDVI)
    where a = 1841.6, b = 2.5262 (R² = 0.9922)
"""

from typing import Dict, Union, Optional
import numpy as np

DEFAULT_A = 1841.6
DEFAULT_B = 2.5262

def estimate_yield_from_ndvi(
    ndvi: Union[float, np.ndarray],
    a: float = DEFAULT_A,
    b: float = DEFAULT_B,
    min_ndvi_threshold: float = 0.0
) -> Union[float, np.ndarray]:
    """
    Calculates estimated crop yield (in kg/hectare) using the empirical exponential equation.

    Args:
        ndvi: Single float value or NumPy array of rice crop NDVI
        a: Base coefficient (default: 1841.6)
        b: Exponential growth coefficient (default: 2.5262)
        min_ndvi_threshold: Minimum valid NDVI threshold to filter non-vegetation

    Returns:
        Estimated crop yield in kg/hectare.
    """
    if isinstance(ndvi, (int, float)):
        if ndvi < min_ndvi_threshold or np.isnan(ndvi):
            return 0.0
        return float(a * np.exp(b * ndvi))

    # Array operation
    is_valid = (~np.isnan(ndvi)) & (ndvi >= min_ndvi_threshold)
    yield_map = np.zeros_like(ndvi, dtype=np.float32)
    yield_map[is_valid] = a * np.exp(b * ndvi[is_valid])
    yield_map[~is_valid] = np.nan
    return yield_map

def calculate_yield_statistics(yield_array: np.ndarray) -> Dict[str, float]:
    """
    Computes minimum, maximum, and mean yield statistics from a yield raster array.
    """
    valid_values = yield_array[~np.isnan(yield_array) & (yield_array > 0)]
    if len(valid_values) == 0:
        return {"min_yield": 0.0, "max_yield": 0.0, "mean_yield": 0.0, "valid_pixels": 0}

    return {
        "min_yield": float(np.min(valid_values)),
        "max_yield": float(np.max(valid_values)),
        "mean_yield": float(np.mean(valid_values)),
        "valid_pixels": int(len(valid_values))
    }

def compute_percentage_accuracy(observed: float, actual: float) -> float:
    """
    Calculates Percentage Accuracy (Pa) as defined in Chapter 4 of the thesis:
        Pa = 100 - (|Observed - Actual| / Actual * 100)
    """
    if actual == 0:
        raise ValueError("Actual value cannot be zero when computing percentage accuracy.")
    error_percent = (abs(observed - actual) / actual) * 100.0
    return float(100.0 - error_percent)
