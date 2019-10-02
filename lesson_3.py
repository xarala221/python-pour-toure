# syntaxe
# def nom_de_la_fonctin():
#     print()


# def afficher_nom(nom="Tout le monde"):
#     message = "Bonsoir "+nom
#     return message


# print(afficher_nom("Samb"))


# def age_dune_personne(age=90):
#     return age


# print(age_dune_personne())

def ma_fonction(**var):
    return var["prenom"]


print(ma_fonction(prenom="Makhtar"))
