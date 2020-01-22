import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')
        
import ui.user_entries
import life_cycle.cycle_game 
import tiles.tiles_acces 
import tiles.tiles_moves 
import ui.play_display 
import game.play 


def test_line_pack():
    
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [0, 0, 2, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    
    line_pack(plateau,1,0,0)
    assert plateau['tiles']==[0, 0, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur A"
    
    line_pack(plateau,0,0,0)
    assert plateau['tiles']==[0, 0, 0, 2, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur B"
    
    line_pack(plateau,1,0,1)
    assert plateau['tiles']==[0, 0, 2, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur C"
    
    line_pack(plateau,0,2,1)
    assert plateau['tiles']==[0, 2, 0, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur D"
    print("line_pack: OK") 
    
def test_line_move():
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [0, 0, 2, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    
    line_move(plateau,1,0)
    line_move(plateau,1,0)
    assert plateau['tiles']==[0, 0, 2, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur A"
    
    line_move(plateau,0,0)
    assert plateau['tiles']==[0, 0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur B"
    
    line_move(plateau,0,1)
    assert plateau['tiles']==[0, 2, 1, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur C"
    
    line_move(plateau,1,1)
    assert plateau['tiles']==[0, 0, 2, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur D"
    print("line_move: OK")
    
def test_lines_move():
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [0, 0, 2, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    
    lines_move(plateau,1)
    assert plateau['tiles']==[0, 2, 1, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur A"
    
    lines_move(plateau,0)
    assert plateau['tiles']==[0, 0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur B" 
    
    lines_move(plateau,1)
    lines_move(plateau,1)
    assert plateau['tiles']==[2, 1, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur C"
    
    lines_move(plateau,0)
    lines_move(plateau,0)
    assert plateau['tiles']==[0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur D" 
    print("lines_move: OK")
    
def test_column_pack():
    
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [3, 0, 2, 0, 3, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0]
    }
    
    column_pack(plateau,0,0,0)
    assert plateau['tiles']==[0, 0, 2, 0, 3, 0, 1, 0, 3, 0, 0, 0, 2, 0, 0, 0],"Erreur A"
    
    column_pack(plateau,2,1,0)
    assert plateau['tiles']==[3, 0, 2, 0, 3, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0],"Erreur B"
    
    column_pack(plateau,0,2,1)
    assert plateau['tiles']==[3, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur C"
    
    column_pack(plateau,2,3,1)
    assert plateau['tiles']==[3, 0, 1, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],"Erreur D"
    print("column_pack: OK") 
    
def test_column_move():
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [3, 0, 2, 0, 3, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0]
    }
    
    column_move(plateau,0,1)
    assert plateau['tiles']==[6, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur A"
    
    column_move(plateau,2,1)
    assert plateau['tiles']==[3, 0, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],"Erreur B"
    
    column_move(plateau,0,0)
    assert plateau['tiles']==[0, 0, 2, 0, 3, 0, 1, 0, 3, 0, 0, 0, 2, 0, 0, 0],"Erreur C"
    
    column_move(plateau,2,0)
    assert plateau['tiles']==[3, 0, 0, 0, 3, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0],"Erreur D"
    print("column_move: OK")
    
def test_columns_move():
    plateau={
        'n': 4, 
        'nb_cases_libres': 16, 
        'tiles': [3, 0, 2, 0,  3, 0, 1, 2, 2, 0, 0, 1, 0, 0, 0, 3]            
    }
    
    columns_move(plateau,1)
    assert plateau['tiles']==[6, 0, 3, 2, 2, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0],"Erreur A"
                   
    columns_move(plateau,0)
    assert plateau['tiles']==[0, 0, 0, 0, 3, 0, 2, 0, 3, 0, 1, 3, 2, 0, 0, 3],"Erreur B"
                                                                                             
    columns_move(plateau,1)
    columns_move(plateau,1)
    assert plateau['tiles']==[6, 0, 3, 3, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],"Erreur C"
                                                             
    columns_move(plateau,0)
    columns_move(plateau,0)
    assert plateau['tiles']==[0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 2, 0, 1, 6] ,"Erreur D"                                                                            
    print("columns_move: OK")
