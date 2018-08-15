from PInGelo import *

e = Elo()

e.addPlayer("Garrett")
e.addPlayer("Mitch")
e.addPlayer("Ryan")
e.addPlayer("Greg")
e.addPlayer("Tarek")

#print (e.getPlayerRating("Garrett"), e.getPlayerRating("Mitch"))

e.recordMatch("Garrett", "Mitch", "Garrett", 2)

e.recordMatch("Tarek", "Mitch", "Mitch", 3)

e.recordMatch("Ryan", "Greg", "Ryan", 5)

e.recordMatch("Greg", "Garrett", "Garrett", 7)

print('Mitch Rating', e.getPlayerRating("Mitch"))
print('Tarek Rating', e.getPlayerRating("Tarek"))

e.recordMatch("Mitch", "Tarek", "Tarek", 11) #2.46 times as important as regular win

print (e.getRatingList())