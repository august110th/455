SELECT name FROM album
	WHERE year = 2018;

SELECT name FROM song
	WHERE duration_sec = (SELECT MAX(duration_sec) FROM song);

SELECT name FROM song
	WHERE duration_sec >= 210

SELECT name FROM album
	WHERE year BETWEEN 2018 AND 2020;

SELECT name FROM author
	WHERE name NOT LIKE '% %';

SELECT name FROM song
	WHERE name LIKE '%my%';