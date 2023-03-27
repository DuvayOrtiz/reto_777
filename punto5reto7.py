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