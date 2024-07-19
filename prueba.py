import random
print("hello world")
caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
contraseña_generada = ''
longitud = int(input("introduce la longitud de la contraseña"))
longitud_caracteres = (caracteres)
for i in range(longitud):
    contraseña = random.choice(longitud_caracteres)
    contraseña_generada += contraseña
print("la contraseña es:", contraseña_generada)
while True:
    iniciar_sesion = input("ingrese la contraseña")
    if iniciar_sesion == contraseña_generada:
        print("contraseña aceptada")
        break
    else:
        print("contraseña incorrecta, vuelva a intentarlo")
    