-- SQL script to create the 'users' table with unique email constraint
-- - id: Integer, primary key, auto-incremented, not null
-- - email: String (255 characters), unique, not null
-- - name: String (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
