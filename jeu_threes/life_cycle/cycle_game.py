import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')
   
import json
import os

import ui.user_entries
import tiles.tiles_acces 
import tiles.tiles_moves 
import ui.play_display 
import game.play 


def save_game(partie):
    """
    Prend en paramètre une partie.
    Sauvegarde la partie au format json.
    """
    file = open("game_saved.json", "w")
    file.write(json.dumps(partie))
    file.close()

def restore_game():
    """
    Permet de restaurer la partie étant sous forme de fichier json
    Retourne la partie si elle existe
    """
    if os.path.exists("game_saved.json"):
        print('True')
        file = open("game_saved.json","r")
        transformation=file.read()
        partie=json.loads(transformation)
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




