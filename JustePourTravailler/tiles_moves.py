import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')

import tiles.tiles_acces
import game.play

from random import randint

########################################
########################################

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
    next_tiles={}
    if mode =="init":
        
        next_tiles['mode']='init'
        
        a1=tiles(plateau,2)
        next_tiles['0']=a1
        next_tiles['0']['val']=1
        
        a2=tiles(plateau,2)
        next_tiles['1']=a2
        next_tiles['1']['val']=2
        
    elif mode=="encours":
        
        next_tiles['mode']='encours'
        
        a3=tiles(plateau,3)
        next_tiles['0']=a3
        
    if is_game_over(plateau):
        next_tiles['Check']=False
    else:
        next_tiles['Check']=True
    return next_tiles


def tiles(plateau,n):
    
    tiles={}

    tiles['val']=randint(1,n)
    tiles['lig'],tiles['col']=position(plateau)
    return tiles


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


def put_next_tiles(plateau,tiles):
    
    if tiles['mode']=='init':
        
        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']
        if is_room_empty(plateau,tiles['1']['lig'],tiles['1']['col']):
            
            new_lig,new_col=position(plateau)
            plateau['tiles'][4*new_lig+1*new_col]=tiles['1']['val']
            
    if tiles['mode']=='encours':
        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']

    
