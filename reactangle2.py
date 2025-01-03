class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth

    def find_area(self):
        area=self.__length*self.__breadth
        return area
    def __lt__(self, rect2):
        return self.find_area()<rect2.find_area()


r1=Rectangle(4,5)
r1_area = r1.find_area()

r2=Rectangle(5,5)
r2_area = r2.find_area()

print("Area of first rectangle:", r1_area)
print("Area of second rectangle:", r2_area)

if r1<r2:
    print("R2 is greater")
else:
    print("R1 is greater")
