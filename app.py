# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación) finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

# for x in range (3):
#     float(input("ingrese nota:"))
import os
os.system("cls")

usuario = input("ingrese usuario:\n")
passwd = input("ingrese su clave:\n")
if usuario == "pedro" and passwd == "1234":
    print("bienvenido user1")
    nota1user1 = float(input("ingrese nota:\n"))
    nota2user1 = float(input("ingrese nota:\n"))
    nota3user1 = float(input("ingrese nota:\n"))
    promedio1 = (nota1user1 + nota2user1 + nota3user1)/3
    if promedio1 < 4:
        print("reprobado")
    elif promedio1 >= 4 and promedio1 <= 7:
        print("aprovado")
    else:
        print("datos ingresados no corresponden")

elif usuario == "angel" and passwd == "a4s1":
    print("bienvenido user2")
    nota1user2 = float(input("ingrese nota:\n"))
    nota2user2 = float(input("ingrese nota:\n"))
    nota3user2 = float(input("ingrese nota:\n"))
    promedio2 = (nota1user2 + nota2user2 + nota3user2)/3
    if promedio2 < 4:
        print("reprobado")
    elif promedio2 >= 4 and promedio2 <= 7:
        print("aprovado")
    else:
        print("datos ingresados no corresponden")

else:
    print("usario o clave incorrectas")
