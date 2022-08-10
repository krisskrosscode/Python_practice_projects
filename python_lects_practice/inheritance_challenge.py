# 1. create class test and test1    
# 2. inherit test and test1 into test2     
# 3. function a in test    
# 4. function a in test1     
# 5. test2 should inherit function-a from test1 and test both  



class test:
    def a(self):
        print("This a() belongs to class->test")

class test1:
    def a(self):
        print("This a() belongs to class->test1")

class test2(test, test1):
    pass


obj = test2()

test.a(obj) #important
test1.a(obj) #important




