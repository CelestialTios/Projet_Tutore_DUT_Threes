import sys
import os
from pathlib import Path
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import ui.user_entries
import life_cycle.cycle_game
import tiles.tiles_acces
import tiles.tiles_moves
import ui.play_display
import game.play

def test_create_new_play():
    partie=create_new_play()
    assert partie['score'] == 3, "create_new_play: Erreur A"
    partie=create_new_play()
    assert len(partie['plateau']['tuiles'])==16, "create_new_play: Erreur B"
    assert partie['plateau']['n']==4, "create_new_play: Erreur C"

    print("create_new_play: OK")

def test_get_user_move():
    print("################\nSaississer h\n################")
    assert get_user_move()=='h', "get_user_move: Erreur A"

    print("################\nSaississer H\n################")
    assert get_user_move()=='h', "get_user_move: Erreur B"

    print("################\nSaississer m\n################")
    assert get_user_move()=='m', "get_user_move: Erreur B"

    print("################\nSaississer 5 puis x puis B\n################")
    assert get_user_move()=='b', "get_user_move: Erreur C"

    print("################\nSaississer S puis L puis a puis d\n################")
    assert get_user_move()=='d', "get_user_move: Erreur D"

    print("get_user_move: OK")



def test_cycle_play():
    partie=None
    assert not(cycle_play(partie))==True, "cycle_play: Erreur A"

    partie=create_new_play()
    print("################\nSaississer m\n################")
    assert not(cycle_play(partie))==True, "cycle_play: Erreur B"

    print("################\nSaississer h puis b puis m\n################")
    assert not(cycle_play(partie))==True, "cycle_play: Erreur B"



    print("cycle_play: OK")


def test_get_user_menu():
    partie=None
    i=0
    while i <= 1:
        print("################\nSaississer N\n################")
        assert get_user_menu()=='N', 'get_user_move: Erreur A'

        print("################\nSaississer n\n################")
        assert get_user_menu()=='N', 'get_user_move: Erreur B'

        print("################\nSaississer 5 puis x puis B puis l\n################")
        assert get_user_menu()=='L', 'get_user_move: Erreur C'

        print("################\nSaississer c puis C puis q\n################")
        action=get_user_menu()
        if partie==None:
            get_user_menu()
            assert get_user_menu()=='Q', 'get_user_move: Erreur D'
        else:
            assert action=='C' , 'get_user_move: Erreur E'

        print("################\nSaississer s puis S puis L\n################")
        action=get_user_menu()
        if partie==None:
            get_user_menu()
            assert get_user_menu()=='L', 'get_user_move: Erreur F'
        else:
            assert action=='S', 'get_user_move: Erreur G'
        partie=create_new_play()

    print("get_user_move: OK")

def test_save_game():
    partie=create_new_play()
    save_game(partie)
    my_file =Path("game_saved.json")
    assert my_file.is_file()==True, "save_game: Erreur A"
    my_file_not=Path("existepas.json")
    assert not(my_file_not.is_file())==True, "save_game: Erreur B"

    print("save_game: OK")

def test_restore_game():
    my_file=Path("game_saved.json")
    partie=restore_game()
    assert my_file.is_file()==True, "restore_game: Erreur A"

    assert len(partie)==3, "restore_game: Erreur B.1"
    assert len(partie['plateau'])==3, "restore_game: Erreur B.2"
    print("restore_game: OK")


if __name__ == '__main__':
    test_create_new_play()
    test_get_user_move()
    test_cycle_play()
    test_get_user_menu()
    test_save_game()
    test_restore_game()