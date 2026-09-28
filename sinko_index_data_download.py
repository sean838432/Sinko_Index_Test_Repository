'''
Example code to download data from the internet
'''

import pandas as pd

# IEM uses the 3-letter FAA identifier 'CAR' for KCAR
STATION = "CAR"
HOURS = 24  # Hours of data to fetch prior to the current time

# Construct IEM ASOS web service URL
url = (
    f"https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
    f"station={STATION}&"
    f"data=tmpf&data=dwpf&"
    f"hours={HOURS}&"
    f"format=onlycomma"
)

# Load CSV data directly into a pandas DataFrame
df = pd.read_csv(url)

# Save to local CSV file
output_file = "sinko_index_data.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")
print(df.head())
