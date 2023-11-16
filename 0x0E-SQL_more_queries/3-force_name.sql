-- Creates the table force_name.
-- force_name description: id INT, name VARCHAR(256) can’t be null
-- The database name will be passed as an argument of command
-- If the table force_name already exists, the script should not fail
CREATE TABLE IF NOT EXISTS `force_name` (
    `id`   INT,
    `name` VARCHAR(256) NOT NULL
);

