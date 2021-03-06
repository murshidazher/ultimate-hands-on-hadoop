-- Find all the movies with an average less than 2.0
-- Sort them by the total number of ratings

ratings = LOAD '/user/maria_dev/ml-100k/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);

metadata = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);

-- Create relation from another table using FOREACH/GENERATE
nameLookup = FOREACH metadata GENERATE movieID, movieTitle;

ratingsByMovie = GROUP ratings By movieID;

avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating, COUNT(ratings.rating) AS numRatings;

oneStarMovies = FILTER avgRatings BY avgRating < 2.0;

oneStarsWithData = JOIN oneStarMovies BY movieID, nameLookup BY movieID;

finalResults = FOREACH oneStarsWithData GENERATE nameLookup::movieTitle AS movieName, oneStarMovies::avgRating AS avgRating, oneStarMovies::numRatings AS numRatings;

finalResultsSorted = ORDER finalResults BY numRatings DESC;

DUMP finalResultsSorted;
