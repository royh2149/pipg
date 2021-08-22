def add_if_not_none(string: str, to_add: object, end: str, none_end: str, to_join=" ") -> str:
	if to_add is not None:
		if type(to_add) is list:
			string += to_join.join(to_add) + end
		else:
			string += to_add.__str__() + end
	else:
		string += none_end

	return string

class Victim:  # the profile on which to base the generated passwords
	def __init__(self):
		# many characteristics of the victim
		self.first_name = None
		self.last_name = None
		self.more_names = None
		self.email = None
		self.birth_date = None
		self.pets = None

		# holds all the class variables
		self.attrs = [self.first_name, self.last_name, self.more_names, self.email, self.birth_date, self.pets]

	def generate_passwords(self) -> str:
		keywords = []  # base keywords with which to generate the passwords

		# add all the filled params to the keywords
		for param in self.attrs:
			if param is not None:  # ensure the current param is filled
				if type(param) is list:  # add all items in the more_names list
					for val in param:
						keywords.append(param)  # add the current attribute
						keywords.append(param[::-1])  # add the current attribute, reversed
				else:
					keywords.append(param)  # add the current attribute
					keywords.append(param[::-1])  # add the current attribute, reversed

	def __str__(self) -> str:
		# initialize the string
		string = ""

		# add all the attributes of the victim
		string = add_if_not_none(string, self.first_name, " ", "")
		string = add_if_not_none(string, self.more_names, " ", "", " ")
		string = add_if_not_none(string, self.last_name, "\n", "\n")
		string = add_if_not_none(string, self.email, "\n", "")
		string = add_if_not_none(string, self.birth_date, "\n", "")
		string = add_if_not_none(string, self.pets, "", "", ", ")

		return string.strip()

