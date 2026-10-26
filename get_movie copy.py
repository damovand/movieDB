from omdbapi.movie_search import GetMovie
from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = '3dfc9c89'
titles = ['Inception', 'The Matrix', 'Interstellar']
movie_api = GetMovie(api_key=api_key)
movie_data = {}
for title in titles:
    try:
        result = movie_api.get_movie(title=title)
        if result and result.get('Response') == 'True':
            movie_data[result['Title']] = result
    except Exception as e:
        print(f"Error fetching {title}: {e}")
print(movie_data)
if __name__ == '__main__':
    GetMovie.run()