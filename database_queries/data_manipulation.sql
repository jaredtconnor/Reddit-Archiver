-- : character represents user input

--Show users
SELECT * FROM users
ORDER BY userID ASC;

--Show comments
SELECT c.commentID, u.username, p.title, c.body, s.subredditName, c.numUpvotes FROM comments c
LEFT JOIN posts p
ON c.postID = p.postID
LEFT JOIN users u
ON c.userID = u.userID
LEFT JOIN subreddits s
ON p.subredditID = s.subredditID
ORDER BY commentID ASC;

--Show relationship between Subreddits & users
SELECT su.subredditUserID, su.subredditID, s.subredditName, su.userID, u.username FROM subreddits_users su
LEFT JOIN subreddits s ON su.subredditID = s.subredditID
LEFT JOIN users u ON su.userID = u.userID
ORDER BY su.subredditUserID ASC;

--Show Post
SELECT p.postID, p.title, p.body, p.numUpvotes, p.postDate, s.subredditName, u.username FROM posts p
LEFT JOIN subreddits s
ON p.subredditID = s.subredditID
LEFT JOIN users u
ON p.userID = u.userID
ORDER BY postID ASC;

--Show subreddits
SELECT s.subredditID, s.subredditName, s.about, s.numMembers, s.dateCreated FROM subreddits s
ORDER BY s.subredditID ASC;

--Add a new User
INSERT INTO users (username, karma, cakeDay)
VALUES (:usernameInput, :karmaInput, :cakeDayInput);

--Add a new Comment (next 3 queries)
SELECT postID FROM posts
WHERE title = :postTitleInput;

SELECT userID FROM users
WHERE username = :usernameInput;

INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
VALUES (:bodyInput, :numUpvotesInput, :commentDateInput, postID, userID);

--Add a new Post (next 3 queries)
SELECT userID FROM users
WHERE username = :usernameInput;

SELECT subredditID FROM subreddits
WHERE subredditName = :subredditNameInput;

INSERT INTO posts (title, body, numUpvotes, postDate, subredditID, userID)
VALUES (:postTitleInput, :postBodyInput, :numUpvotesInput, :postDateInput, subredditID, userID);

--Add a new Subreddit
INSERT INTO subreddits (subredditName, about, numMembers, dateCreated)
VALUES (:subredditNameInput, :aboutInput, :numMembersInput, :dateCreatedInput);

--Add a relationship between Subreddits & Users (next 3 queries)
SELECT subredditID FROM subreddits
WHERE subredditName = :subredditNameInput;

SELECT userID FROM users
WHERE username = :usernameInput;

INSERT INTO subreddits_users (subredditID, userID)
VALUES (subredditID, userID);

--Filter comments by Username, 'i_love_dachshunds93' as the username will give results
SELECT c.commentID, u.username, p.title, c.body, s.subredditName, c.numUpvotes FROM comments c
LEFT JOIN posts p
ON c.postID = p.postID
LEFT JOIN users u
ON c.userID = u.userID
LEFT JOIN subreddits s
ON p.subredditID = s.subredditID
WHERE u.username = %s
ORDER BY commentID ASC;

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



