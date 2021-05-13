/* Creates the table's based upon the defined reddit_archiver schema */ 

CREATE TABLE subreddits
(
  subredditID INT NOT NULL AUTO_INCREMENT,
  subredditName VARCHAR(255) NOT NULL,
  about VARCHAR(255) NOT NULL,
  numMembers INT NOT NULL,
  dateCreated DATE NOT NULL,
  PRIMARY KEY (subredditID),
  UNIQUE (subredditName, subredditID)
);

INSERT INTO subreddits (subredditName, about, numMembers, dateCreated)
VALUES
	('investing', 'Come lose money with your friends', 1800000, '2008-03-15'),
	('AnimalsBeingDerps', 'Animals acting like complete idiots', 5100, '2013-05-15'),
	('desksetup', 'Post work stations, and desks!', 21900, '2015-06-05'), 
	('pics', 'A place for pictures and photographs.', 27000000, '2008-01-15'),
	('todayilearned', 'Everything you have learned today!', 25800000, '2008-12-18'), 
	('worldnews', 'A place for major news from around the world', 26300000, '2008-01-28'), 
	('Unexpected', 'This subreddit is for unexpected twists in videos and gifs', 3800000, '2013-04-27');
	








CREATE TABLE users
(
  userID INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  karma INT NOT NULL,
  cakeDay DATE NOT NULL,
  PRIMARY KEY (userID),
  UNIQUE (username, userID)
);

CREATE TABLE subreddits_Users
(
  subredditUserID INT NOT NULL AUTO_INCREMENT,
  subredditID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (subredditUserID),
  FOREIGN KEY (subredditID) REFERENCES Subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES Users(userID),
  UNIQUE(subredditUserID)
);

CREATE TABLE posts
(
  postID INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  body VARCHAR(255) NOT NULL,
  numUpvotes INT NOT NULL,
  postDate DATETIME NOT NULL,
  subredditID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (postID),
  FOREIGN KEY (subredditID) REFERENCES Subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES Users(userID),
  UNIQUE(postID)
);

CREATE TABLE comments
(
  commentID INT NOT NULL AUTO_INCREMENT,
  body VARCHAR(255) NOT NULL,
  numUpvotes INT NOT NULL,
  commentDate DATETIME NOT NULL,
  postID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (commentID),
  FOREIGN KEY (postID) REFERENCES Posts(postID),
  FOREIGN KEY (userID) REFERENCES Users(userID),
  UNIQUE(commentID)
);

