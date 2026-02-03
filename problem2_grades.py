students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Amy", 13),
    ("Ibrahima", 7)
]

def moyenne(notes):
    return sum(notes) / len(notes)

print("Liste des étudiants et leurs notes :")
for nom, note in students:
    print(f"{nom} : {note}")

notes = [note for _, note in students]
print("Moyenne de la classe :", moyenne(notes))
print("Note maximale :", max(notes))
print("Note minimale :", min(notes))

admis = [nom for nom, note in students if note >= 10]
ajournes = [nom for nom, note in students if note < 10]

print("Étudiants admis :", admis)
print("Étudiants ajournés :", ajournes)

admis_trie = sorted(admis)
print("Étudiants admis triés :", admis_trie)