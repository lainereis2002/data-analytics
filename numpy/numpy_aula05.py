import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
mask = arr1 % 2 == 0
print(mask, "\n")

pessoas_id_idade = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
print(pessoas_id_idade, "\n")

mask_maior_21 = pessoas_id_idade[: , 1] > 21
print(pessoas_id_idade[mask_maior_21], "\n")
print(np.where(mask_maior_21), "\n")

cartela_bingo = np.array([[16, 10, 3, 15],
                          [14, 23, 17, 27],
                          [6, 19, 3, 1],
                          [10, 4, 18, 19]])
print(cartela_bingo, "\n")

print(np.where(cartela_bingo % 3 == 0, "div3", cartela_bingo), "\n")
print(np.where(pessoas_id_idade > 21, "maior idade", pessoas_id_idade), "\n")
