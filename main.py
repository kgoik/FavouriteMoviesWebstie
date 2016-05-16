import fresh_tomatoes
import urllib
import constants
import webutils

"""
Run this script to start the program.

Add your favourite movies to the fav_movies list using tmdb.org movies id's
"""

fav_movies = ["278", "118340", "24", "2179"]
movies = []

for m in fav_movies:
    # creates new url for api request
    url = (constants.API_URL +
           m +
           constants.API_KEY_PARAM +
           constants.API_KEY +
           constants.API_VIEDO)

    # sends movie description request to api
    response = urllib.urlopen(url)
    # decode response and creates Movie Object
    movie = webutils.movie_decoder(response.read())
    if movie:
        movies.append(movie)

# creates webpage
fresh_tomatoes.open_movies_page(movies)
