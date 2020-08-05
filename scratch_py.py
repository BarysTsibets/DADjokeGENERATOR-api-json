import requests
import random

URL = "https://icanhazdadjoke.com/search"


def dad_joke():
    r = requests.get(URL, headers={'Accept': 'application/json'},
                     params={'term': topic, 'limit': 20})

    data = r.json()
    try:
        random.choice(data['results'])
    except IndexError:
        print(f"no joke with this word{topic}")
    else:
        print(f"I have {len(data['results'])} jokes for you! Here is one: ")
        r_joke = dict(random.choice(data['results']))
        print(r_joke['joke'])


while True:
    print("If u want to stop my Jokes input 'q'")
    topic = input("Let me tell you a joke !Give me a topic of the joke ?")
    dad_joke()
    if topic == "q":
        break









