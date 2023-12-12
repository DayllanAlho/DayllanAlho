# Comparativo de Ferramentas de Visualização de Dados

## Metabase

| Característica                                     | Metabase                                                |
|-----------------------------------------------------|---------------------------------------------------------|
| Conectividade com Redshift (AWS)                    | Sim, suporte para Redshift e várias outras fontes        |
| Recursos de visualização de fácil manipulação        | Sim, interface intuitiva e fácil de usar                 |
| Custeio da ferramenta                                | Open source, gratuito, com opção de suporte pago         |
| Facilidade de compartilhamento com time de trabalho  | Sim, fácil compartilhamento e colaboração                |
| Característica "Fazendo Ciência"                     | Suporte nativo para consultas SQL e análise exploratória|

### Vantagens:
- Open source e gratuito.
- Suporte a consultas SQL.
- Fácil compartilhamento e colaboração.

### Desvantagens:
- Pode ter menos recursos avançados em comparação com ferramentas pagas.

## Power BI

| Característica                                     | Power BI                                                |
|-----------------------------------------------------|---------------------------------------------------------|
| Conectividade com Redshift (AWS)                    | Sim, suporte para Redshift e várias outras fontes        |
| Recursos de visualização de fácil manipulação        | Sim, ampla variedade de gráficos e recursos              |
| Custeio da ferramenta                                | Licenciamento por usuário, com versão gratuita limitada  |
| Facilidade de compartilhamento com time de trabalho  | Sim, integração com o ecossistema Microsoft              |
| Característica "Fazendo Ciência"                     | Suporte avançado para análise de dados e modelagem       |

### Vantagens:
- Rico em recursos e gráficos.
- Integração com o ecossistema Microsoft.

### Desvantagens:
- Licenciamento por usuário pode se tornar caro com um grande número de usuários.

## SuperSet

| Característica                                     | SuperSet                                                |
|-----------------------------------------------------|---------------------------------------------------------|
| Conectividade com Redshift (AWS)                    | Sim, suporte para Redshift e várias outras fontes        |
| Recursos de visualização de fácil manipulação        | Sim, permite criação de dashboards interativos           |
| Custeio da ferramenta                                | Open source, gratuito, suporte pago disponível          |
| Facilidade de compartilhamento com time de trabalho  | Sim, colaboração em tempo real e compartilhamento fácil  |
| Característica "Fazendo Ciência"                     | Suporte para consultas SQL e visualização exploratória  |

### Vantagens:
- Open source e gratuito.
- Colaboração em tempo real.

### Desvantagens:
- Menos amplamente adotado, potencialmente menos recursos disponíveis.

## QlikView e Qlik Sense

| Característica                                     | QlikView e Qlik Sense                                   |
|-----------------------------------------------------|---------------------------------------------------------|
| Conectividade com Redshift (AWS)                    | Sim, suporte para Redshift e diversas outras fontes      |
| Recursos de visualização de fácil manipulação        | Sim, oferece recursos avançados e visualização in-memory |
| Custeio da ferramenta                                | Modelo de licenciamento, com opção de Qlik Sense Cloud   |
| Facilidade de compartilhamento com time de trabalho  | Sim, colaboração e compartilhamento facilitados          |
| Característica "Fazendo Ciência"                     | Suporte para análise de dados avançada e modelagem       |

### Vantagens:
- Recursos avançados de visualização.
- Modelagem de dados avançada.

### Desvantagens:
- Modelo de licenciamento pode ser caro.



# Configuração do Metabase via Docker

## 1. Criação da Conta:

- Abra o link [Metabase Store](https://store.metabase.com/?redirectTo=%2Faccount).
- Crie a sua conta.

## 2. Instalação Local:

- Após criar a conta, acesse a página inicial

![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/Page%20Init.png)

- Vá para "Documentação" e em seguida "Instalação Overview".

![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/Instalattion.png)

- Alternativamente, acesse o link direto: [Metabase Installation](https://www.metabase.com/docs/latest/installation-and-operation/start).

## 3. Configuração via Docker:

- No guia de instalação, selecione "Running on Docker".

![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/Running%20Metabase%20Docker.png)

## 4. Executando no Terminal:

Abra o terminal do seu computador e execute os seguintes comandos:

```bash
docker pull metabase/metabase:latest
```
posteriormente execute:
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```
E, por último:
```
docker logs -f metabase
```
Esses comandos realizarão o seguinte:

- <b><i>docker pull metabase/metabase:latest:</b></i> Obtém a imagem mais recente do Docker
- <b><i>docker run -d -p 3000:3000 --name metabase metabase/metabase:</b></i> Inicia o contêiner Metabase, expondo-o na porta 3000.
- <b><i>docker logs -f metabase:</b></i> Exibe os logs à medida que o Metabase é inicializado.

## 5. Acessando o Metabase:
Após a inicialização ser concluída, acesse sua instância do Metabase em
``` http://localhost:3000```

## 6. Configurando o Metabase:

- Com a porta configurada, abra o programa do Docker em seu computador.

![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/docker.png)

No meu caso, estou utilizando a porta 12345:3000.
Posteriormente clique em:
```
Let's get started
```
![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/boas%20vindas%20.png)

- Faça as configurações adequadas, como nome, senha, linguagem preferida
![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/config.png)

conecte-se com o Redshift
![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/redshift.png)


Posteriormente, preencha as seguintes informações:

  - **Display name:**
  - **Host:**
  - **Port:**
  - **Database name:**
  - **Schemas:**
    **All:**
  - **Username:**
  - **Password:**

Ao entrar você será direcionado para a tela principal

![Configuração do Redshift](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/tela%20inicial%20do%20metabase.png)

## 7. Tela Principal:

- Você será direcionado para a tela principal, onde já existem alguns caminhos conectados.

## 8. Importando Tabela do Redshift:

- Para importar uma tabela do Redshift, vá para a configuração de admin.

![Configuração do Redshift no Metabase](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/Configura%C3%A7%C3%A3o.png)

- Adicione um novo banco de dados e selecione o Amazon Redshift.
![imagem](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/bancos%20%20no%20metabase.png)

- Insira as informações necessárias do Redshift:

  - **Display name:**
  - **Host:**
  - **Port:**
  - **Database name:**
  - **Schemas:**
  - **All**
  - **Username:**
  - **Password:**


## 9. Desenvolvimento do Dashboard:

Após a configuração bem-sucedida e a conexão efetiva entre o Metabase e o Redshift, é o momento de criar um dashboard eficaz para representar as informações do dataset.

Utilize as poderosas ferramentas do Metabase para construir visualizações significativas e informativas. Explore gráficos, tabelas e outros elementos visuais para transmitir de maneira clara os insights do seu conjunto de dados.

Experimente diferentes tipos de visualizações, aplique filtros e faça agrupamentos para destacar padrões e tendências relevantes.

### Passos para Desenvolver o Dashboard:
1. Acesso ao Banco de Dados:
- Acesse o banco de dados relevante no Metabase e inicie a criação de uma nova visualização.

![selecao do banco](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/Sele%C3%A7%C3%A3o%20do%20banco%20.png)


2. Configuração do Painel:
- Para criar um dashboard efetivo, certifique-se de ter pelo menos duas colunas no painel do Metabase.

![Exemplo de Dashboard no Metabase](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/image.png)

3. Visualização Completa:
- Ao finalizar o processo de configuração, a visualização estará completa, proporcionando uma representação gráfica clara e informativa dos dados.

![mediana da quantidade por produto](https://github.com/DayllanAlho/DayllanAlho/blob/dev/DataViz/imagens/mediana%20da%20quantidade%20por%20produto.png)

## 10. Insights do Gráfico da Mediana da Quantidade por Produto:

O gráfico da mediana da quantidade por produto oferece valiosos insights sobre o estoque. Alguns pontos a serem considerados incluem:

Produtos Mais Comuns:

Itens com mediana de quantidade alta, como açúcar, arroz e leite, são frequentemente adquiridos, refletindo sua importância nas compras cotidianas.
Produtos Menos Frequentes:

Produtos com mediana de quantidade baixa, como jogos de videogame ou teclados, são comprados com menor frequência e podem representar itens mais caros ou de uso ocasional.
Variação Regional:

A mediana da quantidade de produtos pode variar entre diferentes regiões e tipos de lojas, oferecendo insights sobre preferências de compra específicas.