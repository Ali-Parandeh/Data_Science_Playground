INSERT INTO professors (firstname, lastname, university_shortname)
VALUES (NULL, 'Miller', 'ETH');


-- null value in column "firstname" violates not-null constraint
-- DETAIL:  Failing row contains (null, Miller, ETH).