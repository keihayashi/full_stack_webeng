import fresh_tomatoes
import media

# information of six movies I selected
shawshank = media.Movie("The Shawshank Redemption", "a story of baker who is sentenced to life in Shawshank State Penitentiary for the murder ", "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco") #NOQA

gatsby = media.Movie("The Great Gatsby", "1925 novel written by American author F. Scott Fitzgerald", "https://upload.wikimedia.org/wikipedia/en/f/f7/TheGreatGatsby_1925jacket.jpeg", "https://www.youtube.com/watch?v=F4_xuHfDWf4") #NOQA

roman_holiday = media.Movie("Roman Holiday", "a holiday of royal princess", "https://upload.wikimedia.org/wikipedia/en/b/b7/Roman_holiday.jpg", "https://www.youtube.com/watch?v=FQ43RROS8TM") #NOQA

lovers = media.Movie("Lovers", "a blind dancer and two police officers", "https://upload.wikimedia.org/wikipedia/en/f/f7/House_of_Flying_Daggers_poster.JPG", "https://www.youtube.com/watch?v=p-nmfwQdkeM") #NOQA

cinderella = media.Movie("Cinderella", "romantic fantasy of Disney", "https://upload.wikimedia.org/wikipedia/en/c/c2/Cinderella_2015_official_poster.jpg", "https://www.youtube.com/watch?v=SxECU8Se_b4") #NOQA

star_wars = media.Movie("Star Wars", "American epic space opera", "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg", "https://www.youtube.com/watch?v=frdj1zb9sMY") #NOQA

# make a list of movies and create a web-page
movies = [gatsby, roman_holiday, lovers, cinderella, star_wars, shawshank]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
