import json
import os

filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(filepath)

actualfile = os.path.join(filepath,'fb_feed\\fddata\\fb.json')

print(actualfile)

file = open(actualfile)
if not file is None:
    data = json.load(file)

    for d in data:
        print((d["fb_name"]),"has",len(d["Frinds"]),"friends")

        for f in d["Frinds"]:
            print(" ", f["fb_name"])
