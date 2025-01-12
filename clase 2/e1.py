#disminuir la variable de lluvia en un 10% para tener en cuenta el agua de lluvia que circula libremente sobre la superficie de un terreno.

#Agregue la variable de lluvia a la variable volumen_reservorio.
volumen_reservorio =  float(4.445e8)
lluvia= float(5e6)
vol_1=  volumen_reservorio/10 
volumen_reservorio= volumen_reservorio - vol_1
print(volumen_reservorio)
#Agregue la variable de lluvia a la variable volumen_reservorio.
volumen_reservorio= volumen_reservorio + lluvia
print(volumen_reservorio)
#Aumentar volumen_reservorio en un 5% para tener en cuenta las aguas pluviales que fluyen en el embalse en los días posteriores a la tormenta.
vol_1= volumen_reservorio%0.05
volumen_reservorio= volumen_reservorio-vol_1
print(volumen_reservorio)
#Disminuir volumen_reservorio en un 2% para tener en cuenta la evaporación
vol_2= volumen_reservorio%0.02
volumen_reservorio= volumen_reservorio -vol_2
print(volumen_reservorio)
#Resta 2.5e5 metros cúbicos de volumen_reservorio para tener en cuenta el agua que se canaliza a regiones áridas.
volumen_reservorio= volumen_reservorio-2.5e5
print(volumen_reservorio)