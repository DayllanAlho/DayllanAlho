# Lambda_Ponderada2

Este é um exemplo de configuração do Lambda criado na AWS integrado com a API Gateway para fins ilustrativos. As imagens e etapas de configuração apresentadas aqui são demonstrativas e não refletem exatamente o que está no repositório real. O repositório contém um nome de função Lambda diferente, código Python diferente e configurações de autenticação alternativas.

Este guia é destinado a fins de aprendizado e não deve ser seguido diretamente para implantação, apenas para observar a esteira de aprendizagem de como criar uma API Gateway na AWSA com função Lambda. Certifique-se de observar a sessão:  abaixo da configuração, denominada Código do Lambda. 
<hr><hr>

## 1. Passos para a Configuração

### 1.1 - Criação do Lambda

1. **Seleção do Serviço Lambda:**
   - Acesse o Laboratório da AWS.
   - Na página inicial, clique em "Serviços" e selecione o serviço "Lambda".

![Seleção do Serviço Lambda](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/1%20-%20Sele%C3%A7%C3%A3o%20do%20servi%C3%A7o%20-%20Lambda.png)

2. **Criação da Função Lambda:**
   - No painel do Lambda, clique em "Funções" no painel de navegação à esquerda.
   - Clique no botão "Criar função" no canto superior direito.

![Criação da Função Lambda](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/2%20-%20Cria%C3%A7%C3%A3o%20da%20fun%C3%A7%C3%A3o%20lambda.png)

3. **Nomeando e Configurando a Função Lambda:**
   - Preencha um nome descritivo para sua função Lambda, por exemplo, "Lambda_Ponderada2".
   - Selecione "Python 3.11" como o tempo de execução.
   - Escolha ou crie uma função de autor que tenha permissões para o que você precisa.
        - A recomendação é que a flag da arquitetura para o código da função deva ser a x86_64, pois nesse caso, como estamos em um ambiente de teste, não há a interferência. Apesar que na produção, o arm64, seja a melhor opção.
        - Selecione a opção de usar uma função existente e deixa a segurança como Open (devido ser um ambiente de teste);
        - A função existente precisa ser a Lab Role.
   - Clique em "Criar função" no canto inferior direito.

![Nomeando e Configurando a Função Lambda](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/3%20-%20Nomeando%20e%20configurando%20fun%C3%A7%C3%A3o.png)

4. **Exemplo de Criação de uma Função Lambda:**
   - No editor de código, cole o código Python fornecido para o Lambda_Ponderada2.

![Exemplo de Criação de uma Função Lambda](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/4%20-%20Exemplo%20de%20cria%C3%A7%C3%A3o%20de%20fun%C3%A7%C3%A3o%20lambda.png)



### 1.2 - Configuração do API Gateway

5. **Visão Geral da Função:**
   - Clique em "Adicionar gatilho" e selecione "API Gateway" como o gatilho.

![Visão Geral da Função](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/5%20-%20Vis%C3%A3o%20geral%20da%20fun%C3%A7%C3%A3o.png)
6. **Adição de Gatilho + Seleção de API Gateway:** 
   - Na configuração do gatilho selecione API Gateway

![Adição de Gatilho + Seleção de API Gateway](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/6%20-%20Adi%C3%A7%C3%A3o%20de%20gatilho%20%2B%20sele%C3%A7%C3%A3o%20de%20API%20Gateway.png)

7. **Criação da API:**
   - Selecione "Criar uma API nova" e escolha "REST API".
   - Clique em "Criar um novo API" e dê um nome à sua API, por exemplo, "API_Ponderada2".

![Criação da API](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/7%20-%20Cria%C3%A7%C3%A3o%20da%20API.png)

8. **API Gateway Criada:**
   - Clique em "Adicionar" para criar o gatilho da API Gateway.

![API Gateway Criada](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/8%20-%20API%20Gateway%20criada.png)

9. **Endpoint da API Gateway:**
   - Na seção "Designer" da função Lambda, você verá o gatilho da API Gateway listado. Clique no nome da API para acessar as configurações da API, depois clique em configurações, logo abaixo.

![Endpoint da API Gateway](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/9%20-%20endpoint%20da%20API%20Gateway.png)

10. **Seleção de POST:**
    - No painel de navegação à esquerda da página da API, clique em "Recursos".
    - Selecione o recurso "POST" para configurar um endpoint de solicitação POST.

![Seleção de POST](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/12%20-%20Sele%C3%A7%C3%A3o%20de%20Post%20.png)

### 1.3 - Configuração de Autorização

11. **Buscando o ARN da Função:**
    - Na página de configuração do método POST, role para baixo até a seção "Configurações de Integração".
    - No campo "Função de AWS Lambda", clique no botão de edição e selecione a função Lambda que você criou.

![ARN da Função](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/14%20-%20Buscando%20o%20ARN%20da%20fun%C3%A7%C3%A3o.png)

### 1.4 - Endpoint REST

12. **Buscando o URL da API Gateway:**
    - Volte para a página principal da sua API.
    - Selecione configuração e pegue a API endpoint.

![URL da API Gateway](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/21%20-%20buscando%20a%20url%20da%20API%20Gateway.png)

13. **Depois do Deploy, Teste do POST no Thunder:**
    - Volte para a área código e clique em deploy.
    - Após realizado o deploy, copie o link da API (URL) e cole na barra de endereço do seu browser.

## 1.5 - Teste do Lambda

14. **Criação do Script Python:**
    - Crie um script Python para testar o Lambda. O código Python deve incluir funções que simulam solicitações com diferentes cenários.

![Criação do Script Python](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/27%20-%20cria%C3%A7%C3%A3o%20do%20script%20python.png)

15. **Instale a extensão Thunder no VSCode, e na área do Auth, Verificando o Username e o Password:**
    - Crie uma função Python para testar autenticação bem-sucedida, onde você verifica o nome de usuário e senha na extensão thunder.

![No Auth, Verificando o Username e o Password](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/29%20-%20No%20auth%2C%20verificando%20o%20username%20e%20o%20password.png)

16. **Username e Password Corretos:**
    - Crie uma função Python para testar autenticação malsucedida com nome de usuário e senha corretos.

![Username e Password Corretos](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/30%20-%20username%20e%20password%2C%20ok.png)

17. **Username e Password Não Autorizado:**
    - Crie uma função Python para testar autenticação malsucedida com nome de usuário e senha não autorizados.

![Username e Password Não Autorizado](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/31%20-%20username%20e%20password%2C%20not%20ok.png)

18. **Configuração do Teste:**
    - Configure o ambiente de teste Python, incluindo a criação de eventos de teste que correspondam aos cenários que você deseja testar.

![Configuração do Teste](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/32%20-%20config.%20teste.png)

19. **Criar Novo Evento de Teste:**
    - Crie novos eventos de teste que representem os cenários desejados. Certifique-se de passar os parâmetros corretos para simular diferentes tipos de solicitações.

![ Novo Evento de Teste](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/33%20-%20criar%20novo%20evento%20de%20teste.png)

20. **Passando os Parâmetros para Acionar um Acesso Não Autorizado:**
    - Execute seus testes Python e verifique se os resultados correspondem às expectativas.

![Parâmetros para Acionar um Acesso Não Autorizado](https://github.com/DayllanAlho/DayllanAlho/blob/dev/API%20Gateway/assets/34%20-%20Passando%20os%20par%C3%A2metros%20para%20acionar%20um%20acesso%20n%C3%A3o%20autorizado.png)

<hr><hr><hr>

## 2. Código do Lambda
O código do Lambda é responsável por autenticar os usuários com base em credenciais fornecidas no cabeçalho de autorização. Ele utiliza um dicionário que mapeia usuários a senhas. Quando as credenciais são válidas, o Lambda retorna um status 200 e processa o corpo da solicitação JSON.

## 3. Testes Python

Para testar o Lambda e garantir que ele atende aos requisitos, foram criadas funções Python separadas que simulam solicitações com diferentes cenários. Estes cenários incluem autenticação bem-sucedida, autenticação malsucedida, evento sem autenticação e verificação do formato JSON.

### 3.1. Autenticação Bem-sucedida

O primeiro teste simula uma solicitação com credenciais válidas, incluindo um corpo JSON bem formatado.
para executar o teste, que foi feito na AWS, foi necessário criar um script python, simulando-o. Para executá-lo é necessário clona o repositório, abrir o local do arquivo e no terminal rodar o seguinte comando: 

``` 
python test.py
```
Ao rodar os comandos você verá a execução de todos os testes no terminal. Além disso, estes foram executados no ambiente AWS, para simulá-los você pode copiar o código e adaptar as chamadas na aba teste, conforme demonstrado no passo 1.6 dos Passos para a Configuração.

### 3.2. Autenticação Malsucedida

O segundo teste simula uma solicitação com credenciais inválidas, incluindo um corpo JSON.

### 3.3. Evento Sem Autenticação

O terceiro teste simula uma solicitação sem credenciais, incluindo um corpo JSON.

## 4. Endpoint REST

O Lambda foi integrado com o API Gateway para criar um endpoint REST. Você pode acessar o endpoint REST no seguinte URL:

https://xxfox8dz2e.execute-api.us-east-1.amazonaws.com/default/Lambda_Ponderada2

## 5. Uso

Você pode usar o endpoint REST para autenticar e processar solicitações com credenciais válidas. Certifique-se de incluir o cabeçalho de autorização com o formato 'Basic usuario:senha'.

## Recapitulando que os prints foram disponibilizados pelo Lucas Britto e a execução dessa atividade foi desenvolvida juntamente com o 
- <b>Pedro Rezende</b>, 
- <b>Izabella Frias</b>, 
- <b>Lucas Britto</b>, 
- <b>Giovanna Furlan</b>. 

## Sem eles nada disso seria possível.