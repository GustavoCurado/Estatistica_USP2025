import pandas as pd
from scipy.stats import spearmanr, kendalltau, pearsonr

# Lê o CSV
caminho_arquivo = '/home/gustavo/Área de Trabalho/GitHub/Estatistica_USP2025/dataset_WIFI7.csv'
dados = pd.read_csv(caminho_arquivo)

# Seleção das colunas
c1 = dados.iloc[:, 0]  # Frequência
c8 = dados.iloc[:, 7]  # S11

# Função para calcular e exibir correlações
def calcular_correlacoes(x, y, descricao=''):
    rho, pval = spearmanr(x, y)
    tau, pval_k = kendalltau(x, y)
    r, pval_p = pearsonr(x, y)
    
    print(f"\n{descricao}")
    print(f"Spearman: {rho:.3f}, p-valor: {pval:.3f}")
    print(f"Kendall: {tau:.3f}, p-valor: {pval_k:.3f}")
    print(f"Pearson: {r:.3f}, p-valor: {pval_p:.3f}")

# Correlação Global
calcular_correlacoes(c1, c8, descricao='Correlação Global')

# Correlação para n=0 até 1000
calcular_correlacoes(c1[:1000], c8[:1000], descricao='Correlação Bloco 1 (n=0 a 1000)')

# Correlação para n=1000 até 2000
calcular_correlacoes(c1[1000:2000], c8[1000:2000], descricao='Correlação Bloco 2 (n=1000 a 2000)')

# Correlação para n=2000 até 3000
calcular_correlacoes(c1[2000:3000], c8[2000:3000], descricao='Correlação Bloco 3 (n=2000 a 3000)')
