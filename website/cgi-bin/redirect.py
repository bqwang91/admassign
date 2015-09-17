#!/usr/bin/env python
import os
import Cookie
import cgi, cgitb 

cgitb.enable() # for troubleshooting


print "Content-Type: text/html\r\n"
print """
<html>
<body>
<h1>Check the cookie</h1>
"""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['user'].value
        print "cookie data: "+data+"<br>"
    except KeyError:
        print "The cookie was not set or has expired<br>"


print """
</body>
</html>

"""
