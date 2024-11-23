print("ERES YOOOOOO?")
afirmations = 0

age = int(input("Ingresa tu edad:"))
if age > 17 or age < 17: 
    print("false")
else:
    print("true")
    afirmations += 1
colour = input("Ingresa tu color:")
if colour == "Blanco" or colour == "Negro": 
    print("true")
    afirmations += 1
else:
    print("false")
favserie = input("Ingresa tus dos series favoritas:")
if favserie == "Silo" and favserie == "Snowpiercer": 
    print("true")
    afirmations += 1
else:
    print("false")
favsong = input("Ingresa tu canción favorita:")
if favsong != "Pauper and the queen" or favsong != "El triste": 
    print("true")
    afirmations += 1
else:
    print("false")
favcellphone = input("Ingresa tu marca telefónica favorita:")
if favcellphone == "Samsung" or favcellphone == "Iphone": 
    print("true")
    afirmations += 1
else:
    print("false")
favcinema = input("Ingresa tu cine favorito:")
if favcinema == "Cinepolis": 
    print("true")
    afirmations += 1
else:
    print("false")
school = input("Ingresa tu escuela:")
if school == "UPAEP" or school == "BUAP": 
    print("true")
    afirmations += 1
else:
    print("false")
favgame = input("Ingresa tus dos juegos favoritos:")
if favgame == "Call of Duty: Infinity Warfare" and favgame == "Assassin's Creed 2": 
    print("true")
    afirmations += 1
else:
    print("false")
name = input("Ingresa tu nombre:")
if name == "Javier": 
    print("true")
    afirmations += 1
else:
    print("false")
country = input("Ingresa tu país:")
if country == "México" or country == "Puebla": 
    print("true")
    afirmations += 1
else:
    print("false")


if afirmations == 10:
    print("SI ERES YO!!!!!😰")
else:
    print("No eres yo jaja😉")