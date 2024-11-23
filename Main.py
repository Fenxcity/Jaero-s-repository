print("Hola mundo")
print("Bienvenido a el test de peliculas")
movie = input("Ingresa la pelicula que viste esta semana")
calification = int(input("Ingresa tu calificación"))

moviemor = input("Ingresa tu pelicula favorita del Festival Internacional del Cine de Morelia")
calificatiomor = int(input("Ingresa tu calificación del FICM"))

finalcalification = (calification+calificatiomor)/2

print("Tu promedio de calificaciones de: ", movie, "y de", moviemor, "es",  finalcalification)