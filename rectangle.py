class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def find_area(self):
        area=self.length*self.breadth
        return area


r1=Rectangle(4,5)
r1_area = r1.find_area()

r2=Rectangle(5,5)
r2_area = r2.find_area()

print("Area of first rectangle:", r1_area)
print("Area of second rectangle:", r2_area)

if r1_area>r2_area:
    print("R1 is greater")
else:
    print("R2 is greater")
