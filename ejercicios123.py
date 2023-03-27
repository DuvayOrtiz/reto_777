# ejercicio 1
x = 1 
y = 2 #---> definimos las variables
while x == y: 
  print(x, y, sep = ", ")  #--->nunca las variables valdran lo mismo
  x += 2 
  y += 10 
print(x, y, sep = ", ") #---> se imprimen igual ya que nunca entran 

# ejercicio 2

z=0   #--->Definimos
while z>=0:
    z+=1      #--->se ejecuta indefinidamente dado que siempre va a ser mayor
    
# ejercicio 3

o:int=0 #--->variable
while not(65<=o<=90):   #--->Se sigue haciendo siempre y cuando no este en ese rango
    o=int(input("ingresar entero: "))
    print("El entero " + str(o) + " es en el el codigo ASCII " + chr(o))
    
