class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
        #ecapsulation
    def lastname(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay =int(self.pay* (1+percent))
        return self.pay
    #operator overloading
    def __repr__(self):
        return '[Person:%s,%s]'%(self.name,self.pay)
    

class Manager(Person):
    def __init__(self, name,  pay=0):
        super().__init__(name, 'mgr', pay)
    def giveRaise(self, percent,bonus=0.10):
        self.pay =Person.giveRaise(self,percent+bonus)
        return self.pay


if __name__ =='__main__':
    bob=Person('Bob Kilo')
    Lucy=Person('Lucy lop','Doc',59000)
    tom = Manager('Tom Joe' ,100000)
    print(bob)
    print(Lucy)
    
    # print(Lucy.name,Lucy.pay)
    # print(bob.lastname(),Lucy.lastname())    
    # print(Lucy.giveRaise(.20));
    # print(Lucy,bob)

    tom.giveRaise(0.20)
   
    print(tom)
