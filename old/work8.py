# mario, 2 characters, แดง: อายุน้ำหนักส่วนสูง (โจมตีป้องกัน), เขียว: อายุน้ำหนักส่วนสูง (เวทป้องกัน)

class Mario:
    def dang(self,name, age,weight,height,power):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.power = power
        print(self.name,'age:',self.age,"weight:", self.weight, "height:", self.height, "power:", self.power)

mar= Mario()
mar.dang("แดง",42,22,187,"โจมตีป้องกัน")
mar2= Mario()
mar2.dang("เขียว",53,234,176,"เวทป้องกัน")
mar3= Mario()
mar3.dang("น้ำตาล",32,53,299,"น้ำตาล")