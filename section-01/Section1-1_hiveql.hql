-- SQL Script section 1.1

-- Finding the most highly rated movies on IMDB using HADOOP and HIVE
SELECT movie_id, count(movie_id) as ratingCount
FROM ratings
GROUP By movie_id
ORDER BY ratingCount
DESC;

-- Finding out the name of movie_id = 50 as most highly rated movie
SELECT name
FROM movie_names
where movie_id = 50;

