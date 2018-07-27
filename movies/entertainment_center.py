import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

batman_vs_superman = media.Movie("Batman vs Superman",
                     "Batman and Superman face off",
                     "https://en.wikipedia.org/wiki/Batman_v_Superman:_Dawn_of_Justice#/media/File:Batman_v_Superman_poster.jpg",
                     "https://www.youtube.com/watch?v=IwfUnkBfdZ4")

#batman_vs_superman.show_trailer()

hercules = media.Movie("Hercules",
                       "The Rock is a hero fighting bad guys",
                       "https://en.wikipedia.org/wiki/File:Hercules_(2014_film).jpg",
                       "https://www.youtube.com/watch?v=OwlynHlZEc4")

#hercules.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "A guy loses his job and now substitutes as a teacher in a school",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille",
                          "Rat loves cooking and wants to become a chef",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A guy goes back in time at midnight, has a nice time and feels nostalgic",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

Holy_Ghost_Reborn = media.Movie("Holy Ghost Reborn Movie",
                                 "Dareen Wilson does a beautiful documentary on Wonder",
                                 "https://en.wikipedia.org/wiki/File:Holy_Ghost_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=gjVuet2tgF4")


movies = [toy_story, batman_vs_superman, hercules, school_of_rock, ratatouille, midnight_in_paris, Holy_Ghost_Reborn]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
