# Liste de commandes et articles commandés
commandes = [
    [
        "1",
        ["2001/10/C", "1001/10/C", "4001/10/C", "1001/10/C", "4001/10/C", "1001/10/C"],
        ["55.3", "60.333", "1020", "2304.34", "434", "999.999999"],
    ],
    ["2", ["1001/12/B", "1001/09/W", "1001/10/C"], ["10.0000", "140.122", "200.3456"]],
    [
        "3",
        ["5005/18/C", "1493/12/C", "4004/10/C", "1001/14/C"],
        ["100.1", "140.122", "200.3456", "2129.86554"],
    ],
]


# Fonctionnalités
# Tous les prix doivent être formatés à 2 chiffres après la virgule
# ------------------------------
# 1 - Afficher le numéro de chaque commande et le nombre total d'articles commandés.
def commandes_numbers():
    for commande in commandes:
        num_commande = commande[0]
        articles = commande[1]
        number_articles = len(articles)
        print(f"La commande numéro : {num_commande} possède {number_articles} articles commandés.")

print("fonction commandes_numbers():")
commandes_numbers()
print("\n")

# ------------------------------
# 2 - Afficher la liste de tous les articles commandés, sans doublons.

print("fonction commandes_sans_doublon():")
def commandes_sans_doublon():
    articles_commandes = list()

    for commande in commandes:
        for article in commande[1]:
            if article not in articles_commandes:
                articles_commandes.append(article)

    for article in articles_commandes:
        print(f"L'article {article} a été commandé sans doublon")

commandes_sans_doublon()
print("\n")
# -----------------------------
# Via set (plus rapide)
print("fonction commandes_sans_doublon_set():")
def commandes_sans_doublon_set():
    articles_commandes = set()

    for commande in commandes:
        articles_commandes.update(commande[1])

    for article in articles_commandes:
        print(f"L'article {article} a été commandé sans doublon")

commandes_sans_doublon_set()
print("\n")
# ------------------------------
# 3 - Créer une fonction appelée recherche_commande_par_article qui prend en entrée un identifiant d'article
# et renvoie la liste des numéros de commande dans lesquels cet article a été commandé.
# Si l'article n'a pas été commandé,la fonction doit renvoyer une liste vide.

print("fonction recherche_commande_par_article(id_article):")
def recherche_commande_par_article(id_article):
    liste_commande = list()

    for commande in commandes:
        if id_article in commande[1]:
            liste_commande.append(commande[0])

    return liste_commande

recherche_commande_par_article('1001/50/C')
print("\n")
# ------------------------------
# 4 - Créer une fonction appelée ajouter_commande qui prend en entrée un numéro de commande et
# une liste d'articles, puis ajoute cette commande à la liste des commandes existantes. Assurez-vous de vérifier si la commande existe déjà.

print("fonction ajouter_commande(num_commande, liste_articles):")
# ajout de l'entrée prix_article afin qu'une commande ait à la fois les articles commandés ainsi que leur prix

def ajouter_commande(num_commande, liste_articles, prix_articles):
    if len(liste_articles) == 0:
        print(f"La commande {num_commande} ne contient pas d'articles")
        return

    if len(prix_articles) == 0:
        print(f"La commande {num_commande} ne contient pas de prix pour les articles")
        return

    for commande in commandes:
        if num_commande == commande[0]:
            print(f"La commande {num_commande} existe déjà !")
            return

    if len(liste_articles) != len(prix_articles):
        print("Le nombre de prix d'articles doit correspondre au nombres d'articles")
        return

    new_commande = [num_commande, liste_articles, prix_articles]

    commandes.append(new_commande)
    return commandes

ajouter_commande('6', ["5005/18/C", "1493/12/C", "4004/10/C", "1001/14/C"], ["100.1", "140.122", "2129.86554"])
print("\n")

# ------------------------------
# 5 - Créer une fonction appelée supprimer_commande qui prend
# en entrée un numéro de commande et supprime cette commande de la liste des commandes existantes,
# si elle existe.

print("fonction supprimer_commande(num_commande):")

def supprimer_commande(num_commande):
    for commande in commandes:
        if num_commande == commande[0]:
            commandes.remove(commande)
            break
    print(commandes)

supprimer_commande('2')
supprimer_commande('6')
supprimer_commande('1')
print("\n")

# ------------------------------
# 6 - Demander à l'utilisateur d'entrer un numéro de commande,
# puis afficher les articles de cette commande s'ils existent ainsi que le prix total de la commande.
# Sinon, afficher un message indiquant que la commande n'a pas été trouvée.

def rechercher_comande(num_commande):
    for commande in commandes:
        if num_commande == commande[0]:
            return commande[1], commande[2]
    return None, None

def somme_prix(liste_prix):
    somme = sum(float(prix) for prix in liste_prix)
    return "{:.2f}".format(somme)

num_commande_user = input("Entrez un numéro de commande : ")

articles, prix_articles = rechercher_comande(num_commande_user)

if articles != None and prix_articles != None:
    somme = somme_prix(prix_articles)
    print(f"La commande numéro {num_commande_user} possèdant les articles : {articles} pour la somme de {somme} €")
else:
    print(f"La commande numéro {num_commande_user} n'as pas été trouvée")

print("\n")
# ------------------------------
# 7 - Demander à l'utilisateur d'entrer un numéro de commande,
# afficher le nombre d'articles par commande ainsi que le prix moyen du panier.

def prix_moyen(liste_prix):
    somme = sum(float(prix) for prix in liste_prix)
    moyenne = somme / len(liste_prix)
    return "{:.2f}".format(moyenne)

num_commande_user = input("Entrez un numéro de commande : ")

articles, prix_articles = rechercher_comande(num_commande_user)

if articles != None and prix_articles != None:
    nombre_articles = len(articles)
    moyenne = prix_moyen(prix_articles)
    print(f"La commande numéro {num_commande_user} possède {nombre_articles} articles pour un prix moyen de {moyenne} €")
else:
    print(f"La commande numéro {num_commande_user} n'as pas été trouvée")