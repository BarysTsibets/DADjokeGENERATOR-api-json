import requests
import random
from pyfiglet import figlet_format
from termcolor import colored


URL = "https://icanhazdadjoke.com/search"
header = figlet_format("DAD joke 3000!")
header = colored(header, color="magenta")

print("If u want to stop my Jokes input 'z'")

def dad_joke():
    r = requests.get(URL, headers={'Accept': 'application/json'},
                     params={'term': topic, 'limit': 20})

    data = r.json()
    try:
        random.choice(data['results'])
    except IndexError:
        print(f"no joke with this word {topic}")
    else:
        print(f"I have {len(data['results'])} jokes for you! Here is one: ")
        r_joke = dict(random.choice(data['results']))
        print(r_joke['joke'])


while True:
    print(header)
    topic = input("Let me tell you a joke !Give me a topic of the joke ?")
    dad_joke()
    if topic == "z":
        print("See U soon !")
        break

