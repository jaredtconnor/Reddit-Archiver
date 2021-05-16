from flask import Flask, render_template, json, request, redirect, url_for
from getpass import getpass
import os
from pymysql import NULL
from db_connection import Database


# Configuration
app = Flask(__name__)
db = Database()

# Routes 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/subreddits')
def subreddit(): 
    return render_template("subreddits.html")

@app.route('/posts', methods=['GET'])
def posts(): 

    post_data = db.read_posts()

    return render_template("posts.html", post_data = post_data)

@app.route('/posts', methods=['POST'])
def add_post(): 

    title = request.form.get('post_title')
    subreddit = request.form.get('post_subreddit')
    username = request.form.get('post_username')
    body = request.form.get('post_body')
    num_upvotes = request.form.get('num_upvotes')
    date = request.form.get('post_date')

    print(f''' 
            Title: {title}
            Subreddit: {subreddit}
            Username: {username}
            Body: {body}
            Upvotes: {num_upvotes}
            Date: {date}
    ''')


    return redirect(url_for('posts'))

@app.route('/users')
def users(): 
    return render_template("users.html")

@app.route('/comments')
def comments(): 
    comment_data = db.read_comments() 

    return render_template("comments.html", comment_data = comment_data)

@app.route('/subreddits_users')
def subreddits_users():
    return render_template("subreddits_users.html")

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
