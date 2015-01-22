
-- Run with:
-- psql -f filename.sql

-- examples...
INSERT INTO tasktype (tasktype_id, name) VALUES (1, 'ISIP 500');

INSERT INTO participant (admin_date) 
    VALUES (to_date('2014-09-01', 'YYYY-MM-DD'));

/*
SELECT * from participant;

 participant_id | admin_date
----------------+------------
              1 | 2014-09-01

SELECT * from tasktype;

 tasktype_id |   name
-------------+----------
           1 | ISIP 500
*/

-- participant ID and task ID must already be present in those tables

INSERT INTO stamp (sequence, stamp_type, instrument, 
                   micros, participant_id, tasktype_id) 
    VALUES (1, 'tap', 'right', 
            908752389, 1, 1);

/*
SELECT * FROM stamp;
 stamp_id | sequence | stamp_type | instrument |  micros   | participant_id | tasktype_id
----------+----------+------------+------------+-----------+----------------+-------------
        2 |        1 | input      | right      | 908752389 |              1 |           1
(1 row)
*/


