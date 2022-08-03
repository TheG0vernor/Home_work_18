from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director):
        return self.session.query(Movie).filter(Movie.director == director).all()

    def get_by_genre(self, genre):
        return self.session.query(Movie).filter(Movie.genre == genre).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def post_create(self, movie):
        created_movie = Movie(**movie)

        self.session.add(created_movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        del_movie = self.get_one(mid)

        self.session.delete(del_movie)
        self.session.commit()
