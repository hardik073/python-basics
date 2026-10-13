

#We’ll get weather data for the past 7 days, analyze it, visualize it, and save it.
# Install required libraries: pip install requests pandas matplotlib

import requests
from datetime import datetime, timedelta

#Calclulate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

#Format dates for API (YYYY-MM0-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

import pandas as pd

daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

avg_temp = df['max_temp'].mean()

# You can still use it like a normal number:
if avg_temp > 20:
    print("It's a warm week!")
else:
    print("It's a bit cool this week!")