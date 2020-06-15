class multiply:

    def square(self,num):
        return num* num

class Cube(multiply):
    def __init__(self):
        pass

    def __call__(self,num):
        return num*num*num

    def square(self,num):
        return super().square(num)

cube = Cube()
print(type(cube))
print(cube(5))
print(cube.square(3))
