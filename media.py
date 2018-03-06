class Movie():
    '''
    This class is used to get informations about my favourite movies
    It gets information like title, poster, story line and trailer URL
    and initialises the variables.
    '''
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

