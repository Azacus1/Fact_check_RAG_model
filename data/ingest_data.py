import requests
import json

def download_data(url):
    response = requests.get(url)
    return response.json()

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    news_url = 'https://api.sampledata.com/news'
    news_data = download_data(news_url)
    save_data(news_data, 'data/news_data.json')
