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
    Retourne la position(lig,col) et la valeur alÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tatoire d'un nombre de
    tuiles dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©pendant du mode(init,encours) de la partie.

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
    """
    Crée un dictionnaire contenant toutes les informations d'une tuiles: sa valeur et sa position(lig,col)

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-n: valeur maximal de la tuiles possible
    """
    tiles={}

    tiles['val']=randint(1,n)
    tiles['lig'],tiles['col']=position(plateau)
    return tiles


def position(plateau):
    """
    Retourne une position(lig,col) du plateau ‚étant vide

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
    """
    Place les tuiles obtenues dans le plateau

    @param-plateau:dictionnaire contenant les informations du plateau
    @param-tiles: dictionnaire contenant les informations des/la prochaine(s) tuile(s)
    """
    if tiles['mode']=='init':

        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']
        if is_room_empty(plateau,tiles['1']['lig'],tiles['1']['col']):

            new_lig,new_col=position(plateau)
            plateau['tiles'][4*new_lig+1*new_col]=tiles['1']['val']

    if tiles['mode']=='encours':
        plateau['tiles'][4*tiles['0']['lig']+1*tiles['0']['col']]=tiles['0']['val']

def line_pack(plateau,num_lig,debut,sens):
    """
    Permet le déplacement des tuiles d'une ligne du plateau dans un sens donné, à partir d'un début
    tout en appliquant les règles du jeu Threes.

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-num_lig: valeur étant la position (lig) de la ligne influencée
    @param-debut: valeur étant la position (col) où commence la fonction
    @param-sens: sens du mouvement des tuiles
                -0 : déplacement vers la droite
                -1 : déplacement vers la gauche
    """
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
    """
    Permet le déplacement des tuiles d'une ligne dans une direction selon le sens donné,
    tout en appliquant les règles du jeu Threes.

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-num_lig: valeur étant la position (lig) de la ligne influencée
    @param-sens: sens du mouvement des tuiles
                -0 : déplacement vers la droite
                -1 : déplacement vers la gauche
    """

    if sens == 1 :
        val = 1
    elif sens == 0 :
        val = -1

    debut=check_zero(plateau,num_lig,val)       #Donne la colonne oÃ¹ l'on commence
    if debut > 1 :
        Verif=addition(plateau,num_lig,val)

    debut=check_zero(plateau,num_lig,val)
    print(debut)
    line_pack(plateau,num_lig,debut,sens)

def check_zero(plateau,num_lig,val):
    """
    Permet de savoir où doit commencer le déplacement des tuiles

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-num_lig: valeur étant la position (lig) de la ligne influencée
    @param-val: permet de savoir où commence la variable col
    """

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
    """
    Vérifie si une addition est possible pour modifier la valeur de la tuile qui écrase
    par la nouvelle valeur

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-num_lig: valeur étant la position (lig) de la ligne influencée
    @param-val: permet de savoir où commence la variable col
    """

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
    """
    Permet le déplacement des tuiles de tout le plateau dans un sens donné,
    tout en appliquant les règles du jeu Threes.

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-sens: sens du mouvement des tuiles
                -0 : déplacement vers la droite
                -1 : déplacement vers la gauche
    """

    i=0
    while i< plateau['n']:
        line_move(plateau,i,sens)
        i+=1


def play_move(plateau,sens):
    """
    Permet le déplacement des tuiles du plateau dans une direction selon le sens donné,
    tout en appliquant les règles du jeu Threes.

    @param-plateau: dictionnaire contenant les informations du plateau
    @param-sens: sens du mouvement des tuiles
                -'b':bas
                -'h':haut
                -'d':droite
                -'g':gauche
    """

    if sens =="b":
        columns_move(plateau,0)
    elif sens=="h":
        columns_move(plateau,1)
    elif sens=="d":
        lines_moves(plateau,0)
    elif sens=="g":
        lines_moves(plateau,1)
    return

