-- : character represents user input

--Show Users
SELECT * FROM Users;

--Show Comments
SELECT * FROM Comments;

--Show relationship between Subreddits & Users
SELECT * FROM Subreddits_Users;

--Add a new User
INSERT INTO Users (username, karma, cakeDay)
VALUES (:usernameInput, :karmaInput, :cakeDayInput);

--Add a new Comment
INSERT INTO Comments (body, numUpvotes, commentDate, postID, userID)
VALUES (:bodyInput, :numUpvotesInput, :commentDateInput, :postIDInput, :userIDInput);

--Add a relationship between Subreddits & Users
INSERT INTO Subreddits_Users (subredditID, userID)
VALUES (:subredditIDInput, :userIDInput);

--Filter Comments by Username, 'i_love_dachshunds93' as the username will give results
SELECT Comments.body, Users.username FROM Comments
INNER JOIN Users ON Comments.userID=Users.userID
WHERE Users.username = :username;

--Edit (Update) a Comment
UPDATE Comments SET body = :newComment
WHERE Comments.commentID = :commentID;

--Delete a Comment
DELETE FROM Comments
WHERE Comments.commentID = :commentID;

--Delete a User
DELETE FROM Users
WHERE Users.userID = :userID;

--Removes the relationship between a Subreddit and a User
DELETE FROM Subreddits_Users
WHERE Subreddits_Users.subredditUserID = :subredditUserID;