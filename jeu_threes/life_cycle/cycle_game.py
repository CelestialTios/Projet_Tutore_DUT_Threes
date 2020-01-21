import json
import os

from user_entries import *
from tiles_acces import *
from tiles_moves import *
from play_display import *
from play import *


def save_game(partie):
    file = open("game_saved.json", "w")
    file.write(json.dumps(partie))
    file.close()

def restore_game():
    if os.path.exists("game_saved.json"):
        print('True')
        file = open("game_saved.json","r")
        partie=file.read()
    else:
        print('False')
        partie=create_new_play()
    return partie


def cycle_play(partie):
    """
    Permet de jouer une partie de Threes
    L'utilisateur jouera jusqu'à perdre ou jusqu'à ce qu'il demande le menu

    Retourne True si la partie est terminée, retourne False si le joueur demande le menu

    @param-partie:dictionnaire contenant le plateau de jeu, le score et la prochaine tuile
    """

    #Vérifie s'il existe une partie ou en crée une nouvelle
    if partie is None:
        partie=create_new_play()


    while not(is_game_over(partie['plateau'])):
    #   -1 Afficher plateau
        affichage_moyen(partie['plateau'])
        print(" ")


    #   -2 Afficher prochaine tuile
        print("La prochaine tuile est",partie['next_tile'][0]['val'])
        print(" ")


    #   -3 Mouvement du joueur
        action=get_user_move()

        if action=='m':
            return False

        else:
            play_move(partie['plateau'],action)
            put_next_tiles(partie['plateau'],partie['next_tile'])
            partie['score']=get_score(partie['plateau'])
            partie['next_tiles']=get_next_alea_tiles(partie['plateau'],'encours')
        is_game_over(partie['plateau'])


    #   -4 Retourne True si terminée
    return is_game_over(partie['plateau'])

if __name__=='__main__':
    restore_game()




