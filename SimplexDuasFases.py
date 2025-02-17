import re
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from colorama import Fore, Style
from colorama import Fore, Back, Style


class SimplexDuasFases:
    def __init__(self):
        pass

    def PivoZ(self, base):
        linha_z = base[len(base)-1]
        indice_coluna = 0
        indice_linha = 0

        for indice in range(len(linha_z)-1):
            valor_linha = 0
            if linha_z[indice] < valor_linha:
                valor_linha = linha_z[indice]
                indice_coluna = indice

        coluna_pivo = []
        for linha in base:
            coluna_pivo.append(linha[indice_coluna])

        coluna_b = []
        for linha in base:
            coluna_b.append(linha[len(base)+1])

        valor_da_divisao = 500

        for i in range(len(coluna_pivo)):
            if coluna_b[i] >= 0 and coluna_pivo[i] > 0:
                if coluna_b[i]/coluna_pivo[i] < valor_da_divisao:
                    valor_da_divisao = coluna_b[i]/coluna_pivo[i]
                    indice_linha = i

        cordenadas_pivo = [indice_linha, indice_coluna]
        return cordenadas_pivo

    def Eliminacao_Z(self, base):
        coordenadas_pivo = self.PivoZ(base)
        pivo = base[coordenadas_pivo[0]][coordenadas_pivo[1]]
        linha_pivo = base[coordenadas_pivo[0]]
        ultima_linha = base[len(base)-1]

        if pivo != 1: 
            for i in range(len(linha_pivo)):
                linha_pivo[i] = round(linha_pivo[i] / pivo, 2)

        for linha in base:
            linha_pivo_base = linha[coordenadas_pivo[1]]

            if linha_pivo_base < 0 and linha != linha_pivo:
                for i in range(len(linha)):
                    linha[i] = round(abs(linha_pivo_base) * linha_pivo[i] + linha[i], 2)

            elif linha_pivo_base > 0 and linha != linha_pivo:
                for i in range(len(linha)):
                    linha[i] = round(-linha_pivo_base * linha_pivo[i] + linha[i], 2)

        for i in range(len(ultima_linha)-1):
            if ultima_linha[i] < 0:
                self.Apresentar_Tabela(base)
                self.Eliminacao_Z(base)
                return
            
        self.Apresentar_Tabela(base)
        self.Apresentar_Final_Etapa("ELIMINACAO 'Z' CONCLUIDA!")


    def PivoW(self, base):
        linha_w = base[len(base)-1]
        indice_coluna = 0
        indice_linha = 0

        for indice in range(len(linha_w)-1):
            valor_linha = 0
            if linha_w[indice] < valor_linha:
                valor_linha = linha_w[indice]
                indice_coluna = indice

        coluna_pivo = []
        for linha in base:
            coluna_pivo.append(linha[indice_coluna])
        coluna_pivo.pop(-2)  # REMOVENDO ITEM Z COLUNA DO PIVO

        coluna_b = []
        for linha in base:
            coluna_b.append(linha[len(base)+1])
        coluna_b.pop(-2)    # REMOVENDO ITEM Z COLUNA B

        for i in range(len(coluna_pivo)):
            pivo = 10**6
            if coluna_b[i] > 0 and coluna_pivo[i] > 0:
                if coluna_b[i]/coluna_pivo[i] < pivo:
                    pivo = coluna_pivo[i]
                    indice_linha = i

        cordenadas_pivo = [indice_linha, indice_coluna]
        return cordenadas_pivo

    def Eliminacao_W(self, base):
        pivo = base[self.PivoW(base)[0]][self.PivoW(base)[1]]
        linha_pivo = base[self.PivoW(base)[0]]

        if pivo != 1: 
            for i in range(len(linha_pivo)):
                try:
                    linha_pivo[i] = linha_pivo[i]/pivo
                except ZeroDivisionError:
                    linha_pivo[i] = 10**3

        for linha in base:
            linha_pivo_base = linha[self.PivoW(base)[1]]

            if linha_pivo_base < 0 and linha != linha_pivo:
                for i in range(len(linha)):
                    linha[i] = abs(linha_pivo_base)*linha_pivo[i] + linha[i]

            elif linha_pivo_base > 0 and linha != linha_pivo:
                for i in range(len(linha)):
                    linha[i] = -linha_pivo_base*linha_pivo[i] + linha[i]

        if base[len(base)-1][len(linha_pivo)-1] == 0:
            base.pop(-1)            # DELETANDO A ÚLTIMA LINHA DO 'W' QUE JÁ FOI ZERADA
            for linha in base:
                linha.pop(-2)         # DELETANDO COLUNA COM VALOR DA VARIAVEL ARTIFICIAL

            self.Apresentar_Tabela(base)
            self.Apresentar_Final_Etapa("ELIMINACAO 'W' CONCLUIDA!")

        else:
            self.Apresentar_Tabela(base)
            self.Eliminacao_W(base)
            
        return base

    def Apresentar_Tabela(self, base):
        for i in range(len(base)):
            print(f"LINHA{i} -> {base[i]}")

    def Apresentar_Final_Etapa(self, etapa):
        print(Style.BRIGHT + Fore.RED + 80*'*')
        print('*' + Fore.BLUE + f"                           {etapa}                          " + Fore.RED + '*')
        print(Fore.RED + 80*'*')
        print(Fore.WHITE + Style.RESET_ALL)
