import numpy as np
import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = 'dataset_WIFI7.csv'

# Lê o CSV
dados = pd.read_csv(caminho_arquivo)

# Mostra os nomes das colunas
print("Colunas encontradas:", dados.columns.tolist())

# Copia todas as colunas do CSV para arrays
arrays_numpy = {}
for coluna in dados.select_dtypes(include=[np.number]).columns:
    arrays_numpy[coluna] = dados[coluna].to_numpy()

# Exemplo: acesso aos arrays
for nome_coluna, array in arrays_numpy.items():
    print(f"Array da coluna '{nome_coluna}':")
    print(array)

