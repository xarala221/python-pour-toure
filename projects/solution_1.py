transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]

# Tache 1
# solution 1 -> avec la fonction sum()
# transaction_sum = sum(transaction_list)
# print(transaction_sum)
# solution 2 -> Ecrire une boucle
# transaction_sum = 0
# for transaction in transaction_list:
#     transaction_sum += transaction

# print(transaction_sum)
# Tache 2
# element_5 = transaction_list[4]
# print(element_5)

# Tache 3
# ordonner
transaction_list.sort()
# print(transaction_list)

# Tache 4
# l'element le plus bpetit de la liste
element_plus_petit = min(transaction_list)
# print(element_plus_petit)

# Tache 5
# dernier lement
dernier_element = transaction_list[-1]
# print(dernier_element)

# Tache 6
non_dupliques = set(transaction_list)
# set_to_list = list(non_dupliques)
# print(non_dupliques)
# declares une liste vide
# faire une boucle sur la liste des transactions
# verfier si l'element retourner n'est pas dans ta nouvelle liste
# si oui > ajoute cet element dans ta nouvelle liste
# afficher ta nouvelle liste

nouvelle_liste = []
for transaction in transaction_list:
    if transaction not in nouvelle_liste:
        nouvelle_liste.append(transaction)
# print(nouvelle_liste)


# Tache 7
# supprimer le dernier element
# transaction_list.pop()
# print(transaction_list)
# Tached 8
# copier
# liste_copier = transaction_list.copy()
# liste_copier = transaction_list[:]
# print(liste_copier)

# Tache 9
# la moyenne
moyenne = sum(transaction_list)/len(transaction_list)
# print(moyenne)

# Tache 10
# ajout +1
ajout = []
for transaction in transaction_list:
    transaction += 1
    ajout.append(transaction)

# print(ajout)

# Tache 11
chiffre_paires = []
for transaction in transaction_list:
    if transaction % 2 == 0:
        chiffre_paires.append(transaction)

print(chiffre_paires)
