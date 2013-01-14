from urllib2 import Request, urlopen, URLError

request = Request('http://www.pastesoft.com')

try:
	responses = urlopen(request)
	paste = responses.read()
	print paste
	# print paste[1:200]
except URLError, e:
	print 'No data. Error ', e

# -- OR ---

# import requests

# Make a GET request here and assign the result to kittens:
# kittens = requests.get('http://placekitten.com/')

# print kittens.text[559:1000]

# ----------------
# -- OR --

# from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
# kittens = urlopen('http://placekitten.com')

# response = kittens.read()
# body = response[559:1000]

# Add your 'print' statement here!
# print body

# ----------------
