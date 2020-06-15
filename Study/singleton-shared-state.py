class Borg:

    __shared_state = dict()

    def __init__(self):

        self.__dict__ = self.__shared_state
        self.state = 'Prashant'
        self.a = 20
        print(self.__dict__)

    def __str__(self):
        print(self.__dict__)
        return self.state

if __name__ == '__main__':
    o1 = Borg()
    o2 = Borg()
    o3 = Borg()

    o1.state = "varma"
    o1.a = 50
    print(o1)
    print(o2)

    print(o1.a)
    print(o2.a)
    print(o3.a)