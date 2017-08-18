import media
# import media module where the Movie class has been defined
import fresh_tomatoes
# import fresh_tomatoes module


# Initialise instances of the class Movie
toy_story = media.Movie(
    "Toy Story",
    "Story about a boy and his toys that come to life",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A Marine on an alien planet",
    "http://s3.foxfilm.com/intlportal2/dev-temp/fr-FR/____55940f2091eb6.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


dunkerque = media.Movie(
    "Dunkerque",
    "The evacuation of Dunkerque during the WWII",
    "http://fr.web.img2.acsta.net/c_215_290/pictures/17/06/15/14/31/266314.jpg",
    "https://www.youtube.com/watch?v=XNupATI9P0Q")


lamour_dure_3_ans = media.Movie(
    "L'amour dure 3 ans",
    "Love story between a married girl and divorced guy",
    "http://2.bp.blogspot.com/-TA3HhBjAPkI/UxAIsoMRHuI/AAAAAAABP-s/JL3MmW-8JcM/s1600/L'amour+dure+trois+ans+Cover.jpg",
    "https://www.youtube.com/watch?v=ly2GowrVpUI")

rock_n_roll = media.Movie(
    "Rock & Roll",
    "The story of a frustrated old guy",
    "http://fr.web.img6.acsta.net/pictures/16/12/08/13/39/179029.jpg",
    "https://www.youtube.com/watch?v=LyF-RnkOBoc")

vas_vis_et_deviens = media.Movie(
    "Vas vis et deviens",
    "The story of an adopted child who finds his mother back",
    "http://fr.web.img6.acsta.net/medias/nmedia/18/35/56/16/18409991.jpg",
    "https://www.youtube.com/watch?v=c1T2FX3qKmQ")

movies = [toy_story, avatar, dunkerque, lamour_dure_3_ans, rock_n_roll, vas_vis_et_deviens]
# Create a list with all the movies
fresh_tomatoes.open_movies_page(movies)
# Use the method open_movies_page from the module fresh_tomatoes to open a web page displaying the list of movies 



