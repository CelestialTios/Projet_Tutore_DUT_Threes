﻿from game.play import *

def check_indice(p,i):
        """
        Prend en paramètre un indice et un dictionnaire correspondant Ã  un plateau\n",
        Retourne True si l'indice est compris entre 0 et n-1\n",
        """

        if i<=p['n']-1 and i>=0:
            return True
        else:
            return False

def check_room(p,lig,col):

        """
        Prend en paramètre deux entiers correspondant aux numéros de ligne et colonne et un dictionnaire correspondant à un plateau
        Retourne True si les numéros de ligne et colonne sont compris entre 0 et n-1
        """

        if check_indice(p,lig)==False or check_indice(p,col)==False: # Utilisation de la fonction check_indice car le nombre de colonnes est identique au nombre de lignes, tous deux valant n
            return False
        else:
            return True

def get_value(p,lig,col):
    """
    Retourne la valeur de la case (lig,col)
    Enonce erreur si lig ou col n'est pas valide

    @param-p: dictionnaire contenant les informations du plateau
    @param-lig: numérotation de la ligne de la case
    @param-col: numérotation de la colonne de la case
    """

    assert check_room(p,lig,col) == True, "Erreur perçu dans lig ou col"

    val=p['tiles'][4*lig+1*col]

    return val


def set_value(p,lig,col,val):
    """
    Change la valeur de la case(lig,col)
    Enonce erreur si lig ou col n'est pas valide

    @param-p :dictionnaire contenant les informations du plateau
    @param-lig : numérotation de la ligne de la case
    @param-col : numérotation de la colonne de la case
    @param-val : nouvelle valeur assigné à la case(lig,col)
    """
    assert check_room(p,lig,col) == True, "Erreur perçu dans lig ou col"
    p['tiles'][4*lig+1*col]=val
    return

def is_room_empty(p,lig,col):
        """
        Prend en paramètre deux entiers correspondant aux numeros de ligne et colonne et un dictionnaire correspondant à un plateau
        Retourne True si la valeur obtenue à la position (lig;col) vaut 0
        """

        if not get_value(p,lig,col)==0: # Utilisation de la fonction get_value pour voir si la tuile est vide ou non
            return False # Retourne False quand get_value ne retourne pas 0
        else:
            return True



