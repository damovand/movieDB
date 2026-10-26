from flask import Flask, jsonify, request, render_template
from get_movie import test_omdb_api
from dotenv import load_dotenv
import os

load_dotenv()

global api_key
api_key = os.getenv('OMDB_API_KEY')  # Load the API key from environment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movieInfo', methods=['GET'])
def get_movie():
    movie_title = request.args.get('title')
    if not movie_title:
        return jsonify({'error': 'Title parameter is required'}), 400

    movie_data = test_omdb_api(api_key, movie_title)
    #if 'Error' in movie_data:
    #    return jsonify({'error': movie_data['Error']}), 404

    return movie_data  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8020, debug=True) 

