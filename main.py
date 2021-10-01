import json
import requests
import os
from pathlib import Path
from time import sleep

data = requests.get("https://raw.githubusercontent.com/dconnolly/chromecast-backgrounds/master/backgrounds.json")
backgrounds_json = data.content
backgrounds_dict = json.loads(backgrounds_json)

Path(os.path.expanduser('~') + "/Pictures/chromecast-backgrounds").mkdir(parents=True, exist_ok=True)

i = 1
for item in backgrounds_dict:
    print(item['url'])
    response = requests.get(item['url'])
    filename, extension = os.path.splitext(item['url'])

    if len(response.content) > 5000:
        of = open(
            os.path.expanduser('~')
            + "/Pictures/chromecast-backgrounds/background-" + str(i) + "." + extension, "wb")
        of.write(response.content)
        i += 1
        sleep(0.25)
