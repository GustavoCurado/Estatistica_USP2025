import pandas as pd
import numpy as np

# Lê o CSV
caminho_arquivo = '/home/gustavo/Área de Trabalho/GitHub/Estatistica_USP2025/dataset_WIFI7.csv'
dados = pd.read_csv(caminho_arquivo)

# c1 = Frequência, c8 = S11
c1 = dados.iloc[:, 0].to_numpy()
c8 = dados.iloc[:, 7].to_numpy()

intervalos = []
inicio = None  # Para marcar quando S11 fica <= -10

for i in range(len(c8)):
    if c8[i] <= -10:
        if inicio is None:
            inicio = c1[i]  # Marca a frequência de início do intervalo
    else:
        if inicio is not None:
            fim = c1[i]  # Marca a frequência de fim do intervalo
            intervalos.append((inicio, fim))
            inicio = None  # Reseta para procurar próximo intervalo

# Caso o último valor de c8 seja <= -10, fecha o intervalo no final
if inicio is not None:
    fim = c1[-1]
    intervalos.append((inicio, fim))

print("Intervalos de Frequência onde S11 <= -10 dB:")
for i, (start, end) in enumerate(intervalos, 1):
    size = end - start
    print(f"Intervalo {i}: {start:.3f} GHz até {end:.3f} GHz -> Tamanho do intervalo: {size:.3f} GHz")

# Definir blocos de interesse
bloco1 = intervalos[0:4]  # intervalos 1 a 4 (índices 0 a 3)
bloco3 = intervalos[8:12]  # intervalos 9 a 12 (índices 8 a 11)

# Extrair inícios e finais dos blocos
inicios_bloco1 = np.array([x[0] for x in bloco1])
finais_bloco1 = np.array([x[1] for x in bloco1])
inicios_bloco3 = np.array([x[0] for x in bloco3])
finais_bloco3 = np.array([x[1] for x in bloco3])

# Calcular diferenças entre blocos correspondentes (bloco1 - bloco3)
dif_inicios = inicios_bloco1 - inicios_bloco3
dif_finais = finais_bloco1 - finais_bloco3
dif_combinadas = np.concatenate([dif_inicios, dif_finais])

# Função para calcular média e variância amostral
def estatisticas(dados):
    media = np.mean(dados)
    variancia = np.var(dados, ddof=1)  # ddof=1 para variância amostral
    return media, variancia

media_inicios, var_inicios = estatisticas(dif_inicios)
media_finais, var_finais = estatisticas(dif_finais)
media_comb, var_comb = estatisticas(dif_combinadas)

print("\n\nEstatísticas das diferenças entre a Configuração 1 e a 3:\n")
print(f"Média das diferenças entre inícios: {media_inicios:.6f} GHz")
print(f"Variância amostral das diferenças entre inícios: {var_inicios:.6f} GHz²\n")
print(f"Média das diferenças entre finais: {media_finais:.6f} GHz")
print(f"Variância amostral das diferenças entre finais: {var_finais:.6f} GHz²\n")
print(f"Média das diferenças combinadas (inícios + finais): {media_comb:.6f} GHz")
print(f"Variância amostral das diferenças combinadas: {var_comb:.6f} GHz²")

