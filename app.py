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

'''
####################################################################################
Subreddits Section
####################################################################################


'''
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


@app.route('/update_subreddits', methods=['POST'])
def update_subreddits():
    update_data = {
        'subredditID': request.form.get('subredditID'),
        'name': request.form.get('subredditName'),
        'num_users': request.form.get('numMembers'),
        'about': request.form.get('about'),
        'date': request.form.get('dateCreated'),
        'updated': request.form.get('updated')
    }

    if update_data['updated'] == "0":
        if ' ' in update_data['date']:
            i = update_data['date'].find(' ')
            update_data['date'] = update_data['date'][:i]
        return render_template("update_subreddits.html", update_data=update_data)

    else:
        db.update_subreddits(update_data)

        return redirect(url_for('subreddits'))


@app.route('/delete_subreddits', methods=['POST'])
def delete_subreddit():

    delete_data = {
        'subredditID': request.form.get('subredditID')
    }

    db.delete_subreddit(delete_data)

    return redirect(url_for('subreddits'))


'''
####################################################################################
Post Section
####################################################################################


'''
@app.route('/posts', methods=['GET'])
def posts(): 

    post_data = db.read_posts()
    subreddit_data = db.read_subreddits()
    user_data = db.read_users()

    return render_template("posts.html", post_data=post_data, subreddit_data=subreddit_data, user_data=user_data)


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

    subreddit_data = db.read_subreddits()
    user_data = db.read_users()

    if update_data['updated'] == "0":
        if ' ' in update_data['date']:
            i = update_data['date'].find(' ')
            update_data['date'] = update_data['date'][:i]
        return render_template("update_posts.html", update_data=update_data, subreddit_data=subreddit_data, user_data=user_data)

    else:
        db.update_post(update_data)

        return redirect(url_for('posts'))


@app.route('/delete_posts', methods=['POST'])
def delete_posts():
    delete_data = {
        'postID': request.form.get('postID')
    }

    db.delete_post(delete_data)
    return redirect(url_for('posts'))

'''
####################################################################################
Users Section
####################################################################################


'''
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


@app.route('/update_users', methods=['POST'])
def update_users():
    update_data = {
        'userID': request.form.get('userID'),
        'username': request.form.get('username'),
        'karma': request.form.get('karma'),
        'cakeDay': request.form.get('cakeDay'),
        'updated': request.form.get('updated')
    }

    print(update_data)

    if update_data['updated'] == "0":
        if ' ' in update_data['cakeDay']:
            i = update_data['cakeDay'].find(' ')
            update_data['cakeDay'] = update_data['cakeDay'][:i]
        return render_template("update_users.html", update_data=update_data)

    else:
        db.update_users(update_data)

        return redirect(url_for('users'))


@app.route('/delete_users', methods=['POST'])
def delete_users():
    delete_data = {
        'userID': request.form.get('userID')
    }

    db.delete_users(delete_data)

    return redirect(url_for('users'))

'''
####################################################################################
Comments Section
####################################################################################


'''
@app.route('/comments', methods=['GET'])
def comments(): 
    comment_data = db.read_comments()
    post_data = db.read_posts()
    user_data = db.read_users()

    return render_template("comments.html", comment_data=comment_data, post_data=post_data, user_data=user_data)


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


@app.route('/delete_comments', methods=['POST'])
def delete_comments():
    delete_data = {
        'commentID': request.form.get('commentID')
    }

    db.delete_comment(delete_data)
    return redirect(url_for('comments'))

'''
####################################################################################
Subreddit_user Section
####################################################################################


'''
@app.route('/subreddits_users', methods=['GET'])
def subreddits_users():
    subreddits_users_data = db.read_subreddits_users()
    subreddit_data = db.read_subreddits()
    user_data = db.read_users()

    return render_template("subreddits_users.html", subreddits_users_data=subreddits_users_data, subreddit_data=subreddit_data, user_data=user_data)


@app.route('/subreddits_users', methods=['POST'])
def add_subreddit_user():

    subreddit_user_data = {
        'subreddit_name': request.form.get('subreddit_name'),
        'username': request.form.get('username')
    }

    db.insert_subreddit_user(subreddit_user_data)

    return redirect(url_for('subreddits_users'))


@app.route('/delete_subs_users', methods=['POST'])
def delete_subreddit_user():
    delete_data = {
        'subredditUserID': request.form.get('subredditUserID')
    }

    db.delete_subreddit_user(delete_data)

    return redirect(url_for('subreddits_users'))

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4932)) 
    app.run(port=port, debug=False) 
