import json
import os


def showProduct(num=9):
    print("My Product Count ", num)

showProduct(8)

print("1 > ", os.path.dirname(__file__))
print("2 > ", os.path.dirname(__file__), '..')
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("3 > ", filepath)
actualfile = os.path.join(filepath, 'Data\\Address.json')
print("4 > ", actualfile)


f = open(actualfile)
if not f is None:
    data = json.load(f)
    for x in data:
        print(x["countryid"],x["country"])
        for s in x["state"]:
            print("  ",s["stateid"],s["state"])
            for a in s["addresses"]:
                print ("        ",a["postcode"])

# Closing file
f.close()


