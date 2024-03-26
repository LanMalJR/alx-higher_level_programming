USE hbtn_0c_0;

-- Create the table "first_table"
CREATE TABLE first_table (
  id INT(11) DEFAULT NULL,
  name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Check current character set and collation
SHOW CREATE DATABASE hbtn_0c_0;
SHOW CREATE TABLE first_table;
DESCRIBE first_table;

-- Convert database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert table character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert column character set and collation
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;