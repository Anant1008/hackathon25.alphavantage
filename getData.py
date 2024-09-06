import requests
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=G54BOOT15IDPBJSF'
r = requests.get(url)
data = r.json()
with open('response_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # Use 'indent=4' to make the JSON pretty-printed

print("Data saved to response_data.json")
print(data)