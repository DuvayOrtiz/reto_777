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