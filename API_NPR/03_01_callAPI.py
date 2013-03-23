from urllib2 import urlopen
from json import load

url = "http://api.npr.org/query?apiKey="
key = "API_KEY" # fake id only for the test
url = url + key

url = url + "&numResults=3&format=json&id="
npr_id = raw_input("Which NPR ID do you want to query?")
url += npr_id #1001, 1002, ... 1007

response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
	print story['title']['$text']