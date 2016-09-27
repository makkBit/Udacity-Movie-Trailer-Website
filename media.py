# this module defines the class 'Movie',
# to create objects in entertainment_center.py module
class Movie():
	"""documentation of the class, accessed by ClassName.__doc__
	This class defines the blueprint of the movies"""
	# constructor to create space in memory 
	# for the instance of the class
	def __init__(self,movie_title,poster_image,
				trailer_youtube,id_youtube):
		# instance variables
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.trailer_youtube_id = id_youtube
