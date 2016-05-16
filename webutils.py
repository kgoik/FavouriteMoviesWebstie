import json
import movie
import constants as c

"""
movie_decoder creates Movie object from json

Arguments:
 - response - json response from api
"""


def movie_decoder(response):
    # loads json to python dict
    movie_json = json.loads(response)

    # check for movie title in json
    if 'original_title' in movie_json:
        title = movie_json['original_title']

    # check for movie poster url in json
    if 'poster_path' in movie_json:
        poster_url = movie_json['poster_path']

    # check for movie youtube key in json
    if 'videos' in movie_json:
        videos = movie_json['videos']
        videos_list = videos['results']
        if len(videos_list) > 0:
            youtube_id = videos_list[0]['key']

    # if all argumnents exists return Movie object
    if title and poster_url and youtube_id:
        return movie.Movie(title,
                           c.POSTER_URL + poster_url,
                           c.YOUTUBE_WATCH_URL + youtube_id)

    return False
