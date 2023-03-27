#num4
a = 25e+6
b = 18.9e+6
c = 2022 #Se asignan los valores de las variables
while b < a: #Mientras b sea menor que a se ejecuta
  print(c,a,b, sep = ", ") 
  a=a+(a*0.02) 
  b=b+(b*0.03)
  c+=1 # Se aumentan los años y el porcentaje de aumento anual
print("este año.") 
print(c,a,b, sep = ", ") #se imprime el año en el que se sobrepasa la poblacion