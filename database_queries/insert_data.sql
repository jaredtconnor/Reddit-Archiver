INSERT INTO Subreddits (subredditName, about, numMembers, dateCreated) VALUES
('OSUOnlineCS', 'Subreddit about OSU Online CS program!', 5000, '2016-10-21'),
('Random_Subreddit', 'Subreddit for posts about random things', 10000, '2010-03-08'),
('pizza', 'subreddit to discuss pizza!', 400000, '2013-06-10'),
('Kanye', 'Subreddit to discuss Kanye West', 300000, '2011-09-05');


INSERT INTO Users (username, karma, cakeDay) VALUES
('osu_cs_user', 672, '2020-05-04'),
('random_user', 196, '2020-05-05'),
('i_love_dachshunds93', 524, '2020-05-05'),
('peter_90', 245, '2020-05-06');


INSERT INTO Subreddits_Users (subredditID, userID) VALUES
(1, 1),
(1, 2),
(2, 1),
(1, 3);


INSERT INTO Posts (title, body, numUpvotes, postDate, subredditID, userID) VALUES
('CS 325 Midterm Format', 'Post Body', 9, '2021-05-04 23:54:32', 1, 1),
('Golden Retriver goes Mountain Biking', 'Post Body', 1000, '2021-05-04 23:55:45', 2, 1),
('Margherita Pizza', 'I love pizza', 55, '2021-05-12 12:08:34', 3, 3),
('blah blah', 'random post!', 1, '2021-05-12 18:33:09', 2, 4);


INSERT INTO Comments (body, numUpvotes, commentDate, postID, userID) VALUES
('difficult!', 2, '2021-05-04 23:58:32', 1, 2),
('Comment', 4, '2021-05-04 23:56:09', 2, 3),
('I love pizza', 2, '2021-05-12 12:09:34', 3, 4),
('blah', 1, '2021-05-12 18:36:09', 3, 3);
