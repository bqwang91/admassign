#!/usr/bin/env python
import os
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
import pymongo
from pymongo import MongoClient
import py2neo
from py2neo import Graph
import Cookie
import cgi, cgitb 
import json

cgitb.enable() # for troubleshooting

data = cgi.FieldStorage()
recommendation_type = data["recommendation_type"].value

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		user_id=c['user'].value.strip()

		print "Content-Type: text/html\n"
		
		# Connect to MongoDb
		client = MongoClient('localhost', 27017)
		db = client["comp5338Demo"]

		#Connect to Neo4j
		graph = Graph()

		artists_html = ""							
		top_5_artists_by_friends = None
		if recommendation_type is '1':
			top_5_artists_by_friends = graph.cypher.execute("match (u:User {userId:'" + str(user_id) + "'})-[:HAS_FRIEND]-(b:User)-[l:LISTENED]->(a:Artist) where not (u)-[:LISTENED]->(a) return a.artistId, a.name, sum(l.listening_count) order by sum(l.listening_count) desc limit 5")
			for result in top_5_artists_by_friends:
				artists_by_id = db.artists.find({"_id" : result["a.artistId"]})
				for artist in artists_by_id:
					artists_html += '<div class="col-sm-6 col-md-9"><div class="thumbnail">' + "<img src='...' alt='...'>" + '<div class="caption"><h3>' + artist['name'] + '</h3>' + '<p><b>profile url:</b> ' + artist['url'] + '</p>' + '<p>Listened by your firends:<b>' + str(result['sum(l.listening_count)']) + '</b> times</p>' + '<p>Listened by all: <b>' + str(artist['listening_count']) + '</b> times</p>' + '<p><b>' + str(artist['listener_count']) + '</b> listeners</p>' + "<p><a class='btn btn-primary listen' artist_id='" + artist['_id'] + "' role='button'>Listen</a></p></div></div></div>"
		elif recommendation_type is '2':
			top_5_artists_by_friends = graph.cypher.execute("match (u:User {userId:'" + str(user_id) + "'})-[:HAS_FRIEND]-(b:User)-[:LISTENED]->(a:Artist) where not (u)-[:LISTENED]->(a) return a.artistId, a.name, count(*) order by count(*) desc limit 5")
			for result in top_5_artists_by_friends:
				artists_by_id = db.artists.find({"_id" : result["a.artistId"]})
				for artist in artists_by_id:
					artists_html += '<div class="col-sm-6 col-md-9"><div class="thumbnail">' + '<img src="..." alt="...">' + '<div class="caption"><h3>' + artist['name'] + '</h3>' + '<p><b>profile url:</b> ' + artist['url'] + '</p>' + '<p><b>' + str(result['count(*)']) + '</b> of your friends has listened</p>' + '<p>Listened by all: <b>' + str(artist['listening_count']) + '</b> times</p>' + '<p><b>' + str(artist['listener_count']) + '</b> listeners</p>' + "<p><a class='btn btn-primary listen' artist_id='" + artist['_id'] + "' role='button'>Listen</a></p></div></div></div>"
		elif recommendation_type is '3':
			top_5_artists_by_friends = graph.cypher.execute("match (u:User {userId:'35'})-[:TAGGED]->(t1:Tag) with collect(t1.tagValue) as tags with tags[toInt(rand()*size(tags))] as tagPick match (t2:Tag {tagValue:tagPick})<-[:HAS_TAG]-(a:Artist), (u2:User {userId:'35'}), (a)<-[:LISTENED]-(u3:User) where not (u2)-[:LISTENED]->(a:Artist) return a.artistId, a.name, count(distinct u3), tagPick order by count(distinct u3) desc limit 5")
			for result in top_5_artists_by_friends:
				artists_by_id = db.artists.find({"_id" : result["a.artistId"]})
				for artist in artists_by_id:
					artists_html += '<div class="col-sm-6 col-md-9"><div class="thumbnail">' + '<img src="..." alt="...">' + '<div class="caption"><h3>' + artist['name'] + '</h3>' + '<p><b>profile url:</b> ' + artist['url'] + '</p>' + '<p>tagged by: <b>' + str(result['tagPick']) + '</b></p>' + '<p>Listened by all: <b>' + str(artist['listening_count']) + '</b> times</p>' + '<p><b>' + str(artist['listener_count']) + '</b> listeners</p>' + "<p><a class='btn btn-primary listen' artist_id='" + artist['_id'] + "' role='button'>Listen</a></p></div></div></div>"

		artists_html += "<script type='text/javascript' src='assets/js/main.js'></script>"
		print "success" + '\t' + artists_html.encode('ascii','ignore')

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
