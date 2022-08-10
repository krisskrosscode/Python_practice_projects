


from audioop import mul


class BonusDistribution:
    def __init__(self, empID, empRating) -> None:
        self.empID = empID
        self.empRating = empRating
        self.__bonusRatingA = "70%"
        self.__bonusRatingB = "60%"
        self.__bonusRatingC = "50%"
        self.__bonusRatingD = "30%"
        self.__bonusRatingE = "No Bonus"


    def bonusCalculator(self) -> str:

        if self.empRating == 'A':
            bonus = self.__bonusRatingA
            msg = "Bonus for this employee is " + bonus
            return msg

        elif self.empRating == 'B':
            bonus = self.__bonusRatingB
            msg = "Bonus for this employee is " + bonus
            return msg
        
        elif self.empRating == 'C':
            bonus = self.__bonusRatingC
            msg = "Bonus for this employee is " + bonus
            return msg

        elif self.empRating == 'D':
            bonus = self.__bonusRatingD
            msg = "Bonus for this employee is " + bonus
            return msg
        
        else:
            bonus = self.__bonusRatingE
            msg = "Bonus for this employee is " + bonus
            return msg
         
    def updateBonusRating(self, var, value):
        if var == 'A':
            self._BonusDistribution__bonusRatingA = value
        
        else:
            print("no bonus for this employee")

# ## now we will try to change the values of __bonusRating of say A from 70% to 75%
# emp1 = BonusDistribution(2, 'A')
# emp1._BonusDistribution__bonusRatingA = "75%"
# emp3 = BonusDistribution(45, 'A')
# print(emp1.bonusCalculator())
# print(emp3.bonusCalculator())

# emp4 = BonusDistribution(23, 'A')
# emp4.updateBonusRating('A', "95%")
# print(emp4.bonusCalculator())

# emp1.updateBonusRating('B' , "76%")
# print(emp1.bonusCalculator())

class multiplynumeric:
    def __init__(self, a) -> None:
        self.a = a
    
    def __mul__(self,  other):
        return self.a * other.a
    
    def __add__(self, other):
        return self.a + other.a

m = multiplynumeric(9)
n = multiplynumeric(2)

print(type(m), type(n))
print(m.a * n.a) 
print(m*n)

print(m+n) #https://www.codingem.com/python-__add__-method/#:~:text=%23%20prints%20%22Apple%22-,The%20__add__()%20Method%20in%20Python,-The%20__add__()