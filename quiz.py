# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input

a = float(input("Ingrese el valor del lado a: "))

b = float(input("Ingrese el valor del lado b: "))

c = float(input("Ingrese el valor del lado C: "))

# processing
if a + b > c:
   Resultado = ("Los numeros si forman un triangulo")
   if a + c > b:
     Resultado = ("Los numeros si forman un triangulo")
     if b + c > a:
        Resultado = ("Los numeros si forman un triangulo")
else:
    Resultado= ("Los numero no forman un triangulo")

# output
print("Los lados", a, ",", b, "y", c, Resultado)

