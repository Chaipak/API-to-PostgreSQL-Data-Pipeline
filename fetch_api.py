import requests

def fetch_data():
    """Fetch data from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []