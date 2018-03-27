class people():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print('%s在睡觉'%self.name)

class man(people):
    def __init__(self,name,age,money):
        people.__init__(self,name,age)
        self.money = money
        print('%s有%s元'%(self.name,self.money))

    def sleep(self):
        people.sleep(self)
        print('%s重构了sleep'%self.name)
p1 = people('teat1',22)
p1.sleep()

m1 = man('test2',25,1000)
m1.sleep()