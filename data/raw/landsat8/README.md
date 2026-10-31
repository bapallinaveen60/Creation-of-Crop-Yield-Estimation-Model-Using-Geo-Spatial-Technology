# Landsat 8 OLI/TIRS Satellite Data Specifications

This directory contains information and instructions for acquiring the multi-spectral satellite imagery used in this study.

## Scene Details
- **Satellite / Sensor**: Landsat 8 Operational Land Imager (OLI) & Thermal Infrared Sensor (TIRS)
- **Spatial Resolution**: 30 meters (multispectral)
- **Acquisition Date**: February 23, 2020 (`2020-02-23`)
- **Phenological Stage**: Mature / Heading stage of the Rabi paddy crop
- **Coordinate Reference System**: WGS 1984 UTM Zone 44N (EPSG: 32644)
- **Data Provider**: USGS EarthExplorer ([https://earthexplorer.usgs.gov/](https://earthexplorer.usgs.gov/))

## Spectral Bands Reference

| Band | Band Name | Wavelength ($\mu m$) | Resolution ($m$) | Primary Role in This Project |
|---|---|---|---|---|
| **Band 1** | Coastal Aerosol | 0.43 – 0.45 | 30 | Atmospheric corrections |
| **Band 2** | Blue | 0.45 – 0.51 | 30 | Water body delineation |
| **Band 3** | Green | 0.53 – 0.59 | 30 | **FCC Composite (Band 3)** |
| **Band 4** | Red | 0.64 – 0.67 | 30 | **FCC (Band 4) & NDVI Red absorption** |
| **Band 5** | Near Infrared (NIR) | 0.85 – 0.88 | 30 | **FCC (Band 5) & NDVI NIR reflectance** |
| **Band 6** | Shortwave Infrared 1 (SWIR 1) | 1.57 – 1.65 | 30 | Moisture monitoring |
| **Band 7** | Shortwave Infrared 2 (SWIR 2) | 2.11 – 2.29 | 30 | Geological / mineral mapping |
| **Band 8** | Panchromatic | 0.50 – 0.68 | 15 | Sharpening |
| **Band 9** | Cirrus | 1.36 – 1.38 | 30 | Cloud screening |
| **Band 10**| Thermal Infrared (TIRS 1) | 10.60 – 11.19 | 100 | Surface temperature |
| **Band 11**| Thermal Infrared (TIRS 2) | 11.50 – 12.51 | 100 | Thermal validation |

## Instructions for Storing Data Locally
Raw Landsat 8 scenes (`.tar.gz` or uncompressed GeoTIFF `.TIF` files) should be placed here locally.
Due to file size constraints, raw GeoTIFFs are excluded from Git commits via `.gitignore`.
