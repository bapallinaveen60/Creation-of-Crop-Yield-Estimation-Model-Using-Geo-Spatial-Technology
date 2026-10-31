"""
Project Configuration and Global Parameters
"""

from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"

# Landsat 8 Band Mapping for Standard FCC & NDVI
LANDSAT8_BANDS = {
    "COASTAL": "B1",
    "BLUE": "B2",
    "GREEN": "B3",
    "RED": "B4",
    "NIR": "B5",
    "SWIR1": "B6",
    "SWIR2": "B7",
    "PAN": "B8",
    "CIRRUS": "B9",
    "TIRS1": "B10",
    "TIRS2": "B11",
}

# Standard False Color Composite Band Order: (NIR, RED, GREEN) -> (B5, B4, B3)
FCC_BANDS = ("NIR", "RED", "GREEN")

# Land Use / Land Cover Classes
LULC_CLASSES = {
    1: {"name": "Rice Crop", "color": "#00FF00", "fcc_signature": "Bright Red"},
    2: {"name": "Vegetation and Other Crops", "color": "#008000", "fcc_signature": "Dark Red"},
    3: {"name": "Fallow Land and Barren Land", "color": "#D2B48C", "fcc_signature": "Pinkish Yellow"},
    4: {"name": "Built-up", "color": "#FF0000", "fcc_signature": "Cyan / Light Blue"},
    5: {"name": "Waterbodies", "color": "#0000FF", "fcc_signature": "Black / Dark Blue"},
    6: {"name": "Sandbar", "color": "#FFFF00", "fcc_signature": "Bright White"},
}

RICE_CLASS_ID = 1

# Empirical Exponential Yield Equation Parameters: y = a * exp(b * x)
# Calibrated for Rabi Rice in Godavari Delta, Andhra Pradesh
YIELD_MODEL_COEFFICIENT_A = 1841.6
YIELD_MODEL_COEFFICIENT_B = 2.5262
YIELD_MODEL_R_SQUARED = 0.9922

# Ground Truth Baseline Metrics (Andhra Pradesh Rabi 2019-2020)
GROUND_TRUTH = {
    "East Godavari": {
        "actual_area_ha": 166544.0,
        "observed_area_ha": 150485.8,
        "area_accuracy_pa": 90.35,
        "actual_yield_kg_per_ha": 5333.551,
        "observed_yield_kg_per_ha": 5418.36,
        "yield_accuracy_pa": 98.41,
    },
    "West Godavari": {
        "actual_yield_kg_per_ha": 5394.66,
        "observed_yield_kg_per_ha": 5379.22,
        "yield_accuracy_pa": 99.71,
    }
}
