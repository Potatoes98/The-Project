# lovely imports
import sys, termios, tty

class reader():
	def __init__(self):
		self.ascii = {
			"\x1b[A": "UP_ARROW",
			"\x1b[B": "DOWN_ARROW",
			"\x1b[C": "RIGHT_ARROW",
			"\x1b[D": "LEFT_ARROW"
		}
	def getch(self, toprint = False, printer="", amt=1):
		"""
		Gets a key press, or series of key presses
		Adapted from https://code.activestate.com/recipes/134892/

		Currently supports lowercase letters, capital letters
		(Shift + a letter), other CHARACTERS on keyboard,
		and arrow keys
		"""
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		chrs = []
		try:
			tty.setraw(sys.stdin.fileno())
			for _ in range(amt):
				ch = sys.stdin.read(1)
				if ch == "\x1b":
					ch2 = sys.stdin.read(1)
					if ch2 == "[":
						ch3 = sys.stdin.read(1)
						if (ch + ch2 + ch3) in self.ascii.keys():
							chrs.append(self.ascii[(ch + ch2 + ch3)])
							continue
				else:
					if toprint:
						print(ch, end="")
						sys.stdout.flush()
					chrs.append(ch)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return chrs

	"""def get_arrow(self):
		arrow_key = self.getch("", 3)
		try:
			return self.arrow_key_ascii[arrow_key]
		except:
			return None"""
  
	def read_input(self, mask=""):
		read_input = ""
		char = self.getch()
		while char != "\r":
			if char == "\x7f":
				read_input = read_input[:-1]
			else:
				read_input += char
			char = self.getch()
		return read_input
      
	def read_pwd(self, confirm=False, text=""):
		if confirm:
			print("Confirm Password: ", end="")
		elif text:
			print(text, end="")
		else:
			print("Password: ", end="")
			sys.stdout.flush()
    
		char = " "
		printer = "•"
		read_input = ""

		char = self.getch(printer)
		while char != "\r":
			if char == "\x7f":
				read_input = read_input[:-1]
			else:
				read_input += char
			char = self.getch(printer)
			return read_input