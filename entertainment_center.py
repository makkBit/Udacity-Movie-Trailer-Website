import media # file containing 'Movie' class
import fresh_tomatoes # file containing 'open_movies_page' function

# intances/objects of the Movie class
forest_gump = media.Movie("Forest Gump","https://s-media-cache-ak0.pinimg.com/originals/1b/c6/b7/1bc6b788ab41e7e5fa55f474b340cba4.jpg",
						"https://www.youtube.com/watch?v=uPIEn0M8su0","uPIEn0M8su0")
deadpool = media.Movie("Deadpool","http://www.impawards.com/2016/posters/deadpool.jpg",
						"https://www.youtube.com/watch?v=ZIM1HydF9UA","ZIM1HydF9UA")

liarliar = media.Movie("Liar Liar","http://www.impawards.com/1997/posters/liar_liar_ver1.jpg",
						"https://www.youtube.com/watch?v=k0DA75eOltA","k0DA75eOltA")

three_idiots = media.Movie("3 idiots","https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
							"https://www.youtube.com/watch?v=xvszmNXdM4w","xvszmNXdM4w")

barfi = media.Movie("Barfi","http://www.indicine.com/img/2012/07/barfi.jpg",
					"https://www.youtube.com/watch?v=yZxrao3zou4","yZxrao3zou4")

ace_ventura = media.Movie("Ace Ventura - When  nature calls","http://www.impawards.com/1995/posters/ace_ventura_when_nature_calls.jpg",
						  "https://www.youtube.com/watch?v=n1ZVImkf_TQ","n1ZVImkf_TQ")

# all Movie instances stored in a list
movies = [forest_gump,deadpool,ace_ventura,three_idiots,barfi,liarliar]

# movie instances list provided to open_movies_page function
# defined in fresh_tomatoes file
# in order to build the html file
fresh_tomatoes.open_movies_page(movies)