-- Lists all records of the table second_table
-- Doesn't list rows without a name value
-- Results display score and name (in this order)
-- Records are listed by descending score
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
