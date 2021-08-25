class Quest:
    	
	#Initialises a quest.
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
    		
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.req = req
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.complete = False

	#Returns the quest's description.
	def get_info(self):
		return self.desc

	#Returns whether or not the quest is complete.
	def is_complete(self):
		return self.complete	

	#Returns a command that the user can input to attempt the quest.
	def get_action(self):
		return self.action

	#Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed.
	def get_room_desc(self):
		return self.room.get_short_desc()

	# Allows the player to attempt this quest
	#Check the cumulative skill or will power of the player and all their items. 
	#If this value is larger than the required skill or will threshold for this quest's completion, 
	#they succeed and are rewarded with an item (the room's description will also change because of this)
	#Otherwise, nothing happens
	def attempt(self, player):

		req_split = self.req.split(" ")
		req_type = req_split[0] 
		req_value = int(req_split[1]) #value of req
		if self.complete == True:
			print("You have already completed this quest.")
			
		#check the type of req 'skill or will'	
		elif req_type == 'SKILL':
			if player.get_skill() >= req_value:
				self.complete = True
				player.take(self.reward)
				print(self.pass_msg)
			else:
				print(self.fail_msg)
		elif req_type == 'WILL':
			if player.get_will() >= req_value:
				self.complete = True
				player.take(self.reward)
				print(self.pass_msg)
			else:
				print(self.fail_msg)	
			
			
			
