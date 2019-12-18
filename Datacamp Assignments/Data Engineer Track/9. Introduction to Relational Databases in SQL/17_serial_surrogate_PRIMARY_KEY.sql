-- Add a SERIAL surrogate key

-- Since there's no single column candidate key in professors 
-- (only a composite key candidate consisting of firstname, 
-- lastname), you'll add a new column id to that table.

-- This column has a special data type serial, which turns the 
-- column into an auto-incrementing number. This means that, 
-- whenever you add a new professor to the table, it will 
-- automatically get an id that does not exist yet in 
-- the table: a perfect primary key!


-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

-- Have a look at the first 10 rows of professors
SELECT * FROM professors LIMIT 10;