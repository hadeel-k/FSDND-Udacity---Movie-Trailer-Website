import fresh_tomatoes
import media

tag = media.Movie("Tag",
                        "Storyline",
                        "https://screensprite.com/wp-content/uploads/2018/04/tag.jpg",
                        "https://www.youtube.com/watch?v=kjC1zmZo30U")

tomb_raider = media.Movie("Tomb Raider",
                        "Storyline",
                        "http://cdn.collider.com/wp-content/uploads/2017/12/tomb-raider-poster-alicia-vikander.jpg",
                        "https://www.youtube.com/watch?v=rOEHpkZCc1Y")

wonder = media.Movie("Wonder",
                        "Storyline",
                        "https://1.bp.blogspot.com/-1-TL89QnvEg/WhLkU1-jmpI/AAAAAAAB4Ec/QrZ7YWUBGbQmUq6p0Yi5Q1pYphHO-MuwACLcBGAs/s1600/wonder-2017-movie-poster-12.jpg",
                        "https://www.youtube.com/watch?v=ZDPEKXx_lAI")

black_panther = media.Movie("Black Panther",
                        "Storyline",
                        "http://cdn.collider.com/wp-content/uploads/2017/11/black-panther-poster.jpg",
                        "https://www.youtube.com/watch?v=dxWvtMOGAhw")

rampage = media.Movie("Rampage",
                        "Storyline",
                        "http://www.joblo.com/posters/images/full/rampage_ver2_xxlg.jpg",
                        "https://www.youtube.com/watch?v=coOKvrsmQiI")

mollys_game = media.Movie("Molly’s Game",
                        "Storyline",
                        "http://cdn.collider.com/wp-content/uploads/2017/09/mollys-game-poster.jpg",
                        "https://www.youtube.com/watch?v=Vu4UPet8Nyc")

movies = [tag, tomb_raider, wonder, black_panther, rampage, mollys_game]
fresh_tomatoes.open_movies_page(movies)
