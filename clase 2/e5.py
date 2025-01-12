#La ley de Coulomb describe matemáticamente la fuerza eléctrica producida entre dos cargas 
k= 8.85e-12
q1=float(input("dime la carga 1: "))
q2=float(input("dime la carga 2: "))
r=float(input("dime el radio: "))
fuerza_electrica= k*(q1*q2)/r**2
print(fuerza_electrica)