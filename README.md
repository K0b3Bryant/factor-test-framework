# Factor Testing Framework

## Overview
This framework analyzes the relationship between a time series of returns and multiple factors. It runs regression analysis to evaluate factor significance and calculates alpha, beta, and p-values for each factor. The framework also includes input validation and supports rolling factor analysis.

---

## Key Features
1. **Factor Regression Analysis**:
   - Tests the significance of multiple factors on a return series.
   - Calculates alpha, factor coefficients (beta), and p-values.

2. **Rolling Analysis**:
   - Performs rolling regressions over a configurable window size to assess the stability of factor significance over time.

3. **Input Validation**:
   - Ensures input data includes the necessary columns and checks for overlapping dates between returns and factors.

4. **Configurable Parameters**:
   - Parameters like significance thresholds, rolling window size, and date format can be adjusted in the configuration file.

---

## Project Structure
- **main.py**: Entry point for the framework. Validates inputs, runs factor analysis, and outputs results.
- **utils.py**: Core functions for validation, factor regression analysis, and rolling regressions.
- **config.py**: Centralized configuration for all parameters.
