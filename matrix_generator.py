import random 
import numpy as np

def generate_matrice(n):
	n_square = n *n 
	lst = random.sample(range(0,n_square),n_square)
	lst = np.array(lst)
	lst = lst.reshape(n, n)
	return lst
