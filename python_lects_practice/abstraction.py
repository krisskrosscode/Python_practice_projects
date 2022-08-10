class test:
    def __init__(self, a, b) -> None:
        self.a = a*4
        self.__a = a
        self.b = b



class test1(test):#inheritance
    def __init__(self,j, *args) -> None:
        super(test1, self).__init__(*args)
        self.j = j


m = test1(4,5,7)
print(m.j)
print(m.a)
print(m.b)