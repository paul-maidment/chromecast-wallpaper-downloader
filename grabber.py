import requests
import re
import json
import os
from pathlib import Path
from time import sleep
import hashlib

Path(os.path.expanduser('~') + "/Pictures/downloaded-backgrounds").mkdir(parents=True, exist_ok=True)

rawChromecastHomeHTML = requests.get("https://clients3.google.com/cast/chromecast/home").content
raw = re.findall(b"(JSON\.parse\('.+'\))\)\.", rawChromecastHomeHTML)[0] 
filtered = raw.replace(b"\\x5b",b"[").replace(b"\\x22", b"\"").replace(b"\\/", b"/").replace(b"\\\\u003d", b"=").replace(b"\\x5d", b"]").replace(b"JSON.parse(\'", b"").split(b"]]]],[")
j = filtered[0].decode('utf-8') + "]]]]]"
decoded = json.loads(j)
for item in decoded[0]:
    response = requests.get(item[0])
    filename, extension = os.path.splitext(item[0])

    outfilename = hashlib.md5(response.content)

    if len(response.content) > 5000 and os.path.isfile(os.path.expanduser('~') + "/Pictures/downloaded-backgrounds/" + outfilename.hexdigest() + ".jpg") == False:
        of = open(
            os.path.expanduser('~')
            + "/Pictures/downloaded-backgrounds/" + outfilename.hexdigest() + ".jpg" , "wb")
        of.write(response.content)
        sleep(0.25)
