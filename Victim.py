from typing import List


class Victim:  # the profile on which to base the generated passwords
	def __init__(self):
		# many characteristics of the victim
		self.first_name = None
		self.last_name = None
		self.more_names = None
		self.email = None
		self.birth_date = None
		self.pet = None

		# holds all the class variables
		self.attrs = [self.first_name, self.last_name, self.more_names, self.email, self.birth_date, self.pet]

	def generate_passwords(self) -> str:
		keywords = []  # base keywords with which to generate the passwords

		# add all the filled params to the keywords
		for param in self.attrs:
			if param is not None:  # ensure the current param is filled
				if type(param) is List:  # add all items in the more_names list
					for val in param:
						keywords.append(param)  # add the current attribute
						keywords.append(param[::-1])  # add the current attribute, reversed
				else:
					keywords.append(param)  # add the current attribute
					keywords.append(param[::-1])  # add the current attribute, reversed

