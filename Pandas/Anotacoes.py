import pandas as pd  # Importando a biblioteca pandas para manipulação de dados tabulares

# Definindo o caminho do arquivo CSV (local ou remoto)
# url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
url = "aluguel.csv"  # Usando arquivo local para leitura dos dados

# Carregando o arquivo CSV com separador ponto e vírgula para um DataFrame
dados = pd.read_csv(url, sep=";")

# Exibindo as 5 primeiras linhas para verificar a estrutura inicial dos dados
print(dados.head())

# Exibindo as 5 últimas linhas para verificar consistência ao final do dataset
print(dados.tail())

print(type(dados))  # Verificando o tipo do objeto 'dados' (deve ser um DataFrame)

print(dados.shape)  # Obtendo as dimensões do DataFrame: (linhas, colunas)

# Listando todos os nomes das colunas disponíveis no DataFrame
print(dados.columns)

# Mostrando informações detalhadas: colunas, tipos de dados e valores não-nulos
print(dados.info())

# Acessando uma coluna específica do DataFrame pelo nome
print(dados["Nome da coluna desejada"])

# Acessando múltiplas colunas simultaneamente usando lista de nomes
print(dados[["Nome da coluna 1", "Nome da coluna 2"]])

# Análise estatística: agrupando por tipo de imóvel e calculando médias de todas as colunas numéricas
print(dados.groupby("Tipo").mean(numeric_only=True))

# Análise específica: calculando apenas a média dos valores de aluguel por tipo de imóvel
print(dados.groupby("Tipo")["Valor"].mean())

# Análise ordenada: obtendo médias de valores por tipo, organizadas em ordem crescente
print(dados.groupby("Tipo")[["Valor"]].mean().sort_values(by="Valor"))

# Criando um novo DataFrame com as médias de valores por tipo de imóvel, ordenado do mais barato ao mais caro
df_preco_tipo = dados.groupby("Tipo")[["Valor"]].mean().sort_values(by="Valor")

# Visualização: gerando gráfico de barras para comparar visualmente os preços médios por tipo
# Personalizado com tamanho grande (14x10) e cor roxa para melhor visualização
df_preco_tipo.plot(kind="bar", figsize=(14, 10), color="purple")

# Lista de categorias de imóveis classificados como comerciais para filtrar o dataset
imoveis_comerciais = [
    'Conjunto Comercial/Sala',
    'Prédio Inteiro',
    'Loja/Salão',
    'Galpão/Depósito/Armazém',
    'Casa Comercial',
    'Terreno Padrão',
    'Loja Shopping/ Ct Comercial',
    'Box/Garagem',
    'Chácara',
    'Loteamento/Condomínio',
    'Sítio',
    'Pousada/Chalé',
    'Hotel',
    'Indústria'
]

# Exibindo todos os tipos de imóveis únicos presentes no dataset original
print(dados.Tipo.unique())

# Filtrando dataset para manter APENAS imóveis comerciais (usando query com variável externa @)
dc = dados.query('@imoveis_comerciais in Tipo')

# Verificando os tipos únicos após filtragem (deve conter apenas imóveis comerciais)
print(dc.Tipo.unique())

# Filtrando dataset para manter APENAS imóveis NÃO comerciais (complemento do filtro anterior)
df = dados.query('@imoveis_comerciais not in Tipo')

# Verificando os tipos únicos após filtragem (deve conter apenas imóveis residenciais)
print(df.Tipo.unique())

# Exibindo a contagem de cada tipo de imóvel no DataFrame filtrado (não comerciais)
print(df.Tipo.value_counts(normalize=True))

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

print(df_percentual_tipo)

df_percentual_tipo.plot(kind='barh', figsize=(14, 10), color = 'green', xlabel='Tipo', ylabel='Percentual')

df = df.query('Tipo == "Apartamento"')

print(df.head())



