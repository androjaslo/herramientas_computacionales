#!/usr/bin/python
# -*- coding: utf8 -*-
a=input("Ingrese un numero mayor o igual a cero para la base : ") 
b=input("Ingrese un numero mayor o igual a cero para la potencia : ") 

def potencia(x,n):

	if n==0:
		return 1

	return x*potencia(x,n-1)
print ('La potencia de ', b ,'es igual a ', potencia(a,b))
