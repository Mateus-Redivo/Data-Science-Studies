# Importando a biblioteca NumPy para manipulação de arrays numéricos
import numpy as np
# Importando Matplotlib para visualização de dados
import matplotlib.pyplot as plt

# Definindo o caminho para o arquivo de dados de referência
url = 'referencia.csv'

# NOTA: Esta linha contém variáveis não definidas (inicio, final, incrementacao)
# Carrega dados do arquivo CSV selecionando colunas específicas baseadas em um intervalo
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(inicio, final + 1, incrementacao))

# Carrega dados do arquivo apples_ts.csv que contém séries temporais de preços de maçãs
# Usa vírgula como delimitador e seleciona as colunas de 1 até 87 (88 exclusivo)
# Provavelmente cada coluna representa uma semana ou período específico
dado = np.loadtxt("apples_ts.csv", delimiter=",", usecols = np.arange(1, 88, 1))

# Transpõe o array (converte linhas em colunas e vice-versa)
# Útil para reorganizar os dados quando precisamos mudar a orientação da matriz
# Após a transposição, as linhas representam períodos e as colunas representam cidades
dado_transposto = dado.T

print(dado.ndim) # Número de dimensões do array (Linhas e Colunas, 1D, 2D, etc.)

print(dado.size) # Número total de elementos no array (linhas × colunas)

print(dado.shape) # Tupla com o tamanho de cada dimensão do array (Linhas, Colunas)

# Cria um array com valores de 1 a 87 que correspondem aos períodos de tempo analisados
datas = np.arange(1, 88, 1)

# Extrai uma submatriz do dado transposto, selecionando todas as linhas (:) e as colunas 1 a 5
# Representa os preços em diferentes cidades ao longo do tempo
precos = dado_transposto[:, 1:6]

# Extrai dados de cada cidade em vetores separados para análise individual
# Cada vetor contém a série temporal completa dos preços de maçãs para uma cidade
Moscow = precos[:, 0]        # Série temporal de preços em Moscou
Kaliningrad = precos[:, 1]   # Série temporal de preços em Kaliningrado
Petersburg = precos[:, 2]    # Série temporal de preços em São Petersburgo
Krasnodar = precos[:, 3]     # Série temporal de preços em Krasnodar
Ekaterinburg = precos[:, 4]  # Série temporal de preços em Ecaterimburgo

# Divide a série temporal de Moscou em segmentos anuais para comparação entre anos
# Cada segmento contém 12 valores (possivelmente mensais)
Moscow_ano1 = Moscow[0:12]   # Dados do primeiro ano para Moscou
Moscow_ano2 = Moscow[12:24]  # Dados do segundo ano para Moscou
Moscow_ano3 = Moscow[24:36]  # Dados do terceiro ano para Moscou
Moscow_ano4 = Moscow[36:48]  # Dados do quarto ano para Moscou

# Cria um gráfico de linhas comparando os preços em Moscou ao longo dos 4 anos
# O eixo X representa os meses (1-12) e o eixo Y representa os preços
plt.plot(np.arange(1, 13, 1), Moscow_ano1, label='Ano 1')
plt.plot(np.arange(1, 13, 1), Moscow_ano2, label='Ano 2')
plt.plot(np.arange(1, 13, 1), Moscow_ano3, label='Ano 3')
plt.plot(np.arange(1, 13, 1), Moscow_ano4, label='Ano 4')
plt.legend(['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4'], loc='upper left')
# plt.show()  # Comentado para evitar exibição automática do gráfico

# Compara os arrays para verificar se os padrões de preço se repetem entre anos
print(np.array_equal(Moscow_ano1, Moscow_ano2)) # Verifica se os preços do ano 1 são idênticos aos do ano 2

print(np.allclose(Moscow_ano3, Moscow_ano4, 10)) # Verifica se os preços dos anos 3 e 4 são similares com tolerância de 10

# Código duplicado removido (verificação de igualdade já feita acima)

# Contagem de valores NaN na série temporal de Kaliningrad
print(sum(np.isnan(Kaliningrad)))

# Interpolação linear para preencher um valor ausente em Kaliningrad (índice 4)
# Calcula a média dos valores vizinhos para substituir o valor ausente
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])  

# Visualiza a série temporal de Kaliningrad após correção do valor ausente
plt.plot(datas, Kaliningrad)  
plt.show()

# Calcula preços médios para Moscou e Kaliningrado para comparação
np.mean(Moscow)
np.mean(Kaliningrad)

# Definição da equação da reta para modelagem linear
# y = ax + b, onde 'a' é o coeficiente angular e 'b' é o coeficiente linear
y = ax + b

# Define o eixo x como as datas (períodos de tempo)
x = datas

# Cria uma linha de tendência linear com coeficiente angular 0.52 e intercepto 80
y = 0.52 * x + 80

# Compara graficamente os dados reais de Moscou com a linha de tendência
plt.plot(datas, Moscow)  # Dados reais
plt.plot(x, y)  # Linha de tendência

# Calcula o erro quadrático médio (RMSE) entre os dados reais e a linha de tendência
# Medida da qualidade do ajuste do modelo linear aos dados
print(np.sqrt(np.sum((np.power(Moscow - y, 2)))))

print(np.linalg.norm(Moscow - y))

# Calcula a norma euclidiana entre os dados reais e o modelo fixo (y = 0.52*x + 80)
# Essa norma representa o erro total do modelo
print(np.linalg.norm(Moscow - y))

# Preparação para regressão linear usando mínimos quadrados
Y = Moscow  # Variável dependente (preços em Moscou)
X = datas   # Variável independente (períodos de tempo)
n = np.size(Moscow)  # Tamanho da amostra

# Cálculo do coeficiente angular (a) usando a fórmula de regressão linear
# Esta é a fórmula de mínimos quadrados para estimar o coeficiente angular
a = ((n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2))

# Cálculo do coeficiente linear (b) usando o coeficiente angular e as médias
b = np.mean(Y) - a * np.mean(X)

# Criação do modelo de regressão linear otimizado
y = a * X + b

# Calcula o erro (norma) do modelo otimizado
print(np.linalg.norm(Moscow - y))

# Adiciona dois pontos específicos no gráfico para destacar previsões do modelo
# Marca com estrela vermelha o valor previsto para o período 41.5
plt.plot(41.5, 41.5 * a + b, '*r')
# Marca com estrela vermelha o valor previsto para um período futuro (100)
plt.plot(100, 100 * a + b, '*r')

# Exibe o gráfico com os dados reais, linha de tendência e pontos marcados
plt.show()

# Gera 100 números inteiros aleatórios entre 40 e 100 (não utilizado no código)
np.random.randint(low = 40, high = 100, size = 100)

# Cria 100 coeficientes angulares aleatórios entre 0.10 e 0.90 para simulação
coef_angulares = np.random.uniform(low = 0.10, high = 0.90, size = 100)

# Inicializa um array vazio para armazenar os erros de cada modelo simulado
norma = np.array([])

# Testa cada coeficiente angular gerado aleatoriamente
for i in range(100):
    # Calcula e armazena o erro (norma) para cada coeficiente angular
    # Mantém o mesmo coeficiente linear (b) calculado anteriormente
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

# Define uma semente para reprodutibilidade dos números aleatórios
np.random.seed(16)

# Combina os erros calculados e seus respectivos coeficientes angulares em um array 2D
dados = np.column_stack([norma, coef_angulares])

# Salva os resultados da simulação em um arquivo CSV para análise posterior
np.savetxt("dados.csv", dados, delimiter = ",")
