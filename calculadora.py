def suma(a,b):
    return (a+b)
def resta(a,b):
    return (a-b)
def multiplicacion(a,b):
    return (a*b)
def division(a,b):
    return (a/b)
print ("Favor ingresar operacion a realizar")
print("1 - SUMA")
print("2 - RESTA")
print("3 - MULTIPLICACION")
print("4 - DIVISION")
operacion = input("\n")
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
if (operacion=="1"):
 print("El resultado es : ", suma(a,b))
elif (operacion=="2"):
 print("El resultado es : ", resta(a,b))
elif (operacion=="3"):
 print("El resultado es : ", multiplicacion(a,b))
elif (operacion=="4"):
 print("El resultado es : ", division(a,b))
else:
 print("Ingrese una operacion valida")
