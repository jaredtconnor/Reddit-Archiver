-- : character represents user input

--Show subreddits
SELECT s.subredditID, s.subredditName, s.about, s.numMembers, s.dateCreated FROM subreddits s
ORDER BY s.subredditID ASC;

--Add a new Subreddit
INSERT INTO subreddits (subredditName, about, numMembers, dateCreated)
VALUES (:subredditNameInput, :aboutInput, :numMembersInput, :dateCreatedInput);

--Edit (Update) a Subreddit
UPDATE subreddits
SET numMembers = :newNumMembers,
about = :newAbout,
dateCreated = :newDateCreated
WHERE subreddits.subredditID = :subredditID;

--Delete a Subreddit (next 2 queries)
DELETE FROM subreddits_users
WHERE subreddits_users.subredditID = :subredditID;

DELETE FROM subreddits
WHERE subreddits.subredditID = :subredditID;

--Show users
SELECT * FROM users
ORDER BY userID ASC;

--Add a new User
INSERT INTO users (username, karma, cakeDay)
VALUES (:usernameInput, :karmaInput, :cakeDayInput);

--Edit (Update) a User
UPDATE users
SET username = :newUsername,
cakeDay = :newCakeDay,
karma = :newKarma,
WHERE users.userID = :userID;

--Delete a User (next 2 queries)
DELETE FROM subreddits_users
WHERE subreddits_users.userID = :userID;

DELETE FROM users
WHERE users.userID = :userID;

--Show relationship between Subreddits & users
SELECT su.subredditUserID, su.subredditID, s.subredditName, su.userID, u.username FROM subreddits_users su
LEFT JOIN subreddits s ON su.subredditID = s.subredditID
LEFT JOIN users u ON su.userID = u.userID
ORDER BY su.subredditUserID ASC;

--Add a relationship between Subreddits & Users (next 3 queries)
SELECT subredditID FROM subreddits
WHERE subredditName = :subredditNameInput;

SELECT userID FROM users
WHERE username = :usernameInput;

INSERT INTO subreddits_users (subredditID, userID)
VALUES (subredditID, userID);

--Removes the relationship between a Subreddit and a User
DELETE FROM subreddits_users
WHERE subreddits_users.subredditUserID = :subredditUserID;

--Show Post
SELECT p.postID, p.title, p.body, p.numUpvotes, p.postDate, s.subredditName, u.username FROM posts p
LEFT JOIN subreddits s
ON p.subredditID = s.subredditID
LEFT JOIN users u
ON p.userID = u.userID
ORDER BY postID ASC;

--Add a new Post (next 3 queries)
SELECT userID FROM users
WHERE username = :usernameInput;

SELECT subredditID FROM subreddits
WHERE subredditName = :subredditNameInput;

--If subreddit name or username are left blank, subredditID or userID will be NULL
INSERT INTO posts (title, body, numUpvotes, postDate, subredditID, userID)
VALUES (:postTitleInput, :postBodyInput, :numUpvotesInput, :postDateInput, subredditID, userID);

--Edit (Update) a Post (next 3 queries), if subreddit name or username are left blank, subredditID or userID will be NULL
SELECT userID FROM users
WHERE username = :username;

SELECT subredditID FROM subreddits
WHERE subredditName = :subredditName;

UPDATE posts
SET title = :newTitle,
    body = :newBody,
    numUpvotes = :newNumUpvotes,
    subredditID = subredditID,
    userID = userID
WHERE posts.postID = :postID;

--Delete a Post
DELETE FROM posts
WHERE posts.postID = :postID;

--Show comments
SELECT c.commentID, u.username, p.title, c.body, s.subredditName, c.numUpvotes FROM comments c
LEFT JOIN posts p
ON c.postID = p.postID
LEFT JOIN users u
ON c.userID = u.userID
LEFT JOIN subreddits s
ON p.subredditID = s.subredditID
ORDER BY commentID ASC;

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

--Add a new Comment (next 3 queries)
SELECT postID FROM posts
WHERE title = :postTitleInput;

SELECT userID FROM users
WHERE username = :usernameInput;

--If post title or username are left blank, postID or userID will be NULL
INSERT INTO comments (body, numUpvotes, commentDate, postID, userID)
VALUES (:bodyInput, :numUpvotesInput, :commentDateInput, postID, userID);

--Edit (Update) a Comment (next 3 queries), if post title or username are left blank, subredditID or postID will be NULL
SELECT userID FROM users
WHERE username = :username;

SELECT postID FROM posts
WHERE title = :title;

UPDATE comments
SET body = :newBody,
    numUpvotes = :newNumUpvotes,
    postID = postID,
    userID  = userID
WHERE comments.commentID = :commentID;

--Delete a Comment
DELETE FROM comments
WHERE comments.commentID = :commentID;
