#!/usr/bin/env python
import os
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
import pymongo
from pymongo import MongoClient
import Cookie
import cgi, cgitb 
import json

cgitb.enable() # for troubleshooting

data = cgi.FieldStorage()
search_tag_name = data["tag_name"].value

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		data=c['user'].value.strip()

		print "Content-Type: text/html\n"
		
		# Connect to MongoDb
		client = MongoClient('localhost', 27017)
		db = client["test"]

		top_5_artists_by_tag = db.artists.find({"tags" : search_tag_name}).sort("listening_count",direction=-1).limit(5)

		artists_html = ""
		for artist in top_5_artists_by_tag:
			artists_html += '<li class="list-group-item clearfix"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>' + '<span class="artist-name">' + artist['name'] + '</span>'+ '<span class="pull-right">Number of listeners:' +  str(artist['listening_count']) + '</span>'+ '</li>'
		
		print "success" + '\t' + artists_html

	except KeyError:
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
