import requests

URL = "https://icanhazdadjoke.com/search"

r = requests.get(URL,
                 headers={'Accept': 'application/json'},
                 params={'term': 'cat','limit': 5}
                 )
data = r.json()
for x in data['results']:
    print(x)

print(data)
