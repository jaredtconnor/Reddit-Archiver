INSERT INTO subreddits (subredditName, about, numMembers, dateCreated) VALUES
('OSUOnlineCS', 'Subreddit about OSU Online CS program!', 5000, '2016-10-21'),
('Random_Subreddit', 'Subreddit for posts about random things', 10000, '2010-03-08'),
('pizza', 'subreddit to discuss pizza!', 400000, '2013-06-10'),
('Kanye', 'Subreddit to discuss Kanye West', 300000, '2011-09-05'), 
('investing', 'Come lose money with your friends', 1800000, '2008-03-15'),
('AnimalsBeingDerps', 'Animals acting like complete idiots', 5100, '2013-05-15'),
('desksetup', 'Post work stations, and desks!', 21900, '2015-06-05'), 
('pics', 'A place for pictures and photographs.', 27000000, '2008-01-15'),
('todayilearned', 'Everything you have learned today!', 25800000, '2008-12-18'), 
('worldnews', 'A place for major news from around the world', 26300000, '2008-01-28'), 
('Unexpected', 'This subreddit is for unexpected twists in videos and gifs', 3800000, '2013-04-27');

INSERT INTO users (username, karma, cakeDay) VALUES
('osu_cs_user', 672, '2020-05-04'),
('random_user', 196, '2020-05-05'),
('i_love_dachshunds93', 524, '2020-05-05'),
('peter_90', 245, '2020-05-06');


INSERT INTO subreddits_users (subredditID, userID) VALUES
(1, 1),
(1, 2),
(2, 1),
(1, 3);


INSERT INTO posts (title, body, numUpvotes, postDate, subredditID, userID) VALUES
('CS 325 Midterm Format', 'Post Body', 9, '2021-05-04', 1, 1),
('Golden Retriver goes Mountain Biking', 'Post Body', 1000, '2021-05-04', 2, 1),
('Margherita Pizza', 'I love pizza', 55, '2021-05-12', 3, 3),
('blah blah', 'random post!', 1, '2021-05-12', 2, 4);


INSERT INTO comments (body, numUpvotes, commentDate, postID, userID) VALUES
('difficult!', 2, '2021-05-04', 1, 2),
('Comment', 4, '2021-05-04', 2, 3),
('I love pizza', 2, '2021-05-12', 3, 4),
('blah', 1, '2021-05-12', 3, 3);
