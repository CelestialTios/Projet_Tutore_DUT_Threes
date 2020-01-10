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


def put_next_tiles(plateau,tiles):

    if tiles['mode']=='init':

        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']
        if is_room_empty(plateau,tiles['1']['lig'],tiles['1']['col']):

            new_lig,new_col=position(plateau)
            plateau['tiles'][4*new_lig+1*new_col]=tiles['1']['val']

    if tiles['mode']=='encours':
        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']

        
def line_pack(plateau,num_lig,debut,sens):

    if sens==1:                             # Vers la gauche
        i=1
        while i < plateau['n']-debut:
            tass=get_value(plateau,num_lig,debut+i)     #Prend la valeur de la case ÃƒÂ  droite de celle actuelle
            set_value(plateau,num_lig,debut+i-1,tass)   #Met la valeur de la case actuelle ÃƒÂ  la valeur tass
            i+=1
        set_value(plateau,num_lig,3,0)          #Met la derniÃƒÂ¨re case ÃƒÂ  droite ÃƒÂ  la valeur 0

    elif sens==0:                           # Vers la droite
        i=1
        while i < plateau['n']:
            tass=get_value(plateau,num_lig,debut-i)     #Prend la valeur de la case ÃƒÂ  gauche de celle actuelle
            set_value(plateau,num_lig,debut-i+1,tass)   #Met la valeur de la case actuelle ÃƒÂ  la valeur tass
            i+=1
        set_value(plateau,num_lig,0,0)          #Met la derniÃƒÂ¨re case ÃƒÂ  gauche ÃƒÂ  la valeur 0

    else:
        return False

    return True

def line_move(plateau,num_lig,sens):
    if sens==1:
        val=1
    elif sens==0:
        val=-1

    debut=check_zero(plateau,num_lig,val)       #Donne la colonne oÃ¹ l'on commence
    if debut>1:
        Verif=addition(plateau,num_lig,val)

    debut=check_zero(plateau,num_lig,val)

    line_pack(plateau,num_lig,debut,sens)

def check_zero(plateau,num_lig,val):
    if val==1:
        col=0
    elif val==(-1):
        col=4
    posZero=get_value(plateau,num_lig,col)
    while posZero != 0:
        col=col+val
        posZero=get_value(plateau,num_lig,col)
    return col

def addition(plateau,num_lig,val):
    if val==1:
        col=0
    elif val==-1:
        col=4
    while col != plateau['n']-col:
        num1=get_value(plateau,num_lig,col)
        col=col+val
        num2=get_value(plateau,num_lig,col)
        if num1== num2:
            set_value(plateau,num_lig,col-val,0)
            set_value(plateau,num_lig,col,num1*2)
            return True
    return  False


def lines_moves(plateau,sens):
    i=0
    while i< plateau['n']:
        line_move(plateau,i,sens)
        i+=1
