# importing the website generating file
import fresh_tomatoes
import media

'''
    making objects/instances of class Movie having
    Name, Story Line, Poster URL, Youtube Trailer URL
'''
star_wars = media.Movie("Star Wars",
                        '''The Imperial Forces under orders from cruel Darth
                        (David Prowse) hold Princess Leia(Carrie Fisher)
                        hostage, in their efforts to quell the rebellion
                        against the Galactic Empire.''',  # noqa
                        '''https://encrypted-tbn0.gstatic.com/images?q=tbn:
                        ANd9GcT2-hXRZtI5-YQEZd2v4mtcP7hr2rMnOShjyqhEQJ0Vcbdued
                        ObpQ''',  # noqa
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY"
                        )

x_men = media.Movie("X-Men",
                    '''They are children of the atom, homo superior,
                    the next link in the chain of evolution.''',
                    "https://wallscover.com/images/dark-reign-7.jpg",
                    "https://youtu.be/nbNcULQFojc"
                    )

spider_man = media.Movie("Spider Man",
                        "With great power comes great responsibility.",
                        '''https://encrypted-tbn0.gstatic.com/
                        images?q=tbn:ANd9GcS9OE8XwojRerPJWuwT
                        _spJtuPYO2WGO2xPyrp_Qe311byOgSndOw''',  # noqa
                        "https://youtu.be/xrzXIaTt99U"
                        )

thor = media.Movie("Thor",
                    '''As the son of Odin (Anthony Hopkins),
                    king of the Norse gods, Thor (Chris Hemsworth) will soon
                    inherit the throne of Asgard from his aging father.''',
                    '''https://wallpaperscraft.com/image/thor_the_dark_world_chris_
                    hemsworth_thor_natalie_portman_jane_foster_93962_300x533.jpg''',  # noqa
                    "https://www.youtube.com/watch?v=JOddp-nlNvQ"
                    )

avengers = media.Movie("The Avengers",
                        '''When Thor's evil brother, Loki (Tom Hiddleston),
                        gains access to the unlimited power of the energy
                        cube called the Tesseract''',  # noqa
                        '''https://encrypted-tbn0.gstatic.com/image
                        s?q=tbn:ANd9GcSVeJp7N-eRjO8yAI89Z2eaflvyt2u
                        cEZeztcBykQCYzFxIr89Y5Q''',  # noqa
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8"
                        )

angry_birds = media.Movie("Angry Birds",
                            '''Flightless birds lead a mostly happy existence,
                            except for Red(Jason Sudeikis), who just can't get
                            past the daily annoyances of life''',  # noqa
                            '''https://encrypted-tbn0.gstatic.com/images?q=tbn: 
                            ANd9GcRpU3UhrOI_swZ9Hxbw2JV6vAo5Ho1YWrEX1QVwcsbmaiwL8aE0''',  # noqa
                            "https://www.youtube.com/watch?v=1U2DKKqxHgE"
                        )

# making a list of objects
movie = [thor, x_men, spider_man, star_wars, avengers, angry_birds]

'''
    passing the list of movies to the open_movies_page() func
    of fresh_tomatoes module
'''
fresh_tomatoes.open_movies_page(movie)

