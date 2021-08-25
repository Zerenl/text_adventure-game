class Adventurer:
	def __init__(self):
		self.inventory = []
		self.skill = 5 
		self.will = 5
	def get_inv(self):
		
		return inventory

	#Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make.
	def get_skill(self):
		sum_skill = self.skill
		if len(self.inventory) !=0:
			i = 0
			while i <len(self.inventory):
				sum_skill += int(self.inventory[i].skill_bonus)
				if sum_skill < 0:
					sum_skill = 0
				i += 1
		return sum_skill 

	#Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make.
	def get_will(self):
		sum_will = self.will
		if len(self.inventory) !=0:
			i = 0
			while i <len(self.inventory):
				sum_will += int(self.inventory[i].will_bonus)
				if sum_will < 0:
					sum_will = 0
				i += 1
		return sum_will

	# Adds an item to the adventurer's inventory.
	def take(self, item):
		self.inventory.append(item)
			
	#Shows adventurer stats and all item stats.
	def check_self(self):
		print("\nYou are an adventurer, with a SKILL of 5 and a WILL of 5.")
		print("You are carrying:\n")
		if len(self.inventory) == 0:
			print("Nothing.\n")
		else:
			i = 0
			while i<len(self.inventory):
				print(self.inventory[i].name)
				print("Grants a bonus of {} to SKILL.".format(self.inventory[i].skill_bonus))
				print("Grants a bonus of {} to WILL.\n".format(self.inventory[i].will_bonus))
				i += 1
			
		print("With your items, you have a SKILL level of {} and a WILL power of {}.".format(self.get_skill(), self.get_will()))	
