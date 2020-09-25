import numpy as np
import matrix_generator as mg

n = 5

lst = mg.generate_matrice(n)

print(np.matrix(lst))
print()

cnt = 0

def check_neighbor(lst, idx_X, idx_Y):

	global cnt
	found = False
	nb = lst[idx_X][idx_Y]
	min_idx_x = idx_X
	min_idx_y = idx_Y

	print("minimum temporaire : ", nb)

	for x in range(-1, 2):
		for y in range(-1, 2):

			if x == y == 0:
				break
			if (idx_X + x < n) and (idx_Y + y < n):

				print("nombre comparé",lst[idx_X + x][idx_Y + y])
				cnt += 1		

				if nb > lst[idx_X + x][idx_Y + y]:
					nb = lst[idx_X + x][idx_Y + y]
					min_idx_x = idx_X + x
					min_idx_y = idx_Y + y
					found = True

	if found is True:
		print("nombre choisi : ", nb)
		print()
		return check_neighbor(lst, min_idx_x, min_idx_y)
	else:
		return nb, min_idx_x, min_idx_y


mini = lst[n//2][0]
x = n//2
y = 0

for nb in range(1, n):
	if lst[n//2][nb] < mini:
		mini = lst[n//2][nb]
		y = nb

nb, idx_x, idx_y = check_neighbor(lst, x, y)

print()
print("minimum local : ", nb)
print("nombre de comparaison : ", cnt)
