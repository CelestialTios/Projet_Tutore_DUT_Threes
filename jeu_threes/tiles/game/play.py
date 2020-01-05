from tiles_moves import *


def init_play():
    """
    Retourne un dictionnaire possédant trois clés correspondant respectivement à:
    la taille n*n du plateau,
    au nombre de cases libres,
    aux tuiles.
    """

    p={}
    p['n']=4
    p['nb_cases_libres']=16
    p['tiles']=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return p

def is_game_over(p):
    """
    Retourne True si la partie est terminée
    Utilise la fonction get_nb_empty_rooms
    pour vérifier le nombre de case disponible

    @param-p:dictionnaire contenant les informations du plateau
    """
    if get_nb_empty_rooms(p)==0:
        return True

    return False



def get_score(p):
    """
    Retourne le score du plateau

    @param-p:dictionnaire contenant les informations du plateau
    """
    score=0
    i=0
    while i < len(p['tiles']):
        score += p['tiles'][i]
        i += 1
    return score