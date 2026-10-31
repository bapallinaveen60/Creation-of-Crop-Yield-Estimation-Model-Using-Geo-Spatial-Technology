# Results & Discussion

## 1. Crop Area Extraction & SVM Classification

Supervised classification using the Support Vector Machine (SVM) algorithm on standard Landsat 8 False Color Composite (FCC: Bands 5, 4, 3) yielded high separability between paddy fields and non-crop land covers.

### East Godavari Crop Area Evaluation
- **Actual Cultivated Paddy Area**: $166,544.0\,\text{Hectares}$
- **Observed (Classified) Area**: $150,485.8\,\text{Hectares}$
- **Absolute Difference**: $16,058.2\,\text{Hectares}$
- **Classification Accuracy ($P_a$)**: **$90.35\%$**

The discrepancy of $\approx 9.65\%$ is primarily attributed to mixed-pixel effects along bunds, narrow irrigation canals, and smallholder fragmented parcels near settlements.

---

## 2. Crop Yield Model Results

Applying the exponential yield formula:
$$\text{Yield} (\text{kg/ha}) = 1841.6 \times e^{2.5262 \times \text{NDVI}}$$

### East Godavari (Development Study Area)

| Metric | Estimated Value | Ground Truth Value | Accuracy ($P_a$) |
|---|---|---|---|
| **Minimum Yield** | $3,790.21\,\text{kg/ha}$ | — | — |
| **Maximum Yield** | $7,046.50\,\text{kg/ha}$ | — | — |
| **Mean Observed Yield** | **$5,418.36\,\text{kg/ha}$** | **$5,333.55\,\text{kg/ha}$** | **$98.41\%$** |

### West Godavari (Validation Study Area)

| Metric | Estimated Value | Ground Truth Value | Accuracy ($P_a$) |
|---|---|---|---|
| **Minimum Yield** | $3,492.45\,\text{kg/ha}$ | — | — |
| **Maximum Yield** | $7,265.99\,\text{kg/ha}$ | — | — |
| **Mean Observed Yield** | **$5,379.22\,\text{kg/ha}$** | **$5,394.66\,\text{kg/ha}$** | **$99.71\%$** |

---

## 3. Key Findings

1. **High Explanatory Power of Peak Heading NDVI**:
   - The exponential regression curve demonstrates that mature rice canopy NDVI strongly correlates with final harvested grain yield ($R^2 = 0.9922$).
2. **Spatial Transferability**:
   - The model developed on East Godavari performed with an astonishing **$99.71\%$ accuracy** when transferred directly to West Godavari, confirming its applicability across the Godavari delta agro-ecological tract.
3. **Operational Value**:
   - Unlike conventional Crop Cutting Experiments (CCEs) that take weeks or months post-harvest, satellite-based remote sensing provides spatially distributed yield maps **weeks before harvest**, enabling timely decisions for agricultural procurement, logistics, credit, and crop insurance.
