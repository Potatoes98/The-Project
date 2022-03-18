from replit import audio
import random

class Sound:
  def __init__(self, path, volume=1, loops=False, name=False):
    self.path = path
    self.volume = volume
    self.loops = loops
    self.isPlaying = False
    if name:
      self.name = name
    else:
      self.name = str(random.randint(1000000, 9999999))
  
  def play(self):
    if not self.isPlaying:
      self.source = audio.play_file(self.path, self.volume)
      self.isPlaying = True

  def stop(self):
    if self.isPlaying:
      self.source.toggle_playing()
      self.isPlaying = False

  def restart(self):
    if not self.isPlaying:
      self.source.toggle_playing()
      self.isPlaying = True