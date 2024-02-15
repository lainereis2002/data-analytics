import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import numpy as np

arr1_2d = np.array([[1,2],[3,4]])
arr2_2d = np.array([[5,6],[7,8]])
arr3_2d = np.array([[9,2],[3,4]])

arr_3d = np.array([arr1_2d, arr2_2d, arr3_2d])
print("ABAIXO ESTÁ O ARRAY DE 3 DIMENSÕES\n")
print(arr_3d)
print("\n")
arr_4d = np.array([arr_3d, arr_3d])
print("ABAIXO ESTÁ O ARRAY DE 3 DIMENSÕES\n")
print(arr_4d)
print("\n")

arr2_3d = np.zeros((3,4,2)) #3 dimensões / 4 linhas / 2 colunas
print("ABAIXO ESTÁ O ARRAY DE 3 DIMENSÕES\n")
print(arr2_3d)
print("\n")

print("ABAIXO ESTÁ O SHAPE ARRAY DE 3 DIMENSÕES\n")
print(arr2_3d.shape)
print("\n")

print("ABAIXO ESTÁ O ARRAY DE 3 DIMENSÕES ACHATADO EM UMA ÚNICA\n")
print(arr2_3d.flatten())
print("\n")

print("ABAIXO ESTÁ O RESHAPE DO ARR_3D\n")
print(arr_3d.reshape((4,3)))
print("\n")


'''reduza um array (5,7) a apenas uma dimensão'''
a57 = np.random.random((5,7))
print(a57.flatten())
print("\n")

'''crie um array que irá representar as cartelas de um bingo
os numeros da cartela variam entre 1 e 3, vc terá 10 participantes
cada cartela tera 12 números (4,3)'''
bingo = np.random.randint(1, 31, size=(10, 4, 3))
print(bingo)
print("\n")

'''faça o reshape das cartelas para que haja 5 cartelas 4 linhas e 6 cartelas'''
bingoreshape = bingo.reshape((5,4,6))
print(bingoreshape)
print("\n")
