#Super
class Student:
    #class variable
    def __init__(self,name,height,weight):
        # instance variable
        self.__name = name
        self.__height = height
        self._weight = weight

    def _showData(self):
        print("ชื่อนักเรียน = "+self.__name)
        print("ส่วนสูง = ",format(self.__height))
        print("น้ำหนัก = "+self._weight)
        #รายได้ต่อปี
    def _getBMI(self):
        return self._weight/(self.__height/100)**2
    def __str__(self):
        return ("ชื่อนักเรียน = {},น้ำหนัก = {},ส่วนสูง = {}".format(self.__name,self._weight,self.__height))

class Student1(Student):
    def __init__(self,name,height,weight):
        super().__init__(name,height,weight)
        
class Student2(Student):
    def __init__(self,name,height,weight):
        super().__init__(name,height,weight)
    
class Student3(Student):
    def __init__(self,name,height,weight):
        super().__init__(name,height,weight)

class Student4(Student):
    def __init__(self,name,height,weight):
        super().__init__(name,height,weight)
        
s1 = Student1("1",150,45)
#print(account._getIncome())
print(s1.__str__())
print(s1._getBMI())
s2 = Student2("2",158,60)
#print(programmer._getIncome())
print(s2.__str__())
print(s2._getBMI())
s3 = Student3("3",150,70)
#print(sale._getIncome())
print(s3.__str__())
print(s3._getBMI())
s4=Student4("4",160,55)
print(s4.__str__())
print(s4._getBMI())