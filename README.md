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

---

## Usage
1. Prepare your input data as two DataFrames:
   - **Returns Data**:
     - `Date`: The date for each observation (YYYY-MM-DD format).
     - `Returns`: The return series to analyze.
   - **Factors Data**:
     - `Date`: The date for each observation.
     - One or more columns representing factor values.

2. Update the `CONFIG` file as needed:
   - `date_format`: Format of the date column (default is `%Y-%m-%d`).
   - `p_value_threshold`: Significance threshold for factors (default is `0.05`).
   - `rolling_window_size`: Window size for rolling analysis (default is `20`).

3. Run `main.py` to execute the factor analysis and view the results:
   - Outputs alpha, beta, and p-values for significant factors.
   - Includes results for rolling regressions if enabled.

---
