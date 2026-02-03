def compter_voyelles(phrase):
    voyelles = "aeiouy"
    return sum(1 for c in phrase if c in voyelles)

phrase = input("Entrez une phrase : ")

phrase_min = phrase.lower()

mots = phrase_min.split()

nb_mots = len(mots)
mot_plus_long = max(mots, key=len)
nb_voyelles = compter_voyelles(phrase_min)

nouvelle_phrase = []
for mot in mots:
    if len(mot) % 2 == 0:
        nouvelle_phrase.append(mot.upper())
    else:
        nouvelle_phrase.append(mot)

print("Nombre total de mots :", nb_mots)
print("Mot le plus long :", mot_plus_long)
print("Nombre total de voyelles :", nb_voyelles)
print("Nouvelle phrase :", " ".join(nouvelle_phrase))