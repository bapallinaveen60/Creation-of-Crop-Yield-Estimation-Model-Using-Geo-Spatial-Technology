"""
End-to-End Pipeline Runner
==========================
Executes the full crop yield modeling workflow:
1. Load or simulate Landsat 8 multispectral bands (Bands 3, 4, 5)
2. Compute False Color Composite (FCC)
3. Compute NDVI
4. Extract Rice Crop Mask
5. Apply Exponential Yield Model
6. Generate Validation Statistics
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np

from src.indices.ndvi_calculator import calculate_ndvi, extract_crop_ndvi
from src.modeling.yield_model import (
    estimate_yield_from_ndvi,
    calculate_yield_statistics,
    compute_percentage_accuracy
)
from src.config import GROUND_TRUTH

def run_sample_demonstration():
    print("=" * 65)
    print("  GeoVision Crop Yield Estimation Model Pipeline (Andhra Pradesh)")
    print("=" * 65)

    print("\n[Step 1] Loading Model Ground Truth Parameters...")
    eg_truth = GROUND_TRUTH["East Godavari"]
    wg_truth = GROUND_TRUTH["West Godavari"]

    print(f"  • East Godavari Actual Rice Area:  {eg_truth['actual_area_ha']:,} ha")
    print(f"  • East Godavari Actual Rice Yield: {eg_truth['actual_yield_kg_per_ha']:,} kg/ha")
    print(f"  • West Godavari Actual Rice Yield: {wg_truth['actual_yield_kg_per_ha']:,} kg/ha")

    print("\n[Step 2] Testing Exponential Yield Function:")
    print("  Formula: Yield (kg/ha) = 1841.6 * exp(2.5262 * NDVI)")

    test_ndvis = {
        "Min NDVI": 0.285720,
        "Mean NDVI": 0.408456,
        "Max NDVI": 0.531192
    }

    for label, val in test_ndvis.items():
        est_yield = estimate_yield_from_ndvi(val)
        print(f"  • {label:<10} ({val:.6f}) -> Estimated Yield: {est_yield:,.2f} kg/ha")

    print("\n[Step 3] Accuracy Assessment Comparison:")
    pa_eg_area = compute_percentage_accuracy(eg_truth["observed_area_ha"], eg_truth["actual_area_ha"])
    pa_eg_yield = compute_percentage_accuracy(eg_truth["observed_yield_kg_per_ha"], eg_truth["actual_yield_kg_per_ha"])
    pa_wg_yield = compute_percentage_accuracy(wg_truth["observed_yield_kg_per_ha"], wg_truth["actual_yield_kg_per_ha"])

    print(f"  • East Godavari Classified Area Accuracy: {pa_eg_area:.2f}% (Expected: 90.35%)")
    print(f"  • East Godavari Rice Yield Accuracy:      {pa_eg_yield:.2f}% (Expected: 98.41%)")
    print(f"  • West Godavari Validation Accuracy:      {pa_wg_yield:.2f}% (Expected: 99.71%)")

    print("\n[Step 4] Pipeline Simulation on Synthetic 2D Field Array:")
    # Synthetic grid representing 100x100 pixels of Godavari delta paddy fields
    np.random.seed(42)
    nir_sample = np.random.uniform(0.35, 0.65, size=(100, 100))
    red_sample = np.random.uniform(0.08, 0.22, size=(100, 100))

    simulated_ndvi = calculate_ndvi(nir_sample, red_sample)
    simulated_yield = estimate_yield_from_ndvi(simulated_ndvi)
    stats = calculate_yield_statistics(simulated_yield)

    print(f"  • Simulated Mean NDVI:  {np.nanmean(simulated_ndvi):.4f}")
    print(f"  • Simulated Min Yield:  {stats['min_yield']:,.2f} kg/ha")
    print(f"  • Simulated Max Yield:  {stats['max_yield']:,.2f} kg/ha")
    print(f"  • Simulated Mean Yield: {stats['mean_yield']:,.2f} kg/ha")

    print("\nPipeline execution completed successfully.")
    print("=" * 65)

if __name__ == "__main__":
    run_sample_demonstration()
