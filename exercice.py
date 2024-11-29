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
    print("Choisissez une liste pour supprimer un todo")
    print("1 - A faire ", afaire)
    print("2 - Fait ", fait)
    print("3 - A Fair ", afair)
    choice = input()
    match choice:
        case "1":
            print("lequel voulez vous supprimez ?")
            print(afaire)
            choice = input()
            print("Êtes vous sûr ?")
            print("1 - Oui")
            print("2 - Non")
            resp = input()
            match resp:
                case '1':
                    afaire.remove(choice)
                case '2':
                    pass
            print("A faire ", afaire)
            print("Fait ", fait)
            print("A fair ", afair)
        case '2':
            print("lequel voulez vous supprimez ?")
            print(fait)
            choice = input()
            print("Êtes vous sûr ?")
            print("1 - Oui")
            print("2 - Non")
            resp = input()
            match resp:
                case '1':
                    fait.remove(choice)
                case '2':
                    pass
            print("A faire ", afaire)
            print("Fait ", fait)
            print("A fair ", afair)
        case '3':
            print("lequel voulez vous supprimez ?")
            print(afair)
            choice = input()
            print("Êtes vous sûr ?")
            print("1 - Oui")
            print("2 - Non")
            resp = input()
            match resp:
                case '1':
                    afair.remove(choice)
                case '2':
                    pass
            print("A faire ", afaire)
            print("Fait ", fait)
            print("A fair ", afair)
            
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