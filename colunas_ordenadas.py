#Esse código lê os dados do CSV e plot os dados de cada coluna de forma ordenada

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

fig, ax = plt.subplots(2,4, figsize=(5, 25))

ax[0][0].plot(range(c8.size), np.sort(c1))
ax[0][1].plot(range(c8.size), np.sort(c2))
ax[0][2].plot(range(c8.size), np.sort(c3))
ax[0][3].plot(range(c8.size), np.sort(c4))
ax[1][0].plot(range(c8.size), np.sort(c5))
ax[1][1].plot(range(c8.size), np.sort(c6))
ax[1][2].plot(range(c8.size), np.sort(c7))
ax[1][3].plot(range(c8.size), np.sort(c8))

ax[0][0].set_title("Frequency (Ghz)")
ax[0][1].set_title("Length of patch (mm)")
ax[0][2].set_title("Width of patch (mm)")
ax[0][3].set_title("Length of Substrate (mm)")
ax[1][0].set_title("Width of Substrate (mm)")
ax[1][1].set_title("Area of Slots (mm^2)")
ax[1][2].set_title("Radius of Circular Slot (mm)")
ax[1][3].set_title("S11 (dB)")

ax[0][0].grid()
ax[0][1].grid()
ax[0][2].grid()
ax[0][3].grid()
ax[1][0].grid()
ax[1][1].grid()
ax[1][2].grid()
ax[1][3].grid()

plt.show()
