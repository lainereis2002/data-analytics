import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import numpy as np

arr = np.array([2, 4, 6, 7, 8])
print(arr[1]) #4
print(arr[0], "\n") #2

cartela_bingo = np.array([[16, 10, 3, 15],
                          [14, 23, 17, 27],
                          [6, 19, 3, 1],
                          [10, 4, 18, 19]])
print(cartela_bingo, "\n")

print(cartela_bingo[:, 1], "\n") #toda coluna do índice 1 mostrado como linha
print(cartela_bingo[:, 1].shape, "\n") #tamanho
print(cartela_bingo[:, 1].reshape((4,1)), "\n") #transformando em coluna novamente
print(cartela_bingo[0], "\n") #toda primeira linha

print(np.sort(cartela_bingo), "\n") #ordenando
print(np.sort(cartela_bingo, axis=0), "\n") #considerando o eixo 0 (colunas)

