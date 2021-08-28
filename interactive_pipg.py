from Victim import Victim
from const_values import EMPTY


def launch_interactive_pipg() -> None:
    victim = Victim()  # create the victim

    # ask the user for the various details of the victim, and save his answers
    print("Enter every detail you want. If you haven't got something, just press enter")
    inp = input("First Name: ")
    victim.first_name = EMPTY if inp.strip() == "" else inp.strip().lower()

    inp = input("Last Name: ")
    victim.last_name = EMPTY if inp.strip() == "" else inp.strip().lower()

    inp = input("More Names, separated by commas: ")
    victim.more_names = EMPTY if inp.strip() == "" else inp.strip().lower().split(",")

    inp = input("Email: ")
    victim.email = EMPTY if inp.strip() == "" else inp.strip().lower().split("@")[0]

    inp = input("Birth Date (DD/MM/YY): ")
    victim.birth_date = EMPTY if inp.strip() == "" else inp

    inp = input("Pets: ")
    victim.pets = EMPTY if inp.strip() == "" else inp.strip().lower().split(",")

    reverse = input("Reverse the values? [Y/N] ")

    inp = input("Output to filename (left empty to ignore): ")
    filename = inp.lower()

    # create the passwords
    passwords = victim.generate_passwords(True if reverse.lower()[0] == "y" else False)

    # output to file if necessary
    if filename != "":
        result_file = open(filename, "w")
        result_file.write(passwords)
        result_file.close()

    print(passwords)  # print the generated passwords
