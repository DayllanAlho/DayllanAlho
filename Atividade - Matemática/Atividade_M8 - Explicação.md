# Matemática - Módulo 8

Aqui está o link para a planilha do Google Sheets contendo todos os cálculos e fórmulas relacionados a esta atividade: [Planilha do Google Sheets](https://docs.google.com/spreadsheets/d/1vTbpmiSD1ffZgQQ2k8GGXThORZguCUCF-zRTGJQH0rI/edit?usp=sharing)

# Primeira Questão

Suponha que você está realizando um problema de clusterização usando o algoritmo k-médias em um conjunto de dados no Excel. Você foi solicitado a calcular os centroides de três clusters: C1 = {Marcos, Ana, Silvio}, C2 = {Amanda, Marta}, e C3 = {Ronaldo, Josias, Rose, Claudio}. Os dados das pessoas e os centroides iniciais estão dados na tabela a seguir:

### Tabela

| Pessoa  | Cabelo | Peso  | Idade |
|---------|--------|-------|-------|
| Marcos  | 0      | 113   | 36    |
| Ana     | 10     | 68    | 34    |
| Ronaldo | 2      | 41    | 10    |
| Amanda  | 6      | 35    | 8     |
| Marta   | 4      | 9     | 1     |
| Josias  | 1      | 77    | 70    |
| Rose    | 8      | 73    | 41    |
| Claudio | 10     | 82    | 38    |
| Silvio  | 6      | 91    | 45    |

### Centróides Iniciais

| Cluster   | Cabelo       | Peso        | Idade       |
|-----------|--------------|-------------|-------------|
| Cluster 1 | 5,333333333  | 90,66666667 | 38,33333333 |
| Cluster 2 | 5            | 22          | 4,5         |
| Cluster 3 | 5,25         | 68,25       | 39,75       |

## Resposta

Para calcular os centroides de cada cluster, realizamos a média das características (Cabelo, Peso e Idade) de todas as pessoas em cada cluster. Os centroides são os seguintes:

**Cluster 1 (C1):**
- Cabelo: (0 + 10 + 6) / 3 = 5,333333333
- Peso: (113 + 68 + 91) / 3 = 90,66666667
- Idade: (36 + 34 + 45) / 3 = 38,33333333

**Cluster 2 (C2):**
- Cabelo: (6 + 4) / 2 = 5
- Peso: (35 + 9) / 2 = 22
- Idade: (8 + 1) / 2 = 4,5

**Cluster 3 (C3):**
- Cabelo: (2 + 1 + 8 + 10) / 4 = 5,25
- Peso: (41 + 77 + 73 + 82) / 4 = 68,25
- Idade: (10 + 70 + 41 + 38) / 4 = 39,75

Esses centroides representam as características médias dos pontos de dados em cada cluster e são usados para atualizar a atribuição de pontos aos clusters em cada iteração do algoritmo k-médias.

# Segunda Questão

## Questão

Considerando k = 3 e os centroides x1 = (3,33, 52,33, 15), x2 = (7,33, 63,67, 27,33) e x3 = (5, 80,33, 52), execute o algoritmo k-médias, assumindo que o critério de parada é ter executado 3 iterações.

## Passo a Passo

### 1. Cálculo das Distâncias na 1ª Iteração

Nesta etapa, executamos a 1ª iteração do algoritmo k-médias. Os centroides iniciais são os seguintes:

#### Centróides Iniciais:

| Centróide | Cabelo | Peso  | Idade |
|-----------|--------|-------|-------|
| Centróide 1 | 3,33 | 52,33 | 15   |
| Centróide 2 | 7,33 | 63,67 | 27,33 |
| Centróide 3 | 5    | 80,33 | 52   |

#### Cálculo da Distância para a 1ª Iteração:

| Pessoa | Cabelo | Peso | Idade | Cluster |
|--------|--------|------|-------|---------|
| Marcos | 0      | 113  | 36    | 3       |
| Ana    | 10     | 68   | 34    | 2       |
| Ronaldo | 2     | 41   | 10    | 1       |
| Amanda | 6      | 35   | 8     | 1       |
| Marta  | 4      | 9    | 1     | 1       |
| Josias | 1      | 77   | 70    | 3       |
| Rose   | 8      | 73   | 41    | 3       |
| Claudio | 10    | 82   | 38    | 3       |
| Silvio | 6     | 91   | 45    | 3       |

### 2. Cálculo das Distâncias na 2ª Iteração

Na 2ª iteração, atualizamos os centroides com base na atribuição de clusters da 1ª iteração. Os novos centroides são calculados como a média das características das pessoas em cada cluster.

#### Centróides Após a 1ª Iteração:

| Centróide | Cabelo | Peso  | Idade |
|-----------|--------|-------|-------|
| Centróide 1 | 4   | 28,33 | 6,33  |
| Centróide 2 | 10  | 68    | 34    |
| Centróide 3 | 5   | 87,2  | 46    |

#### Cálculo da Distância para a 2ª Iteração:

| Pessoa | Cabelo | Peso | Idade | Cluster |
|--------|--------|------|-------|---------|
| Marcos | 0      | 113  | 36    | 3       |
| Ana    | 10     | 68   | 34    | 2       |
| Ronaldo | 2     | 41   | 10    | 1       |
| Amanda | 6      | 35   | 8     | 1       |
| Marta  | 4      | 9    | 1     | 1       |
| Josias | 1      | 77   | 70    | 3       |
| Rose   | 8      | 73   | 41    | 3       |
| Claudio | 10    | 82   | 38    | 3       |
| Silvio | 6     | 91   | 45    | 3       |

### 3. Cálculo das Distâncias na 3ª Iteração

Na 3ª iteração, repetimos o processo de atualização dos centroides com base na atribuição de clusters da 2ª iteração.

#### Centróides Após a 2ª Iteração:

| Centróide | Cabelo | Peso  | Idade |
|-----------|--------|-------|-------|
| Centróide 1 | 4   | 28,33 | 6,33  |
| Centróide 2 | 9,33 | 74,33 | 37,67 |
| Centróide 3 | 2,33 | 93,67 | 50,33 |

#### Cálculo da Distância para a 3ª Iteração:

| Pessoa | Cabelo | Peso | Idade | Cluster |
|--------|--------|------|-------|---------|
| Marcos | 0      | 113  | 36    | 3       |
| Ana    | 10     | 68   | 34    | 2       |
| Ronaldo | 2     | 41   | 10    | 1       |
| Amanda | 6      | 35   | 8     | 1       |
| Marta  | 4      | 9    | 1     | 1       |
| Josias | 1      | 77   | 70    | 3       |
| Rose   | 8      | 73   | 41    | 3       |
| Claudio | 10    | 82   | 38    | 3       |
| Silvio | 6     | 91   | 45    | 3       |

## Conclusão

O algoritmo k-médias foi executado por três iterações, atualizando os centroides em cada iteração com base na atribuição de clusters da iteração anterior. Este processo ajuda a agrupar as pessoas em clusters com características semelhantes. Os cálculos detalhados das distâncias para cada iteração foram apresentados.


# Cálculo do Erro Quadrático

Após a 3ª iteração, calculamos o erro quadrático com base nos clusters resultantes da última iteração.

#### Cálculo do Erro Quadrático:

- Cluster 1 (x1): 40,54994814
- Cluster 2 (x2): 18,880991
- Cluster 3 (x3): 56,99331464


# QUESTÕES A SEREM RESPONDIDAS
i. **Qual foi a partição encontrada?**

Na última iteração (3ª iteração), a partição encontrada é a seguinte:

- Cluster 1 (C1): Pessoas mais próximas de X1 (Centroide 1).
  - Ronaldo
  - Amanda
  - Marta

- Cluster 2 (C2): Pessoas mais próximas de X2 (Centroide 2).
  - Ana
  - Rose
  - Claudio

- Cluster 3 (C3): Pessoas mais próximas de X3 (Centroide 3).
  - Marcos
  - Josias
  - Silvio

ii. **Qual é o erro quadrático dessa partição?**

O erro quadrático da partição é calculado após a 3ª iteração e é como segue:
- Cluster 1 (x1): Erro quadrático = 40,54994814
- Cluster 2 (x2): Erro quadrático = 18,880991
- Cluster 3 (x3): Erro quadrático = 56,99331464

iii. **Quais são os centroides que representam a partição encontrada?**

Os centroides que representam a partição encontrada são os centroides da última iteração (3ª iteração). Portanto, são os seguintes:

- Cluster 1 (C1): Centróide 1 (x1): (4, 28,33, 6,33)
- Cluster 2 (C2): Centróide 2 (x2): (9,33	74,33	37,66)
- Cluster 3 (C3): Centróide 3 (x3): (2,33, 93,67, 50,33)

iv. **Quais são os centroides após a primeira iteração?**

Os centroides após a primeira iteração foram calculados da seguinte forma:

- Cluster 1 (C1): Centróide 1 (x1): (4, 28,33, 6,33)
- Cluster 2 (C2): Centróide 2 (x2): (10, 68, 34)
- Cluster 3 (C3): Centróide 3 (x3): (5, 87,2, 46)


v. **Você identifica algum potencial significado dos clusters encontrados?**

Com base nos dados e na divisão dos clusters nas duas iterações, podemos obter alguns insights:

#### Na Média dos Clusters (Após a 1ª Iteração):

- **Cluster 1 (Marcos, Ana, Silvio):**
  - Tem a média mais alta de cabelo (5.33), indicando cabelos de maior comprimento.
  - Tem a média mais alta de peso (90.67), indicando um peso mais alto.
  - Tem a média de idade como segunda mais alta (38.33), sugerindo que esse cluster contém uma média intermediária de idade.

- **Cluster 2 (Amanda, Marta):**
  - Tem a média mais baixa de cabelo (5.00), indicando cabelos de comprimento baixo.
  - Tem a média mais baixa de peso (22.00), indicando um peso mais baixo.
  - Tem a média mais baixa de idade (4.50), sugerindo que esse cluster contém pessoas mais jovens.

- **Cluster 3 (Ronaldo, Josias, Rose, Claudio):**
  - Tem uma média intermediária de cabelo (5.25), indicando cabelos de comprimento médio.
  - Tem uma média intermediária de peso (68.25).
  - Tem uma média mais alta de idade (39.75), indicando idade mais avançada.

### Na 3ª Iteração (Após a 3ª Iteração):

- **Centróide 1 (x1 - Ronaldo, Amanda, Marta):**
  - Tem a média de cabelo intermediário (4.00), indicando cabelos de comprimento relativamente curto.
  - Tem a média mais baixa de peso (28.33), indicando um peso mais baixo.
  - Tem a média mais baixa de idade (6.33), sugerindo que esse cluster contém pessoas mais jovens.

- **Centróide 2 (x2 - Ana, Rose, Claudio):**
  - Tem uma média mais alta de cabelo (9.33), indicando cabelos de comprimento longo.
  - Tem uma média intermediária de peso (74.33), indicando um peso intermediário.
  - Tem uma média intermediária de idade (37.67), sugerindo uma idade intermediária.

- **Centróide 3 (x3 - Marcos, Josias, Silvio):**
  - Tem a média mais baixa de cabelo (2.33), indicando cabelos de comprimento mais curto.
  - Tem a média mais alta de peso (93.67), indicando um peso mais alto.
  - Tem uma média mais alta de idade (50.33), sugerindo que esse cluster contém pessoas mais velhas.

Portanto, com base na divisão dos clusters, podemos inferir que:

- O Cluster 1 (x1) após a 3ª iteração parece conter pessoas mais jovens, com cabelos de comprimento relativamente curto, peso mais baixo.

- O Cluster 2 (x2) após a 3ª iteração parece conter pessoas com idade intermediária, cabelos de comprimento longo e peso intermediário.

- O Cluster 3 (x3) após a 3ª iteração parece conter pessoas mais velhas, com cabelos de comprimento mais curto e peso mais alto.

