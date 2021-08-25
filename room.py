class Room:
	#Initialises a room. Do not change the function signature (line 2)
	def __init__(self, name):
		self.name = name
		self.quest = None
		self.north = None
		self.south = None
		self.east = None
		self.west = None

	#Returns the room's name.
	def get_name(self):
		return self.name

	#Returns a string containing a short description of the room.
	#This description changes based on whether or not a relevant quest has been completed in this room.
	#If there are no quests that are relevant to this room,
	#this should return: 'There is nothing in this room.
	def get_short_desc(self):

		if self.quest == None:
			return "There is nothing in this room."
		elif self.quest.is_complete() == True:
			return self.quest.after
		else:
			return self.quest.before
	
	#If a quest can be completed in this room, returns a command that the user can input to attempt the quest
	def get_quest_action(self):
		if self.quest == None:
			return
		else:
			return self.quest.get_action()
		
	#Sets a new quest for this room
	def set_quest(self, q):
		self.quest = q

	#Returns a Quest object that can be completed in this room.
	def get_quest(self):
		if self.quest.is_complete() == False:
			return self.quest
	
	#Creates an path leading from this room to another
	def set_path(self, dir, dest):
		if dir == "NORTH":
			self.north = dest
			return self.north
		elif dir == "SOUTH":
			self.south = dest
			return self.south
		elif dir == "EAST":
			self.east = dest
			return self.east
		elif dir == "WEST":
			self.west = dest
			return self.west
	
	#Creates a drawing depicting the exits in each room.
	def draw(self):
		height = 11
		width = 22
		print("")
		line = ""
		# Print top +----+
		if height > 0:
			line += "+"
			i = 0
			while i < width-2:
				if i == 9 and self.north != None:
					line += "NN"
					i += 2
				else:
					line += "-"
					i += 1
			line += "+"
		# Print middle |    |
		i = 0
		while i < height-2:
			if i == 4 and self.west != None:
					line += "\nW"
			else:		
				line += "\n|"
			index = 0
			while index < width-2:
				line += " "
				index += 1
			if i == 4 and self.east != None:
					line += "E"
			else:
				line += "|"
			i += 1
		# Print bottom +----+
		if height > 1:
			i = 0
			line += "\n+"
			while i < width-2:
				if i == 9 and self.south != None:
					line += "SS"
					i += 2
				else:
					line += "-"
					i += 1
			line += "+"
		print(line)
		print("You are standing at the {}.".format(self.name))
		print(Room.get_short_desc(self))
	
	#Returns an adjoining Room object based on a direction given.
	#(i.e. if dir == "NORTH", returns a Room object in the north)
	def move(self, dir):
		if dir == "NORTH" or dir == "N":
			if self.north == None:
				print("You can't go that way.")
				return self
			else:
				print("You move to the north, arriving at the {}.".format(self.north.name))
				self.north.draw()
				return self.north
		elif dir == "SOUTH" or dir == "S":
			if self.south == None:
				print("You can't go that way.")
				return self
			else:
				print("You move to the south, arriving at the {}.".format(self.south.name))
				self.south.draw()
				return self.south
		elif dir == "WEST" or dir == "W":
			if self.west == None:
				print("You can't go that way.")
				return self
			else:
				print("You move to the west, arriving at the {}.".format(self.west.name))
				self.west.draw()
				return self.west
		elif dir == "EAST" or dir == "E":
			if self.east == None:
				print("You can't go that way.")
				return self
			else:
				print("You move to the east, arriving at the {}.".format(self.east.name))
				self.east.draw()
				return self.east
