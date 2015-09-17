#!/usr/bin/env python

import cgi, cgitb 
import sys

cgitb.enable() # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()

#this is the actual output
print "Content-Type: text/html\n"
#print data["name"].value
print "hello"

'''
import cgi
import cgitb; cgitb.enable()

print "Content-type: text/html"

print 
"""

<html>

<head>
	<title>Sample</title>
</head>

<body>
	<h3>Hello</h3>
</body>
</html>




"""
'''
