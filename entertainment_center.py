import fresh_tomatoes
import media

# 1st movie's details
tag = media.Movie("Tag", "Storyline",
                  "http://www.impawards.com/2018/posters/tag_ver2.jpg",
                  "https://www.youtube.com/watch?v=kjC1zmZo30U")

# 2nd movie's details
tomb_raider = media.Movie("Tomb Raider", "Storyline",
                          "https://image.ibb.co/fA7cGU/tomb_raider.jpg",
                          "https://www.youtube.com/watch?v=rOEHpkZCc1Y")

# 3rd movie's details
wonder = media.Movie("Wonder", "Storyline",
                     "http://www.impawards.com/2017/posters/wonder_ver12.jpg",
                     "https://www.youtube.com/watch?v=ZDPEKXx_lAI")

# 4th movie's details
black_panther = media.Movie("Black Panther", "Storyline",
                            "http://www.impawards.com/2018/posters/black_panther_ver2.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")

# 5th movie's details
rampage = media.Movie("Rampage", "Storyline",
                      "http://www.impawards.com/2018/posters/rampage_ver2.jpg",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI")

# 6th movie's details
mollys_game = media.Movie("Molly’s Game", "Storyline",
                          "http://www.impawards.com/2017/posters/mollys_game.jpg",
                          "https://www.youtube.com/watch?v=Vu4UPet8Nyc")

movies = [tag, tomb_raider, wonder, black_panther, rampage, mollys_game]
fresh_tomatoes.open_movies_page(movies)
