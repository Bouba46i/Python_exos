#TODO :
# implementer le game of life
#   matrice n x m
#   j'assume que n > 0 & m > 0	
#
# bonus
#	creer un fichier html avec le resultat
#		se décider du format du resultat
#
import copy
import numpy as np


GOL_matrix = np.array([
	[0, 1, 0, 1, 1],
	[0, 0, 1, 1, 0],
	[0, 1, 0, 0, 1],
	[0, 1, 0, 1, 0]
])



def neighbors_count(matrix, i, j):
    rows, cols = matrix.shape
    i_min = i - 1 if i - 1 >= 0 else 0 
    i_max = i + 2 if i + 2 <= rows else rows 
    j_min = j - 1 if j - 1 >= 0 else 0
    j_max = j + 2 if j + 2 <= cols else cols 
    
    return np.sum(matrix[i_min:i_max, j_min:j_max]) - matrix[i, j]

def will_cell_live(is_living, neig_count):
    if(neig_count == 3): return True
    if(is_living and neig_count == 2): return True
    return False

def gol_iteration(matrix):
    new_matrix = copy.deepcopy(matrix)
    
    for (i, j), value in np.ndenumerate(matrix):
        neig_count = neighbors_count(matrix, i, j)
        new_matrix[i, j] = will_cell_live(value, neig_count)
	
    return new_matrix

# bonus pour apres
# fonction pour creer fichier html

def game_of_life(matrix):

    for i in range(0, 5):
        matrix = gol_iteration(matrix)
    
    # appeler fonction pour creer fichier html
    # print_hmtl(matrix)
    
    return None



game_of_life(GOL_matrix)