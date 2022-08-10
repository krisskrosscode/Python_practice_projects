class Dog:
    def __init__(self, name, year_of_birth, breed) -> None:
        self.name = name
        self.year_of_birth = year_of_birth
        self.breed = breed
    
    def __str__(self) -> str:
        return "name: %s , breed: %s , born in: %d" %(self.name, self.breed, self.year_of_birth)


class Student:
    def __init__(self, name, student_id, school_name, address) -> None:
        self.name = name
        self.student_id = student_id
        self.school_name = school_name
        self.address = address
    
    def __str__(self) -> str:
        return "name: %s , student id : %d , school name : %s, address : %s" %(self.name, self.student_id, self.school_name, self.address)
    

stu =  Student("keshav" ,323, "high_school", "bokaro")
print(stu)

dog1 = Dog("motie",2020, "paumerian")
print(dog1)

dog2  = Dog(stu, 2002, "not known")
print(dog2 , type(dog2))