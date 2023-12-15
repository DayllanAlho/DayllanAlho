# SQL Study Guide
## Introdução

Este guia visa fornecer uma visão abrangente sobre SQL, com ênfase em Common Table Expressions (CTEs) e junção de múltiplas tabelas. O conteúdo abordará conceitos fundamentais, práticas e exemplos de consultas SQL, com foco especial em juntar três ou mais tabelas usando CTE.

# Conteúdo
## 1. CTE (Common Table Expression)

### 1.1 O que é CTE?
CTE, ou Common Table Expression, é uma expressão temporária que pode ser referenciada em uma consulta SELECT, INSERT, UPDATE ou DELETE. Ela ajuda a simplificar consultas complexas e a tornar o código mais legível.

### 1.2 Exemplo Prático - CTE
Considere o seguinte exemplo:
```
WITH TABELACTE AS (
    SELECT
        tabela1.coluna1,
        tabela2.coluna2
    FROM
        tabela1
    INNER JOIN
        tabela2 ON tabela1.chave = tabela2.chave
)
SELECT * FROM TABELACTE;
```

Neste exemplo, TABELACTE é uma CTE que combina colunas específicas de tabela1 e tabela2 usando um INNER JOIN.

## 2. INNER JOIN, LEFT JOIN e RIGHT JOIN
### 2.1 INNER JOIN
O INNER JOIN retorna apenas as linhas que têm correspondência em ambas as tabelas à esquerda e à direita. Exemplo:
```
SELECT *
FROM tabela1
INNER JOIN tabela2 ON tabela1.chave = tabela2.chave;
```

### 2.2 LEFT JOIN
O LEFT JOIN retorna todas as linhas da tabela à esquerda e as linhas correspondentes da tabela à direita. Se não houver correspondência, as colunas da tabela à direita terão valores nulos.

```
SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.chave = tabela2.chave;
```

### 2.3 RIGHT JOIN
O RIGHT JOIN retorna todas as linhas da tabela à direita e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, as colunas da tabela à esquerda terão valores nulos.
```
SELECT *
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.chave = tabela2.chave;
```

## 3. Junção de Três ou Mais Tabelas usando CTE
Para juntar três ou mais tabelas, você pode expandir a lógica de junção em uma CTE. Considere o exemplo abaixo, onde tabela3 é adicionada à mistura:
```
WITH TABELACTE AS (
    SELECT
        tabela1.coluna1,
        tabela2.coluna2,
        tabela3.coluna3
    FROM
        tabela1
    INNER JOIN
        tabela2 ON tabela1.chave = tabela2.chave
    INNER JOIN
        tabela3 ON tabela2.chave = tabela3.chave
)
SELECT * FROM TABELACTE;
```
Neste exemplo, a CTE TABELACTE junta três tabelas usando INNER JOIN entre tabela1, tabela2 e tabela3.

# Conclusão
Este guia fornece uma base sólida para entender os conceitos de CTE e junção de tabelas em SQL. Pratique esses conceitos com diferentes conjuntos de dados para aprimorar suas habilidades. Lembre-se de adaptar os exemplos à sintaxe específica do sistema de gerenciamento de banco de dados que você está usando (por exemplo, MySQL, PostgreSQL, SQL Server). Boa sorte em sua prova de programação!

## 4. Funções Agregadas
- SUM, AVG, COUNT, MAX, MIN: Compreensão e aplicação dessas funções para realizar cálculos agregados.
```
SELECT COUNT(*), AVG(valor)
FROM tabela;
```

As funções agregadas são utilizadas para realizar cálculos em conjuntos de dados, geralmente agrupando ou resumindo informações. Aqui estão algumas das funções agregadas comuns:

- SUM: Calcula a soma dos valores em uma coluna.
- AVG: Calcula a média dos valores em uma coluna.
- COUNT: Conta o número de linhas em um conjunto de resultados.
- MAX: Retorna o valor máximo em uma coluna.
- MIN: Retorna o valor mínimo em uma coluna.

- *SELECT COUNT(): Esta parte da consulta está utilizando a função COUNT()*, que conta o número total de linhas na coluna especificada. No exemplo, está contando o número total de linhas na tabela.

- AVG(valor): Esta parte da consulta está utilizando a função AVG(valor), que calcula a média dos valores na coluna especificada. No exemplo, está calculando a média dos valores contidos na coluna chamada valor.

- FROM tabela: Indica a tabela da qual os dados serão selecionados. No exemplo, substitua "tabela" pelo nome real da tabela em seu banco de dados.


<b>Exemplo Prático:</b>
Suponhamos que tenhamos a seguinte tabela chamada vendas:
```
id	valor
1	100
2	150
3	200
```
Ao executar a consulta acima (SELECT COUNT(*), AVG(valor) FROM vendas;), obteríamos:

- COUNT(*): 3 (pois há 3 linhas na tabela).
- AVG(valor): (100 + 150 + 200) / 3 = 150 (média dos valores na coluna "valor").

## 5. Filtros e Cláusulas WHERE
- WHERE: Uso de condições para filtrar resultados.
```
SELECT coluna
FROM tabela
WHERE condicao;
```
Explicação Detalhada:
SELECT coluna: Indica a coluna da qual você deseja selecionar dados. Substitua "coluna" pelo nome real da coluna desejada.

FROM tabela: Indica a tabela da qual você deseja selecionar dados. Substitua "tabela" pelo nome real da tabela em seu banco de dados.

WHERE condicao: Esta parte da consulta é onde você adiciona uma condição para filtrar os resultados. Substitua "condicao" por uma expressão que as linhas devem atender para serem incluídas no resultado.

<b>Exemplo Prático</b>:
Suponha que tenhamos uma tabela chamada produtos:
```
id	nome	preço
1	Produto A	50
2	Produto B	80
3	Produto C	30
```

Ao executar a seguinte consulta SQL:
```
SELECT nome
FROM produtos
WHERE preço > 50;
```
A consulta retornará os nomes dos produtos onde o preço é maior que 50. O resultado seria:
```
nome
------
Produto B
```

Neste exemplo, a condição especificada na cláusula WHERE foi preço > 50, então apenas o "Produto B" foi incluído no resultado, pois é o único produto com preço maior que 50.

## 6. Ordenação de Resultados - ORDER BY
A cláusula ORDER BY é usada para ordenar os resultados de uma consulta com base em uma ou mais colunas. Você pode especificar a ordenação como ascendente (ASC) ou descendente (DESC). Aqui está uma explicação detalhada do código:

- ORDER BY: Ordenação ascendente ou descendente dos resultados.
```
SELECT coluna
FROM tabela
ORDER BY coluna ASC;
```

<b>Explicação Detalhada:</b>

**SELECT coluna**: Indica a coluna da qual você deseja selecionar dados. Substitua "coluna" pelo nome real da coluna desejada.

FROM tabela: Indica a tabela da qual você deseja selecionar dados. Substitua "tabela" pelo nome real da tabela em seu banco de dados.

**ORDER BY coluna ASC**: Esta parte da consulta especifica a coluna pela qual os resultados serão ordenados e a direção da ordenação (*ASC para ascendente, DESC para descendente*). Substitua "coluna" pelo nome real da coluna pela qual deseja ordenar.

**Exemplo Prático**:
Suponha que tenhamos uma tabela chamada clientes:
```
id	nome	idade
1	Cliente A	25
2	Cliente B	30
3	Cliente C	22
```

Ao executar a seguinte consulta SQL:
```
SELECT nome
FROM clientes
ORDER BY idade ASC;
```
A consulta retorna os nomes dos clientes ordenados pela idade de forma ascendente. O resultado seria:
```
nome
------
Cliente C
Cliente A
Cliente B
```
Neste exemplo, a cláusula ORDER BY foi utilizada para ordenar os resultados pela coluna idade em ordem ascendente.

## 7. Agrupamento de Dados - GROUP BY e HAVING
A cláusula GROUP BY é usada para agrupar os resultados com base em uma ou mais colunas, enquanto a cláusula HAVING é usada para filtrar grupos específicos resultantes do agrupamento. Aqui está uma explicação detalhada do código:

- GROUP BY: Agrupamento de resultados com base em uma ou mais colunas.
- HAVING: Aplicação de condições para filtrar grupos específicos.

```
SELECT coluna, COUNT(*)
FROM tabela
GROUP BY coluna
HAVING COUNT(*) > 1;
```
**Explicação Detalhada**:
SELECT coluna, COUNT(*): Indica as colunas que serão selecionadas na consulta. A função COUNT(*) conta o número de linhas em cada grupo.

*FROM tabela*: Indica a tabela da qual você deseja selecionar dados. Substitua "tabela" pelo nome real da tabela em seu banco de dados.

*GROUP BY coluna*: Agrupa os resultados com base na coluna especificada. Neste exemplo, a consulta agrupa os resultados pela coluna chamada "coluna".

*HAVING COUNT(*) > 1*: Esta parte da consulta aplica uma condição aos grupos resultantes do agrupamento. Neste caso, apenas grupos com mais de uma linha são incluídos no resultado.

**Exemplo Prático**:

Suponha que tenhamos uma tabela chamada pedidos:
```
id	produto	quantidade
1	Produto A	3
2	Produto B	2
3	Produto A	5
```
Ao executar a seguinte consulta SQL:
```
SELECT produto, COUNT(*)
FROM pedidos
GROUP BY produto
HAVING COUNT(*) > 1;
```
A consulta retornará os produtos que aparecem em mais de um pedido e o número de pedidos para cada produto. O resultado seria:
```
produto   | COUNT(*)
-----------|---------
Produto A  | 2
```
Neste exemplo, a consulta agrupa os resultados pela coluna produto e inclui apenas os grupos (produtos) que têm mais de uma entrada (COUNT(*) > 1) no resultado final.

## 8. Subconsultas
As subconsultas são consultas SQL aninhadas dentro de uma consulta externa. Elas podem ser correlacionadas, onde a subconsulta faz referência a colunas da consulta externa, ou não correlacionadas, onde a subconsulta é independente da consulta externa. Aqui está uma explicação detalhada do código:

- Subconsultas correlacionadas e não correlacionadas: Uso de subconsultas para realizar consultas mais complexas.
```
SELECT coluna
FROM tabela
WHERE coluna IN (SELECT coluna FROM outra_tabela);
```

**Explicação Detalhada**:

SELECT coluna: Indica a coluna que será selecionada na consulta externa. Substitua "coluna" pelo nome real da coluna desejada.

FROM tabela: Indica a tabela da qual você está selecionando dados na consulta externa. Substitua "tabela" pelo nome real da tabela em seu banco de dados.

WHERE coluna IN (SELECT coluna FROM outra_tabela): Esta parte da consulta é a subconsulta. Ela seleciona valores da coluna especificada na tabela "outra_tabela" e verifica se a coluna da consulta externa está presente nesse conjunto de valores.

**Exemplo Prático:**

Suponha que tenhamos duas tabelas chamadas clientes e pedidos:
```
Tabela clientes
id_cliente	nome
1	Cliente A
2	Cliente B
3	Cliente C
```
```
Tabela pedidos
id_pedido	id_cliente	produto
1	1	Produto A
2	2	Produto B
3	1	Produto C
```
Ao executar a seguinte consulta SQL:
```
SELECT nome
FROM clientes
WHERE id_cliente IN (SELECT id_cliente FROM pedidos);
```
A consulta retornará os nomes dos clientes que têm pelo menos um pedido associado. O resultado seria:

```
nome
------
Cliente A
Cliente B
```
Neste exemplo, a subconsulta verifica se o id_cliente da tabela clientes está presente na coluna id_cliente da tabela pedidos. Isso retorna os clientes que têm pelo menos um pedido associado na tabela pedidos.

## 9. ALTER TABLE e CRUD Operations
- ALTER TABLE: Modificação da estrutura da tabela.
- INSERT, UPDATE, DELETE: Inserção, atualização e exclusão de dados.
```
INSERT INTO tabela (coluna1, coluna2) VALUES (valor1, valor2);
```

## 10. Índices e Otimização de Consultas
- Índices: Compreensão e criação de índices para otimizar o desempenho de consultas.
```
CREATE INDEX index_name ON tabela (coluna);
```
## 11. Views
- Views: Criação e utilização de views para simplificar consultas complexas.
```
CREATE VIEW nome_view AS
SELECT coluna
FROM tabela
WHERE condicao;
```

