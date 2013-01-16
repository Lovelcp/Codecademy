################## Example response ##########################
# HTTP/1.1 200 OK
# Content-Type: text/xml; charset=UTF-8

# <?xml version="1.0" encoding="utf-8"?>
# <string xmlns="http://www.codecademy.com/">Accepted</string>
##############################################################

# A response line (line 2), which includes the three-digit HTTP status code;
# A header line or lines (line 3), which include further information about the server and its response;
# The body (line 5 and line 6), which contains the text message of the response (for example, "404" would have "file not found" in its body).

import requests
response = requests.get("http://placekitten.com/")

# print the header information from the response
print response.headers

########## RESULT #############
# {'via': '1.1 placekitten.com', 'content-encoding': 'gzip', 'transfer-encoding': 'chunked', 'set-cookie': '__cfduid=db57dc7c7238900fd2ef8c21095ee1bf01358173735; expires=Mon, 23-Dec-2019 23:50:00 GMT; path=/; domain=.placekitten.com', 'server': 'cloudflare-nginx', 'cache-control': 'max-age=7200, must-revalidate', 'date': 'Mon, 14 Jan 2013 14:28:56 GMT', 'cf-ray': '30b82148e65020c', 'content-type': 'text/html'}