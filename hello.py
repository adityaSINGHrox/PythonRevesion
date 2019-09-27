#########
# lets checkout on strings

import os
os.system('clear')
# we need to print like "GET BACK TO WORK"

greetings = 'my boss yelled "GET BACK TO WORK"'
# using esczpe characters like
yo  = 'hey wassup \"FNIE BRO\"'
print(greetings)
print(yo)
#use \n for new line
#############
#concatenation
adi = "yo Man wassup"
singh = " cool Man"
print((adi+singh).upper())
print((adi+singh).lower())
print((adi+singh).capitalize())#starting alphabet
print((adi+singh).title())
print((adi+singh).swapcase())
print(len(adi+singh))
print(greetings[10:15])
print(greetings.split(" ")[5])#seperate wrt " "
#['my', 'boss', 'yelled', '"GET', 'BACK', 'TO', 'WORK"']
