from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""

	file = open(source)
	paths = file.readlines()
	if paths == []:
		print("No rooms exist! Exiting program...")
		exit()
	all_paths = []	
	i = 0
	while i <len(paths):
		path_splite = []
		line = paths[i].strip()
		path = line.split(" > ") # splite three element
		path_splite.append(path[0]) #put element in a list
		path_splite.append(path[1]) 
		path_splite.append(path[2])
		all_paths.append(path_splite) #put the all path list in a list
		i += 1
	file.close()
	return all_paths
	

def create_rooms(paths):
	"""Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""

	rooms = []
	i = 0
	while i<len(paths):
		if len(rooms) == 0: 
			rooms.append(Room(paths[i][0]))
			rooms.append(Room(paths[i][2]))
		else:  # check room's name whether in the list of rooms
			x = 0
			while x < len(rooms):
				if rooms[x].name == paths[i][0]:
					break
				elif x == len(rooms)-1:
					rooms.append(Room(paths[i][0]))
				x += 1	
			y = 0
			while y < len(rooms):
				if rooms[y].name == paths[i][2]:
					break
				elif y == len(rooms)-1:
					rooms.append(Room(paths[i][2]))
				y += 1		
		i += 1
	# set path
	n = 0
	while n <len(rooms):
		x = 0
		while x < len(paths):
			if rooms[n].name == paths[x][0]:
				dir = paths[x][1]
				dest = paths[x][2]
				#match dest with room object
				i = 0
				while i < len(rooms):
					if dest == rooms[i].name:
						dest = rooms[i]
					i += 1	
				rooms[n].set_path(dir, dest)
			x += 1
		n += 1	
	return rooms


def generate_items(source):
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""
	file = open(source)
	item_s = file.readlines()
	items = []
	if item_s != []:	
		i = 0
		while i<len(item_s):
			line = item_s[i].strip()
			token = line.split(" | ")
			name = token[0]
			short = token[1]
			skill_bonus = token[2]
			will_bonus = token[3]
			items.append(Item(name, short, skill_bonus, will_bonus))
			i += 1		
	file.close()
	
	return items



def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""
	
	file = open(source)
	quest_s = file.readlines()
	quests =[]
	if quest_s != []:	
		i = 0
		while i<len(quest_s):
			line = quest_s[i].strip()
			if line:   # used for ignore the blank line
				token = line.split("|")
				reward = token[0].strip()
				action = token[1].strip()
				desc = token[2].strip()
				before = token[3].strip()
				after = token[4].strip()
				req = token[5].strip()
				fail_msg = token[6].strip()
				pass_msg = token[7].strip()
				room = token[8].strip()
				quests.append(Quest(reward, action, desc, before, after, req, fail_msg, pass_msg, room))
			i += 1
	file.close()
	#link between quests and items
	x = 0
	while x < len(quests):
		i = 0
		while i <len(items):
			if quests[x].reward == items[i].name:
				quests[x].reward = items[i]
			i += 1	
		x += 1
	#line between quests and rooms
	y = 0
	while y < len(quests):
		i = 0
		while i < len(rooms):
			if quests[y].room == rooms[i].name:
				quests[y].room = rooms[i]
				rooms[i].set_quest(quests[y]) # set quest in each room
			i += 1
		y += 1	
		
	return quests

#initialize and load config
if __name__ == "__main__":
	try:
		paths = read_paths(sys.argv[1])
		items = generate_items(sys.argv[2])
		rooms = create_rooms(paths)
		quests = generate_quests(sys.argv[3], items, rooms)
	except FileNotFoundError:
		print( "Please specify a valid configuration file.")
		exit()
	except IndexError:
		print("Usage: python3 simulation.py <paths> <items> <quests>")
		exit()
			
	user = Adventurer()
	current_room = rooms[0]
	current_room.draw() #draw the initial room when game started

	# Main loop of the game
	while True:
    	
		#read user command
		command = input('\n>>> ').upper()

		if command == "QUIT":
			print("Bye!")
			break
		elif command == "HELP":
			print("HELP       - Shows some available commands.")
			print("LOOK or L  - Lets you see the map/room again.")
			print("QUESTS     - Lists all your active and completed quests.")
			print("INV        - Lists all the items in your inventory.")
			print("CHECK      - Lets you see an item (or yourself) in more detail.")
			print("NORTH or N - Moves you to the north.")
			print("SOUTH or S - Moves you to the south.")
			print("EAST or E  - Moves you to the east.")
			print("WEST or W  - Moves you to the west.")
			print("QUIT       - Ends the adventure.")
			
			continue
		elif command == "LOOK" or command == "L":
			current_room.draw()
			continue
		elif command == "QUESTS":
			if len(quests) == 0: 
				print("\n=== All quests complete! Congratulations! ===")
				exit()
			else:
				i = 0
				while i <len(quests):
					space = (21-len(quests[i].reward.name))*" "
					if quests[i].complete == False:
						print("#{:02d}: {}{}- {}".format(i, quests[i].reward.name, space, quests[i].desc))
					else: #print a tag after if quest completed
						print("#{:02d}: {}{}- {} [COMPLETED]".format(i, quests[i].reward.name, space, quests[i].desc))
					i += 1
				# check whether all quest completed
				x = 0
				while x < len(quests):
					if quests[x].complete == False:
						break
					x += 1
					if x == len(quests):
						print("\n=== All quests complete! Congratulations! ===")	
						exit()	
			continue
			
		elif command == "INV":
			print("You are carrying:")
			if len(user.inventory) == 0:
				print("Nothing.")
			else:
				i = 0
				while i<len(user.inventory):
					print("- A {}".format(user.inventory[i].name))
					i += 1
			continue
			
		elif command == "CHECK":
			check = input("Check what? ").lower() 
			if check == "me":
				user.check_self()
			else: #check items in inventory
				if len(user.inventory) == 0:
					print("\nYou don't have that!")
				else:	
					i = 0
					while i < len(user.inventory):
						if check == user.inventory[i].name.lower() or check == user.inventory[i].short.lower():
							print("")
							user.inventory[i].get_info()
							print("")
							break
							
						# if item not in inventory print error message
						elif i == len(user.inventory)-1:
							print("You don't have that!")	
						i += 1		
			continue
		# move commands	
		elif command == "N" or command == "NORTH":
			current_room = current_room.move(command)
			continue
		elif command == "S" or command == "SOUTH":
			current_room = current_room.move(command)
			continue
		elif command == "E" or command == "EAST":
			current_room = current_room.move(command)
			continue
		elif command == "W" or command == "WEST":
			current_room = current_room.move(command)
			continue	
		# quest action command	
		elif command == current_room.get_quest_action():
			current_room.quest.attempt(user)
			continue
		# invalid command
		else:
			print("You can't do that.")
			continue
			
			
