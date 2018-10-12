# _*_coding:utf8-
#EP1
'''
1.判断社会安全号码是否符合规范：
'''
'''
def pd(q):
    global a
    if len(a)==11:
        if a[0]>='0' and a[0]<='9' and a[1]>='0' and a[1]<='9' and a[2]>='0' and a[2]<='9':
            if a[3]=='-':
                if (a[4]>='0' and a[4]<='9')and (a[5]>='0' and a[5]<='9'):
                    if a[6]=='-':
                        if (a[7]>='0' and a[7]<='9') and (a[8]>='0' and a[8]<='9') and (a[9]>='0' and a[9]<='9') and (a[10]>='0' and a[10]<='9'):
                            print("Valid SSN")
                        else:
                            print("Invalid SSN")
                    else:
                        print("Invalid SSN")
                else:
                    print("Invalid SSN")
            else:
                print("Invalid SSN")
        else:
            print("Invalid SSN")
    else:
        print("Invalid SSN")
a=str(raw_input("enter a string li ru ddd-dd-dddd:"))
pd(a)
'''



#EP2
'''
创建一个函数fand，输入两个字符串，判断第一个字符串是不是第二个的子串
'''
'''
def fand(n,m):
    a = n
    b = m
    if a in b:
        return 0
    else:
        return -1

a = str(input("enter is str1: "))
b = str(input("enter is str2: "))
c = fand(a,b)
if c == -1:
    print 'no'
else :
    print 'yes'
'''




#EP3
'''
检测密码至少8位，必须是字母和数字，数字不少于2位，创建一个函数jiance

'''
'''
a = str(input("enter password: "))

def jiance(n):
    a = n
    f = 0
    if len(a)>= 8:
        if (a.isalnum() == True):
            for i in range(len(a)):
                if a[i]>='0' and a[i]<='9':
                    f+=1
            if f >= 2:
                print('valid password!')
            else:
                print('invalid password!')
        else:
            print('invalid password!')
    else:
        print('invalid password!')

jiance(a)
'''

#EP4
'''
统计字符串中字母的个数,创建一个countLetters函数

'''
'''
a = str(input("enter str: "))

def countLetters(s):
    a = s
    f = 0
    for i in range(len(a)):
        if (a[i]>= 'a' and a[i]<= 'z') or (a[i]>='A' and a[i]<= 'Z'):
            f+=1
    print ('the is zimu shu:{}'.format(f))
countLetters(a)
'''





#EP5
'''
九键输入字母返回对应数字
'''
'''
a = str(input("enter a string: "))

def getNumber(uppercaseLetter):
    a = uppercaseLetter
    for i in a:
        if (i>='a' and i<='c') or (i>='A' and i<='C'):
            i = '2'
        elif (i>='d' and i<='f') or (i>='D' and i<='F'):
            i = '3'
        elif (i>='g' and i<='i') or (i>='G' and i<='I'):
            i = '4'
        elif (i>='j' and i<='l') or (i>='J' and i<='L'):
            i = '5'
        elif (i>='m' and i<='o') or (i>='M' and i<='O'):
            i = '6'
        elif (i>='p' and i<='s') or (i>='P' and i<='S'):
            i = '7'
        elif (i>='t' and i<='v') or (i>='T' and i<='V'):
            i = '8'
        elif (i>='w' and i<='z') or (i>='W' and i<='Z'):
            i = '9'
        print(i,end='')
    print()
getNumber(a)
'''


#EP6
'''
字符串反转，reverse1函数
'''
'''
a = str(input("enter string: "))
def reverse1(s):
    a = s
    n = len(a)-1
    while n>=0:
        print(a[n],end='')
        n-=1
    print()
reverse1(a)
'''



#EP7
'''
def checkISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        SUM += res

    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print(RES)

str_ = input('>>')
checkISBN(str_)

def checkCard(card_num):
    card_list = list(card_num) # 将字符串转为列表方便计算
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2  # 将所有位数*2
        if res >= 10:
            res_1 = res % 10  # 拿到的个位
            res_2 = res // 10# 拿到的十位
            res_3 = res_2 + res_1
            Res += res_3
        else:
            Res += res

        if i % 2 !=0: # 加和所有奇数位置
            Res_2 += int(card_list[i])

    RES = Res + Res_2
    if RES % 10 == 0:
        print('合法')
    else:
        print('不合法')
card_num = '438857601840707'
checkCard(card_num)
'''

#EP8
'''
a1=input("enter a 12 wei shu:")
a=list(a1)
s=0
j=0
for i in range(len(a)):
    a[i]=int(a[i])
    if (i%2==0):
        a[i]=3*a[i]
    else:
        a[i]=a[i]
    s=s+a[i]
j=10-s%10
if j==10:
    j=0
print(j)
'''






#EP9
'''
成绩排序
'''
'''
a1 = input("enter scores: ")
a = a1.split()
#print(type(a1))
#print(type(a))
best = max(a)
for i in range(len(a)):
    a[i] = int(a[i])
    best = int(best)
    if (a[i]>=best-10):
        print ('student {} score is {} and grade is A'.format(i,a[i]))
    elif (a[i]>=best-20):
        print ('student {} score is {} and grade is B'.format(i,a[i]))
    elif (a[i]>=best-30):
        print ('student {} score is {} and grade is C'.format(i,a[i]))
    elif (a[i]>=best-40):
        print ('student {} score is {} and grade is D'.format(i,a[i]))
    else:
        print ('student {} score is {} and grade is F'.format(i,a[i]))
'''





#EP10
'''
逆序读数字
'''
'''
a1 = input("enter shu:")
a = a1.split()
b = a
print(a)
b.reverse()
print(b)
'''

#EP11
'''
a1 = input("enter integers between 1 and 100:")
a = a1.split()
for j in range(1,101):
    b=0
    for i in a:
        i=int(i)
        if (i == j):
            b+=1
    if(b>0):
        print('{} occurs {} times'.format(j,b))
'''





#EP12
'''
大于等于平均值成绩个数和小于平均值的成绩个数，创建一个求平均值的函数num
'''
'''
a1 = input("enter scores: ")
a = a1.split()
n,m = 0,0
def num(s):
    sum1 = 0
    for i in s:
        i = int(i)
        sum1 += i
    #print(sum1/len(s)*1.0)
    return sum1/len(s)*1.0
b = num(a)
for i in a:
    i = int(i)
    if i >= b:
        n+=1
    else:
        m+=1
print(">=sum: {} times , <sum: {} times".format(n,m))
'''





#EP13
'''
随机产生0-9中1000个数，求出现个数
'''
'''
import random
b = []
for j in range(1000):
    a=random.randint(0,9)
    b.append(a)
for i in range(10):
    print("{} occurs {} times".format(i,b.count(i)))
'''



#EP14
'''
a = input("enter is shu:")
def index(lst):
    b = lst
    d = b.split()
    c =min(d)
    for i in range(len(d)):
        if(d[i]==c):
            print("zui xiao yuan shu xia biao:",i)
index(a)
'''





#EP15
'''
输入数字列表，打乱输出
'''
'''
a = input("enter is string: ")

def shuffle1(lst):
    a = lst
    b = a.split()
    c = set(b)
    d = list(c)
    print(d)
shuffle1(a)
'''
''''''''''''


#EP16
'''
去重
'''
'''
a = input("enter is shu:")
def eliminate(lst):
    a = lst
    b = a.split()
    c = set(b)
    d = list(c)
    print(d)
eliminate(a)
'''



#EP17
'''
判断是否升序
'''
'''
a1=input("enter list:")
def isSorted(lst):
    a=a1.split()
    b=a1.split()
    a.sort()
    print(a)
    print(b)
    if a==b:
        print("the list is already sorted")
    else:
        print("the list is no sorted")
isSorted(a1)
'''


#EP18
'''
冒泡排数字
'''
'''
a1=raw_input("enter a number list:")
a=a1.split()
for i in range(len(a)):
    for j in range(len(a)-1):
        a[j]=int(a[j])
        if (a[j]>a[j+1]):
            a[j]=a[j]
        else:
            a[j],a[j+1]=a[j+1],a[j]
a=list(a)
print(a)
'''





#EP19




#EP20




















