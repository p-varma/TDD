class Singleton:

    __instance = None

    @staticmethod
    def getInstance():

        if not Singleton.__instance:
            Singleton()
        return Singleton.__instance

    def __init__(self):

        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    Singleton.getInstance()
    Singleton.getInstance()
    Singleton.getInstance()
    Singleton.getInstance()


    #print(o1)
        # print(o1.getInstance())
       # print(o2)
    # print(o2.getInstance())
