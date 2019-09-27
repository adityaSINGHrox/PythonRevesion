import os
os.system('clear')
print('')
print('hello world')

#trying out oop
class Person:

    def __init__(self,initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.intitialAge = 0
        else :
            self.initialAge = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.initialAge in range(0,13):
            print('You are young.')
        if self.initialAge in range(13,18):
            print('You are a teenager')
        if self.initialAge >18:
            print('You are old')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.initialAge += 1
        print(self.initialAge)
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
