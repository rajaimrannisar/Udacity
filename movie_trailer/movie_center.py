import fresh_tomatoes
import media

# 1st object of class init with Waar movie attributes
waarmov = media.Movie("WAAR","Maj. Mujtaba is brought out of retirement to"
                      " help the army prevent a devastating terrorist attack",
                      "http://www.gstatic.com/tv/thumb/movieposters/10476741/p10476741_p_v8_aa.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=yMwk622BUbg") 

# 2nd Object of class init with Saya Khuda Zul Jilal movie attributes
skzjmov = media.Movie("Saya E Khuda E Zul Jilal","Story of Pakistani heroes"
                      " of the nation during the war of 1965, what Pakistan"
                      " was supposed to be and what it is today. It also takes"
                      " the audience through a period of history that has been"
                      " forgotten.",
                      "https://upload.wikimedia.org/wikipedia/en/f/fd/Saya_e_Khuda_e_Zuljalal.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=eZl-NzW7vLc")

# 3rd object of class init with Manto movie attributes
mntomov = media.Movie("Manto","A story of a 20th-century writer Manto, who"
                       " grew-up in the showbiz industry of Bombay (now Mumbai)"
                       " and Lahore.",
                       "http://www.fashioncentral.pk/images/celeb-gossip/icons/manto_film_picture.jpg",  # NoQA
                       "https://www.youtube.com/watch?v=Tnfx42fxCZU")

# 4th object of class init with Khamosh Pani: Silent Water movie attributes
khpamov = media.Movie("Khamosh Pani","Khamosh is a 2003 Pakistani film about a"
                      " widowedmother, and her young son set in a late 1970s village in"
                      " Punjab, Pakistan which is coming under radical influence.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Sw_cover_2.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=wh21pKaK5KM")
# 5th object of class init with Gangs of Wasseypur movie attributes
gowpmov = media.Movie("Gangs of Wasseypur","This is an Indian two-part crime film"
                      " Centered on the coal mafia of Dhanbad, and the underlying"
                      " power struggles,politics and vengeance between crime families.",
                      "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=j-AkWDkXcMY")
# 6th object of class init with Bhindi bazaar movie attributes
bhbzmov = media.Movie("Bnindi Bazar Inc.","This is an Indian crime film"
                      " Centered on power struggles ensue in a gang after"
                      " the sudden of their leader.The film is set in the"
                      " underbelly of Mumbai, between the infamous by-lanes"
                      " where crime is prevalent as a way of life.",
                      "https://upload.wikimedia.org/wikipedia/en/f/fe/Bhindi-bazaar-inc.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=evlo66dgKo4")

# Create an array to store all the object in it
movies = [waarmov,skzjmov,mntomov,khpamov,gowpmov,bhbzmov]

# Pass the array to open_movies_page function in th fresh tomotoes class 
fresh_tomatoes.open_movies_page(movies)

