# Variables
# var
# const
# let

# String
# Int

# mon_nom = '25'  # String -> Chaine de
# age = 25  # int
# solde = 100.000  # float Decimal

# age_float = float(age)
# mon_nom_int = int(mon_nom)

# print("Avent ", type(mon_nom))
# print("Apres ", type(mon_nom_int))

# produit = "Savon"
# quantite_en_stock = 20
# prix = 25.10
# quantite_achete = 5

# "Vous avez achete 5 savons, prix global : prix"
# resultat = f"Vous avez achete {quantite_achete} le prix totsl est : {quantite_achete*prix}"
# print(resultat)
# print("Vous avez achete ", quantite_achete,
#       "le prix global est : ", quantite_achete*prix)

# produit_1 = "Savon"
# produit_2 = "Bic"
# quantite_en_stock_1 = 20
# quantite_en_stock_2 = 5
# prix_1 = 25.10
# prix_2 = 100
# quantite_achete_1 = 3
# quantite_achete_2 = 2
# reduction = 50
# payer_en_tranch = 2
# total_panier = prix_1*quantite_achete_1 + prix_2*quantite_achete_2
# print("Panier total ", total_panier)
# total_a_payer = total_panier - reduction
# print("total net ", total_a_payer/payer_en_tranch)


# Structures de donnees

# Listes
# liste vide / tableau vide
produit_en_stcok = []
# produit_en_stcok = ["Savon", "Bic", "Ommo", "Jus d'orange", 21, 1.4, False]
# ajouter un element
# produit_en_stcok.append("Savon")
# produit_en_stcok = ["Savon", "Bic", "Ommo", "Jus d'orange", "a"]
produit_en_stcok[0] = "Cahier"
# print(produit_en_stcok)
# long- size
longueur = len(produit_en_stcok)
# supprimer un element specific
# produit_en_stcok.remove("Savon")
# supprimer le dernier element
# produit_en_stcok.pop()
# renverser les valeurs d'une liste
# produit_en_stcok.reverse()
# compter la presence d'un elemnts
compter = produit_en_stcok.count("a")
# Trouver l'indexe
# index_ommo = produit_en_stcok.index("Ommo")
# print(index_ommo)
# tuple
# declarer un tuple
mon_tuple = ()
# database_name = "gestock"
# database_user = "root"
database_name, database_user, server_name = "gestsock", "root", "localhost"
mon_bd = (database_name, database_user)
# mon_bd[0] = "gesboutique"

# print(mon_bd[0])


# dictionnaires
mon_dict = {}
# mon_dict = dict()
# ajouter un element
# mon_dict["nom"] = "Diop"
mon_dict = {"nom": "Diop", "prenom": "ousseynou", "age": 24}
mon_dict_en_fr = {"go": "Aller"}
print(mon_dict_en_fr.get("go"))

# recuperer une valeur
# recuperer_nom = mon_dict.get("diop", "Mbacke")
print(mon_dict)
