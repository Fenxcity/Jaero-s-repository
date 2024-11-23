print("Escribe las mejores 3 reseñas sobre 'Fausto': ")
first = input("Primera reseña:")
second = input("Segunda reseña:")
third = input("Tercera reseña:")

text1 = len(first)
text2 = len(second)
text3 = len(third)


print("La longitud de tu primera reseña es de:", text1, "; de la segunda es de:", text2, "; y de la tercera es de:", text3)

if text2 < text1 > text3:
    print("La primera reseña es la mayor")
elif text1 < text2 > text3:
    print("La segunda reseña es la mayor")
elif text1 < text3 > text2:
    print("La tercera reseña es la mayor")
else:
    print("Todas tus reseñas tienen la misma longitud")
