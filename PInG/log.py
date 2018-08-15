from PInGelo import *

e = Elo()

e.addPlayer("Garrett")
e.addPlayer("Mitch")
e.addPlayer("Ryan")
e.addPlayer("Greg")
e.addPlayer("Tarek")
e.addPlayer("Shane")


# Tuesday, August 12th
e.recordMatch("Ryan", "Tarek", "Ryan", 2)

e.recordMatch("Ryan", "Tarek", "Ryan", 5)

e.recordMatch("Ryan", "Mitch", "Ryan", 9)

e.recordMatch("Ryan", "Greg", "Ryan", 5)

e.recordMatch("Ryan", "Garrett", "Ryan", 8)

e.recordMatch("Ryan", "Greg", "Ryan", 5)

e.recordMatch("Garrett", "Mitch", "Garrett", 3)

e.recordMatch("Garrett", "Tarek", "Garrett", 2)

# Wednesday, August 13th
e.recordMatch("Ryan", "Greg", "Ryan", 2)

e.recordMatch("Ryan", "Mitch", "Ryan", 4)

e.recordMatch("Ryan", "Shane", "Shane", 3)

e.recordMatch("Tarek", "Shane", "Shane", 6)

e.recordMatch("Ryan", "Tarek", "Tarek", 3)

#[('Mitch', 1455.816459318874), ('Tarek', 1463.6404469478928), ('Greg', 1465.4543413625136), 
#('Garrett', 1506.341969567264), ('Shane', 1534.0773933833457), ('Ryan', 1574.6693894201103)]
#scores before model update


#print (e.getRatingList())

print (e.getListInOrder())