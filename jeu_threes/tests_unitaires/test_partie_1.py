from play import*

def test_init_play():
    plateau=init_play()

    assert plateau['n']== 4 ,       "Erreur A"
    assert not(plateau['n']== 5) ,  "Erreur B"
    assert plateau['nb_cases_libres']== 4 ,"Erreur A"