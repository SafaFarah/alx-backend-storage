-- SQL script to create the 'users' table with the following attributes:
-- - id: Integer, primary key, auto-incremented, not null
-- - email: String (255 characters), unique, not null
-- - name: String (255 characters)
-- - country: Enum ('US', 'CO', 'TN'), not null, default is 'US'

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
