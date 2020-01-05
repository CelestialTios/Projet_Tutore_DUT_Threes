import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath +'/../')


#############################
#  Fonction de la partie 1  #
#############################

def affichage_simple(p):
    msg=""
    col=0
    while col < p['n']:
        lig=0
        while lig < p['n']:
            msg += str(p['tiles'][4*col+1*lig]).rjust(4,' ')
            lig+=1
        msg+= '\n'
        col+=1
    print(msg)

def affichage_moyen(p):
    msg="=================\n"
    col=0
    while col < p['n']:
        lig=0
        msg += "|"
        while lig < p['n']:
            msg += str(p['tiles'][4*col+1*lig]).rjust(2,' ')
            msg += "|".rjust(2," ")
            lig+=1

        msg+= '\n=================\n'
        col+=1

    print(msg)
