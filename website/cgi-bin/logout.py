#!/usr/bin/env python

import Cookie

import cgi

# set the cookie to expire
c=Cookie.SimpleCookie()
c['user']=''
c['user']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

# print the HTTP header
print c
print "Content-type: text/html\n\n"

redirectURL = "http://localhost:8001"

print 'Location: %s' % redirectURL
print # HTTP says you have to have a blank line between headers and content
print '<html>'
print '  <head>'
print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print '  </head>' 
print '  <body>'
print '  </body>'
print '</html>'