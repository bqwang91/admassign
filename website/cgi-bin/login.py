#!/usr/bin/env python
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
import cgi, cgitb 
import Cookie
import pymongo
from pymongo import MongoClient
import py2neo
from py2neo import Graph

cgitb.enable() # for troubleshooting

data = cgi.FieldStorage()
user_id = data["user_id"].value

graph = Graph()

current_user = ""
user_id_record = graph.cypher.execute("MATCH (u:User {userId:'" + str(user_id) + "'}) RETURN u.userId")
if len(user_id_record) > 0:
	current_user = user_id_record[0]["u.userId"]

if current_user is not  "":
	c = Cookie.SimpleCookie()
	c['user'] = current_user
	
	print c
	print "Content-type: text/html\n\n"

	# empty lines so that the browser knows that the header is over
	print ""
	print ""
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
else:
	print "Content-Type: text/html\n"
	print "fail"


