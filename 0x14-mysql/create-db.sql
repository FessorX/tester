-- Create db on the master server
CREATE DATABASE IF NOT EXISTS D_corp;

-- Create table
CREATE TABLE IF NOT EXISTS D_corp.tabl
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
);

-- Insert an entry
INSERT INTO `D_corp.tabl` (`name`) VALUES ("Musa");
