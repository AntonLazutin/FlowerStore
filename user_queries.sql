-- DROP TABLE IF EXISTS User;

-- CREATE TABLE IF NOT EXISTS User (
--     id INTEGER PRIMARY KEY UNIQUE,
--     username TEXT NOT NULL UNIQUE,
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL,
--     hashed_pass TEXT NOT NULL UNIQUE,
--     is_staff INTEGER NOT NULL CHECK (is_staff in (0,1))
-- );

-- INSERT INTO User (username, first_name, last_name, hashed_pass, is_staff)
-- VALUES("palemale", "Anton", "Lazutin", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", 1);

-- /*password - password*/

-- INSERT INTO User (username, first_name, last_name, hashed_pass, is_staff)
-- VALUES("a_abobus", "Aboba", "Abobus", "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5", 0);

-- /*password - qwerty*/

SELECT * FROM User
WHERE username="palemale";