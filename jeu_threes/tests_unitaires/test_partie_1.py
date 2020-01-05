import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')

import tiles.tiles_acces
import tiles.tiles_moves

p={'n':4,'nb_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}

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
