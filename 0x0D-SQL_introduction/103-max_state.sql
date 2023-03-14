-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- Write a script that displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
