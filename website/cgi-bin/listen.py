#!/usr/bin/env python
import os
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
import pymongo
from pymongo import MongoClient
import py2neo
from py2neo import Graph
import Cookie
import cgi, cgitb 
import json

cgitb.enable() # for troubleshooting

data = cgi.FieldStorage()
artist_id = data["artist_id"].value

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

		graph = Graph()

		artist_test = graph.cypher.execute("match (u:User {userId:'" + user_id + "'})-[r:LISTENED]->(a:Artist {artistId:'" + artist_id + "'}) RETURN a")

		resultHtml = ""
		if len(artist_test) is 0:
			graph.cypher.execute("match (a:Artist {artistId:'" + artist_id + "'}), (u:User {userId:'" + user_id + "'}) create (u)-[:LISTENED {listening_count:1}]->(a)")
			graph.cypher.execute("match (a:Artist {artistId:'" + artist_id + "'}) SET a.listenCount = a.listenCount + 1")
			db.artists.update_one({'_id' : artist_id},{'$inc': {'listening_count': 1}}, upsert=False)
			db.artists.update_one({'_id' : artist_id},{'$inc': {'listener_count': 1}}, upsert=False)			
		else:
			graph.cypher.execute("match (u:User {userId:'" + user_id + "'})-[r:LISTENED]->(n:Artist {artistId:'" + artist_id + "'}) set r.listening_count = r.listening_count + 1")
			graph.cypher.execute("match (a:Artist {artistId:'" + artist_id + "'}) SET a.listenCount = a.listenCount + 1")
			graph.cypher.execute("match (a:Artist {artistId:'" + artist_id + "'}) SET a.uniqueCount = a.uniqueCount + 1")			
			db.artists.update_one({'_id' : artist_id},{'$inc': {'listening_count': 1}}, upsert=False)

		'''
		graph.cypher.execute("match (u:User {userId:'" + user_id + "'})-[r:LISTENED]->(n:Artist {artistId:'" + artist_id + "'}) set r.listening_count = r.listening_count + 1")
		graph.cypher.execute("match (a:Artist {artistId:'" + artist_id + "'}), (u:User {userId:'" + user_id + "'}) create (u)-[:LISTENED {listening_count:1}]->(a)")
		'''
		
		print "success" + '\t' + resultHtml.encode('ascii','ignore')

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
