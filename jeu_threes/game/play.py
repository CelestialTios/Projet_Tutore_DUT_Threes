import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')
        
import tiles.tiles_moves

#############################
#  Fonction de la partie 1  #
#############################

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

#############################
#  Fonction de la partie 3  #
#############################

def create_new_play():
    """
    Retourne une partie sous forme de dictionnaire contennant 3 clés:
    
    - Plateau correspondant au plateau de jeu;
    - Next_tiles correspondant à la prochaine tuile à placer;
    - Score correspondant au score en cours obtenu par le joueur sur le plateau.
    
    """
    partie={}
    
    partie['plateau']=init_play()                  #initialisation d'un plateau via init_play
    get_next_alea_tiles(partie['plateau'],"init")  #tuiles placéees via get_next_alea_tiles

    partie['next_tiles']=tiles(partie['plateau'],3) #mémortisation de la valeur de la prochaine tuile via tiles
    
    partie['score']=get_score(partie)           #score du joueur via get_score
    return partie


