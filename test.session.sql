--@block
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each record
    url TEXT NOT NULL,                         -- Full URL
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(255) NOT NULL             -- Password (real or anonymized)
);


--@block

SELECT * from users;

--@block
ALTER TABLE users
ADD COLUMN protocol VARCHAR(5) AFTER url;
