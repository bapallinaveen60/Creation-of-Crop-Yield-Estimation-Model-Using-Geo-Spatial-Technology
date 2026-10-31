# Data Directory Structure

This directory organizes all raw inputs, vector boundaries, and intermediate processed rasters used across the project pipeline.

## Directory Layout

```
data/
├── raw/
│   ├── boundaries/         # District boundary shapefiles (East & West Godavari)
│   ├── landsat8/           # Raw Landsat 8 OLI/TIRS satellite bands (B2 to B5)
│   └── statistics/         # District-level crop census & yield statistics
│       └── crop_statistics_ap_rabi_2019_2020.csv
└── processed/
    ├── fcc/                # False Color Composite rasters (B5, B4, B3)
    ├── ndvi/               # Normalized Difference Vegetation Index rasters
    └── yield_maps/         # Final estimated paddy yield raster layers (kg/ha)
```

## Data Management Policy
- Intermediate and large raster outputs (`.TIF`, `.tif`, `.img`) are excluded from Git via `.gitignore` to maintain a lean repository size (< 25 MB).
- Scripts and notebooks produce reproducible outputs automatically from raw input files.
