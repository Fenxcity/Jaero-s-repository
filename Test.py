user = "Jaero"
password = "Jaero337*"

user = input("Ingresa tu usuario")
password = input("Ingresa tu contraseña")
if user == "Jaero":
    print("Usuario correcto")
    if password == "Jaero337*":
        print("Contraseña aceptada")
    else: 
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")