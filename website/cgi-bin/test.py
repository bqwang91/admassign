#!/usr/bin/python
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/pymongo-3.0.3-py2.7-macosx-10.10-x86_64.egg')
import cgi, cgitb 
import pymongo
from pymongo import MongoClient

cgitb.enable() # for troubleshooting

#get post or get data
data = cgi.FieldStorage()


client = MongoClient('localhost', 27017)
db = client["bwan4674"]

posts = db.blog

first_post = posts.find_one()


#this is the actual output
print "Content-Type: text/html\n"
print data["name"].value
print first_post
