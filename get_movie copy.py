from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = '3dfc9c89'

# Function to test OMDb API response
def test_omdb_api(api_key, movie_title):
    """
    Calls the OMDb API for a given movie title and validates the returned data.
    """
    base_url = "http://www.omdbapi.com/"
    params = {
        "t": movie_title,  # Search by title
        "apikey": api_key
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params, timeout=5)

        # Check HTTP status
        if response.status_code != 200:
            print(f"❌ HTTP Error: {response.status_code}")
            return False

        # Parse JSON
        data = response.json()

        # Check if API returned an error
        if data.get("Response") == "False":
            print(f"❌ API Error: {data.get('Error')}")
            return False

        # Validate expected fields
        expected_fields = ["Title", "Year", "Genre", "Director", "Actors", "imdbRating"]
        missing_fields = [field for field in expected_fields if field not in data]

        if missing_fields:
            print(f"❌ Missing fields in response: {missing_fields}")
            return False

        # Print validated data
        print("✅ API call successful and data validated:")
        for field in expected_fields:
            print(f"{field}: {data[field]}")

        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False


if __name__ == "__main__":
    # Replace with your OMDb API key
    API_KEY = api_key
    MOVIE_TITLE = "Inception"

    # Run the test
    test_omdb_api(API_KEY, MOVIE_TITLE)
