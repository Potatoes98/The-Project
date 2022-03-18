# lovely jubbly imports
from threading import Thread
import time
import sys
import os
import random
import math
from modules import *
from replit import audio
import readkeys

print("WARNING\nThis repl contains sound. If you would not like to use it, please mute your computer or the tab.\n\nPress any key to continue.")
readkeys.getkey()
clear()
print("If you recive a pop up regarding audio and/or hear a tone, please press any key to continue. Else, please reload and/or use 'kill 1' in the shell.")
test = audio.play_tone(3, 700, 1, volume=0.25)
readkeys.getkey()
test.toggle_playing()

mainText = ["Play", "Login | WIP", "Create Account | WIP", "About | WIP"]
extraText = ["The Project | V0.0.1 | IN DEV", "Created by Archit and Sunny", ""]
while True:
  selection = createMenu(mainText, 0, 63, extraText, 63)

  if selection == "Play":
    clear()
    thunder = Sound("thunder.mp3", name="thunder")
    thunder.play()
    typing("Entering game...", 2)
    break
  elif selection == "Login":
    pass
  elif selection == "Create Account":
    pass
  elif selection == "About":
    pass

clear()


# Game starts here
typing("Boom!\nThunder strikes once more as you walk back home.")
thunder.stop()