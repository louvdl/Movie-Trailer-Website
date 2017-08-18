import webbrowser


class Movie():
    # Create the class Movie
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Create spaces in the memory for a new instance
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Method that shows the movie trailer
        webbrowser.open(self.trailer_youtube_url)



