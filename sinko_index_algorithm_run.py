'''
Example code for computing the Sinko index
'''

import numpy as np
import pandas as pd


def calculate_rh(temp_f, dew_f):
    """Calculates Relative Humidity (%) using the Magnus-Tetens formula."""
    # Convert Fahrenheit to Celsius
    t_c = (temp_f - 32.0) * (5.0 / 9.0)
    td_c = (dew_f - 32.0) * (5.0 / 9.0)

    # Saturation vapor pressure (es) and actual vapor pressure (e) in hPa
    es = 6.112 * np.exp((17.67 * t_c) / (t_c + 243.5))
    e = 6.112 * np.exp((17.67 * td_c) / (td_c + 243.5))

    # Compute RH percentage and clamp between 0% and 100%
    rh = (e / es) * 100.0
    return np.clip(rh, 0.0, 100.0)


# Read the IEM observation CSV
df = pd.read_csv("sinko_index_input_data.csv")

# Convert temperature and dewpoint to numeric types, coercing invalid strings (e.g. 'M') to NaN
df["tmpf"] = pd.to_numeric(df["tmpf"], errors="coerce")
df["dwpf"] = pd.to_numeric(df["dwpf"], errors="coerce")

# Clean out rows missing temperature or dewpoint observations
df = df.dropna(subset=["tmpf", "dwpf"]).copy()

# Compute RH and round to the nearest whole integer
df["rh"] = calculate_rh(df["tmpf"], df["dwpf"]).round(0).astype(int)

# Save output to CSV
output_file = "sinko_index_output.csv"
df.to_csv(output_file, index=False)

print(f"Calculated RH for {len(df)} rows and saved to {output_file}:")
print(df[["station", "valid", "tmpf", "dwpf", "rh"]].head())
