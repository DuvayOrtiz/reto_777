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
    
x=int(input("¿50 es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor")) # se empieza en el promedio de 0 100 Ai¿si es mas "logico"
y = adiv(x,min,max)
print(y)