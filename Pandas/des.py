import pandas as pd

url = "aluguel.csv"

dados = pd.read_csv(url, sep=";")

# Verifica quais as colunas disponiveis
print("\nColunas disponíveis:")
print(dados.columns)

# Usando query para filtrar imóveis com uma ou mais suítes
imoveis_com_suites = dados.query('Suites >= 1')

# Informa o numero total de imóveis com uma ou mais suítes
print(f"\nTotal de imóveis com uma ou mais suítes: {len(imoveis_com_suites)}")
print(imoveis_com_suites.head())

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

dc = dados.query('@imoveis_comerciais in Tipo')

df = dados.query('@imoveis_comerciais not in Tipo')


df['Quartos'].mean()

len(df['Bairro'].unique())

df['Bairro'].nunique()

df.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False)

df_bairros = df.groupby('Bairro')[['Valor']].mean(
).sort_values('Valor', ascending=False).head()

df_bairros.plot(kind='barh', figsize=(14, 10), color='blue')
