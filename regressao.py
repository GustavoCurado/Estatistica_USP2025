import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Lê o CSV
caminho_arquivo = '/home/gustavo/Área de Trabalho/GitHub/Estatistica_USP2025/dataset_WIFI7.csv'
dados = pd.read_csv(caminho_arquivo)

# Configurações
graus = [3, 20]  # Grau 3 e Grau 10
blocos = [(0, 1000), (1000, 2000), (2000, 3000)]

fig, axs = plt.subplots(2, 3, figsize=(18, 10))

for row, grau in enumerate(graus):
    for col, (start, end) in enumerate(blocos):
        x = dados.iloc[start:end, 0]  # Frequência
        y = dados.iloc[start:end, 7]  # S11

        # Regressão polinomial
        coef = np.polyfit(x, y, grau)
        polinomio = np.poly1d(coef)

        # Valores ajustados para o gráfico
        x_lin = np.linspace(x.min(), x.max(), 500)
        y_pred = polinomio(x_lin)

        # Calcular R²
        y_ajustado = polinomio(x)
        r2 = r2_score(y, y_ajustado)

        # Plotar
        ax = axs[row, col]
        ax.scatter(x, y, s=10, label='Dados Originais', color='blue')
        ax.plot(x_lin, y_pred, color='red', linewidth=2, label=f'Ajuste grau {grau}')
        ax.set_title(f'Bloco {col+1} (n={start}-{end})\nGrau {grau}, R²={r2:.3f}')
        ax.set_xlabel('Frequência (GHz)')
        ax.set_ylabel('S11 (dB)')
        ax.legend()
        ax.grid()

plt.tight_layout()
plt.show()

