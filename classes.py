class Employee():
    pay_rise=1.04
    number_of_employees=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=self.fname+'.'+self.lname+'@company.com'
        Employee.number_of_employees +=1
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    def display_pay(self):
        return self.pay
    def increase_pay(self):
        self.pay = self.pay * self.pay_rise
        return self.pay
obj1=Employee('Harsha','Peddula',17000)
print(Employee.display_pay(obj1))
print(obj1.email)
print(obj1.fullname())
print(obj1.display_pay())
obj1.increase_pay()
print(obj1.increase_pay())
obj2=Employee('Virat','Kohli',10000)
obj2.pay_rise=2.00
obj1.pay_rise=3.00
print(obj1.increase_pay())
print(Employee.number_of_employees)
