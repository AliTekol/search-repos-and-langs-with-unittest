import requests
import json

def github_search(a,b):
    links = []
    params = {'q': a +'language:'+ b}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    json_file = response.json()
    for item in json_file['items']:
        links.append(item['url'])      
    return links

query = "arduino"
language = "python"
repos = github_search(query, language)