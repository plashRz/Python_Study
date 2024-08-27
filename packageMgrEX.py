import cowsay
import sys
import requests
import json

# if len(sys.argv) ==  2:
#     cowsay.cow("Hello,", sys.argv[1])

# Note pip is the buldled package manager
# pip install packageName to get new packages 
# pypi.org python package community

if len(sys.argv) !=  2:
    sys.exit("Band name required")

response = requests.get("http://itunes.apple.com/search?entity=song&limit=2&term="+ sys.argv[1])
# print(json.dumps(response.json(), indent=2))
res=response.json()

for item in res["results"]:
    print(item["trackName"])