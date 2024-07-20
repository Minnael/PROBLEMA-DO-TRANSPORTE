from SimplexInterface import SimplexInterface
from SimplexDuasFases import SimplexDuasFases

if __name__ == "__main__":
   linhas = int(input("NÚMERO DE LINHAS: "))
   colunas = int(input("NÚMERO DE COLUNAS:"))

   matriz = SimplexInterface().criar_matriz(linhas, colunas)
   base_canonica = SimplexDuasFases().Eliminacao_W(matriz)
   SimplexDuasFases().Eliminacao_Z(base_canonica)