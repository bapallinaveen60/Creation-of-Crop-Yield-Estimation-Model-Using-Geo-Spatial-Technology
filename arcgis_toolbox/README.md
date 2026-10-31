# ArcGIS ModelBuilder & ArcPy Toolbox

This folder contains instructions, schemas, and script tools to implement the **Rice Yield Model** inside ESRI ArcGIS (ArcMap 10.x or ArcGIS Pro).

---

## 1. How the Model Was Built in ArcMap 10.8

As documented in Chapter 4 of the thesis report:
1. Open ArcMap standard interface and click the **ModelBuilder** icon in the Standard Toolbar.
2. Add the **Raster Calculator** tool from `Spatial Analyst Tools > Map Algebra`.
3. Set the input parameter to: `Crop_NDVI` (Single Band Raster).
4. Set the expression:
   ```text
   1841.6 * Exp(2.5262 * "%Crop_NDVI%")
   ```
5. Mark `Crop_NDVI` as a **Model Parameter** (Input) and `Output Crop Yield` as a **Model Parameter** (Output).
6. Save the model into an ArcGIS Toolbox named `Rice_Yield.tbx`.

---

## 2. Using the ArcPy Script Tool (`Rice_Yield_Model.py`)

If you want to create an ArcGIS Python Script Tool in ArcToolbox:
1. Open **ArcToolbox** in ArcMap or ArcGIS Pro.
2. Right click any Custom Toolbox > **Add > Script...**
3. Set Name to `RiceYieldEstimator` and Label to `Rice Yield Estimator`.
4. Point the script file to `Rice_Yield_Model.py`.
5. In the **Parameters** tab:
   - Parameter 0: `Input Crop NDVI Raster` (Type: `Raster Layer`, Direction: `Input`)
   - Parameter 1: `Output Crop Yield Raster` (Type: `Raster Layer`, Direction: `Output`)
6. Click Finish. You can now execute the tool from the ArcToolbox GUI just like any native spatial analyst tool!

---

## 3. Command Line Execution

```bash
python arcgis_toolbox/Rice_Yield_Model.py path/to/crop_ndvi.tif path/to/crop_yield_output.tif
```
