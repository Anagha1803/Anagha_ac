SELECT AVG(rating)
FROM ratings JOIN movies ON movies.id = ratings.movies_id
WHERE year = 2012;

-- joining the tables ratings and movies on the movie_id

