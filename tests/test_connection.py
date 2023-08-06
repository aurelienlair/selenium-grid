import requests


def test_selenium_hub_connection():
    hub_url = "http://localhost:4444"

    try:
        response = requests.get(f"{hub_url}/wd/hub/status")
        response.raise_for_status()
        print("Selenium Hub connection successful.")
    except requests.exceptions.RequestException as e:
        print("Error connecting to Selenium Hub:")
        print(e)


if __name__ == "__main__":
    test_selenium_hub_connection()
