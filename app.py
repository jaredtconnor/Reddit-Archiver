from flask import Flask, render_template, json, request
from getpass import getpass
import os
from db_connection import connection

# Configuration
app = Flask(__name__)

# Routes 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/subreddit')
def subreddit(): 
    return render_template("subreddits.html")

@app.route('/posts')
def posts(): 
    return render_template("posts.html")

@app.route('/test_route')
def test_route(): 

    query = "SELECT * FROM Comments"

    cursor = connection.cursor()
    cursor.execute(query) 

    connection.close()

    return json.dumps(cursor.fetchall())

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4932)) 
    app.run(port=port, debug=False) 