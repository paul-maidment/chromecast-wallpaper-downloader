import json
import requests
import os
from time import sleep

data = requests.get("https://raw.githubusercontent.com/dconnolly/chromecast-backgrounds/master/backgrounds.json")
backgrounds_json = data.content
backgrounds_dict = json.loads(backgrounds_json)

i = 1
for item in backgrounds_dict:
    print(item['url'])
    response = requests.get(item['url'])
    filename, extension = os.path.splitext(item['url'])

    if len(response.content) > 5000:
        of = open('output/background-' + str(i) + "." + extension, "wb")
        of.write(response.content)
        i += 1
        sleep(0.25)
