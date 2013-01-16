import json
from pprint import pprint

f = open('pets.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)

# {u'pets': [{u'name': u'Jeffrey', u'species': u'Giraffe'},
#           {u'name': u'Gustav', u'species': u'Dog'},
#           {u'name': u'Gregory', u'species': u'Duck'}]}