#!/usr/bin/python
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
import cgi, cgitb 
import pymongo
from pymongo import MongoClient
import py2neo
from py2neo import Graph

cgitb.enable() # for troubleshooting

#get post or get data
data = cgi.FieldStorage()

#MongoDb
client = MongoClient('localhost', 27017)
db = client["bwan4674"]

posts = db.blog

first_post = posts.find_one()

#neo4j
graph = Graph()
graph.cypher.execute("CREATE (a:Person {name:{N}})", {"N": "Alice"})


#this is the actual output
print "Content-Type: text/html\n"

#GET data from front end
print data["name"].value

#Neo4j data
for record in graph.cypher.stream("MATCH (n) RETURN n LIMIT 10"):
    print record[0]

#MongoDb data
print first_post
