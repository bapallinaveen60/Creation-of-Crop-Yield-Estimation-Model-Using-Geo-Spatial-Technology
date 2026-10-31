"""
Geospatial Utility Functions
"""

from pathlib import Path
from typing import Dict, Union, Any
import numpy as np

def pixels_to_hectares(pixel_count: int, pixel_resolution_meters: float = 30.0) -> float:
    """
    Converts pixel count to area in hectares for square pixels.
    Area (m2) = pixel_count * resolution^2
    Area (ha) = Area (m2) / 10,000
    """
    area_m2 = pixel_count * (pixel_resolution_meters ** 2)
    return area_m2 / 10000.0

def save_numpy_to_geotiff(
    data: np.ndarray,
    reference_raster_path: Union[str, Path],
    output_raster_path: Union[str, Path],
    nodata: float = -9999.0,
    dtype: str = "float32"
) -> Path:
    """
    Saves a 2D numpy array to a GeoTIFF using spatial metadata from a reference raster.
    """
    try:
        import rasterio
    except ImportError:
        raise ImportError("rasterio is required to export GeoTIFFs.")

    output_raster_path = Path(output_raster_path)
    output_raster_path.parent.mkdir(parents=True, exist_ok=True)

    with rasterio.open(reference_raster_path) as ref:
        meta = ref.meta.copy()
        meta.update(
            driver="GTiff",
            count=1,
            dtype=dtype,
            nodata=nodata,
            height=data.shape[0],
            width=data.shape[1]
        )

        with rasterio.open(output_raster_path, "w", **meta) as dst:
            dst.write(data.astype(dtype), 1)

    return output_raster_path

def format_summary_table(metrics: Dict[str, Any]) -> str:
    """
    Formats dictionary metrics into a readable text table.
    """
    lines = ["Metric Name                     | Value", "-" * 45]
    for k, v in metrics.items():
        if isinstance(v, float):
            val_str = f"{v:,.2f}"
        else:
            val_str = str(v)
        lines.append(f"{k:<32} | {val_str}")
    return "\n".join(lines)
