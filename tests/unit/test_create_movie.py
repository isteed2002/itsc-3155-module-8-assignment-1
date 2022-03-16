# TODO: Feature 2
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    
    movie_repository_singleton.create_movie('Forrest Gump', 'Robert Zemeckis', 4)
    movie = Movie('Forrest Gump', 'Robert Zemeckis', 4)

    assert type(movie) == Movie
    assert movie.title == 'Forrest Gump'
    assert movie.director == 'Robert Zemeckis'
    assert movie.rating == 4