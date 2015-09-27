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
search_name = data["artist_name"].value

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

		artists_by_name = db.artists.find({"name" : search_name})

		artists_html = ""
		for artist in artists_by_name:
			artists_html += '<div class="col-sm-6 col-md-5"><div class="thumbnail">' + '<img src="..." alt="...">' + '<div class="caption"><h3>' + artist['name'] + '</h3>' + '<p><b>profile url:</b> ' + artist['prof_url'] + '</p>' + '<p>Listened <b>' + str(artist['listening_count']) + '</b> times</p>' + '<p><b>' + str(artist['listener_count']) + '</b> listeners</p>' + '<p><a href="#" class="btn btn-primary" role="button">Listen</a></p></div></div></div>'
		
		if artists_by_name.count() is 0:
			artists_html = "<h4>No Artist has found</h4>"
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
