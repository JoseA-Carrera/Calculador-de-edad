'''
*Ejercicio 1*
crear un calculador que cuente los dias, meses, y años
para determinar la edad del usuario
'''

from datetime import date

print("****calculador de edad****")

a = int(input("\ningrese su año de nacimiento: "))
b = int(input("ingrese su mes de nacimiento: "))
c = int(input("ingrese su dia de nacimiento: "))

def calculo_de_edad(fecha_nacimiento):
    hoy = date.today()
    result = hoy.year - fecha_nacimiento.year
    result -= ((hoy.month, hoy.day)<(fecha_nacimiento.month, fecha_nacimiento.day))
    return result

nacio = date(a, b, c)
edad = calculo_de_edad(nacio)

if edad>0 and edad<100:
    print(f"\nEl usuario tiene {edad} años de edad")
    if edad>18:
        print("Es mayor de edad")
    elif edad<18:
        print("Es menor de edad")
else:
    print("\ntenes que agregar el nuemro del mes ejemplo: enero es 1")
