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
		# Get top5 artists by number of liseners
		popular_artists_two = db.artists.find().sort("listener_count",direction=-1).limit(5)
		# Get top5 artists by 
		#popular_artists_one = db.artists.find().sort("listening_count",direction=-1).limit(5)

		artists_list_one = ""
		for artist in popular_artists_one:
			artists_list_one += '<li class="list-group-item clearfix"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>' + '<span class="artist-name">' + artist['name'] + '</span>'+ '<span class="pull-right">Listening count:' +  str(artist['listening_count']) + '</span>'+ '</li>'
		
		artists_list_two = ""
		for artist in popular_artists_two:
			artists_list_two += '<li class="list-group-item clearfix"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>' + '<span class="artist-name">' + artist['name'] + '</span>'+ '<span class="pull-right">Number of listeners:' +  str(artist['listener_count']) + '</span>'+ '</li>'

		print "success" + '\t' + data
		print '\t' + artists_list_one + '\t' + artists_list_two

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
