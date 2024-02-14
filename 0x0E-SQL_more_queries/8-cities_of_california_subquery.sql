-- lists all the cities of cali that can be found in the DB
USE hbtn_0d_usa;
SELECT * FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = 'California')
ORDER BY  `id` ASC;
