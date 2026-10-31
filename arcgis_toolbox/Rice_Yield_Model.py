"""
Rice Crop Yield Estimation Model for ArcGIS (ArcPy Tool)
=========================================================
B.Tech Thesis Project: Creation of Crop Yield Estimation Model Using Geo-Spatial Technology
Department of Geo-Engineering & RDT, Andhra University College of Engineering

This script automates the calculation of Paddy Crop Yield (kg/ha) from an input
crop-masked NDVI raster layer using the empirical exponential yield equation:

    Yield (kg/ha) = 1841.6 * exp(2.5262 * Crop_NDVI)

Usage:
    - In ArcMap 10.x / ArcGIS Pro: Attach this script to a Custom Geoprocessing Script Tool.
    - CLI execution with arcpy:
        python Rice_Yield_Model.py <input_crop_ndvi_raster> <output_yield_raster>
"""

import sys
import os

def calculate_crop_yield(input_ndvi_path, output_yield_path):
    try:
        import arcpy
        from arcpy.sa import Exp, Raster
        
        # Check out Spatial Analyst extension license
        if arcpy.CheckExtension("Spatial") == "Available":
            arcpy.CheckOutExtension("Spatial")
        else:
            raise RuntimeError("Spatial Analyst extension is required but not available.")
        
        arcpy.AddMessage(f"Processing Input Crop NDVI: {input_ndvi_path}")
        
        # Load input raster
        ndvi_raster = Raster(input_ndvi_path)
        
        # Empirical coefficients from East Godavari study
        # Yield = a * exp(b * NDVI)
        a = 1841.6
        b = 2.5262
        
        arcpy.AddMessage(f"Applying Yield Equation: Yield = {a} * exp({b} * NDVI)")
        
        # Geoprocessing calculation: 1841.6 * Exp(2.5262 * NDVI)
        yield_raster = a * Exp(b * ndvi_raster)
        
        # Save output raster
        arcpy.AddMessage(f"Saving Output Crop Yield Map to: {output_yield_path}")
        yield_raster.save(output_yield_path)
        
        arcpy.AddMessage("Crop Yield Estimation completed successfully!")
        arcpy.CheckInExtension("Spatial")
        return output_yield_path

    except ImportError:
        # Fallback implementation using GDAL/Rasterio if arcpy is not present
        print("ArcPy not detected in current environment. Using open-source rasterio engine...")
        import numpy as np
        import rasterio

        with rasterio.open(input_ndvi_path) as src:
            ndvi = src.read(1).astype(np.float32)
            nodata = src.nodata
            profile = src.profile.copy()

            # Mask nodata or non-crop areas
            mask = (ndvi != nodata) if nodata is not None else ~np.isnan(ndvi)
            
            yield_arr = np.zeros_like(ndvi, dtype=np.float32)
            yield_arr[mask] = 1841.6 * np.exp(2.5262 * ndvi[mask])
            
            if nodata is not None:
                yield_arr[~mask] = nodata
            else:
                yield_arr[~mask] = np.nan

            profile.update(dtype=rasterio.float32, nodata=nodata if nodata is not None else -9999.0)
            
            with rasterio.open(output_yield_path, 'w', **profile) as dst:
                dst.write(yield_arr, 1)

        print(f"Crop yield raster written successfully to: {output_yield_path}")
        return output_yield_path

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        in_raster = sys.argv[1]
        out_raster = sys.argv[2]
    else:
        # Default ArcToolbox parameter fetching
        try:
            import arcpy
            in_raster = arcpy.GetParameterAsText(0)
            out_raster = arcpy.GetParameterAsText(1)
        except Exception:
            print("Usage: python Rice_Yield_Model.py <input_crop_ndvi_raster> <output_yield_raster>")
            sys.exit(1)

    calculate_crop_yield(in_raster, out_raster)
