import sys
from const_values import *
from interactive_pipg import launch_interactive_pipg
from Victim import Victim

cur_arg_type = ARGUMENT
OUTPUT_TO_FILE = False
filename = ""
reverse = False

if len(sys.argv) < 2:  # ensure enough arguments were entered
    readme = open(README_FILE, "r")  # open the README file in read mode
    print(readme.read())  # print the contents of the file
    readme.close()  # close the file
    sys.exit(ARGS_ERROR)  # exit the program with an error code

victim = Victim()  # create the victim
arguments = sys.argv[1:]  # the command line arguments, without the program name

for index, val in enumerate(arguments):  # iterate through the arguments
    if val[0] == "-":  # check whether the current parameter is an argument
        if cur_arg_type != ARGUMENT:  # check if the current argument should be a value
            print("Missing value!")
            sys.exit(ARGS_ERROR)

        cur_arg_type = VALUE  # update the current argument type for the next iteration

        arg = val[1:]  # the remaining of the argument

        if arg == "i" or arg == "-interactive":
            launch_interactive_pipg()
            sys.exit(0)  # exit the program with a successful exit code

        # update the appropriate attribute of the victim
        if arg == "f" or arg == "-fname":
            victim.first_name = arguments[index+1].lower()
        elif arg == "l" or arg == "-lname":
            victim.last_name = arguments[index + 1].lower()
        elif arg == "m" or arg == "-moren":
            victim.more_names = arguments[index + 1].split(",")
            victim.more_names = [name.lower() for name in victim.more_names]
            victim.more_names.extend([name.title() for name in victim.more_names])
        elif arg == "e" or arg == "-email":
            victim.email = arguments[index + 1].split("@")[0]
        elif arg == "d" or arg == "-birthdate":
            victim.birth_date = arguments[index + 1]
        elif arg == "p" or arg == "-pets":
            victim.pets = arguments[index + 1].split(",")
            victim.pets = [pet.lower() for pet in victim.pets]
            victim.pets.extend([pet.title() for pet in victim.pets])
        elif arg == "r" or arg == "-reverse":
            reverse = True
            cur_arg_type = ARGUMENT  # leave current argument type as is, since -r has no value
        elif arg == "o" or arg == "-output":
            OUTPUT_TO_FILE = True  # mark that the passwords should be outputted to a file
            filename = arguments[index + 1]  # store the desired filename

    else:  # current parameter is a value
        if cur_arg_type != VALUE:  # check if the current argument should be an argument
            print("Missing argument!")
            sys.exit(ARGS_ERROR)

        cur_arg_type = ARGUMENT  # update the current argument type for the next iteration


passwords = victim.generate_passwords(reverse)  # generate the passwords

# write the generated passwords to a file if necessary
if OUTPUT_TO_FILE:
    result_file = open(filename, "w")
    result_file.write(passwords)
    result_file.close()

print(passwords)  # print the generated passwords



