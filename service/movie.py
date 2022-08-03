class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_by_director(self, director):
        return self.movie_dao.get_by_director(director)

    def get_by_genre(self, genre):
        return self.movie_dao.get_by_genre(genre)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def post_create(self, data):
        return self.movie_dao.post_create(data)

    def put_update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.id = data.get("id")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.movie_dao.update(movie)

    def patch_update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get("title")
        if 'description' in data:
            movie.description = data.get("description")
        if 'trailer' in data:
            movie.trailer = data.get("trailer")
        if 'year' in data:
            movie.year = data.get("year")
        if 'rating' in data:
            movie.rating = data.get("rating")
        if 'genre_id' in data:
            movie.genre_id = data.get("genre_id")
        if 'director_id' in data:
            movie.director_id = data.get("director_id")

        self.movie_dao.update(movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid)
