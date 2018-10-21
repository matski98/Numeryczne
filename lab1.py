# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:50:40 2018
@author: student198
"""
#1
from math import sqrt
k = 1240 * sqrt(7)
m = 4467
l = 2j
d = k+m
c = d+l
#2
print(d)
print( "{a:.3f}".format(a = d ) )
print( "{a:.20f}".format(a = d ))
#3
from math import pi
r=17
h=33
S=2*r*pi*h+2*r**2*pi
print(S)
#4
"""
r to promień podstawy walca
h to jego wysokosc
S to pole powierzchni
"""
#5
from math import sin
x1=1
r=2
t=1
B=((x1+r)/(r*sin(2*x1)+3.3456))*x1**(t-r)
print(B)
#6
import numpy
a = sqrt(2)
M=numpy.array([[a,1,-a],[0,1,1],[-a,a,1]])
print(M)
print("--------------------")
Minv = numpy.linalg.inv(M)
print(Minv)
print("--------------------")
Mt = numpy.transpose(M)
print(Mt)
print("--------------------")
Mdet=numpy.linalg.det(M)
print(Mdet)
print("--------------------")
#7
print("M1x1: {0} ".format(M[0,0]))
print("M3x3: {0} ".format(M[2,2]))
print("M3x2: {0} ".format(M[2,1]))
w1 = numpy.array( [M[:,2]])
print("trzecia kolumna: {0}".format(w1))
w2 = numpy.array([M[1,:]])
print("drugi wiersz: {0}".format(w2))
#8
coeff = [1,-7,3,43,-28,-60]
print(numpy.roots(coeff))
#9
ciag1 = numpy.arange(1,10,2.5)
print(ciag1)
ciag2 = numpy.linspace(1,10,num=5)
print(ciag2)
#10
def funkcja(x):
    return x**3-3*x
import matplotlib.pyplot as plt
x = numpy.linspace(-1,1)
y = []
for i in x:
    y.append(funkcja(i))
plt.plot(x, y)
plt.title('Wykres 1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('x**3-3*x')
plt.show()

x = numpy.linspace(-5,5)
y = [funkcja(i) for i in x]
plt.plot(x, y)
plt.title('Wykres 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('x**3-3*x')
plt.show()

x = numpy.linspace(0,5)
y = funkcja(x)
plt.plot(x, y)
plt.title('Wykres 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('x**3-3*x')
plt.show()

#11
def cieplo(m,v):
    return m*v**2/2
m1=2500
m=m1*0.001
v1=60
v=v1/3.6
Q=cieplo(m,v)
print("ciepo wydzielone w kilokaloriach: {0}".format(Q*0.0002388458966275))
print("ciepo wydzielone w dzulach: {0}".format(Q))
x=numpy.linspace(200,0)
y=[cieplo(3,i/3.6) for i in x]
plt.plot(x, y)
plt.xlim(200,0)
plt.title('Wykres cieplo, liniowy')
plt.xlabel('V [km/h]')
plt.ylabel('Q [J]')
plt.legend('w')
plt.show()

x=numpy.linspace(200,0)
y=[cieplo(3,i/3.6) for i in x]
plt.semilogy(x, y)
plt.xlim(200,0)
plt.title('Wykres cieplo, logarytmiczny')
plt.xlabel('V [km/h]')
plt.ylabel('Q [J]')
plt.legend('w')
plt.show()
