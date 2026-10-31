# Mathematical Formulation & Model Derivation

This document outlines the mathematical foundation, index formulas, regression analysis, and accuracy evaluation metrics used in the study.

## 1. Normalized Difference Vegetation Index (NDVI)

The Normalized Difference Vegetation Index quantifies the difference between the reflectance of the Near-Infrared (NIR) spectrum (strongly reflected by healthy green plant mesophyll) and the Red spectrum (strongly absorbed by photosynthetic pigments such as chlorophyll $a$ and $b$):

$$\text{NDVI} = \frac{\rho_{\text{NIR}} - \rho_{\text{Red}}}{\rho_{\text{NIR}} + \rho_{\text{Red}}}$$

For Landsat 8 OLI:
$$\text{NDVI} = \frac{\text{Band 5} - \text{Band 4}}{\text{Band 5} + \text{Band 4}}$$

Values range theoretically from $-1.0$ to $+1.0$. For active vegetative paddy at heading/maturity:
$$\text{NDVI}_{\text{rice}} \in [0.2857, 0.5312]$$

---

## 2. Exponential Yield Estimation Model

Agricultural crop yields follow non-linear growth dynamics with respect to canopy density and chlorophyll content. An exponential regression model was fitted between field-level crop yield ($y$ in $kg/\text{ha}$) and observed satellite NDVI ($x$):

$$y = a \cdot e^{b \cdot x}$$

Where:
- $y$ = Estimated paddy yield ($kg/\text{hectare}$)
- $x$ = Rice crop NDVI value
- $a = 1841.6$ (Base productivity factor)
- $b = 2.5262$ (Canopy growth response coefficient)

### Empirical Fit Points

| Parameter | Observed NDVI ($x$) | Derived / Statistical Yield ($y$ in $kg/\text{ha}$) | Source |
|---|---|---|---|
| Minimum Point | $0.285720$ | $3,730.887$ | Interpolated |
| Mean Point | $0.408456$ | $5,333.551$ | District Census Ground Truth |
| Maximum Point | $0.531192$ | $6,936.216$ | Interpolated |

### Goodness of Fit
$$R^2 = 0.9922$$

The coefficient of determination indicates that $99.22\%$ of the spatial variance in estimated yield is explained by the exponential relationship with mature canopy NDVI.

---

## 3. Crop Area Calculation

$$\text{Area}_{\text{pixels}} = \sum_{i=1}^{N} 1$$
$$\text{Area} (m^2) = \text{Count} \times (\Delta x \times \Delta y) = \text{Count} \times (30 \times 30) = \text{Count} \times 900$$
$$\text{Area} (\text{Hectares}) = \frac{\text{Area} (m^2)}{10,000}$$

---

## 4. Percentage Accuracy Assessment ($P_a$)

The accuracy of the model relative to actual ground truth statistics is calculated as:

$$P_a = 100 - \left( \frac{|\text{Observed} - \text{Actual}|}{\text{Actual}} \times 100 \right)$$

### Applied to Paddy Area (East Godavari):
$$P_a = 100 - \left( \frac{|150485.8 - 166544|}{166544} \times 100 \right) = 100 - 9.64\% = 90.35\%$$

### Applied to Rice Yield (East Godavari):
$$P_a = 100 - \left( \frac{|5418.36 - 5333.551|}{5333.551} \times 100 \right) = 100 - 1.59\% = 98.41\%$$

### Applied to Rice Yield (West Godavari Validation):
$$P_a = 100 - \left( \frac{|5379.22 - 5394.66|}{5394.66} \times 100 \right) = 100 - 0.29\% = 99.71\%$$
