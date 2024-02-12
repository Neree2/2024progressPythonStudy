class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_it(self):
        print("name: ",self.name,'age: ',self.age)

class Dog(Animal):
    def __init__(self,name,age,breed) :
        super().__init__(name,age)
        self.breed=breed
    def dis_it(self):
        print('name: ',self.name,'age: ',self.age,'breed: ',self.breed)

class Cat(Animal):
    def __init__(self,name,age,breed) :
        super().__init__(name,age)
        self.breed=breed
    def dis_it(self):
        print('name: ',self.name,'age: ',self.age,'breed: ',self.breed)

dog1=Dog('pup',4,'lots of Breed')
dog1.dis_it()