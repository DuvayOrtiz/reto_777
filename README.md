# Reto_777
# Tareita :D 

## *Ejercicios* :art:
- Diseñe un algoritmo que involucre un ciclo y que nunca ingrese al ciclo.
- Diseñe un algoritmo que involucre un ciclo y que se ejecute indefinidamente.
- Diseñe un algoritmo que pida un valor entero, y que siga leyendo valores enteros mientras que alguno de esos valores no represente el código ASCII de una letra mayúscula en el abc del inglés.
### Num1 :bug:
```ruby
#Ejercicio 1
x = 1 
y = 2 #---> definimos las variables
while x == y: 
  print(x, y, sep = ", ")  #--->nunca las variables valdran lo mismo
  x += 2 
  y += 10 
print(x, y, sep = ", ") #---> se imprimen igual ya que nunca entran 
```
### Num2 :pencil:
```ruby
# ejercicio 2

z=0   #--->Definimos
while z>=0:
    z+=1      #--->se ejecuta indefinidamente dado que siempre va a ser mayor
```
### Num3 :pear:
```ruby
# ejercicio 3

o:int=0 #--->variable
while not(65<=o<=90):   #--->Se sigue haciendo siempre y cuando no este en ese rango
    o=int(input("ingresar entero: "))
    print("El entero " + str(o) + " es en el el codigo ASCII " + chr(o))
```
## *Punto 1* :zap:
- Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```ruby
#num1
x=1 #----> Declaramos x y 
y=x**2 
while x<=100:   #----> Se llega hasta 100
    print(x,y, sep=",") #----> Se imprimen los resultados 
    x+=1
    y=x**2   #----> se aumentan hasta 100
print("listo")
```
![mermaid-diagram-2023-03-26-215616](https://user-images.githubusercontent.com/124726079/228079968-46338acb-075c-4ec7-801b-b8acb20192fa.png)

## *Punto 2* :fire:
- Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```ruby
#num2
x=1
y=2 #----> Asignamos desde el primer impar y par 
while x<=1000: 
    print(x) #----> se imprimen los x y
    x+=2 #---->Se incrementan los numeros en dos hasta el 1000
while y<=1000: 
    print(y) 
    y+=2 
print("listo")
```
![mermaid-diagram-2023-03-26-220232](https://user-images.githubusercontent.com/124726079/228080144-e45e73c7-6de2-4163-806d-04ccc4521863.png)

## *Punto 3* :sparkles:
- Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```ruby
#num3
x=int(input("ingresar numero mayor igual que 2: ")) #Pedir una variable
if x%2!=0: #En caso de que sea impar lo ponemos en su par inmediato por izquierda
    x-=1 
while x>=2 and x%2==0:
    print(x) # El numero es par entonces solo se imprime y se disminuye de a dos
    x-=2
print("listo")
```
![mermaid-diagram-2023-03-26-222549](https://user-images.githubusercontent.com/124726079/228080185-ff2b0f77-f026-4be7-9f64-7867c66e55ab.png)

## *Punto 4* :rocket:
- En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
```ruby
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
```
## *Punto 5* :carrot:
- Imprimir el factorial de un número natural n dado.
```ruby
#num5
def fact(x): # defino una funcion
    if x==0 or x==1:
        return 1   # en caso de que sea 1 o 0 su factorial es 1
    elif x<0:
        return("no definido") # los negativos no estan definidos
    else:
        b=x*fact(x-1)  # se multiplica el numero por sus antecendentes hasta la unidad
        return b
x=int(input("ingresar numero entero. "))  #se pide la variable
print("el factorial de ", x, "es", fact(x)) #se muestra la respuesta
```
## *Punto 6* :orange:
- Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
```ruby
#num6
def pro(min,max): 
    return (min+max)//2 # Se define una funcion que sea el promedio de dos variables
min = 0
max = 100 # el minimo es 0 y el maximo 100 ya que este es el rango del ejercicio
def adiv(x,min,max):
    if x==1:
        max = pro(min,max) #En caso de que sea menor se redefine el max 
        print(pro(min,max))
        x=int(input("¿El anterior es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor"))
        return adiv(x,min,max)
    if x==2:
        max = pro(min,max) #En caso de que sea mayor se redefine el min
        print(pro(min,max))
        x=int(input("¿El anterior es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor"))
        return adiv(x,min,max)
    if x==0:
        w ="se lo adivine toche Uwu" # ya hemos adivinado el numero
        return w
    
x=int(input("¿50 es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor")) # se empieza en el promedio de 0 100 Asi es mas "logico"
y = adiv(x,min,max)
print(y)
```
## *Punto 7* :apple:
- Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
```ruby
#num7
x = 50 
def div(x): # definimos una funcion
    s=[] #hcaemos un conjunto vacio
    for i in range (1,(x//2)+1): #se va hasta la mitad de x ya qeu hasta ahi van los divisores
            if x%i==0:
                s.append(i) # se buscan divisores y se unen 
    s.append(x) # se pone la x ya que un numero es divisible por si mismo
    return s
for i in range(1,51): #se hace para todos enteros hasta 50
    print(i,":",div(i)) #se muestran en pantalla
```
## *Punto 8* :green_apple:
- Implementar el algoritmo que muestre los números primos del 1 al 100.
```ruby
#num8
def criba(n): #se define la funcion 
    primos = [True] * (n+1) #se definen todos los valores como verdaderos
    primos[0], primos[1] = False, False #se quita el 0 y el 1
    for i in range(2, int(n**0.5)+1): # se hace un rango hasta la raiz del numero
        if primos[i]:
            for j in range(i**2,n+1,i): #se exluyen los cuadrados 
                primos[j] = False
    return [i for i in range(n+1) if primos[i]] #se devuelven los trues
n = 100 #asigno n
x = criba(n)
print(x) # imprimo :D
```

















































