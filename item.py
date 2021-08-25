class Item:
	
	#Initialises an item.
	def __init__(self, name, short, skill_bonus, will_bonus):
		self.name = name
		self.short = short
		self.skill_bonus = skill_bonus
		self.will_bonus = will_bonus

	#Returns an item's name.
	def get_name(self):
		return self.name

	#Returns an item's short name.
	def get_short(self):
		return self.short

	#Prints information about the item.
	def get_info(self):
		print(self.name)
		print("Grants a bonus of {} to SKILL.".format(self.skill_bonus))
		print("Grants a bonus of {} to WILL.".format(self.will_bonus))

	#Returns the item's skill bonus.
	def get_skill(self):
		return self.skill_bonus

	#Returns the item's will bonus.
	def get_will(self):
		return self.will_bonus
