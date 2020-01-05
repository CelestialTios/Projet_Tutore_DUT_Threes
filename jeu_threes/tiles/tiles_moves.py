import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')

import tiles.tiles_acces

#############################
#  Fonction de la partie 1  #
#############################

def get_nb_empty_rooms(p):
        """
        Prend en paramètre un dictionnaire correspondant au plateau de jeu
        Retourne le nombre de cases, soit le nombre de case de valeur 0
        """

        nbr_zeros=0
        i=0
        while i<len(p['tiles']):
            if p['tiles'][i]==0:
                nbr_zeros+=1
            i+=1

        return nbr_zeros
#############################
#  Fonction de la partie 2  #
#############################

def get_next_alea_tiles(plateau,mode):
    """
    Retourne la position(lig,col) et la valeur alétatoire d'un nombre de
    tuiles dépendant du mode(init,encours) de la partie.

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-mode: cast(string), choisit le nombre de tuiles donner
    """

    return tuiles

def tuiles(plateau,mode):
    """

    """
    next_tuiles={}
    if mode=="init":
        n=2
    elif mode=="encours":
        n=3

    next_tuiles['val']=randint(1,n)
    next_tuiles['lig'],next_tuiles['col']=position(plateau)
    return next_tuiles

def position(plateau):
    """
    Retourne une position(lig,col) du plateau étant vide

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-lig: numérotation de la ligne de la case
    @param-col: numérotation de la colonne de la case
    """
    lig=randint(0,3)
    col=randint(0,3)
    while not(is_room_empty(plateau,lig,col)):
        lig=randint(0,3)
        col=randint(0,3)
        is_room_empty(plateau,lig,col)
    return lig,col

plateau=init_play()
print(tuiles(plateau,'init'))
