print("Bienvenido a 'Mejores peliculas del año'")

movies = "La sustancia Robot salvaje Terrifier"

movie1 = input("Ingresa tu primera película favorita de este año: ")
movie2 = input("Ingresa tu segunda película favorita de este año: ")
movie3 = input("Ingresa tu tercera película favorita de este año: ")

result1 = movies.find(movie1)
result2 = movies.find(movie2)
result3 = movies.find(movie3)

results = result1, result2, result3
print("De acuerdo a tus resultados y los charts de este año el top es: ", results)