class Firstclass():
    def setdata(self,value):
        self.data=value
    def display(self):
        print (self.data)

l1=Firstclass();
l2=Firstclass();
l1.setdata('Out');
l1.display()
l2.setdata('in')
l2.display();
l1.data='New'
l1.display()
print('*************************************')
##inheritance
class SecondClass(Firstclass):
    def display(self):
        return super().display()
p=SecondClass()
p.setdata(9)
p.display();
l1.display()
print('*************************************')
class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value;
    def __add__(self,value):
        return ThirdClass(self.data+other)
    def __str__(self) -> str:
        return '[ThirdClass:%s]' % self.data
    def __mul__(self,other):
        self.data*=other

a=ThirdClass('Last');
a.display()
print(a)
print('*************************************')

class Person:
    def __init__(self,names,job,age=None):
        self.names=names
        self.job=job
        self.age=age;
    def info(self):
        return (self.names,self.info)
per1=Person('llll',['f','t'])
print(per1.job,per1.info())
print(vars(per1))