a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b)

c = a.copy()
c.append(5)
print(a, c)
print(a is c, a == c[:4])

import copy

board = [[0, 0], [0, 0]]
shallow = board.copy()
shallow[0][0] = 9
print(board)
deep = copy.deepcopy(board)
deep[1][1] = 7
print(board, deep)
