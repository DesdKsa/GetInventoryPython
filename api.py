import requests
import json

API_URL = "https://api.desdksamarket.com/v1/inventory/"
API_KEY = "tu-api-key"

def fetch_and_save_data():
    url = f"{API_URL}?key={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            output = []

            for product in data:
                output.append({
                    'Name': product['Product_title'],
                    'Description': product['Product_info'],
                    'Price': product['Product_price']
                })

            with open("products.json", "w") as file:
                json.dump(output, file, indent=4)

            print("The products have been saved in products.json")
        else:
            print(f"Error in the request: Code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    fetch_and_save_data()
