#num1
x=1 #----> Declaramos x y 
y=x**2 
while x<=100:   #----> Se llega hasta 100
    print(x,y, sep=",") #----> Se imprimen los resultados 
    x+=1
    y=x**2   #----> se aumentan hasta 100
print("listo")