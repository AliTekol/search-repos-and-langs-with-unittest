import requests
import json

def github_search(a,b):
    files = []
    params = {'q': a +'language:'+ b}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    json_file = response.json()
    for item in json_file['items']:
        files.append(item['url'])
        
    return files

query = "arduino"
language = "python"
repos = github_search(query, language)