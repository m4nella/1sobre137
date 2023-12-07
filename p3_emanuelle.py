# -*- coding: utf-8 -*-
"""P3_EMANUELLE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zqkS9Bn7jqLGr7vHdTMpXKpw6bil2nrB

## Prova 3 - Pt. 2

### Instruções

1. Salve uma cópia do notebook
2. Renomeie o notebook no seguinte formato: P3_NOME.ipynb
3. Preencha a célula abaixo com suas informações
4. Responda as questões
5. Salve o arquivo .ipynb na sua máquina
6. Envie o arquivo na tarefa aberta no canvas

**Nome:**

**RA:**

## Spotify 2023

O conjunto de dados que será analisado pode ser encontrado no seguinte link:

https://raw.githubusercontent.com/caio-c-silva/algoritmos/main/notebooks_atividades/spotify-2023_modificado.csv

Os dados apresentam as músicas mais reproduzidas em 2023 segundo o Spotify. Abaixo segue uma descrição de cada coluna.

| Coluna  | Comentário    |
|------|------|
|   `titulo`  | Título da Música|
|`artista` | Artista que gravou a música. Algumas músicas foram gravadas por mais de um artista (feat.)|
|`ano` | Ano de lançamento da música|
|`mes` | Mês de lançamento da música|
|`dia` | Dia do mês em que a música foi lançada|
|`bpm` | Número de beats por minuto|
|`tom` | A tonalidade em que a música foi gravada|
|`modo` | O modo (maior ou menor) em que a música foi gravada|
|`reproducoes_milhoes` | Número de reproduções de cada música apresentado em milhões de reproduções|

Utilizando a biblioteca `pandas`, responda as seguintes perguntas:

1. Crie um novo dataframe contendo as 5 músicas mais reproduzidas que foram gravadas pelo cantor Bruno Mars.
"""

import pandas as pd

link_csv = 'https://raw.githubusercontent.com/caio-c-silva/algoritmos/main/notebooks_atividades/spotify-2023_modificado.csv'

df = pd.read_csv(link_csv)
print(df)

df_bruno = df[df['artista'].str.contains('bruno mars')]
top5 = df_bruno.nlargest(5, 'reproducoes_milhoes')
print(top5)

"""2. Faça um gráfico de pizza mostrando os dados que foram selecionados no item 1."""

top5[[('reproducoes_milhoes')]].plot(kind='pie',
                                                    subplots=True,
                                                  autopct="%.2f",
                                                  fontsize=10,
                                                  ylabel='',
                                               legend=False)

"""3. Considerando as 5 músicas mais reproduzidas que foram gravadas pelo cantor Bruno Mars, qual a média do andamento das músicas em bpm."""

top5['bpm'].mean()

"""4. Considerando as 5 músicas mais reproduzidas que foram gravadas pelo cantor Bruno Mars, qual a soma total de reproduções."""

top5.groupby('reproducoes_milhoes').sum()

"""5. Considerando as 5 músicas mais reproduzidas que foram gravadas pelo cantor Bruno Mars, mostre a soma de reproduções agrupadas por ano."""

top5.groupby('ano')[['reproducoes_milhoes']].sum()