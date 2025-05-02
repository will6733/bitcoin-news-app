import os
from flask import Flask, jsonify, send_file, request
import requests

app = Flask(__name__)

NEWS_API_KEY = "2a86beb3faf54c6795fbc918e191d962"
@app.route('/')
def index():
    return send_file('index.html')
@app.route('/api/bitcoin-news')
def get_bitcoin_news():
    query = request.args.get('q', 'bitcoin')
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'sortBy': 'publishedAt',
        'pageSize': 10,
        'language': 'en',
        'apiKey': NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return jsonify(articles)
    else:
        return jsonify({'error': 'Failed to fetch news'}), 500
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)