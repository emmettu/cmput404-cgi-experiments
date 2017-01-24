#!/usr/bin/env python
import os
import sys
import urlparse
from templates import login_page, secret_page

print "Content-Type: text/html"

username = 'emmett'
password = 'test'

length = os.environ['CONTENT_LENGTH']
cookie = os.environ['HTTP_COOKIE']

logged_in = False
if cookie == 'logged-in=True':
	logged_in = True

if length:
	bytes_to_read = int(length)
	content = sys.stdin.read(bytes_to_read)
	params = urlparse.parse_qs(content)
	#print "<pre>", content, "</pre>"
	if params['username'][0] == username and params['password'][0] == password:
		print "Set-Cookie: logged-in=True"
		logged_in = True
		
print

if not logged_in:
	print login_page()

else:
	print secret_page(username, password)
