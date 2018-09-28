#EP1
'''
i,j,n,m = 0,0,0,0
a = eval(raw_input("enter an integer, the input ends if it is 0: "))
while (a != 0):
    if(a > 0):
        i+=1
        n+=a
    if (a < 0):
        j+=1
        m+=a
    a = eval(raw_input("enter an integer, the input ends if it is 0: "))
print("zhengshu: {},fushu: {},sum: {}".format(i,j,(n+m)*1.0/(j+i)))
'''
#EP2
'''
a = 10000 
i,s = 0,0
for i in range(10):
    a=a*(1+0.05)
print("10 years later ${}".format(a))
for i in range(4):
    s=s+a
    a=a*(1+0.05)
print("4 years add {}".format(s))
'''
#EP3
'''
i,j,n,m = 0,0,0,0
a = eval(raw_input("enter an integer, the input ends if it is 0: "))
while (a != 0):
    if(a > 0):
        i+=1
        n+=a
    if (a < 0):
        j+=1
        m+=a
    a = eval(raw_input("enter an integer, the input ends if it is 0: "))
print("zhengshu: {},fushu: {},sum: {}".format(i,j,(n+m)*1.0/(j+i)))
'''
#EP4
'''
i,s = 0,0
for i in range(100,1001):
    if(i%5==0)&(i%6==0):
        s+=1
        print i, 
    if s == 10 :
        print
        s = 0
'''
#EP5
'''
n = 100
m = 25
while (n*n < 12000):
    n+=1
print n
while (m*m*m > 12000):
    m-=1
print m
'''
#EP6
'''
i =0.05
p = eval(raw_input(">>"))
t = eval(raw_input(">>"))
f1 = p*pow(1+i,t)
f2 = f1/(12*t)
print("%.5f     %.2f   %.2f"%(i,f2,f1))
while(i<=0.08):
    i+=0.00125
    f1=p*pow(1+i,t)
    f2=f1/(12*t)
    print("%.5f     %.2f   %.2f"%(i,f2,f1))
'''





#EP7
'''
f = 50001
s = 0
for i in range(1,50001):
    s+=1.0/(f-i)
print s
'''


#EP8
'''
i = 1
s = 0
for i in range(50):
    s = s+(2*i-1)*1.0/(2*i+1)
print s
'''
#EP9
'''
import math
n = eval(raw_input("enter a i :"))

s = 0
for i in range(1,n+1):
    s = s+(pow(-1,i+1))*1.0/(2*i-1)
print 4*s
'''

#EP10
'''
for i in range(1,10000):
    s=0
    for j in range(1,i/2+1):
        if (i%j==0):
            s+=j
    if (s==i):
        print i
'''
#EP11
'''
a = 0
for i in range(1,8):
    for j in range(i+1,8):
        a+=1
        print i,j
print a
'''




