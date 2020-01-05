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

#########################
#  module tiles_acces   #
######################### 

def test_check_indice():
    p={'n':4,'nb_cases_libres':16,'tiles':[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]}
    assert check_indice(p,3)==True, "Erreur A"
    assert check_indice(p,5)==False, "Erreur B"
    assert not check_indice(p,6)==True, "Erreur C"
    print("Fonction check_indice: OK")
    
def test_check_room():
    p={'n':4,'nb_cases_libres':16,'tiles':[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]}
    assert check_room(p,2,1)==False, "Erreur A"
    assert check_room(p,0,0)==True, "Erreur B"
    assert check_room(p,0,2)==False, "Erreur C"
    assert not check_room(p,3,1)==True, "Erreur D"
    print("Fonction check_room : OK")

def test_get_value():
    p={'n':4,'nb_cases_libres':16,'tiles':[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]}
    assert get_value(-1,10)==False, "Erreur A"
    assert get_value(p,8,0)==False, "Erreur B"
    assert get_value(p,1,8)==False, "Erreur C"
    assert get_value(p,0,0)==0, "Erreur D"
    assert get_value(p,2,3)==3, "Erreur E"
    print("Fonction get_value : OK")
         
def test_set_value():
    p={'n':4,'nb_cases_libres':16,'tiles':[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]}
    set_value(p,0,0,3)
    assert p['tiles'][4*0+0]==3, "Erreur A"
    set_value(p,3,0,1)
    assert p['tiles'][4*3+0]==1, "Erreur B"
    set_value(p,2,1,0)
    assert p['tiles'][4*2+1]==0, "Erreur C"
    print("Fonction set_value : OK")
          
def test_is_room_empty():
    p={'n':4,'nb_cases_libres':16,'tiles':[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]}
    assert is_room_empty(p,0,0)==True, "Erreur A"
    assert not is_room_empty(p,1,2)==False, "Erreur B"
    assert is_room_empty(p,3,0)==True, "Erreur C"
    print("Fonction is_room_empty : OK")
    
#########################
#  module tiles_moves   #
#########################

#########################
#      module play      #
#########################

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

    
