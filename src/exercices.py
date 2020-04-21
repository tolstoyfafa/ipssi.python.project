#!/usr/bin/env python3
from math import *

def ex_1(n):
    a = (n+1)**3
    print("puissance 3 =>  a:",n,a)
    b = sqrt(a)
    print("racine => b: ", b)
    c = a/n
    print("quotien => c: ", c)
    d = a%n
    print("reste de division => d: ", d)
    e = (a + 5)/(n-1)
    print("reste de division  (a + 5)/(n-1) => e: ", d)
    f = a * c * d
    print("produit de tout   => f: ", f)
def ex_2(pur_price, tva):
    res = pur_price*(1+tva/100)
    return res


def ex_3():
    val = int(input("Hello, please enter the year:"))
    if(val%4==0 and val%100!=0 or val%400==0):
        print("bisextile")
    else:
        print("not bisxtile")

def ex_4():
    n = int(input("Chosse 0 for Fahrenhit and 1 for Celsius: "))
    if n==0:
        print("You choose to convert in Celsius")
        v = int(input("Enter your temperature :  "))
        t = (v - 32) * 5 / 9
        print("Temp in Celsius is", t)
        return t
    elif n==1:
        print("You choose to convert to Fahrenhite")
        v = int(input("Enter your temperature :  "))
        t = v * 9 / 5 + 32
        print("Temp in Fahrenheit is", t)
        return t
    else:
        print("Maybe wrong manip ?! :) ")
        return None
def ex_5():
    text = str(input("Enter a text and I will compute voyeles :"))
    compteur = 0
    voy = "aeiouyAEIOUY"
    for i in text :
        if i in voy :
            compteur += 1
    print("you have : ", compteur)
    return 

""" def ex_3(n):
def ex_4(n):
def ex_5(n): """
ex_1(5)
x = ex_2(20, 17)
print("HT:", x)
ex_3()
x = ex_4()
print("Temp:", x)
ex_5()