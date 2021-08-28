The Personal Information Password Generator - PIPG

All rights reserved - @RoyHatton - github.com/royh2149

Free to use. Please use this tool only for legal purposes, I won't be held responsible in case you don't.

Credit to Yuval Shtalman for introducing me to the CeWL tool and pointing out for me how common "personal" passwords are.

PIPG generates many common passwords based on the inputed personal information.

Usage:
    gpipg = open the Graphical PIPG
    pipg [-i interactive] [-f first name] [-l last name] [-m name1,name2,name3...] 
         [-p name1,name2,name3...] [-d birthdate] [-e email] [-o <file>]

Arguments:
    -i, --interactive   a PIPG interactive input shell. Overrides all other options.
    -d, --birthdate     victim's birthdate. Format: DD/MM/YY
    -e, --email         victim's email
    -f, --fname         victim's first name
    -l, --lname         victim's last name
    -m, --moren         additional names. Use comma delimiter: -m name1,name2...
    -p, --pets          victim's pets' names. Use comma delimiter: -m name1,name2...
    -o, --output        output the generated passwords to a file
