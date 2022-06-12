# pip install requests
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit() # exit the program prematurely

# htttp request from python to server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])  # limited with 1 song
#print(response.json())
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])