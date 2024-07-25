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
'''
Max = 10**9

matriz = np.array([[Max, -10, -12, -8, -9, -5, 0, -10, Max, -15, -16, -8, -10, 0, -12, -15, Max, 
      -10,	-8, -12, 0, -8, -16, -10, Max, -15, -5, 0, -9, -8, -8, -15, -Max, -20, 
      0, -5, -10, -12, -5, -20, Max, 0, 0, 0,	0, 0, 0, 0, Max, 0],
     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 400],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
         1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 250],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 350],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,	1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
         0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 600],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
         0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 250],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 250],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 500]])'''

Max = 10**9

matriz = np.array([
    [1,Max,-10,-12,-8,-9,-5,-10,Max,-15,-16,-8,-10,-12,-15,Max,-10,-8,-12,-8,-16,-10,Max,-15,-5,-9,-8,-8,-15,Max,-20,-5,-10,-12,-5,-20,Max,0,0,0,0,0,0,0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 400],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 250],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 350],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 600],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 250],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 250],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 500],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 150],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 100]
])
def Pivotacao_Negativa(matriz, coluna):
   #DEFINIR POSIÇÃO DAS DUAS LINHAS PRINCIPAIS.
   linhaX = 0
   linhaY = 0
   for linha in range(matriz.shape[0]):
      if matriz[linha, coluna] == 1:
        linhaY = linha
        
      if matriz[linha, coluna] ==-1:
        linhaX = linha

   #FAZENDO A SUBTRACAO.
   matriz[linhaX] = matriz[linhaX] + matriz[linhaY]
   print(f"L{linhaX} + L{linhaY}")

   #TRABALHANDO A LINHA INICIAL L0.
   '''valor_L0 = int(abs(matriz[0, coluna]))
   matriz[0] = matriz[0] + (valor_L0 * matriz[linhaY])
   print(f"L0 + {valor_L0}L{linhaY}")'''


def Pivotacao(matriz, coluna):
   #DEFINIR POSIÇÃO DAS DUAS LINHAS PRINCIPAIS.
   valores = []
   posicao_linhas = []
   for linha in range(1, matriz.shape[0]):
      if matriz[linha, coluna] == 1:
        posicao_linhas.append(linha)
        valores.append(matriz[linha, len(matriz[linha])-1])

   #VERFICIAR ÚLIMA VALOR DAS LINHAS E COMPARAR.
   linhaY = posicao_linhas[valores.index(min(valores))]
   posicao_linhas.remove(linhaY)

   #FAZENDO A SUBTRACAO.
   for linha in posicao_linhas:
      matriz[linha] = matriz[linha] - matriz[linhaY]
      print(f"L{linha} - L{linhaY}")
    

   #TRABALHANDO A LINHA INICIAL L0.
   '''valor_L0 = int(abs(matriz[0, coluna]))
   matriz[0] = matriz[0] + (valor_L0 * matriz[linhaY])
   print(f"L0 + {valor_L0}L{linhaY}")'''


Pivotacao(matriz, 4) 

Pivotacao(matriz, 6)
Pivotacao(matriz, 6)
Pivotacao_Negativa(matriz, 6)

Pivotacao(matriz, 7)

Pivotacao(matriz, 9)
Pivotacao_Negativa(matriz, 9)

Pivotacao(matriz, 11)
Pivotacao_Negativa(matriz, 11)

Pivotacao(matriz, 16)

Pivotacao(matriz, 19)

Pivotacao(matriz, 26)

Pivotacao(matriz, 31)

Pivotacao(matriz, 38)

Pivotacao(matriz, 39)
Pivotacao_Negativa(matriz,39)

Pivotacao(matriz, 40)

Pivotacao(matriz, 7)
Pivotacao_Negativa(matriz, 7)



matriz[0] = matriz[0] + 8*matriz[1] + 5*matriz[13] + 10*matriz[7] + 15*matriz[10] + 8*matriz[2] + 10*matriz[3] + 8*matriz[4] + 8*matriz[5] + 5*matriz[6]


matriz[6] = matriz[6] - matriz[11]
matriz[7] = matriz[7] + matriz[11]
matriz[10] = matriz[10] - matriz[11]
matriz[12] = matriz[12] + matriz[10]
matriz[0] = matriz[0] -5*matriz[11]

matriz[0] = matriz[0] -3*matriz[10]
matriz[4] = matriz[4] - matriz[10]
matriz[7] = matriz[7] + matriz[10]
matriz[12] = matriz[12] - matriz[10]



ConstrutorTabelas.criar_tabela_excel(matriz, 'matriz')