#!/usr/bin/python
# -*- coding: utf8 -*-
a=input("Ingrese un numero mayor o igual a cero : ")
def sumatoria(n):

	if n==1:
		return 1
	if n==0:
		print 0
	return n+ sumatoria(n-1)
print sumatoria(a)
