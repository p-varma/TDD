# import os


def list(path):
    elements = os.listdir(path)
    for element in elements:
        abspath = path + f'\\{element}'
        if os.path.isdir(abspath):
            list(abspath)
        print(abspath)



#list(r'd:\TDD')


def factorial(n):
    fact = 1
    if n> 1:
        fact = n * factorial(n-1)
    return fact

#print(factorial(5))

class Attendees:

    __number_of_participants= 0

    def __init__(self,name):
        self.name = name
        Attendees.__number_of_participants +=1


    def get_name(self):
        return self.name

    @staticmethod
    def get_participants():
        return Attendees.__number_of_participants



