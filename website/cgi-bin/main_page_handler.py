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

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		data=c['user'].value.strip()

		# Connect to MongoDb
		client = MongoClient('localhost', 27017)
		db = client["test"]

		print "Content-Type: text/html\n"

		# Get top5 artists by listening count
		popular_artists_one = db.artists.find().sort("listening_count",direction=-1).limit(5)

		print "success" + '\t' + data
		for artist in popular_artists_one:
			print '\t' + '<li class="list-group-item clearfix"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>' + '<span class="artist-name">' + artist['name'] + '</span>'+ '<span class="pull-right">Listening count:' +  str(artist['listening_count']) + '</span>'+ '</li>'
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