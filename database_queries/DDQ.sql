-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 20, 2021 at 07:09 AM
-- Server version: 10.4.18-MariaDB-log
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_goinsli`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `commentID` int(11) NOT NULL,
  `body` varchar(255) NOT NULL,
  `numUpvotes` int(11) NOT NULL,
  `commentDate` date NOT NULL,
  `postID` int(11) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`commentID`, `body`, `numUpvotes`, `commentDate`, `postID`, `userID`) VALUES
(1, 'difficult!', 2, '2021-05-04 23:58:32', 1, 2),
(2, 'Comment', 4, '2021-05-04 23:56:09', 2, 3),
(3, 'I love pizza', 2, '2021-05-12 12:09:34', 3, 4),
(4, 'blah', 1, '2021-05-12 18:36:09', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `postID` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `body` varchar(255) NOT NULL,
  `numUpvotes` int(11) NOT NULL,
  `postDate` date NOT NULL,
  `subredditID` int(11) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`postID`, `title`, `body`, `numUpvotes`, `postDate`, `subredditID`, `userID`) VALUES
(1, 'CS 325 Midterm Format', 'Post Body', 9, '2021-05-04 23:54:32', 1, 1),
(2, 'Golden Retriver goes Mountain Biking', 'Post Body', 1000, '2021-05-04 23:55:45', 2, 1),
(3, 'Margherita Pizza', 'I love pizza', 55, '2021-05-12 12:08:34', 3, 3),
(4, 'blah blah', 'random post!', 1, '2021-05-12 18:33:09', 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `subreddits`
--

DROP TABLE IF EXISTS `subreddits`;
CREATE TABLE `subreddits` (
  `subredditID` int(11) NOT NULL,
  `subredditName` varchar(255) NOT NULL,
  `about` varchar(255) NOT NULL,
  `numMembers` int(11) NOT NULL,
  `dateCreated` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subreddits`
--

INSERT INTO `subreddits` (`subredditID`, `subredditName`, `about`, `numMembers`, `dateCreated`) VALUES
(1, 'OSUOnlineCS', 'Subreddit about OSU Online CS program!', 5000, '2016-10-21'),
(2, 'Random_Subreddit', 'Subreddit for posts about random things', 10000, '2010-03-08'),
(3, 'pizza', 'subreddit to discuss pizza!', 400000, '2013-06-10'),
(4, 'Kanye', 'Subreddit to discuss Kanye West', 300000, '2011-09-05'),
(5, 'investing', 'Come lose money with your friends', 1800000, '2008-03-15'),
(6, 'AnimalsBeingDerps', 'Animals acting like complete idiots', 5100, '2013-05-15'),
(7, 'desksetup', 'Post work stations, and desks!', 21900, '2015-06-05'),
(8, 'pics', 'A place for pictures and photographs.', 27000000, '2008-01-15'),
(9, 'todayilearned', 'Everything you have learned today!', 25800000, '2008-12-18'),
(10, 'worldnews', 'A place for major news from around the world', 26300000, '2008-01-28'),
(11, 'Unexpected', 'This subreddit is for unexpected twists in videos and gifs', 3800000, '2013-04-27');

-- --------------------------------------------------------

--
-- Table structure for table `subreddits_users`
--

DROP TABLE IF EXISTS `subreddits_users`;
CREATE TABLE `subreddits_users` (
  `subredditUserID` int(11) NOT NULL,
  `subredditID` int(11) NOT NULL,
  `userID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subreddits_users`
--

INSERT INTO `subreddits_users` (`subredditUserID`, `subredditID`, `userID`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `karma` int(11) NOT NULL,
  `cakeDay` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `username`, `karma`, `cakeDay`) VALUES
(1, 'osu_cs_user', 672, '2020-05-04'),
(2, 'random_user', 196, '2020-05-05'),
(3, 'i_love_dachshunds93', 524, '2020-05-05'),
(4, 'peter_90', 245, '2020-05-06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentID`),
  ADD UNIQUE KEY `commentID` (`commentID`),
  ADD KEY `postID` (`postID`),
  ADD KEY `userID` (`userID`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`postID`),
  ADD UNIQUE KEY `postID` (`postID`),
  ADD KEY `subredditID` (`subredditID`),
  ADD KEY `userID` (`userID`);

--
-- Indexes for table `subreddits`
--
ALTER TABLE `subreddits`
  ADD PRIMARY KEY (`subredditID`),
  ADD UNIQUE KEY `subredditName` (`subredditName`,`subredditID`);

--
-- Indexes for table `subreddits_users`
--
ALTER TABLE `subreddits_users`
  ADD PRIMARY KEY (`subredditUserID`),
  ADD UNIQUE KEY `subredditUserID` (`subredditUserID`),
  ADD KEY `subredditID` (`subredditID`),
  ADD KEY `userID` (`userID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
  ADD UNIQUE KEY `username` (`username`,`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `postID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `subreddits`
--
ALTER TABLE `subreddits`
  MODIFY `subredditID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `subreddits_users`
--
ALTER TABLE `subreddits_users`
  MODIFY `subredditUserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`postID`) REFERENCES `posts` (`postID`),
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`subredditID`) REFERENCES `subreddits` (`subredditID`),
  ADD CONSTRAINT `posts_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);

--
-- Constraints for table `subreddits_users`
--
ALTER TABLE `subreddits_users`
  ADD CONSTRAINT `subreddits_users_ibfk_1` FOREIGN KEY (`subredditID`) REFERENCES `subreddits` (`subredditID`),
  ADD CONSTRAINT `subreddits_users_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
