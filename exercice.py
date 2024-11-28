afaire = []
afair = []
fait = []

def lister_todos():
    print("A faire ", afaire)
    print("Fait ", fait)
    print("A fair ", afair)

def creer_todo():
    print('Nom de la tache')
    afaire.append(input())

def modifier_statut_todo():
    print("lequel voulez vous modifiez ?")
    print("A faire ", afaire)
    print("Fait ", fait)
    choice = input()
    if choice in afaire :
        fait.append(choice)
        afaire.remove(choice)
        print("A faire ", afaire)
        print("Fait ", fait)
        print("A fair ", afair)
    elif choice in fait :
        print("Error tu ne peux pas faire ça !")
        afair.append(choice)
        fait.remove(choice)
        print("A faire ", afaire)
        print("Fait ", fait)
        print("A fair ", afair)
    else :
        print("Ce todo n'existe pas !")
    
def supprimer_todo():
    pass

choix = ''
while choix != 'q':
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')