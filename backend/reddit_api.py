# Basic setup
import praw

client_id = 'QJDHzN5NvEyi5w'
secret_key = '7QYkpvR1Mt3tf7eQsZks_AlSKrXesA'
user_agent = 'RArchiver:v1 (by u/Scrape_340)'
username = 'Scrape_340'
password = 'OSUCS340'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=secret_key,
    user_agent=user_agent,
    username=username,
    password=password,
)

# Can turn off if want to post or comment
reddit.read_only = True


# Subreddit
subreddit = reddit.subreddit("OSUOnlineCS")

# # Print subreddit name
# print(subreddit.display_name)
#
# # Print subreddit description
# # We might not want to save this because it's long
# print(subreddit.description)
#
# # Print subreddit # of members
# print(subreddit.subscribers)
#
# # Print subreddit creation date
# # In UNIX time, need to convert it
# print(subreddit.created_utc)


# Posts
# Iterate through posts (Submissions) in a subreddit
# Can specify sort (new, hot, top, etc.) & # of posts
for submission in subreddit.new(limit=1):

    # # Print post title
    # print(submission.title)
    #
    # # Print post body
    # # Might want to check if it's a text post first via
    # # if submission.is_self
    # print(submission.selftext)
    #
    # # Print post # of upvotes
    # print(submission.score)
    #
    # # Print post creation date
    # # In UNIX time, need to convert it
    # print(submission.created_utc)
    #
    # # Print reddit post ID (NOT the FK)
    # print(submission.id)
    #
    # # Print post author (NOT the FK, a Redditor instance)
    # print(submission.author)

    # Comments on post (a CommentForest instance (top level comments), have to iterate through it)
    comments = submission.comments


# Comments
# Iterate through comments in a CommentForest (top level forest)
# Can specify sort (new, hot, top, etc.)
    for comment in comments:
        # Print comment body
        print(comment.body)
        #
        # # Print comment # of upvotes
        # print(comment.score)
        #
        # # Print comment creation date
        # # In UNIX time, need to convert it
        # print(comment.created_utc)
        #
        # # Print the post that this comment belongs to (NOT the FK, a Submission instance)
        # print(comment.submission)
        #
        # Print post author (NOT the FK, a Redditor instance)
        author = comment.author


# Users
#         # Print the username
#         print(author.name)
#
#         # Print user karma
#         print(author.link_karma + author.comment_karma)
#
#         # Print cake day
#         # In UNIX time, need to convert it
#         print(author.created_utc)
#
#         # Print user comments
#         # Need to iterate over them
#         print(author.comments)
#
#         # Print user posts
#         # Can filter various ways
#         for sub in author.submissions.top("all"):
#             print(sub.title)
