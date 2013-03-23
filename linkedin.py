# https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code
#                                           &code=AUTHORIZATION_CODE
#                                           &redirect_uri=YOUR_REDIRECT_URI
#                                           &client_id=YOUR_API_KEY
#                                           &client_secret=YOUR_SECRET_KEY
#

import oauth2 as oauth
import urlparse 
 
cKey           = "nt84qf0wg07i"
cSecret        = "3JCNElwU2ouMNhY3"
consumer = oauth.Consumer(cKey, cSecret)
client = oauth.Client(consumer)

# get the token
request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])
  
request_token = dict(urlparse.parse_qsl(content))

# redirect to provider
authorize_url =      'https://api.linkedin.com/uas/oauth/authorize'
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print 

# manual verification (PIN)
accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')


# get Access Token
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)
 
resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))
 
print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print
print "You may now access protected resources using the access tokens above."
print