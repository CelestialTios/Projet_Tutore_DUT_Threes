import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')

import tiles.tiles_acces
import tiles.tiles_moves
import game.play
import ui.play_display


########################################################
########################################################

#########################
#      module play      #
#########################
def test_init_play():
    plateau=init_play()

    assert plateau['n']== 4 ,       "Erreur A"
    assert not(plateau['n']== 5) ,  "Erreur B"
    assert plateau['nb_cases_libres']== 16 ,      "Erreur C"
    assert not(plateau['nb_cases_libres']== 14) , "Erreur D"
    assert plateau['tiles'] == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] , "Erreur E"
    assert not(plateau['tiles'] == [2,0,0,3,0,0,0,0,4,0,0]) , "Erreur F"
    assert not(plateau['tiles'] == [0]) , "Erreur F"
    print("Fonction init_play : OK")

def test_is_game_over():
    p1={'n':4,'nb_cases_libres':16,'tiles':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}
    assert is_game_over(p1)==True,"Erreur A"
    p2={'n':4,'nb_cases_libres':16,'tiles':[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    assert not(is_game_over(p2))==True, "Erreur B"
    p3={'n':4,'nb_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0]}
    assert not(is_game_over(p3))==True, "Erreur B"
    print("Fonction is_game_over : OK")

def test_get_score():
    p1={'n':4,'nb_cases_libres':16,'tiles':[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]}
    assert get_score(p1)==16, "Erreur A"
    p2={'n':4,'nb_cases_libres':16,'tiles':[3,6,6,24,6,12,2,3,2,1,3,6,1,2,2,1]}
    assert get_score(p1)==80, "Erreur B"
    p3={'n':4,'nb_cases_libres':16,'tiles':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}
    assert not(get_score(p1)==0), "Erreur C"
    print("Fonction get_score : OK")
    
