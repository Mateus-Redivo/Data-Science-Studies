from scipy.stats import norm  # Importa a distribuição normal da biblioteca scipy
import numpy as np  # Importa numpy para operações matemáticas

'''
EXERCÍCIO 1: DISTRIBUIÇÃO NORMAL - VIDA ÚTIL DE LÂMPADAS
O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída, com média igual a 720 dias e desvio padrão igual a 30 dias. 
Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:

1) Entre 650 e 750 dias
2) Mais que 800 dias
3) Menos que 700 dias
'''

# Parâmetros da distribuição normal
media = 720  # Média da vida útil das lâmpadas (em dias)
desvio_padrao = 30  # Desvio padrão da vida útil (em dias)

# Item A: Probabilidade entre 650 e 750 dias
# Padronização dos valores usando Z = (X - μ) / σ
Z_inferior = (650 - media) / desvio_padrao  # Z para 650 dias
Z_superior = (750 - media) / desvio_padrao  # Z para 750 dias

# P(650 < X < 750) = P(Z_inferior < Z < Z_superior) = F(Z_superior) - F(Z_inferior)
probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print("{0:.2%}".format(probabilidade))  # Exibe resultado em formato percentual

# Item B: Probabilidade de durar mais que 800 dias
Z = (800 - media) / desvio_padrao  # Padronização do valor 800

# P(X > 800) = 1 - P(X ≤ 800) = 1 - F(Z)
probabilidade = 1 - norm.cdf(Z)
print("{0:.2%}".format(probabilidade))

# Item C: Probabilidade de durar menos que 700 dias
Z = (700 - media) / desvio_padrao  # Padronização do valor 700

# P(X < 700) = F(Z)
probabilidade = norm.cdf(Z)
print("{0:.2%}".format(probabilidade))


'''
EXERCÍCIO 2: CÁLCULO DE ÁREAS SOB A CURVA NORMAL PADRÃO
Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python, encontre a área sob a curva normal para os valores de Z abaixo:

1) Z < 1,96
2) Z > 2,15
3) Z < -0,78
4) Z > 0,59
'''

# Item A: P(Z < 1,96)
# norm.cdf() calcula a função de distribuição acumulada
probabilidade = norm.cdf(1.96)
print("{0:0.4f}".format(probabilidade))

# Item B: P(Z > 2,15)
# P(Z > 2,15) = 1 - P(Z ≤ 2,15)
probabilidade = 1 - norm.cdf(2.15)
# Alternativa: norm.sf(2.15) calcula diretamente a função de sobrevivência
print("{0:0.4f}".format(probabilidade))

# Item C: P(Z < -0,78)
probabilidade = norm.cdf(-0.78)
print("{0:0.4f}".format(probabilidade))

# Item D: P(Z > 0,59)
probabilidade = 1 - norm.cdf(0.59)
# Alternativa: norm.sf(0.59)
print("{0:0.4f}".format(probabilidade))

'''
EXERCÍCIO 3: MARGEM DE ERRO PARA ESTIMATIVA DE MÉDIA
Para estimar o valor médio gasto por cada cliente de uma grande rede de fast-food, foi selecionada uma amostra de 50 clientes.

Assumindo que o valor do desvio padrão da população seja de R$ 6,00 e que esta população se distribui normalmente, 
obtenha a margem de erro desta estimativa para um nível de confiança de 95%.
'''

# Para 95% de confiança, α = 0,05, logo α/2 = 0,025
# O valor crítico Z é o percentil 97,5% (1 - 0,025) da distribuição normal padrão
z = norm.ppf(0.975)  # norm.ppf() calcula o percentil inverso (quantil)

# Parâmetros do problema
desvio_padrao = 6  # Desvio padrão populacional em R$
n = 50  # Tamanho da amostra

# Cálculo da margem de erro: E = Z * (σ / √n)
# Onde σ / √n é o erro padrão da média
e = z * (desvio_padrao / np.sqrt(n))
print("R$ {0:0.2f}".format(e))

'''
EXERCÍCIO 4: INTERVALO DE CONFIANÇA PARA A MÉDIA POPULACIONAL
Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída, 
com desvio padrão populacional igual a 11, resultou em uma média amostral de 28.

Qual o intervalo de confiança de 90% para a média populacional?
'''

# Parâmetros do problema
media_amostral = 28  # Média calculada da amostra
desvio_padrao = 11  # Desvio padrão conhecido da população
n = 1976  # Tamanho da amostra

# norm.interval() calcula diretamente o intervalo de confiança
# confidence: nível de confiança (90% = 0.90)
# loc: centro da distribuição (média amostral)
# scale: erro padrão da média (σ / √n)
intervalo_confianca = norm.interval(
    confidence=0.90, loc=media_amostral, scale=desvio_padrao / np.sqrt(n))
print("Intervalo de 90% de confiança para a média populacional:", intervalo_confianca)


'''
EXERCÍCIO 5: CÁLCULO DO TAMANHO DA AMOSTRA
O valor do gasto médio dos clientes de uma loja de conveniência é de R$ 45,50. 
Assumindo que o desvio padrão dos gastos é igual a R$ 15,00, 
qual deve ser o tamanho da amostra para estimarmos a média populacional com um nível de significância de 10%?

Considere que o erro máximo aceitável seja de 10%.
'''

# Parâmetros do problema
media = 45.5  # Média populacional conhecida em R$
sigma = 15  # Desvio padrão populacional em R$
significancia = 0.10  # Nível de significância (α = 10%)
confianca = 1 - significancia  # Nível de confiança (90%)

# Cálculo do valor crítico Z para 90% de confiança
# Para 90% de confiança: α = 0.10, α/2 = 0.05
# Z crítico corresponde ao percentil 95% (0.5 + 0.45) da distribuição normal padrão
z = norm.ppf(0.5 + (confianca / 2))

# Cálculo do erro máximo aceitável
erro_percentual = 0.10  # 10% da média como erro máximo
e = media * erro_percentual  # Erro absoluto: 10% de R$ 45,50 = R$ 4,55

# Cálculo do tamanho da amostra usando a fórmula: n = (Z * σ / E)²
# Onde: Z = valor crítico, σ = desvio padrão populacional, E = erro máximo
n = (z * (sigma / e)) ** 2
print("Tamanho da amostra necessário:", n.round())

''''
Um fabricante de farinha verificou que, 
em uma amostra aleatória formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos, 
apresentou um desvio padrão amostral do peso igual a 480 g.

Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de confiança igual a 95%,
 qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?

'''

N = 2000  # Tamanho total da população
z = norm.ppf((0.5 + (0.95 / 2)))  # Valor crítico Z para 95% de confiança
s = 0.48  # Desvio padrão amostral em kg (480 g = 0.48 kg)
e = 0.3  # Erro máximo aceitável em kg

# Cálculo do tamanho da amostra usando a fórmula de amostragem para proporções finitas
n = ((z ** 2) * (s ** 2) * (N)) / \
    (((z ** 2) * (s ** 2)) + ((e ** 2) * (N - 1)))
print("Tamanho da amostra necessário:", int(n.round()))
