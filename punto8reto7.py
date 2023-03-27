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
    