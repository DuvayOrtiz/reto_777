#num3
x=int(input("ingresar numero mayor igual que 2: ")) #Pedir una variable
if x%2!=0: #En caso de que sea impar lo ponemos en su par inmediato por izquierda
    x-=1 
while x>=2 and x%2==0:
    print(x) # El numero es par entonces solo se imprime y se disminuye de a dos
    x-=2
print("listo")