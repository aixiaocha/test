#EP:1
'''
celsius = raw_input("Enter a degree in Celsius:")
float_c = float(celsius)
fahrenheit = (9/5.0) * float_c +32
print("{} Celsius is {} Fahrenheit".format(float_c,fahrenheit))
'''
#EP:2
'''
x,y = eval(raw_input("Enter the radius and length of a cylinder:"))
area = x*x*3.142
volume = area * y
print('The area is {}\nThe vloume is {}\n'.format(area,volume))
'''
#EP:3
'''
yingci = float(raw_input("Enter a value for feet: "))
m= yingci * 0.305
print("{} feet is {} meters".format(yingci,m))
'''
#EP:4
'''
M = float(raw_input("Enter the amount of water in kilograms: "))
initial = float(raw_input("Enter the initial temperature "))
final = float(raw_input("Enter then final temperature "))
Q = M * (final - initial) * 4184
print("The energy needed is {}".format(Q))
'''
#EP:5
'''
e,g = eval(raw_input("Enter balance and interest raet(e,g.,3 for 3% )"))
l = e*(g/1200.0)
print("The interest is %.5f"%(l))
'''
#EP:6
'''
v0,v1,t = eval(raw_input("Enter v0,v1,and t: "))
a=(v1-v0)/t
print("The average acceleration is %.4f"%(a))
'''
#EP:7
'''
t1 = float(raw_input("Enter the monthly saving amount:"))

t2 = t1 * (1+0.00417)
t3 = (t2 + 100) * 1.00417
t4 = (t3 + 100) * 1.00417
t5 = (t4 + 100) * 1.00417
t6 = (t5 + 100) * 1.00417
t7 = (t6 + 100) * 1.00417

print("After the sixth month,the account value is %.2f"%(t7))
'''
#EP:8


num = int(raw_input("Enter a number between 0 and 1000 :"))

a = num/100
b = num/10%10
c =num%10

d= a+b+c
print("The sum of the digits is {}".format(d))








