class Alphabetizer_Filter:

	def __init__(self):
		self.lines = []


	#Add circular shifted lines: Done
	def Add_Lines(self, lines):

		self.lines.extend(lines)


	#Sort all of the circular shifted lines and return them
	def Get_Ordered_Lines(self):

		ordered_lines = []

		return ordered_lines