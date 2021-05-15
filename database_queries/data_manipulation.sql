-- : character represents user input

--Show users
SELECT * FROM users;

--Show comments
SELECT * FROM comments;

--Show relationship between Subreddits & users
SELECT * FROM subreddits_users;

--Show Post
SELECT * FROM post; 

--Show subreddits
SELECT * FROM subreddits;

--Add a new User
INSERT INTO users (username, karma, cakeDay)
VALUES (:usernameInput, :karmaInput, :cakeDayInput);

--Add a new Comment
INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
VALUES (:bodyInput, :numUpvotesInput, :commentDateInput, :postIDInput, :userIDInput);

--Add a new Post
INSERT INTO posts (title, body, numUpvotes, postDate, subredditID, userID) 
VALUES (:title, :body, :numUpvotes, :postDate, :subredditID, :userID)

--Add a new Subreddit
INSERT INTO subreddits (subredditName, about, numMembers, dateCreated)
VALUES (:subredditName, :about, :numMembers, :dateCreated)

--Add a relationship between Subreddits & users
INSERT INTO subreddits_users (subredditID, userID)
VALUES (:subredditIDInput, :userIDInput);

--Filter comments by Username, 'i_love_dachshunds93' as the username will give results
SELECT comments.body, users.username FROM comments
INNER JOIN users ON comments.userID=users.userID
WHERE users.username = :username;

--Filter subreddits by Posts, containing posts with >= 100 upvotes
SELECT subreddits.subredditName, posts.title, posts.numUpvotes, posts.Date FROM subreddits
LEFT JOIN posts ON subreddits.subredditID = posts.subredditID
WHERE posts.numUpvotes >= 100;

--Edit (Update) a Comment
UPDATE comments SET body = :newComment
WHERE comments.commentID = :commentID;

--Edit (Update) a Post's body and title
UPDATE posts 
SET title = :newTitle, 
    body = :newBody
WHERE posts.postID = :postID

--Edit (Update) a Subreddits description
UPDATE subreddits
SET about = :newAbout
WHERE subreddits.subredditID = :subredditID

--Delete a Comment
DELETE FROM comments
WHERE comments.commentID = :commentID;

--Delete a User
DELETE FROM users
WHERE users.userID = :userID;

--Removes the relationship between a Subreddit and a User
DELETE FROM subreddits_users
WHERE subreddits_users.subredditUserID = :subredditUserID;

--Delete a Post
DELETE FROM posts 
WHERE posts.postID = :postID; 

--Delete a Subreddit
DELETE FROM subreddits 
WHERE subreddits.subredditID = :subredditID; 



