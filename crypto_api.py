import requests

cryptocurrency = input("Enter The Crypto Currency Name : ").lower()

url = f"https://api.coingecko.com/api/v3/coins/{cryptocurrency}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Details for {cryptocurrency.upper()}:")
    print("Name:", data['name'])
    print("Symbol:", data['symbol'])
    print("Current Price (₹):", data['market_data']['current_price']['inr'])
    
else:
    print(f"Failed to fetch data for {cryptocurrency}. Status code:", response.status_code)
