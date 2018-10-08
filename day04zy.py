#EP1
'''
def getPentagonalNumber(n):
    i = 1
    for i in range(1,n+1):
        s = (i*(3*i-1)*1.0)/2
        print (str(s)+'  ',end='')
        if i%10==0:
            print()
getPentagonalNumber(100)
'''
#EP2
'''
def sum(n):
    s= 0
    while(n%10!=0):
        a=n%10
        b=n//10
        s=s+a
        n=b
    print(s)
a= eval(raw_input("enter a int:"))
sum(a)

'''


#EP3
'''
def display(n1,n2,n3):
    b=[n1,n2,n3]
    b.sort()
    print(b)
a1,a2,a3=eval(raw_input("enter three numbers:"))
display(a1,a2,a3)
'''



#EP4
'''
inves = eval(input("the amount inversted:"))
monthly = eval(input("annual interest rate:"))
print("annual\tfuture value")
def funtureinver(inves,monthly,years):
    return inves*pow((1+monthly/100/12),years*12)
for i in range(1,31):
    c=funtureinver(inves,monthly,i)
    print("%d\t%.2f"%(i,c),end=" ")
    print()
'''




#EP5
'''
def printchars(c1,c2,number):
    m=0
    a=ord(c1)
    b=ord(c2)+1
    for i in range(a,b):
        print(chr(i),end='')
        m=m+1
        if(m%number==0):
            print("")
a,b=input("enter start to end ascii:").split(',')
c = eval(input("enter number:"))
printchars('1','Z',10)
'''



#EP6
'''
def number(year):
    if((year%4==0)&(year%100!=0))|(year%400==0):
        print("%d:366"%(i))
    else:
        print("%d:365"%(i))
for i in range(2010,2021):
    number(i)
'''




#EP7
'''
def distance(a1,b1,a2,b2):
    print(((a1-a2)*(a1-a2)+(b1-b2)*(b1-b2))**0.5)
a1,b1=eval(raw_input("enter a1 and a2 for point1: "))
a2,b2=eval(raw_input("enter a1 and a2 for point2: "))
distance(a1,b1,a2,b2)
'''



#EP8

'''
import math
print ("p\t2^p-1")
def n(a):
    f=0
    for j in range(2,int(math.sqrt(a)+1)):
        if a%j==0 :
            f = 0
        else :
            f = 1
    return f
print("2\t3")
for i in range(1,32):
    c=pow(2,i)-1
    if(n(c)):
        print("%d\t%d"%(i,c))
'''

#EP9
'''
from time import *
print(ctime(time()))
'''

#EP10

'''
import random

n = random.randint(1,6)
m = random.randint(1,6)
s = n+m

if (s==2)|(s==3)|(s==12):
    print("you rolled {} + {} = {}\nyou lose".format(n,m,s))
elif (s==7)|(s==11):
    print("you rolled {} + {} = {}\nyou win".format(n,m,s))
else :
    print("you rolled {} + {} = {}\nyou is {}".format(n,m,s,s))
    n1 = random.randint(1,6)
    m1 = random.randint(1,6)
    s1 = n1+m1
    if(s1!=s):
        print("you rolled {} + {} = {}\nyou lose".format(n1,m1,s1))
    else :
        print("you rolled {} + {} = {}\nyou win".format(n1,m1,s1))
'''



#EP11










