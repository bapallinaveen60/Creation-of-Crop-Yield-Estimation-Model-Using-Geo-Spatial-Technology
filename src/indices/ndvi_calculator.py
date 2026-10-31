"""
Normalized Difference Vegetation Index (NDVI) Calculation & Crop Mask Extraction
"""

from typing import Optional, Union, Tuple
import numpy as np

def calculate_ndvi(
    nir: np.ndarray,
    red: np.ndarray,
    eps: float = 1e-8
) -> np.ndarray:
    """
    Computes Normalized Difference Vegetation Index (NDVI) from Near-Infrared and Red bands:
        NDVI = (NIR - Red) / (NIR + Red)

    Args:
        nir: Near-infrared band array (Band 5 in Landsat 8)
        red: Red band array (Band 4 in Landsat 8)
        eps: Small epsilon to prevent division by zero

    Returns:
        NDVI array with values bounded in [-1.0, 1.0]
    """
    nir_f = nir.astype(np.float32)
    red_f = red.astype(np.float32)

    denominator = nir_f + red_f
    numerator = nir_f - red_f

    # Avoid zero division
    with np.errstate(divide="ignore", invalid="ignore"):
        ndvi = np.where(denominator > eps, numerator / denominator, np.nan)

    # Bound values to valid physical limits
    ndvi = np.clip(ndvi, -1.0, 1.0)
    return ndvi

def extract_crop_ndvi(
    ndvi: np.ndarray,
    classification_map: np.ndarray,
    crop_class_id: int = 1,
    nodata_value: float = np.nan
) -> np.ndarray:
    """
    Extracts NDVI values strictly for the specified crop class mask (e.g. Rice = 1).
    Equivalent to ArcMap Con(classification == 1, ndvi) / Extract by Attributes.
    """
    crop_mask = (classification_map == crop_class_id)
    crop_ndvi = np.where(crop_mask, ndvi, nodata_value)
    return crop_ndvi
