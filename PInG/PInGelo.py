"""
Created 8-12-18
Help from https://github.com/HankMD/EloPy
Garrett Laz
"""
import math, operator

class Elo:
	"""
	class that represents implementation of Elo Ranking System
	"""

	def __init__(self, base_rating=1500):
		"""
		Runs at init of class object.
		@param base_rating - rating of a new player.
		"""
		self.base_rating = base_rating
		self.players = []

	def __getPlayerList(self):
		"""
		Returns the player list.
		@return - the list of all player objects
		"""
		return self.players

	def getPlayer(self, name):
		for player in self.players:
			if player.name == name:
				return player
		return None

	def contains(self, name):
		"""
		Returns true if this object contains a player with the given name.
		Otherwise returns false.
		@param name - name to check for.
		"""
		for player in self.players:
			if player.name == name:
				return True
		return False

	def addPlayer(self, name, rating=None):
		"""
		Adds a new player to the implementation.
		@param name - The name to identify a specific player.
		@param rating - The player's rating.
		"""
		if rating == None:
			rating = self.base_rating

		self.players.append(_Player(name=name,rating=rating))

	def removePlayer(self, name):
		"""
		Removes a new player to the implementation.
		@param name - The name to identify a specific player.
		"""
		self.__getPlayerList().remove(self.getPlayer(name))

	def recordMatch(self, name1, name2, winner, pd):
		"""
		Called after a match is played, NOTE: ties are not allowed in this model
		@param name1 - name of first player
		@param name2 - name of second player
		@param winner - name of winner, usually garrett
		@param pd - point differential in the game, must be positive
		"""
		player1 = self.getPlayer(name1)
		player2 = self.getPlayer(name2)

		expected1 = player1.compareRating(player2)
		expected2 = player2.compareRating(player1)
		
		#k = len(self.__getPlayerList()) * 20 
		#k = 20
		k = 45

		rating1 = player1.rating
		rating2 = player2.rating

		if winner == name1:
			score1 = 1.0
			score2 = 0.0
		elif winner == name2:
			score1 = 0.0
			score2 = 1.0
		else:
			raise InputError('One of the names must be the winner.')

		ratingdiff = rating1-rating2

		#marginOfVictoryMult1 = math.log(pd + 1) * (2.2/((ratingdiff)*.001+2.2)) # mov matters more
		marginOfVictoryMult2 = ((pd + 3) ** 0.8) / (7.5 + 0.0006 *ratingdiff) # mov matters less

		#print('marginOfVictoryMult1', marginOfVictoryMult1)

		print('marginOfVictoryMult2', marginOfVictoryMult2)

		newRating1 = rating1 + k * marginOfVictoryMult2 * (score1 - expected1)
		newRating2 = rating2 + k * marginOfVictoryMult2 * (score2 - expected2)

		if newRating1 < 0:
			newRating1 = 0
			newRating2 = rating1 - rating2
		elif newRating2 < 0:
			newRating2 = 0
			newRating1 = rating1 - rating2

		player1.rating = newRating1
		player2.rating = newRating2

	def getPlayerRating(self, name):
		"""
		Returns the rating of the player with the given name.
		@param name - name of the player.
		@return - the rating of the player with the given name.
		"""
		player = self.getPlayer(name)
		return player.rating

	def getRatingList(self):
		"""
		Returns list of all ratings
		@return list of all ratings.
		"""
		lst = []
		for player in self.__getPlayerList():
			lst.append((player.name,player.rating))
		return lst

	def getListInOrder(self):
		"""
		Returns list of all players and their ratings in order from worst to best.
		Uses operator import !!!
		@return list of all sorted ratings.
		"""
		lst = []
		sorted_lst = sorted(self.__getPlayerList(), key=operator.attrgetter('rating'))
		for player in sorted_lst:
			lst.append((player.name,player.rating))
		return lst

class _Player:
	"""
	Class that represents a player in elo rating system. for use by Elo
	"""

	def __init__(self, name, rating):
		"""
		Runs at initialization of class object.
		@param name - name of player
		@param rating - rating of player
		"""
		self.name = name
		self.rating = rating

	def compareRating(self, opponent):
		"""
		Compares the two rating of the this player and the opponent
		@param opponent - the player to compare against
		@returns - The expected score between the two players.
		"""

		# more reading can be found here: http://www.matterofstats.com/mafl-stats-journal/2013/10/13/building-your-own-team-rating-system.html
		return ( 10**( ( opponent.rating-self.rating )/400.0 ) + 1) ** -1







		