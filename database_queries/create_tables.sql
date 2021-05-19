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

CREATE TABLE users
(
  userID INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  karma INT NOT NULL,
  cakeDay DATE NOT NULL,
  PRIMARY KEY (userID),
  UNIQUE (username, userID)
);

CREATE TABLE subreddits_users
(
  subredditUserID INT NOT NULL AUTO_INCREMENT,
  subredditID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (subredditUserID),
  FOREIGN KEY (subredditID) REFERENCES subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES users(userID),
  UNIQUE(subredditUserID)
);

CREATE TABLE posts
(
  postID INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  body VARCHAR(255) NOT NULL,
  numUpvotes INT NOT NULL,
  postDate DATETIME NOT NULL,
  subredditID INT,
  userID INT,
  PRIMARY KEY (postID),
  FOREIGN KEY (subredditID) REFERENCES subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES users(userID),
  UNIQUE(postID)
);

CREATE TABLE comments
(
  commentID INT NOT NULL AUTO_INCREMENT,
  body VARCHAR(255) NOT NULL,
  numUpvotes INT NOT NULL,
  commentDate DATETIME NOT NULL,
  postID INT,
  userID INT,
  PRIMARY KEY (commentID),
  FOREIGN KEY (postID) REFERENCES posts(postID),
  FOREIGN KEY (userID) REFERENCES users(userID),
  UNIQUE(commentID)
);

