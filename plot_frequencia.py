import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
caminho_arquivo = '/home/gustavo/Área de Trabalho/GitHub/Estatistica_USP2025/dataset_WIFI7.csv'

# Lê o CSV
dados = pd.read_csv(caminho_arquivo)

c1 = dados.iloc[:, 0].to_numpy()
c2 = dados.iloc[:, 1].to_numpy()
c3 = dados.iloc[:, 2].to_numpy()
c4 = dados.iloc[:, 3].to_numpy()
c5 = dados.iloc[:, 4].to_numpy()
c6 = dados.iloc[:, 5].to_numpy()
c7 = dados.iloc[:, 6].to_numpy()
c8 = dados.iloc[:, 7].to_numpy()

print("c1:", c1)
print("c2:", c2)
print("c3:", c3)
print("c4:", c4)
print("c5:", c5)
print("c6:", c6)
print("c7:", c7)
print("c8:", c8)

fig, ax = plt.subplots(1,3, figsize=(15, 5))

ax[0].scatter(c1[:1000], c8[:1000], s=1)
ax[1].scatter(c1[1000:2000], c8[1000:2000], s=1)
ax[2].scatter(c1[2000:3000], c8[2000:3000], s=1)

ax[0].set_title("Frequência (GHz) x S11 de n=0 até 1000")
ax[1].set_title("Frequência (GHz) x S11 de n=1000 até 2000")
ax[2].set_title("Frequência (GHz) x S11 de n=2000 até 3000")

ax[0].grid()
ax[1].grid()
ax[2].grid()

plt.show()
