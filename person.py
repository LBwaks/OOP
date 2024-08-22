class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
        #ecapsulation
    def lastname(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        return int(self.pay* (1+percent))
    #operator overloading
    def __repr__(self):
        return '[Person:%s,%s]'%(self.name,self.pay)

if __name__ =='__main__':
    bob=Person('Bob Kilo')
    Lucy=Person('Lucy lop','Doc',59000)

    
    # print(Lucy.name,Lucy.pay)
    # print(bob.lastname(),Lucy.lastname())    
    # print(Lucy.giveRaise(.20));
    print(Lucy,bob)
