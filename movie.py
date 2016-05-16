class Movie():
    """
    Stores basic data about the movie

    Arguments:
     - title - movie title
     - poster_image_url - url that leads to movies poster
     - trailer_youtube_urlk - url that leads to movies trailer on youtube_link
    """

    def __init__(self, title, poster_url, youtube_link):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link
