import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import ui.user_entries
import life_cycle.cycle_game
import tiles.tiles_acces
import tiles.tiles_moves
import ui.play_display
import game.play


def test_line_pack():

    plateau = {
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 1, 0]
    }

    line_pack(plateau, 1, 0, 1)
    assert plateau['tuiles'] == [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 1, 0], "line_pack: Erreur A"

    line_pack(plateau, 1, 2, 1)
    assert plateau['tuiles'] == [0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 0, 0, 0, 1, 0], "line_pack: Erreur B"

    line_pack(plateau, 2, 0, 1)
    assert plateau['tuiles'] == [0, 2, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 1, 0], "line_pack: Erreur C"

    line_pack(plateau, 3, 3, 0)
    assert plateau['tuiles'] == [0, 2, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], "line_pack: Erreur D"

    line_pack(plateau, 1, 3, 0)
    assert plateau['tuiles'] == [0, 2, 0, 0, 0, 2, 3, 0, 2, 2, 0, 0, 0, 0, 0, 1], "line_pack: Erreur E"

    print("line_pack: OK")

def test_line_move () :
    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [0, 0, 2, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    line_move(plateau,1,0)
    assert plateau['tuiles'] ==[0, 0, 2, 1, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0], "line_move:Erreur A"

    line_move(plateau,0,0)
    assert plateau['tuiles'] ==[0, 0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0], "line_move:Erreur B"

    line_move(plateau,1,0)
    assert plateau['tuiles'] ==[0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0], "line_move:Erreur C"

    line_move(plateau,1,0)
    assert plateau['tuiles'] ==[0, 0, 0, 3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0], "line_move:Erreur D"

    line_move(plateau,0,1)
    assert plateau['tuiles'] ==[0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0], "line_move:Erreur E"

    print("line_move: OK")

def test_lines_move():
    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [0, 0, 2, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    }

    lines_move(plateau,0)
    assert plateau['tuiles']==[0, 0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 1],"lines_move:Erreur A"

    lines_move(plateau,1)
    assert plateau['tuiles']==[0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0],"lines_move:Erreur B"

    lines_move(plateau,1)
    assert plateau['tuiles']==[0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],"lines_move:Erreur C"

    lines_move(plateau,1)
    assert plateau['tuiles']==[3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],"lines_move:Erreur D"

    lines_move(plateau,0)
    assert plateau['tuiles']==[0, 3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],"lines_move:Erreur D"

    print("lines_move: OK")

def test_column_pack():

    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [0, 2, 0, 0, 0, 2, 3, 0, 0, 2, 2, 3, 0, 0, 0, 0]
    }
    column_pack(plateau,1,3,0)
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 2, 3, 0, 0, 2, 2, 3, 0, 2, 0, 0],"column_pack:Erreur A"

    column_pack(plateau,2,3,0)
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0],"column_pack:Erreur B"

    column_pack(plateau,2,0,1)
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 2, 3, 0, 0, 2, 2, 3, 0, 2, 0, 0],"column_pack:Erreur C"

    column_pack(plateau,3,1,1)
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 2, 0, 0],"column_pack:Erreur D"

    column_pack(plateau,1,3,0)
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 0, 3, 3, 0, 2, 2, 0, 0, 2, 0, 0],"column_pack:Erreur E"

    print("column_pack: OK")

def test_column_move():
    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [3, 0, 2, 0, 3, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0]
    }

    column_move(plateau,0,1)
    assert plateau['tuiles']==[6, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],"column_move:Erreur A"

    column_move(plateau,2,1)
    assert plateau['tuiles']==[6, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"column_move:Erreur B"

    column_move(plateau,0,0)
    assert plateau['tuiles']==[0, 0, 3, 0, 6, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],"column_move:Erreur C"

    column_move(plateau,2,0)
    assert plateau['tuiles']==[0, 0, 0, 0, 6, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0],"column_move:Erreur D"

    column_move(plateau,0,0)
    assert plateau['tuiles']==[0, 0, 0, 0, 0, 0, 3, 0, 6, 0, 0, 0, 2, 0, 0, 0],"column_move:Erreur E"

    column_move(plateau,0,0)
    assert plateau['tuiles']==[0, 0, 0, 0, 0, 0, 3, 0, 6, 0, 0, 0, 2, 0, 0, 0],"column_move:Erreur F"


    print("column_move: OK")

def test_columns_move():
    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [3, 0, 2, 0,
                  3, 0, 1, 2,
                  2, 0, 0, 1,
                  0, 0, 0, 3]
    }

    columns_move(plateau,1)
    assert plateau['tuiles']==[6, 0, 3, 2, 2, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0],"columns_move:Erreur A"

    columns_move(plateau,0)
    assert plateau['tuiles']==[0, 0, 0, 0, 6, 0, 3, 2, 2, 0, 0, 1, 0, 0, 0, 3],"columns_move:Erreur B"

    columns_move(plateau,0)
    assert plateau['tuiles']==[0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 3, 3, 2, 0, 0, 3],"columns_move:Erreur C"

    columns_move(plateau,1)
    assert plateau['tuiles']==[0, 0, 0, 0, 6, 0, 3, 3, 2, 0, 0, 3, 0, 0, 0, 0],"columns_move:Erreur D"

    print("columns_move: OK")

def test_play_move():
    plateau={
        'n': 4,
        'nb_cases_libres': 16,
        'tuiles': [3, 0, 2, 0,
                   3, 0, 1, 2,
                   2, 0, 0, 1,
                   0, 0, 0, 3]
    }
    play_move(plateau,'b')
    assert plateau['tuiles'] == [0, 0, 0, 0, 3, 0, 2, 0, 3, 0, 1, 3, 2, 0, 0, 3], "play_move:Erreur A"

    play_move(plateau,'b')
    assert plateau['tuiles'] == [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 2, 0, 1, 6], "play_move:Erreur B"

    play_move(plateau,'h')
    assert plateau['tuiles'] == [0, 0, 0, 0, 6, 0, 2, 0, 2, 0, 1, 6, 0, 0, 0, 0], "play_move:Erreur C"

    print("play_move: OK")


if __name__ == '__main__':
    test_line_pack()
    test_line_move()
    test_lines_move()
    test_column_pack()
    test_column_move()
    test_columns_move()
    test_play_move()
    print("\nPartie 2: opérationnel")
