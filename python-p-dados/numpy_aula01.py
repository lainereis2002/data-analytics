import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import numpy as np

l = [4, 8, 2, 12, 5, 8, 0]
arr1 = np.array(l)
print(arr1, "\n")

#ele faz tipo uma matriz de zeros
print(np.zeros((2,2)), "\n")

#são iguais, eles listam de um numero até outro
print(list(range(1,11))) #aqui tem vírgula
arr2 = np.arange(1, 11) #aqui não tem vírgula
print(arr2,"\n")

print(type(arr2), "\n")

#numero aleatórios
arr3 = np.random.random((3,3))
print(arr3, "\n")


'''crie um array com 4 linhas e 3 colunas com valores aleatórios'''
q1 = np.random.random((4,3))
print(q1, "\n")

'''crie um array com 5 colunas e 10 linhas inicializados com zeros'''
q2 = np.zeros((10,5))
print(q2, "\n")

'''crie um array com valores inteiros de 3 linhas e 5 colunas com valores aleatórios'''
q3 = np.random.randint(30, size=(3,5)) #primeiro vc coloca até que n-1 vc quer q seja o valor e depois coloca o tamanho da matriz
print(q3, "\n")
