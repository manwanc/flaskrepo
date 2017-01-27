#!/usr/bin/env python
 
from flask import Flask, render_template, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import TodoListResource
from resources import TodoResource

poll_data = {
   'question' : 'Which web framework do you use?',
   'fields'   : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}
############
###########
import os
import pymongo
import datetime
from pymongo import MongoClient
 
from flask import Flask, render_template, redirect, url_for, request

client = MongoClient()
# db = client.test_database
db = client['testdatabase']
collection = db['testcollections']
# collection = db.test_collection
app = Flask(__name__)
 
poll_data = {
   'question' : 'Which web framework do you use?',
   'fields'   : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}
post = {  "author": "Mike",
          "text": "My first blog post!",
          "tags": ["mongodb", "python", "pymongo"],
          "date": datetime.datetime.utcnow()}
user = {  "name": "mike",
          "pass": "123", 
          "date": datetime.datetime.utcnow()}
filename = 'data.txt'
 
@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)
  
@app.route('/About')
def rootAbout():
    return render_template('About.html', data=poll_data)
  
@app.route('/Contact')
def rootContact():
    return render_template('Contact.html', data=poll_data)
  
  
@app.route('/create')
def roocreate():
    return render_template('create.html', data=poll_data)
  
@app.route('/createpoll' , methods=['GET','POST'])
def createpoll():
    # if request.method == 'POST':
    #     # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    return render_template('createpoll.html', data=poll_data)
  

@app.route('/Home')
def Homee():
    return render_template('poll.html', data=poll_data)
@app.route('/poll')
def poll():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write( vote + '\n' )
    out.close()
    postpoll = { "selected": vote, "date": datetime.datetime.utcnow()}
    posts = db.post
    post_id = collection.insert_one(postpoll).inserted_id
    post_id
    return render_template('thankyou.html', data=poll_data,voted=vote)
 
@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0
 
    f  = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1
 
    return render_template('results.html', data=poll_data, votes=votes)
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
           return render_template('poll.html', data=poll_data)
    # if request.method == 'GET': 
    #        return render_template('poll.html', data=poll_data)
    return render_template('login.html', error=error)

sap = 0

@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None 
    if request.method == 'POST':
        postpoll = { "user": request.form['username'], "pass": request.form['password']}
        posts = db.users
        post_id = posts.insert_one(postpoll).inserted_id 
    return render_template('poll.html', data=poll_data)
    
  

    #alembic migrations
    #alchemy sql



api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')


# @app.route('/')
# def root():
#     return render_template('login.html', data=poll_data)
if __name__ == '__main__':
    app.run(debug=True)