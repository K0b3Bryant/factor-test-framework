import pandas as pd
import numpy as np
import statsmodels.api as sm
from config import CONFIG

def validate_inputs(returns_data: pd.DataFrame, factors_data: pd.DataFrame):
    # Ensure required columns exist
    if 'Date' not in returns_data.columns or 'Returns' not in returns_data.columns:
        raise ValueError("Returns data must have 'Date' and 'Returns' columns.")
    if 'Date' not in factors_data.columns:
        raise ValueError("Factors data must have a 'Date' column.")

    # Check date formats and ensure consistency
    returns_data['Date'] = pd.to_datetime(returns_data['Date'], format=CONFIG['date_format'])
    factors_data['Date'] = pd.to_datetime(factors_data['Date'], format=CONFIG['date_format'])

    # Merge on Date to align data
    merged_data = pd.merge(returns_data, factors_data, on='Date', how='inner')

    if merged_data.empty:
        raise ValueError("No overlapping dates between returns and factors data.")

    # Validate return values
    if CONFIG['return_type'] == 'log':
        if not np.allclose(merged_data['Returns'], np.log1p(merged_data['Returns']), atol=0.05):
            raise ValueError("Log returns are inconsistent with a 5% tolerance.")

    return merged_data[['Date', 'Returns']], merged_data.drop(columns=['Returns'])

def perform_factor_analysis(returns: pd.DataFrame, factors: pd.DataFrame):
    returns_values = returns['Returns']
    factors_values = factors.drop(columns=['Date'])

    # Add a constant for alpha
    factors_values = sm.add_constant(factors_values)

    # Run regression
    model = sm.OLS(returns_values, factors_values).fit()

    # Extract significant factors
    significant_factors = model.pvalues[model.pvalues < CONFIG['p_value_threshold']]
    significant_results = model.params.loc[significant_factors.index]

    return pd.DataFrame({
        'Parameter': significant_results,
        'P-Value': model.pvalues.loc[significant_results.index]
    }).rename_axis('Factor').reset_index()
