#!/usr/bin/python
# -*- coding: utf8 -*-
a=1 # Definicion de variable global
b=0
d=0
c=eval(input("Ingrese un número : "))
while d<c:
		b=b+1
		a=a*b
		d=d+1

print ("El factorial de" ,c, " es : ",a)

