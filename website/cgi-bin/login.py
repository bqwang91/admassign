#!/usr/bin/env python
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
import cgi, cgitb 
import Cookie
import pymongo
from pymongo import MongoClient

cgitb.enable() # for troubleshooting

data = cgi.FieldStorage()
user_name = data["name"].value

c = Cookie.SimpleCookie()

c['user'] = user_name

print c
print "Content-type: text/html\n"

# empty lines so that the browser knows that the header is over
print ""
print ""

redirectURL = "http://localhost:8001/main.html"

print 'Location: %s' % redirectURL
print # HTTP says you have to have a blank line between headers and content
print '<html>'
print '  <head>'
print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print '  </head>' 
print '  <body>'
print '  </body>'
print '</html>'


