# Agricultural Statistics Data

This directory stores ground-truth agricultural statistics used to calibrate and validate the crop yield estimation model.

## Primary Sources
1. **Crop Production Statistics Information System (APS)**
   - Portal: [Ministry of Agriculture & Farmers Welfare, Government of India](https://aps.dac.gov.in/APY/Public_Report1.aspx)
   - Scope: District-level seasonal agricultural statistics for Andhra Pradesh, India.
2. **Directorate of Economics and Statistics (DES), Government of Andhra Pradesh**
   - Annual Agricultural Statistics reports for the Rabi season (2019-2020).
3. **ICRISAT (International Crops Research Institute for the Semi-Arid Tropics)**
   - Portal: [https://www.icrisat.org](https://www.icrisat.org)

## Key Ground Truth Values (Rabi 2019–2020)

| District | Area Under Rice (Hectares) | Production (Tonnes) | Actual Yield ($kg/ha$) |
|---|---|---|---|
| **East Godavari** (Model Development) | 166,544 | 888,267 | **5,333.551** |
| **West Godavari** (Model Validation) | 197,320 | 1,064,476 | **5,394.660** |

## Notes
- East Godavari district was used for establishing the empirical exponential regression relationship between Landsat 8 NDVI and field-scale paddy yield.
- West Godavari district served as an independent validation area to test spatial transferability of the developed ArcGIS model.
