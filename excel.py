import pandas as pd
from openpyxl import Workbook
import numpy as np
import io
import ast

# Função que identifica matrizes na string de saída
def extract_matrices(output):
    matrices = []
    lines = output.split('\n')
    current_matrix = []
    for line in lines:
        try:
            # Tenta converter a linha para uma lista
            row = ast.literal_eval(line.strip())
            if isinstance(row, list):
                current_matrix.append(row)
            else:
                if current_matrix:
                    matrices.append(current_matrix)
                    current_matrix = []
        except:
            if current_matrix:
                matrices.append(current_matrix)
                current_matrix = []
    if current_matrix:
        matrices.append(current_matrix)
    return matrices

# Redirecionar a saída de print para um objeto StringIO
output_buffer = io.StringIO()
print_output = [
    "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
    "[[10, 11, 12], [13, 14, 15], [16, 17, 18]]"
]

for matrix in print_output:
    print(matrix, file=output_buffer)

# Obter o valor do buffer de saída
output_value = output_buffer.getvalue()

# Extrair matrizes da saída
matrices = extract_matrices(output_value)

# Criar um novo arquivo Excel
workbook = Workbook()
writer = pd.ExcelWriter('matrizes.xlsx', engine='openpyxl')
writer.book = workbook

# Salvar cada matriz em uma aba (sheet) diferente
for i, matrix in enumerate(matrices):
    df = pd.DataFrame(matrix)
    sheet_name = f'Sheet{i+1}'
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# Salvar o arquivo Excel
writer.save()

print("Matrizes salvas em matrizes.xlsx")
