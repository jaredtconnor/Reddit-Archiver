from flask.globals import request
import pymysql
from pymysql.cursors import DictCursor
import os 

class Database:

    def connect(self):

        # Connection method for the current AWS CS340 db
        return pymysql.connect(
            host=os.environ.get('CS_340_AWS_db_host'),
            user=os.environ.get('CS_340_AWS_db_user'),
            password=os.environ.get('CS_340_AWS_db_pass'),
            database='reddit_archiver',
            cursorclass=pymysql.cursors.DictCursor
        )

    def read_subreddits(self):
        """Reads all information from the subreddits table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(''' 
                            SELECT 
                                s.subredditID, 
                                s.subredditName, 
                                s.about, 
                                s.numMembers, 
                                s.dateCreated
                            FROM subreddits s
                            ORDER BY s.subredditID ASC
                            ''')

            return cursor.fetchall()

        except Exception as e:
            print(e)
            return ()

        finally:
            con.close()

    def insert_subreddit(self, data):
        """Creates a new subreddit in the subreddits table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute(''' 

                       INSERT INTO subreddits (subredditName, about, numMembers, dateCreated)
                       VALUES (%s, %s, %s, %s)
                       ''',

                           (data['name'], data['about'], data['num_users'], data['date'])
                           )
            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def update_subreddits(self, data):
        """Updates an existing subreddit in the subreddits table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            UPDATE subreddits
                            SET 
                                numMembers = %s, 
                                about = %s, 
                                dateCreated = %s
                            WHERE subreddits.subredditID = %s
                            ''', (data['num_users'], data['about'], data['date'], data['subredditID']))

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def delete_subreddit(self, data):
        """Deletes a subreddit from the subreddit table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            DELETE FROM subreddits_users
                            WHERE subredditID = %s
                            ''', data['subredditID'])

            cursor.execute(''' 
                            DELETE FROM subreddits
                            WHERE subredditID = %s
                        ''', data['subredditID'])

            con.commit()
            return True

        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def read_users(self):
        """Reads all information from the users table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(''' 
                            SELECT * FROM users
                            ORDER BY userID ASC
                            ''')
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return()

        finally:
            con.close()

    def insert_user(self, data):
        """Creates a new user in the users table"""
        con = Database.connect(self)
        cursor= con.cursor()

        try:

            cursor.execute('''
                            INSERT INTO users(username, karma, cakeDay)
                            VALUES (%s, %s, %s)
                            ''',
                            (data['username'], data['karma'], data['cakeDay'])
            )

            con.commit()
            return True

        except Exception as e:
            print(e)
            con.rollback()
            return False

        finally:
            con.close()

    def update_users(self, data):
        """Updates an existing user in the user table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                        UPDATE users
                        SET 
                            username = %s,
                            cakeDay = %s, 
                            karma = %s
                        WHERE users.userID = %s
                        ''', (data['username'], data['cakeDay'], data['karma'], data['userID']))

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def delete_users(self, data):
        """Deletes a user from the users table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            DELETE FROM subreddits_users
                            WHERE userID = %s
                            ''', data['userID'])

            cursor.execute(''' 
                            DELETE FROM users
                            WHERE userID = %s
                        ''', data['userID'])

            con.commit()
            return True

        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def read_subreddits_users(self):
        """Reads all information from the subreddits_users table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('''
                            SELECT
                                su.subredditUserID, 
                                su.subredditID,
                                s.subredditName,
                                su.userID,
                                u.username
                            FROM subreddits_users su
                            LEFT JOIN subreddits s ON su.subredditID = s.subredditID
                            LEFT JOIN users u ON su.userID = u.userID
                            ORDER BY su.subredditUserID ASC
                            ''')
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return ()

        finally:
            con.close()

    def insert_subreddit_user(self, data):
        """Creates a relationship between subreddits & users in the subreddits_users table"""
        con = Database.connect(self)
        cursor= con.cursor()

        try:

            cursor.execute(''' 
                            SELECT subredditID
                            FROM subreddits
                            WHERE subredditName = %s
                            ''', data['subreddit_name'])

            subreddit_id = cursor.fetchone()

            cursor.execute(''' 
                            SELECT userID
                            FROM users
                            WHERE username = %s
                        ''', data['username']
                           )

            user_id = cursor.fetchone()

            cursor.execute('''
                            INSERT INTO subreddits_users (subredditID, userID)
                            VALUES (%s, %s)
                            ''',
                            (subreddit_id['subredditID'], user_id['userID'])
            )

            con.commit()
            return True

        except Exception as e:
            print(e)
            con.rollback()
            return False

        finally:
            con.close()

    def delete_subreddit_user(self, data):
        """Deletes a relationship between subreddits & users in the subreddits_users table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            DELETE FROM subreddits_users
                            WHERE subredditUserID = %s
                            ''', data['subredditUserID'])

            con.commit()
            return True

        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def read_posts(self):
        """Reads all information from the posts table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('''
                        SELECT
                        p.postID,
                        p.title,
                        p.body,
                        p.numUpvotes,
                        p.postDate,
                        s.subredditName,
                        u.username
                        FROM posts p
                        LEFT JOIN subreddits s
                        ON p.subredditID = s.subredditID
                        LEFT JOIN users u
                        ON p.userID = u.userID
                        ORDER BY postID ASC
                        ''')

            return cursor.fetchall()

        except Exception as e:
            print(e)
            return()

        finally:
            con.close()

    def insert_post(self, data):
        """Creates a new post in the posts table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute(''' 
                SELECT userID
                FROM users
                WHERE username = %s
            ''', data['username']
                           )

            user_id = cursor.fetchone()

            cursor.execute(''' 
                SELECT subredditID
                FROM subreddits
                WHERE subredditName = %s
            ''', data['subreddit'])

            subreddit_id = cursor.fetchone()

            if data['username'] == "NULL" and data['subreddit'] == "NULL":
                cursor.execute(''' 

                                       INSERT INTO posts (title,body,numUpvotes,postDate,userID, subredditID) 
                                       VALUES (%s, %s, %s, %s, NULL, NULL)
                                       ''',

                               (data['title'], data['body'], data['num_upvotes'], data['date'])
                               )

            elif data['username'] == "NULL" and data['subreddit'] != "NULL":
                cursor.execute(''' 

                                           INSERT INTO posts (title,body,numUpvotes,postDate,userID, subredditID) 
                                           VALUES (%s, %s, %s, %s, NULL, %s)
                                           ''',

                               (data['title'], data['body'], data['num_upvotes'], data['date'],
                                subreddit_id['subredditID'])
                               )
            elif data['username'] != "NULL" and data['subreddit'] == "NULL":
                cursor.execute(''' 

                                           INSERT INTO posts (title,body,numUpvotes,postDate,userID, subredditID) 
                                           VALUES (%s, %s, %s, %s, %s, NULL)
                                           ''',

                               (data['title'], data['body'], data['num_upvotes'], data['date'], user_id['userID'])
                               )
            else:
                cursor.execute(''' 
    
                           INSERT INTO posts (title,body,numUpvotes,postDate,userID, subredditID) 
                           VALUES (%s, %s, %s, %s, %s, %s)
                           ''',

                               (data['title'], data['body'], data['num_upvotes'], data['date'], user_id['userID'],
                                subreddit_id['subredditID'])
                               )
            con.commit()


            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def update_post(self, data):
        """Updates an existing post in the posts table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(''' 
                            SELECT userID
                            FROM users
                            WHERE username = %s
                        ''', data['username']
                           )

            user_id = cursor.fetchone()

            cursor.execute(''' 
                            SELECT subredditID
                            FROM subreddits
                            WHERE subredditName = %s
                        ''', data['subreddit'])

            subreddit_id = cursor.fetchone()

            if data['username'] == "NULL" and data['subreddit'] == "NULL":
                cursor.execute('''
                                UPDATE posts 
                                SET title = %s,
                                body = %s,
                                numUpvotes = %s,
                                postDate = %s,
                                subredditID = NULL,
                                userID = NULL
                                WHERE posts.postID = %s
                                ''',
                                (data['title'], data['body'], data['num_upvotes'], data['date'], data['postID'])
                               )

            elif data['username'] == "NULL" and data['subreddit'] != "NULL":
                cursor.execute('''
                                UPDATE posts 
                                SET title = %s,
                                body = %s,
                                numUpvotes = %s,
                                postDate = %s,
                                subredditID = %s,
                                userID = NULL
                                WHERE posts.postID = %s
                                ''',
                               (data['title'], data['body'], data['num_upvotes'], data['date'],
                                subreddit_id['subredditID'], data['postID'])
                               )

            elif data['username'] != "NULL" and data['subreddit'] == "NULL":
                cursor.execute('''
                                UPDATE posts 
                                SET title = %s,
                                body = %s,
                                numUpvotes = %s,
                                postDate = %s,
                                subredditID = NULL,
                                userID = %s
                                WHERE posts.postID = %s
                                ''',
                               (data['title'], data['body'], data['num_upvotes'], data['date'],
                                user_id['userID'], data['postID'])
                               )

            else:
                cursor.execute('''
                            UPDATE posts 
                            SET title = %s,
                            body = %s,
                            numUpvotes = %s,
                            postDate = %s,
                            subredditID = %s,
                            userID = %s
                            WHERE posts.postID = %s
                            ''',
                            (data['title'], data['body'], data['num_upvotes'], data['date'], subreddit_id['subredditID'],
                             user_id['userID'], data['postID']))

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def delete_post(self, data):
        """Deletes a post from the posts table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            DELETE
                            FROM
                            posts
                            WHERE
                            posts.postID = %s
                        ''', (data['postID']))

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def read_comments(self):
        """Reads all information from the comments table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('''
                SELECT
                    c.commentID,
                    u.username,
                    p.title,
                    c.body,
                    s.subredditName,
                    c.numUpvotes
                FROM comments c
                LEFT JOIN posts p
                ON c.postID = p.postID
                LEFT JOIN users u
                ON c.userID = u.userID
                LEFT JOIN subreddits s
                ON p.subredditID = s.subredditID
                ORDER BY commentID ASC
                ''')

            return cursor.fetchall()

        except Exception as e:
            print(e)
            return()

        finally:
            con.close()

    def filter_comments(self, data):
        """Filter comments by username"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('''
                            SELECT
                            c.commentID,
                            u.username,
                            p.title,
                            c.body,
                            s.subredditName,
                            c.numUpvotes
                            FROM comments c
                            LEFT JOIN posts p
                            ON c.postID = p.postID
                            LEFT JOIN users u
                            ON c.userID = u.userID
                            LEFT JOIN subreddits s
                            ON p.subredditID = s.subredditID
                            WHERE u.username = %s
                            ORDER BY commentID ASC
                            ''', data['username'])
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return ()

        finally:
            con.close()

    def insert_comment(self, data):
        """Creates a new comment in the comments table"""
        con = Database.connect(self)
        cursor= con.cursor()

        try:

            cursor.execute(''' 
                            SELECT userID
                            FROM users
                            WHERE username = %s
                        ''', data['username']
                           )

            user_id = cursor.fetchone()

            cursor.execute(''' 
                            SELECT postID
                            FROM posts
                            WHERE title = %s
                        ''', data['post_title'])

            post_id = cursor.fetchone()

            if data['username'] == "NULL" and data['post_title'] == "NULL":
                cursor.execute('''
                                INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
                                VALUES (%s, %s, %s, NULL, NULL)
                                ''', (data['body'], data['num_upvotes'], data['date'])
                               )

            elif data['username'] == "NULL" and data['post_title'] != "NULL":
                cursor.execute('''
                                INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
                                VALUES (%s, %s, %s, %s, NULL)
                                ''', (data['body'], data['num_upvotes'], data['date'], post_id['postID'])
                               )

            elif data['username'] != "NULL" and data['post_title'] == "NULL":
                cursor.execute('''
                                INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
                                VALUES (%s, %s, %s, NULL, %s)
                                ''', (data['body'], data['num_upvotes'], data['date'], user_id['userID'])
                               )

            else:
                cursor.execute('''
                                INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
                                VALUES (%s, %s, %s, %s, %s)
                                ''', (data['body'], data['num_upvotes'], data['date'], post_id['postID'], user_id['userID'])
                               )
            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def update_comments(self, data):
        """Updates an existing comment in the comments table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute(''' 
                            SELECT userID
                            FROM users
                            WHERE username = %s
                            ''', data['username'])

            user_id = cursor.fetchone()

            cursor.execute(''' 
                            SELECT postID
                            FROM posts
                            WHERE title = %s
                            ''', data['post_title'])

            post_id = cursor.fetchone()

            if data['username'] == "NULL" and data['post_title'] == "NULL":
                cursor.execute('''
                                UPDATE comments 
                                SET body = %s,
                                numUpvotes = %s,
                                commentDate = %s,
                                postID = NULL,
                                userID  = NULL
                                WHERE comments.commentID = %s
                                ''', (data['body'], data['num_upvotes'], data['date'], data['commentID']))

            elif data['username'] == "NULL" and data['post_title'] != "NULL":
                cursor.execute('''
                                UPDATE comments 
                                SET body = %s,
                                numUpvotes = %s,
                                commentDate = %s,
                                postID = %s,
                                userID  = NULL
                                WHERE comments.commentID = %s
                                ''', (data['body'], data['num_upvotes'], data['date'], post_id['postID'], data['commentID']))

            elif data['username'] != "NULL" and data['post_title'] == "NULL":
                cursor.execute('''
                                UPDATE comments 
                                SET body = %s,
                                numUpvotes = %s,
                                commentDate = %s,
                                postID = NULL,
                                userID  = %s
                                WHERE comments.commentID = %s
                                ''', (data['body'], data['num_upvotes'], data['date'],
                                    user_id['userID'], data['commentID'])
                               )

            else:
                cursor.execute('''
                                UPDATE comments 
                                SET body = %s,
                                numUpvotes = %s,
                                commentDate = %s,
                                postID = %s,
                                userID  = %s
                                WHERE comments.commentID = %s
                                ''', (data['body'], data['num_upvotes'], data['date'], post_id['postID'],
                                user_id['userID'], data['commentID'])
                               )

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()

    def delete_comment(self, data):
        """Deletes a comment from the comments table"""
        con = Database.connect(self)
        cursor = con.cursor()

        try:

            cursor.execute('''
                            DELETE
                            FROM
                            comments
                            WHERE
                            comments.commentID = %s
                        ''', (data['commentID']))

            con.commit()

            return True
        except Exception as e:
            print(e)
            con.rollback()

            return False
        finally:
            con.close()
