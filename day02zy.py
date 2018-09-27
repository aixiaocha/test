#EP1
'''
import math
r = eval(raw_input("enter the length from the center to a vertex: "))
s = 2*r*math.sin(3.14/5)
Area = 5*s*s/(4*math.tan(3.14/5))
print("the area of the pentagon is: {}".format(Area))
'''
#EP2
'''
import math
x1,y1 = eval(raw_input("enter porint 1 (latitude and longitude) in degrees: "))
x2,y2 = eval(raw_input("enter porint 2 (latitude and longitude) in degrees: "))
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
d = 6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("the distance between the two point is {} km".format(d))
'''

#EP3
'''
import math
s = eval(raw_input("enter the side: "))
Area = (5*s*s)/(4*math.tan(3.14/5))
print("the area of the pentagon is: {}".format(Area))
'''

#EP4
'''
import math
n = eval(raw_input("enter the number of side: "))
s = eval(raw_input("enter the side: "))
Area = (n*s*s)/(4*math.tan(3.14/n))
print("the area of the pentagon is: {}".format(Area))
'''

#EP5
'''
import math
a = eval(raw_input("enter an ASXII code: "))
d = chr(a)
print("the character is {}".format(d))
'''

#EP6
'''
n = raw_input("enter employee`s name: ")
t = eval(raw_input("enter number of hours worked in a week: "))
mt = eval(raw_input("enter hourly pay rate: "))
ls = eval(raw_input("enter federal tax withholding rat: "))
zs = eval(raw_input("enter state tax withholding rate: "))
print("employee name: {}\nhours worked: {}\npay rate: ${}\ngross pay: ${}\ndeuctions\n  federal withholding(20.0%): ${}\n  state withholding(9.0%): ${}\n  total deduction: ${}\nnet pay: ${}".format(n,t,mt,t*mt,t*mt*ls,t*mt*zs,t*mt*ls+t*mt*zs,t*mt*(1-ls-zs)))
'''
#EP7
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = eval(raw_input("enter an integer: "))
b1 = a/1000
b2 = a/100%10
b3 = a/10%10
b4 = a%10
b5 =b4*1000+b3*100+b2*10+b1
print("the reversed number is: {}".format(b5))
'''
#EP8
'''
text = ''
new_text ='aixincheng'
for i in text:
    new = chr(ord(i)+1)
    new_text =new_text+new
print(new_text)
with open('textep8.txt','w') as f:
    f.write(new_text)

'''



#EP9
'''
import math
a,b,c = eval(raw_input("enter a b c: "))
d =b*b-4*a*c
if d > 0:
    r1 = (-b+math.sqrt(d))/2*a
    r2 = (-b-math.sqrt(d))/2*a
    print("The roots are {} and {}".format(r1,r2))
elif d == 0:
    r1 = (-b+math.sqrt(d))/2*a
    print("the root is {}".format(r1))
else :
    print("the equation has no real roots")
'''
#EP10
'''
import random
a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
d = eval(raw_input("enter a add b =: "))
print(c)
if d == c :
    print("True")
else :
    print("False")
'''
#EP11
'''
n = eval(raw_input("enter today`s day: "))
m = eval(raw_input("enter the number of days elapsed since today: "))
a = ['sunday','monday','tuesday','wednesday','thursday','friday','starday']
print("today is {} and the future day is {}".format(a[n],a[(m-n)%7]))
'''
#EP12
'''
a1,a2,a3 = eval(raw_input("enter three: "))
if a2 > a1 :
    t = a2
    a2 = a1
    a1 = t
if a3 > a2 :
    t = a3
    a3 = a2
    a2 = t
if a2 > a1 :
    t = a2
    a2 = a1
    a1 = t
print a1,a2,a3
'''
#EP13
'''
a1,b1 = eval(raw_input("enter weight and price for package 1: "))
a2,b2 = eval(raw_input("enter weight and price for package 1: "))
n1 = b1/a1*1.0
n2 = b2/a2*1.0
if n1 > n2:
    print("package 2 has the better price")

elif n1 < n2:
    print("package 1 has the better price")
print n1,n2
'''
#EP14
'''
y = eval(raw_input("enter year: "))
m = eval(raw_input("enter month: "))
if (y%4==0) & (y%100 != 0) | (y%400 ==0) :
    a = [31,29,31,30,31,30,31,31,30,31,30,31]
    print("the is {} day".format(a[m-1]))
else :
    a = [31,28,31,30,31,30,31,31,30,31,30,31]
    print("the is {} day".format(a[m-1]))
'''
#EP15
'''
import random
a = random.randint(0,1)
b = eval(raw_input("enter a shu(0 or 1): "))
if b == a :
    print("true")
else :
    print("false")
'''
#EP16
'''
import random
a = random.randint(0,2)
b = int(raw_input("scissor(0), rock(1),paper(2):"))
print(a)
if (a == 0) & (b == 0) :
    print("the computer is scissor,you are scissor, you draw")
elif (a == 0) & (b == 1) :
    print("the computer is scissor,you are rock, you won")
elif (a == 0) & (b == 2) :
    print("the computer is scissor,you are paper, you no won")
elif (a == 1) & (b == 0) :
    print("the computer is rock,you are scissor, you no won")
elif (a == 1) & (b == 1) :
    print("the computer is rock,you are rock, you draw")
elif (a == 1) & (b == 2) :
    print("the computer is rock,you are paper, you won")
elif (a == 2) & (b == 0) :
    print("the computer is paper,you are scissor, you won")
elif (a == 2) & (b == 1) :
    print("the computer is paper,you are rock, you no won")
elif (a == 2) & (b == 2) :
    print("the computer is paper,you are paper, you draw")
'''
#EP17
'''
import random

a = ['hx','fp','mh','ht']
b = ['1','2','3','4','5','6','7','8','9','10','jack','queen','king']
a1=a[random.randint(0,len(a)-1)]
b1=b[random.randint(0,len(b)-1)]
print("the card you picked is the {} of {}".format(b1,a1))
'''
#EP18
'''
a = eval(raw_input("enter a three-digit integer: "))
b = a/100
c = a%10
if (b == c) :
    print("{} is a palindrome".format(a))
else :
    print("{} is not a palindrome".format(a))
'''

#EP19
'''
a,b,c = eval(raw_input("enter three edges: "))

if (a + b > c) and (a - b < c):
    print("the perimeter is {}".format(a+b+c))
else :
    print("enter is not true")
'''    


















