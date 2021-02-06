class Foo:
    def __init__(self):
        self.bar = 'hello!'

    def __getattr__(self, item):
        return 'goodbye!'

    def __getattribute__(self, item):
        our_dict = object.__getattribute__(self, "__dict__")
        if item in our_dict:
            return object.__getattribute__(self, item)
        else:
            return Foo.__getattr__(self, item)


class Bar:
    def __init__(self, x=10):
        self.__x = x

    def setCoord(self, val):
        self.__x = val

    def getCoord(self):
        return self.__x

    def delCoord(self):
        del self.__x

    coord = property(setCoord, getCoord, delCoord)


test = Bar()
test.coord = 12
print(test.coord)
