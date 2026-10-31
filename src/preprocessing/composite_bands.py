"""
False Color Composite (FCC) Generation
=======================================
Combines NIR (Band 5), Red (Band 4), and Green (Band 3) from Landsat 8
to produce an FCC image highlighting active vegetation and paddy fields in bright red.
"""

from pathlib import Path
from typing import Union
import numpy as np

def create_fcc_composite(
    nir_band_path: Union[str, Path],
    red_band_path: Union[str, Path],
    green_band_path: Union[str, Path],
    output_fcc_path: Union[str, Path]
) -> Path:
    """
    Creates a 3-band False Color Composite (FCC) GeoTIFF (NIR -> Red, Red -> Green, Green -> Blue).

    Args:
        nir_band_path: Path to Landsat 8 Band 5 (NIR)
        red_band_path: Path to Landsat 8 Band 4 (Red)
        green_band_path: Path to Landsat 8 Band 3 (Green)
        output_fcc_path: Output GeoTIFF file destination

    Returns:
        Path to generated composite raster.
    """
    try:
        import rasterio
    except ImportError:
        raise ImportError("rasterio is required to generate composite GeoTIFFs. Install with `pip install rasterio`.")

    output_fcc_path = Path(output_fcc_path)
    output_fcc_path.parent.mkdir(parents=True, exist_ok=True)

    with rasterio.open(nir_band_path) as src_nir, \
         rasterio.open(red_band_path) as src_red, \
         rasterio.open(green_band_path) as src_green:

        nir = src_nir.read(1)
        red = src_red.read(1)
        green = src_green.read(1)

        profile = src_nir.profile.copy()
        profile.update(count=3, dtype=nir.dtype)

        with rasterio.open(output_fcc_path, "w", **profile) as dst:
            dst.write(nir, 1)   # Red display channel
            dst.write(red, 2)   # Green display channel
            dst.write(green, 3) # Blue display channel

    return output_fcc_path
