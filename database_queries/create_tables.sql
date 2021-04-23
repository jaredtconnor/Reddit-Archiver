/* Creates the table's based upon the defined reddit_archiver schema */ 

CREATE TABLE Subreddits
(
  subredditName INT NOT NULL,
  description INT NOT NULL,
  numMembers INT NOT NULL,
  dateCreated INT NOT NULL,
  subredditID INT NOT NULL,
  PRIMARY KEY (subredditID),
  UNIQUE (subredditName)
);

CREATE TABLE Users
(
  username INT NOT NULL,
  karma INT NOT NULL,
  cakeDay INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (userID),
  UNIQUE (username)
);

CREATE TABLE Posts
(
  postID INT NOT NULL,
  title INT NOT NULL,
  body INT NOT NULL,
  numUpvotes INT NOT NULL,
  postDate INT NOT NULL,
  subredditID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (postID),
  FOREIGN KEY (subredditID) REFERENCES Subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES Users(userID)
);

CREATE TABLE Relationship
(
  subredditUserID INT NOT NULL,
  subredditID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (subredditUserID),
  FOREIGN KEY (subredditID) REFERENCES Subreddits(subredditID),
  FOREIGN KEY (userID) REFERENCES Users(userID),
  UNIQUE (subredditID, userID)
);

CREATE TABLE Comments
(
  commentID INT NOT NULL,
  body INT NOT NULL,
  numUpvotes INT NOT NULL,
  commentDate INT NOT NULL,
  postID INT NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (commentID),
  FOREIGN KEY (postID) REFERENCES Posts(postID),
  FOREIGN KEY (userID) REFERENCES Users(userID)
);

