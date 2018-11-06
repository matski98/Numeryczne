#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:58:02 2018

@author: mati
"""
def wzgledny(p,p1):
    return abs(p-p1)/p
def bezwzgledny(p,p1):
    return abs(p-p1)
import math
p = math.pi
p1=22/7
print("p: ",p)
print("p*: ",p1)
print("blad wzgledny: ",wzgledny(p,p1))
print("blad bezwzgledny", bezwzgledny(p,p1))  
p=math.e
p1=2.718
print("p: ",p)
print("p*: ",p1)
print("blad wzgledny: ",wzgledny(p,p1))
print("blad bezwzgledny", bezwzgledny(p,p1))
p=10**math.pi
p1=1397
print("p: ",p)
print("p*: ",p1)
print("blad wzgledny: ",wzgledny(p,p1))
print("blad bezwzgledny", bezwzgledny(p,p1))
p=math.factorial(9)
p1=math.sqrt(18*math.pi)*((9/math.e)**9)
print("p: ",p)
print("p*: ",p1)
print("blad wzgledny: ",wzgledny(p,p1))
print("blad bezwzgledny", bezwzgledny(p,p1))
#2
#analitycznie nie zależy poniważ można sprowadzić funkcje do samego pi
def G(n):
    x=[]
    for i in range(1,n+1):
        x.append((10**i*(1+round(math.pi,15)*i*10**-i)-10**i)/i)
    return x

g=G(20)
import matplotlib.pyplot as plt
#print("blad wzgledny: ",wzgledny(math.pi,x[1]))
#print("blad bezwzgledny", bezwzgledny(math.pi,x[1]))
x = [i for i in range(20)]
y = [wzgledny(math.pi,g[i]) for i in range(20)]
plt.semilogy(x, y)
plt.title('blad wzgledny')
plt.xlabel('n')
plt.ylabel('blad')
plt.show()

z = [i for i in range(20)]
w = [bezwzgledny(math.pi,g[i]) for i in range(20)]
plt.semilogy(z, w)
plt.title('blad bezwzgledny')
plt.xlabel('n')
plt.ylabel('blad')
plt.show()
#błąð rośnie ponieważ algorytm jest niestabilny numerycznie
#błąð zaokrąglenia ponieważ p

#3
def e(n):
    a = 0;
    for i in range(n+1):
        a += 1/ math.factorial(i)
    return a

print("blad wzgledny dla n=5: ", wzgledny(math.e,e(5)))
print("blad bezwzgledny dla n=5: ", bezwzgledny(math.e,e(5)))
print("blad wzgledny dla n=10: ", wzgledny(math.e,e(10)))
print("blad bezwzgledny dla n=10: ", bezwzgledny(math.e,e(10)))
#4
a = 1.0
b = 2**-52
print(a+b-a-b)

#mantysa ma 52 bity
#błąd zaokrągleń
#1+2**-53==1



#5
pi = lambda x : math.sqrt(6*sum([1/(i*i) for i in range(1,x)]))
print(pi(1000000))
#błąd odcięcia
