class Employee:
    #class variable 
    _minSalary = 12000
    _maxSalary = 50000
    def __init__(self,name,salary,department):
    #private
        self._name  = name
        self.__salary = salary
        self.__department = department
    #private    
    def _showData(self):
        print(self._name)
        print(self.getSalary())
        print(self.getDepartment())
    #setter 
    def setSalary(self,newsalary):
        self.__salary = newsalary
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
    #getter
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department
#การสร้างวัตถุ
Emp1 = Employee("neree1",50,"โปรแกรมเมอร์")
Emp1.setSalary = 500000
Emp1._showData()
print(Employee._minSalary)
