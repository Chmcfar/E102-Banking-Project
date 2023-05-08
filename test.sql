-- Meant for note keeping not meant to be used as a script


-- Create Tables

-- Create a table w/ name, age, uniqueID 
CREATE TABLE Person (
    name VARCHAR(50), -- name 50char limit
    age smallint UNSIGNED, -- smallint Signed range is from -32768 to 32767, Unsigned range is from 0 to 65535.
    personID int PRIMARY KEY AUTO_INCREMENT -- PRIMARY KEY constraint uniquely identifies each record in a table, Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table
)
-- Create a 
-- Output Table
DESCRIBE Person
-- Insert Record (Row)
INSERT INTO Person (name, age) VALUES ("Jerry", 30) --SQL Version
INSERT INTO Person (name, age) VALUES (%s, %s), ("Jerry", 30) --Connecter Version (Inserts tuple values into string)
-- Show all Records
SELECT * FROM Person
