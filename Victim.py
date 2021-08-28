from typing import List
from itertools import combinations
from const_values import EMPTY, MAX_PASSWORD_LENGTH


# add object to str followed by end, only if it is not empty
def add_if_not_empty(string: str, to_add: object, end: str, empty_end: str, to_join=" ") -> str:
    if to_add is not EMPTY:  # check if the object to add is not empty
        if type(to_add) is list:  # check if the object is a list
            string += to_join.join(to_add) + end  # join the list with the to_join token and add to string
        else:  # in case of str
            string += to_add.__str__() + end  # add the str with the ending token
    else:
        string += empty_end  # if the object is empty, add the empty_end to the string

    return string  # return the string


# add to_add to vals_list if it isn't empty. If add_Reverse is True, also add the values in reverse (ab -> ba)
def append_if_not_empty(vals_list: list, to_add: object, add_reverse: bool):
    if to_add is not EMPTY:  # ensure the current param is filled
        if type(to_add) is list:  # add all items in the more_names and pets lists
            for item in to_add:
                vals_list.append(item)  # add the current attribute
                if add_reverse:
                    vals_list.append(item[::-1])  # add the current attribute, reversed
        else:
            vals_list.append(to_add)  # add the current attribute
            vals_list.append(to_add.title())  # add the current attribute, titled
            if add_reverse:
                vals_list.append(to_add[::-1])  # add the current attribute, reversed
                vals_list.append(to_add[::-1].title())  # add the current attribute, reversed and titled


class Victim:  # the profile on which to base the generated passwords
    def __init__(self):
        # many characteristics of the victim
        self.first_name = EMPTY
        self.last_name = EMPTY
        self.more_names = EMPTY
        self.email = EMPTY
        self.birth_date = EMPTY
        self.pets = EMPTY

    def generate_keywords(self, reverse: bool) -> List[str]:
        keywords = []

        # add all the filled params to the keywords list
        append_if_not_empty(keywords, self.first_name, reverse)
        append_if_not_empty(keywords, self.last_name, reverse)
        append_if_not_empty(keywords, self.more_names, reverse)
        append_if_not_empty(keywords, self.email, reverse)
        append_if_not_empty(keywords, self.pets, reverse)

        # add the birthday attributes, split
        if self.birth_date is not EMPTY:
            split_date = self.birth_date.split("/")
            keywords.append(split_date[0])
            keywords.append(split_date[1])
            keywords.append(split_date[2])

        return keywords

    def generate_passwords(self, reverse: bool) -> str:
        keywords = self.generate_keywords(reverse)  # base keywords with which to generate the passwords
        two_items = [''.join(pair) for pair in combinations(keywords, 2)]  # create combinations of 2
        three_items = [''.join(trio) for trio in combinations(keywords, 3)]  # create combinations of 3

        passwords = []  # the result list of passwords
        passwords.extend([pair for pair in two_items if len(pair) < 20])  # add passwords shorter than MAX_PASSWORD_LENGTH
        passwords.extend([trio for trio in three_items if len(trio) < 20])  # add passwords shorter than MAX_PASSWORD_LENGTH
        passwords = "\n".join(passwords)  # turn the passwords list to a string, every password in a separated line
        return passwords  # return the generated passwords

    def __str__(self) -> str:
        # initialize the string
        string = ""

        # add all the attributes of the victim
        string = add_if_not_empty(string, self.first_name, " ", "")
        string = add_if_not_empty(string, self.more_names, " ", "", " ")
        string = add_if_not_empty(string, self.last_name, "\n", "\n")
        string = add_if_not_empty(string, self.email, "\n", "")
        string = add_if_not_empty(string, self.birth_date, "\n", "")
        string = add_if_not_empty(string, self.pets, "", "", ", ")

        return string.strip()
