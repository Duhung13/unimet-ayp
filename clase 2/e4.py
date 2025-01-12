#Considere un triángulo de lados a, b y c. 
# Utilizando la formula de Herón el área de triangulo viene dada por la siguiente ecuación:
from math import sqrt

a=float(input( "dime un numero a:"))
b=float(input("dime un numero b: "))
c= float(input("dime un numero c: "))
s= (a+b+c)/2
area=sqrt((s*(s-a)*(s-b)*(s-c)))
print(area)

