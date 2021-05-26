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


@app.route('/subreddits', methods=['GET'])
def subreddits(): 

    subreddit_data = db.read_subreddits()

    return render_template("subreddits.html", subreddit_data = subreddit_data)


@app.route('/subreddits', methods=['POST'])
def add_subreddit(): 

    subreddit_data = { 
        'name': request.form.get('subreddit_name'),
        'num_users': request.form.get('subreddit_users'),
        'about': request.form.get('subreddit_about'),
        'date': request.form.get('subreddit_date_created')
    }

    db.insert_subreddit(subreddit_data)

    return redirect(url_for('subreddits'))


@app.route('/posts', methods=['GET'])
def posts(): 

    post_data = db.read_posts()

    return render_template("posts.html", post_data = post_data)


@app.route('/update_subreddit', methods=['PUT'])
def update_subreddits():
    update_data = {
        'commentID': request.form.get('commentID'),
        'username': request.form.get('comment_username'),
        'post_title': request.form.get('title'),
        'body': request.form.get('body'),
        'subreddit': request.form.get('subredditName'),
        'num_upvotes': request.form.get('numUpvotes'),
        'date': request.form.get('commentDate'),
        'updated': request.form.get('updated')
    }

    if update_data['updated'] == "0":
        if ' ' in update_data['date']:
            i = update_data['date'].find(' ')
            update_data['date'] = update_data['date'][:i]
        return render_template("update_comments.html", update_data=update_data)

    else:
        db.update_comments(update_data)

        return redirect(url_for('comments'))

@app.route('/posts', methods=['POST'])
def add_post():
    post_data = {
        'title': request.form.get('post_title'),
        'subreddit': request.form.get('post_subreddit'),
        'username': request.form.get('post_username'),
        'body': request.form.get('post_body'),
        'num_upvotes': request.form.get('num_upvotes'),
        'date': request.form.get('post_date')
    }

    db.insert_post(post_data)

    return redirect(url_for('posts'))


@app.route('/update_posts', methods=['POST'])
def update_posts():
    update_data = {
        'postID': request.form.get('postID'),
        'title': request.form.get('title'),
        'subreddit': request.form.get('subredditName'),
        'username': request.form.get('username'),
        'body': request.form.get('body'),
        'num_upvotes': request.form.get('numUpvotes'),
        'date': request.form.get('postDate'),
        'updated': request.form.get('updated')
    }

    if update_data['updated'] == "0":
        if ' ' in update_data['date']:
            i = update_data['date'].find(' ')
            update_data['date'] = update_data['date'][:i]
        return render_template("update_posts.html", update_data=update_data)

    else:
        db.update_post(update_data)

        return redirect(url_for('posts'))


@app.route('/users', methods=['GET'])
def users():
    user_data = db.read_users()

    return render_template("users.html", user_data=user_data)


@app.route('/users', methods=['POST'])
def add_user():

    user_data = {
        'username': request.form.get('username'),
        'karma': request.form.get('karma'),
        'cakeDay': request.form.get('cake_day')
    }

    db.insert_user(user_data)

    return redirect(url_for('users'))


@app.route('/comments', methods=['GET'])
def comments(): 
    comment_data = db.read_comments() 

    return render_template("comments.html", comment_data = comment_data)


@app.route('/comments', methods=['POST'])
def add_filter_comment():
    if request.form.get('filter_username') is None:
        comment_data = {
            'username': request.form.get('username'),
            'post_title': request.form.get('post_title'),
            'body': request.form.get('body'),
            'num_upvotes': request.form.get('num_upvotes'),
            'date': request.form.get('comment_date')
        }

        db.insert_comment(comment_data)

        return redirect(url_for('comments'))

    else:
        filter_data = {
            'username': request.form.get('filter_username')
        }

        comment_data = db.filter_comments(filter_data)

        return render_template("comments.html", comment_data=comment_data)


@app.route('/update_comments', methods=['POST'])
def update_comments():
    update_data = {
        'commentID': request.form.get('commentID'),
        'username': request.form.get('comment_username'),
        'post_title': request.form.get('title'),
        'body': request.form.get('body'),
        'subreddit': request.form.get('subredditName'),
        'num_upvotes': request.form.get('numUpvotes'),
        'date': request.form.get('commentDate'),
        'updated': request.form.get('updated')
    }

    if update_data['updated'] == "0":
        if ' ' in update_data['date']:
            i = update_data['date'].find(' ')
            update_data['date'] = update_data['date'][:i]
        return render_template("update_comments.html", update_data=update_data)

    else:
        db.update_comments(update_data)

        return redirect(url_for('comments'))


@app.route('/subreddits_users', methods=['GET'])
def subreddits_users():
    subreddits_users_data = db.read_subreddits_users()

    return render_template("subreddits_users.html", subreddits_users_data=subreddits_users_data)


@app.route('/subreddits_users', methods=['POST'])
def add_subreddit_user():

    subreddit_user_data = {
        'subreddit_name': request.form.get('subreddit_name'),
        'username': request.form.get('username')
    }

    db.insert_subreddit_user(subreddit_user_data)

    return redirect(url_for('subreddits_users'))


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4932)) 
    app.run(port=port, debug=False) 
