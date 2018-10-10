
# _*_conding:utf8-
#EP1
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getck(self):
        print self.width,self.height
    def getArea(self):
        area = self.width*self.height
        print area
    def getPerimeter(self):
        perimeter = 2*(self.width+self.height)
        print perimeter

def a(n1=1,n2=2):
    rec=Rectangle(n1,n2)
    rec.getck()
    rec.getArea()
    rec.getPerimeter()


if __name__ == '__main__':
    a()
    a(4,40)
    a(3.5,35.7)
'''

#EP2
'''
class Account:
    def __init__(self,id1=0,balance=100,annualInterestRate=0):

        self.__id = id1
        self.balance = balance
        self.__ann = annualInterestRate
        print self.__id
    def getMonthlyInterestRate(self):
        mir = self.__ann/12*1.0/100
        print "monthlyinterestRate:",mir
    def getMonthlyInterest(self):
        mi = self.balance*self.__ann/12*1.0/100
        print "monthlyinterest:",mi
    def withdraw(self,a):
        if a < self.balance:
            print '[+]withdraw',a
        else:
            print 'no money!'
        self.balance = self.balance-a
        return self.balance
    def deposit(self,b):
        self.balance = self.balance+b
        return self.balance
    def unm1(self):
        print self.balance
if __name__ == '__main__':
    acc = Account(1122,20000,4.5)
    acc.withdraw(2500)
    acc.deposit(3000)
    acc.unm1()
    acc.getMonthlyInterestRate()
    acc.getMonthlyInterest()
'''
#EP3
'''
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getperimeter(self):
        per = self.__n*self.__side
        print per
    def getarea(self):
        area = (self.__n*(self.__side**2))/(4*math.tan(math.pi/self.__n))
        print area

if __name__ == '__main__':
    a1 = RegularPolygon()
    a2 = RegularPolygon(6,4)
    a3 = RegularPolygon(10,4,5.6,7.8)
    a1.getperimeter()
    a1.getarea()
    a2.getperimeter()
    a2.getarea()
    a3.getperimeter()
    a3.getarea()
'''


#EP4
'''
class Fan:
    def __init__(self,speed="SLOW",on=False,radius=5,color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    def get(self):
        print ('[+]'self.__speed
        print self.__on
        print self.__radius
        print self.__color
if __name__ == '__main__':
    n1 = Fan("FAST",True,10,"yellow")
    n1.get()
    print
    n2 = Fan("MEDIUM",False,5,"blue")
    n2.get()
'''


#EP5
'''
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def isSolvable(self):
        if(self.__a*self.__d-self.__b*self.__c)!=0:
            return True

    def getX(self):
        x=((self.__e*self.__d)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c))
        print x
    def getY(self):
        y=((self.__a*self.__f)-(self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c))
        print y

if __name__ == '__main__':
    a,b,c,d,e,f = eval(raw_input("enter :"))
    n =  LinearEquation(a,b,c,d,e,f)
    if n.isSolvable()==True:

        n.getX()
        n.getY()
    else:
        print "no"

'''



#EP6
'''
class lll:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def kk(self):
        k1 = (self.y2-self.y1)/(self.x2-self.x1)
        k2 = (self.y4-self.y3)/(self.x4-self.x3)
        if k2 == k1 :
            print("no have jiao dian")
        else:
            return k1,k2
    def bb(self):
        k1,k2 =self.kk()
        b1 = -(k1*self.x1-self.y1)
        b2 = -(k2*self.x3-self.y3)
        return b1,b2
    def yzb(self):
        b1,b2 = self.bb()
        k1,k2 = self.kk()
        y = (b1-(k1*b2))/(k2-k1)
        return y
    def xzb(self):
        b1,b2 = self.bb()
        k1,k2 = self.kk()
        y = self.yzb()
        x = (y-b2)/k2
        return x
    def aa(self):
        x = self.xzb()
        y = self.yzb()
        print (x,y)

lll(2,2,0,0,0,2,2,0).kk()
lll(2,2,0,0,0,2,2,0).bb()
lll(2,2,0,0,0,2,2,0).yzb()
lll(2,2,0,0,0,2,2,0).xzb()
lll(2,2,0,0,0,2,2,0).aa()
'''















