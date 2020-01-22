import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')

def get_user_move():
    """
    Permet au joueur de jouer en effectuant une action selon les règles du jeu Threes
    Retourne l'action choisie.
    """
    print("Quelle est votre action ?")
    print("\t -'h' pour Haut")
    print("\t -'b' pour Bas")
    print("\t -'g' pour Gauche")
    print("\t -'d' pour Droite")
    print("\t -'m' pour retourner au Menu principal")
    value=str(input())
    action=value.lower()
    while action !='h' and action !='b' and action !='g' and action !='d' and action !='m': #boucle obligeant les joueurs à effectuer une action faisable
        value=str(input())
        action=value.lower()
    return action

def get_user_menu():
    """
    Demande au joueur quelle action il veut effectuer.   
    Retourne l'action choisie.
    """
    print("Que souhaitez vous faire ?")
    print("\t -'N' pour créer une nouvelle partie")
    print("\t -'L' pour Charger la partie")
    print("\t -'S' pour Sauvegarder la partie")
    print("\t -'C' pour Reprendre une partie")
    print("\t -'Q' pour terminer le jeu")
    value=str(input())
    action=value.upper()
    while action !='N' and action !='L' and action !='S' and action !='C' and action !='Q': #boucle obligeant les joueurs à effectuer une action faisable
        value=str(input())
        action=value.upper()
    return action
