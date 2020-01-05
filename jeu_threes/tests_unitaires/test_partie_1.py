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

###########################
#  module : tiles_acces   #
###########################    
def test_check_indice():
    assert check_indice(p,3)==True, "Erreur A"
    assert check_indice(p,5)==False, "Erreur B"
    assert not check_indice(p,6)==True, "Erreur C"
    print("Fonction check_indice: OK")
    
def test_check_room():
    assert check_room(p,5,6)==False, "Erreur A"
    assert check_room(p,1,1)==True, "Erreur B"
    assert check_room(p,2,5)==False, "Erreur C"
    assert not check_room(p,5,0)==True, "Erreur D"
    print("Fonction check_room : OK")

def test_get_value():
    assert get_value(-1,10)==False, "Erreur A"
    assert get_value(p,8,0)==False, "Erreur B"
    assert get_value(p,1,8)==False, "Erreur C"
    assert get_value(p,3,2)==0, "Erreur D"
    assert get_value(p,0,2)==0, "Erreur E"
    print("Fonction get_value : OK")

def test_set_value():
    assert  set_value(1,2)==True, "Erreur A"
    assert set_value(0,8)==False, "Erreur B"
    assert not set_value(8,3)==True, "Erreur C"
    assert set_value(10,9)==False, "Erreur D"
    print("Fonction set_value : OK")

def test_is_room_empty():
    assert is_room_empty(p,1,1)==True, "Erreur A"
    assert not is_room_empty(p,1,2)==False, "Erreur B"
    assert is_room_empty(p,3,0)==True, "Erreur C"
    print("Fonction is_room_empty : OK")
    
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
    
###########################
#  module : play_dsplay   #
###########################

def test_affichage_moyen():
    p1={'n':4,'nb_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    assert affichage_moyen(p1)==True,"Erreur A"
    assert not(affichage_moyen(p1))==False,"Erreur B"
    print("Fonction affichage_moyen : OK")
