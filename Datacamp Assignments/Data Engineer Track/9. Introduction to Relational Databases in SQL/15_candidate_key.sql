-- Using the above steps, identify the candidate key by trying out different combination of columns.
-- Try out different combinations
SELECT COUNT(DISTINCT(firstname, lastname)) 
FROM professors;