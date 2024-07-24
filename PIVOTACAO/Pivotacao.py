import numpy as np

from SimplexInterface import SimplexInterface
from ConstrutorTabelas import ConstrutorTabelas

'''linhas = int(input("NÚMERO DE LINHAS: "))
colunas = int(input("NÚMERO DE COLUNAS:"))
matriz = SimplexInterface().criar_matriz(linhas, colunas)'''


matriz = np.array([
   [-20, -15, -10, -12,-8.0, -16,0.0],

   [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 50],
   [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 70],
   [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 20],
   [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 40],
])

def Pivotacao(matriz, coluna):
   #DEFINIR POSIÇÃO DAS DUAS LINHAS PRINCIPAIS.
   valores = []
   posicao_linhas = []
   for linha in range(matriz.shape[0]):
      if matriz[linha, coluna] == 1:
         posicao_linhas.append(linha)
         valores.append(matriz[linha, len(matriz[linha])-1])

   #VERFICIAR ÚLIMA VALOR DAS LINHAS E COMPARAR.
   linhaX = 0 
   linhaY = 0
   for valor in valores:
      if valor > linhaX:
         linhaX = posicao_linhas[0]
         linhaY = posicao_linhas[1]
      else:
         linhaY = posicao_linhas[1]
         linhaX = posicao_linhas[0]

   #FAZENDO A SUBTRACAO.
   matriz[linhaX] = matriz[linhaX] - matriz[linhaY]
   print(f"L{linhaX} - L{linhaY}")

   '''#TRABALHANDO A LINHA INICIAL L0.
   valor_L0 = int(abs(matriz[0, coluna]))
   matriz[0] = matriz[0] + (valor_L0 * matriz[linhaY])
   print(f"L0 + {valor_L0}L{linhaY}")'''



Pivotacao(matriz, 4)
Pivotacao(matriz, 3)



matriz[0] = matriz[0] + (10*matriz[1])
matriz[0] = matriz[0] + (16*matriz[2])
matriz[0] = matriz[0] + (12*matriz[3])
matriz[0] = matriz[0] + (8*matriz[4])
print(matriz)



ConstrutorTabelas.criar_tabela_excel(matriz, 'matriz2')












'''Pivotacao(matriz, 4)
ConstrutorTabelas.criar_tabela_excel(matriz, 'matriz1')
Pivotacao(matriz, 3)
ConstrutorTabelas.criar_tabela_excel(matriz, 'matriz2')'''
