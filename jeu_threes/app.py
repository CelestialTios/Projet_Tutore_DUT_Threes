from user_entries import *
from cycle_game import *
from tiles_acces import *
from tiles_moves import *
from play_display import *
from play import *
import sys

def threes():
    """
    Permet de jouer des parties de Threes, de reprendre une partie sauvegardée
    ou sauvegarder une partie en cours.
    Tout ceci de façon répétée.
    """
    choix=get_user_menu()

    while choix !='Q':
        if choix=='N' or choix=='C':        #Lancer une partie
            if choix=='N':                      #Nouvelle partie
                resultat=cycle_play(None)
            else:                               #Partie chargée
                resultat=cycle_play(partie)

            if resultat:
                print('Votre score est de',partie['score'])
                partie=None
                save_game(partie)

        elif choix=='L':
            partie=restore_game()
            print("Votre partie a été chargée")

        elif choix=='S':
            save_game()
            print("Votre partie est chargée")
        choix=get_user_menu()

    sys.exit()                              #Quitter le jeu
