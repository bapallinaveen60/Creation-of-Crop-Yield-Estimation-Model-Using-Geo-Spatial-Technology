"""
Area of Interest (AOI) Vector Masking / Clipping
"""

from pathlib import Path
from typing import Union

def clip_raster_with_vector(
    input_raster_path: Union[str, Path],
    vector_boundary_path: Union[str, Path],
    output_clipped_path: Union[str, Path]
) -> Path:
    """
    Clips an input raster to the polygon boundary of the AOI.

    Args:
        input_raster_path: Input satellite raster (e.g. Landsat composite)
        vector_boundary_path: AOI vector shapefile / GeoJSON (e.g. East Godavari boundary)
        output_clipped_path: Destination clipped raster file
    """
    try:
        import rasterio
        from rasterio.mask import mask
        import geopandas as gpd
    except ImportError:
        raise ImportError("geopandas and rasterio are required for clipping. Install via `pip install geopandas rasterio`.")

    output_clipped_path = Path(output_clipped_path)
    output_clipped_path.parent.mkdir(parents=True, exist_ok=True)

    gdf = gpd.read_file(vector_boundary_path)

    with rasterio.open(input_raster_path) as src:
        # Match CRS
        if gdf.crs != src.crs:
            gdf = gdf.to_crs(src.crs)

        shapes = [geom for geom in gdf.geometry if geom is not None]
        out_image, out_transform = mask(src, shapes, crop=True)
        out_meta = src.meta.copy()

        out_meta.update({
            "driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform
        })

        with rasterio.open(output_clipped_path, "w", **out_meta) as dest:
            dest.write(out_image)

    return output_clipped_path
