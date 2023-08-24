#!/usr/bin/env -S python3 -u

import random, os, time

gNames = [ "Boba Fett",
           "Darth Vader",
           "Princess Leia",
           "Luke Skywalker",
           "Palpatine",
           "Yoda" ]

gPics = {}

gPicWidth = 50
gPicHeight = 25

def centerString(s, l):
	begin = (l - len(s)) // 2
	retData = (" " * begin) + s + (" " * l)
	return retData[0:l]

def loadPictures():
	picData = open("pictures.ans","r").read().split("\n")
	curLine = 0

	for person in gNames:
		gPics[person] = picData[curLine: curLine + gPicHeight]
		curLine += gPicHeight

def printVersus(char1, char2):
	for i in range(0,gPicHeight):
		if (i == (gPicHeight // 2)):
			print("{}  -VS-  {}".format(gPics[char1][i], gPics[char2][i]))
		else:
			print("{}        {}".format(gPics[char1][i], gPics[char2][i]))
	
	print("")
	print("{}        {}".format(centerString(char1, gPicWidth), centerString(char2, gPicWidth)))

def win():
	os.system("cat flag.txt")
	time.sleep(10)

def battle(char1, char2):
	char1Life = 100
	char2Life = 100

	while( (char1Life > 0) and (char2Life > 0) ):
		dmg1 = random.randint(1,50)
		dmg2 = random.randint(1,50)

		char1Life -= dmg1
		char2Life -= dmg2

		print("{} attacks {} for {}, leaving him with only {} life left".format(char1, char2, dmg1, char1Life))
		print("{} attacks {} for {}, leaving him with only {} life left".format(char2, char1, dmg2, char2Life))

	if (char1Life > 0):
		print("  {} wins!\n".format(char1))
		retVal = 1
	elif (char2Life > 0):
		print("  {} wins!\n".format(char2)) 
		retVal = 2
	else:
		print("  Everyone dies!\n")
		retVal = 0 

	time.sleep(.25)
	return retVal

def main():
	random.seed(int(time.time()))
	loadPictures()

	winStreak = 0

	while(winStreak < 7):

		char1 = random.choice(gNames)
		shortList = gNames[:]
		shortList.remove(char1)
		char2 = random.choice(shortList)

		printVersus(char1, char2)

		selection = input("Who Wins?  1 = {}, 2 = {}, 0 = Everyone dies, q = quit\n".format(char1, char2))

		if (selection == "q"):
			break;

		winner = battle(char1, char2)

		if (winner == int(selection)):
			winStreak += 1
			print("Current win streak: {}".format(winStreak))
		else:
			winStreak = 0

	if (winStreak >= 7):
		win()

	print("Goodbye")

if (__name__ == "__main__"):
	main()
