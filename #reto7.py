#reto7
x=1
y=x**2
while x<=100:
    print(x,y, sep=",")
    x+=1
    y=x**2
print("listo")

#num2
x=1
y=2
while x<=1000:
    print(x)
    x+=2
while y<=1000:
    print(y)
    y+=2
print("listo")
#num3
x=int(input("ingresar numero mayor igual que 2: "))
if x%2!=0:
    x-=1
while x>=2 and x%2==0:
    print(x)
    x-=2
print("listo")
#num4
a = 25e+6
b = 18.9e+6
c = 2022
while b < a: 
  print(c,a,b, sep = ", ") 
  a=a+(a*0.002)
  b=b+(b*0.003)
  c+=1
print("este año.") 
print(c,a,b, sep = ", ")
#num5
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        b=x*fact(x-1)
        return b
x=int(input("ingresar numero entero. "))  
if x<0:
    print("no definido")
else:
    print("el factorial de ", x, "es", fact(x))
#num6
def pro(min,max):
    return (min+max)//2
min = 0
max = 100
def adiv(x,min,max):
    if x==1:
        max = pro(min,max)
        print(pro(min,max))
        x=int(input("¿El anterior es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor"))
        return adiv(x,min,max)
    if x==2:
        min = pro(min,max)
        print(pro(min,max))
        x=int(input("¿El anterior es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor"))
        return adiv(x,min,max)
    if x==0:
        w ="se lo adivine toche Uwu"
        return w
    
x=int(input("¿50 es el número que pensaste?\n(0)=Sí\n(1)=Es menor\n(2)=Es mayor"))
y = adiv(x,min,max)
print(y)
#num7
x = 50
def div(x):
    s=[]
    for i in range (1,(x//2)+1):
            if x%i==0:
                s.append(i)
    s.append(x)
    return s
for i in range(1,51):
    print(i,":",div(i))
#num8
def criba(n):
    primos = [True] * (n+1)
    primos[0], primos[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primos[i]:
            for j in range(i**2,n+1,i):
                primos[j] = False
    return [i for i in range(n+1) if primos[i]]
n = 100
x = criba(n)
print(x)
    
    