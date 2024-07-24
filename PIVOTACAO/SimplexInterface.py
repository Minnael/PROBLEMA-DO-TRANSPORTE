import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from ttkthemes import ThemedTk
from colorama import Fore, Back, Style

class SimplexInterface:
   def criar_matriz(self, m, n):
      janela = ThemedTk(theme="equilux")
      janela.title("SIMPLEX DUAS FASES")

      # Ajustando a largura e altura da janela em função da quantidade de células
      largura = 50 * n + 50  # 50 pixels por célula, mais 50 pixels de margem
      altura = 40 * m + 50   # 30 pixels por célula, mais 50 pixels de margem
      largura_tela = janela.winfo_screenwidth()
      altura_tela = janela.winfo_screenheight()
      pos_x = (largura_tela // 2) - (largura // 2)
      pos_y = (altura_tela // 2) - (altura // 2)
      janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
    
      # Configuração do estilo
      estilo = ttk.Style()
      estilo.configure("TEntry", foreground="white", background="black", fieldbackground="black")
      janela.configure(bg="darkgrey")
      fonte_negrito = Font(family="Arial", size=12, weight="bold")

      entradas = []

      for i in range(m):
         linha = []
         for j in range(n):
            entrada = ttk.Entry(janela, width=4, style="TEntry", font=fonte_negrito)
            entrada.grid(row=i, column=j, padx=5, pady=5)
            linha.append(entrada)
         entradas.append(linha)

      def enviar():
         matriz = []
         for linha in entradas:
            valores_linha = []
            for entrada in linha:
               valor = entrada.get()
               valores_linha.append(float(valor))  # ou int(valor) se preferir inteiros
            matriz.append(valores_linha)
         janela.matriz = matriz
         janela.destroy()

      botao = ttk.Button(janela, text="Enviar", command=enviar)
      botao.grid(row=m, columnspan=n, pady=10)

      # Centralizando as células de entrada da matriz
      janela.grid_rowconfigure(0, weight=1)
      janela.grid_rowconfigure(m, weight=1)

      for i in range(1, m):
         janela.grid_rowconfigure(i, weight=1)

      janela.grid_columnconfigure(0, weight=1)
      janela.grid_columnconfigure(n, weight=1)

      for j in range(1, n):
         janela.grid_columnconfigure(j, weight=1)

      janela.mainloop()
      return janela.matriz
