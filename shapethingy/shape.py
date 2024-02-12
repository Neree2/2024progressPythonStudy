class Shape:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        print(self.num1*(self.num2**2))
class Rectangle(Shape):
    def area(self):
        print(self.num1*self.num2)

def calculate_total_area(are):
    are.area()

circle=Circle(3.14,7)
rectangle=Rectangle(2,34)

calculate_total_area(circle)
calculate_total_area(rectangle)