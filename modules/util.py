# lovely jubbly imports
import time
import sys
import random
from os import system, name
from .reader import reader
import string
from .sound import Sound
import readkeys

# gets lowercase and uppercase letters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def typing(string: str, sleeptime: float = 0, wpm: float = 60):
	for l in string:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(random.uniform(0, 0.7) * 10.0 / wpm)
	if sleeptime != 0:
		time.sleep(sleeptime)


def clear():
	system("clear")

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

  # creates an interactive menu
def createMenu(text, carrotlocation, centerid=0, extraText=[], extraCenter=0):
	r = reader()
	selected = 0
	notSelected = True # changed this code from original
	while notSelected: # changed this code from original
		system("clear")
		for sentence in extraText:
			print(sentence.center(centerid))
    
		for sentence in text:
			if (text.index(sentence) == carrotlocation):
				if (centerid == 0):
					print((sentence + " <").center(centerid))
				else:
					print(("> " + sentence).center(centerid-2))
			else:
				print(sentence.center(centerid))
		
		menuInput = readkeys.getkey()[0]
		if menuInput.lower() == "w" and selected > 0:
			selected -= 1
		elif menuInput.lower() == "s" and selected < len(text) - 1:
			selected += 1
		elif menuInput.lower() == "\r":
			notSelected = False # changed this code from original
			return text[selected] # ok so notSelected is useless but I don't like while True loops so yes
		
		carrotlocation = selected