from ejerci import*
def promMul(numeritos):
    return (n1*n2*n3*n4*n5)**0.5
n1 = float(input("Ingresar número 1: "))
n2 = float(input("Ingresar número 2: "))
n3 = float(input("Ingresar número 3: "))
n4 = float(input("Ingresar número 4: "))
n5 = float(input("Ingresar número 5: "))
numeritos = [n1, n2, n3 , n4 , n5]
print("el promedio aritmetico es  ", prom(numeritos))
print("el promedio multiplicativo es ", promMul(numeritos))
print("la mediana es ", mediana(numeritos))
print("de menor a mayor son ", menMay(numeritos))
print("de menor a mayor son ", mayMen(numeritos))
print("el mayor elevado al menor es ", pot(numeritos))
print("la raiz cubica del menor es ", raiz(numeritos))