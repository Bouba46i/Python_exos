#TODO :
# implementer le game of life
# 	les regles -> implementer les cas cas tricky de matrice
#	lire la matrice (tableau a deux dim n x m)
#	pour chaque cell -> réécrire son destin (c'est dramatique oui)
#	lancer le GOL 5 fois sur la matrice
#	
#
# bonus
#	creer un fichier html avec le resultat
#		se décider du format du resultat
#


GOL_matrix = [
	[0, 1, 0, 1, 1]
	[0, 0, 1, 1, 0]
	[0, 1, 0, 0, 1]
	[0, 1, 0, 1, 0]
]



def neighbors_count(matrix):
    # lire son voisinages + compter les cellules vivantes
    return 0


def is_cell_will_live(is_living, neig_count):
    if(neig_count == 3): return True
    if(is_living and neig_count == 2): return True
    return False

def gol_iteration(matrix):
    new_matrix = [[],[]]
    
	# pour chaque cell, vivante ou non
    # 	compter le nombre de cellules vivantes autour d'elle
    # 	neig_count = neighbors_count(matrix)
    # 	cell_updated = is_cell_will_live(is_living, neig_count)

    return new_matrix

# bonus pour apres
# fonction pour creer fichier html

def game_of_life(matrix):
    # test cas tricky de la matrice

    for i in range(0, 5):
        matrix = gol_iteration(matrix)
        
    # appeler fonction pour creer fichier html
    return 

game_of_life(GOL_matrix)