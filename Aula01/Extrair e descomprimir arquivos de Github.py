import pandas as pd

url_dados = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

#comando para importar e descomprimir o arquivo em que indicamos no caminho da url_dados
dados = pd.read_csv(url_dados, compression = 'zip')

#comando para exibir o conteúdo de dados
dados

#comandos para exibir os 5 primeiros dados da tabela
dados.head

#comando para exibir quantas linhas e colunas a base possui
dados.shape

#imprime somente a colunas
dados['tratamento']

#retorna os valores únicos da coluna tratamento
dados['tratamento'].unique()

#retorna os valores únicos da coluna tempo
dados['tempo'].unique()

#retorna os valores únicos da coluna dose
dados['dose'].unique()

#retorna os valores únicos da coluna droga
dados['droga'].unique()

#retorna os valores únicos da coluna 'g-0'
dados['g-0'].unique()

#conta quantas vezes cada valor apareceu na coluna
dados['tratamento'].value_counts()

###Desafio 01: Investigar por que a classe tratamento é tão desbalanceada?

###Desafio 02: Plotar as 5 últimas linhas da tabela

###Desafio 03: Calcular a proporção das classes tratamento. (Investigando a documentação do Pandas, dica: usar o value_counts)

###Desafio 04: Quantos tipos de drogas foram investigados?

###Desafio 05: Procurar na Documentação do pandas o método query.

###Desafio 06: Renomear as colunas tirando o hífen.

###Desafio 07: Deixar os gráficos bonitões (título, label e etc, procurando no Matplotlib.pyplot)

#comando para plottar o gráfico de pizza
dados['tratamento'].value_counts().plot.pie()
dados['tempo'].value_counts().plot.pie()

#comando para plotar o gráfico de barras
dados['tempo'].value_counts().plot.bar()

#Verifica quais das linhas são maiores do que 0 e quais são menores
dados['g-0'] > 0

#Imprime apenas as linhas em que os valores de 'g-0' são maiores que 0
#Este filtro não elimina as linhas da tabela original
dados[dados['g-0'] > 0]

#Armazena os valores filtrados em uma nova variável
dados_filtrados = dados[dados['g-0'] > 0]
