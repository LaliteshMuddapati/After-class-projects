class add:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def solve(self):
        print(self.num1 + self.num2 + self.num3)

n1=int(input("Enter the value of num1= "))
n2=int(input("Enter the value of num2= "))
n3=int(input("Enter the value of num3= "))

numbers = add(n1, n2, n3)
numbers.solve()