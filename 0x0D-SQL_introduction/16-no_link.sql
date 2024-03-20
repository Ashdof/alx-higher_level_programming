-- Lists all records of second table
-- Skips records without a name value
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
