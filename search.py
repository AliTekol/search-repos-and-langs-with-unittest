import requests
import json


def github_search(a,b):
    params = {'q': a +'language:'+ b}
    
    r = requests.get('https://api.github.com/search/repositories', params=params)
    p = r.json()
    for item in p['items']:
        lists = item['url']
    return lists
    

query = "arduino"
language = "python"

repos = github_search(query, language)