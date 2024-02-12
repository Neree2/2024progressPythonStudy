#inheritance
class Employee:
    __minSalary = 12000
    __maxSalary = 50000
    _companyName = "บริษัท Neree จำกัด"
    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน ="+self.__name)
        print("เงินเดือน =",format(self.__salary))
        print("ตำแหน่ง ="+self._department)

class Accounting:
    __departmentName= "แผนกบัญชี"
    def __init__(self):
        pass
class Programmer:
    __departmentName= "แผนกพัฒนาระบบ"
    def __init__(self):
        pass
class Sale:
    __departmentName= "แผนกขายสินค้า"
    def __init__(self):
        pass

account = Accounting()
programmer = Programmer()
sale = Sale()
