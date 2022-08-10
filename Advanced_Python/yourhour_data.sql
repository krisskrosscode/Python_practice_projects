-- TODO : Import data into mysql server from csv file

-- CREATE TABLE yourhour(
--     s_no INT,
--     date DATE,
--     app_name VARCHAR(100),
--     usage_seconds INT,
--     launch_count INT,
--     is_monitoring VARCHAR(10),
--     is_sys_app VARCHAR(10),
--     package_name VARCHAR(100)
--     );

-- LOAD DATA LOCAL INFILE "yourhour_data.csv"
-- INTO TABLE yourhour
-- FIELDS TERMINATED BY ','
-- IGNORE 1 ROWS;

-- SELECT date, app_name, SUM(usage_seconds/60) usage_mins, SUM(usage_seconds/60)/60 usage_hrs, SUM(usage_seconds/60)/29 avg_per_day
-- FROM yourhour 
-- GROUP BY app_name
-- ORDER BY usage_mins DESC
-- LIMIT 10;

-- SELECT SUM(usage_seconds/60) as sum_mins, SUM(usage_seconds/60)/29 avg_mins_per_day
-- FROM yourhour
-- ;


SELECT date, SUM(usage_seconds)/60 usage_mins, (SUM(usage_seconds)/60)/60 usage_hrs
FROM yourhour
GROUP BY date
ORDER BY date ;

-- SELECT date, app_name, SUM(usage_seconds/60) usage_mins, SUM(usage_seconds/60)/60 usage_hrs, SUM(usage_seconds/60)/29 avg_mins_per_day
-- FROM yourhour 
-- GROUP BY app_name
-- ORDER BY usage_mins DESC
-- LIMIT 10;

-- SELECT DAY(date), app_name, SUM(usage_seconds/60) usage_mins
-- FROM yourhour
-- WHERE app_name = "fancode" OR app_name = "cricbuzz"
-- GROUP BY date, app_name
-- ORDER BY date, app_name;