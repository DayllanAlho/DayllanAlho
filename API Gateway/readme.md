# Lambda_Ponderada2

Este é um Lambda criado na AWS integrado com a API Gateway. Ele atende aos seguintes requisitos:

- Criação de um lambda (denominado Lambda_Ponderada2) na AWS integrado com a API Gateway.
- Utilização do princípio DRY (Don't Repeat Yourself) no código em Python.
- Implementação do Endpoint REST com o API Gateway.
- Utilização do método POST para a implementação do API Gateway.
- Implementação do token de autenticação para o endpoint REST.

<hr><hr>

## Passos para a Configuração

### Criação do Lambda

1. **Seleção do Serviço Lambda:**
   - Acesse o Console da AWS.
   - Na página inicial, clique em "Serviços" e selecione "Lambda" sob "Computação".

![Descrição da imagem](URL_da_sua_imagem)


2. **Criação da Função Lambda:**
   - No painel do Lambda, clique em "Funções" no painel de navegação à esquerda.
   - Clique no botão "Criar função" no canto superior direito.
   - Escolha a opção "Autor de função personalizado" e clique em "Avançar".

![Descrição da imagem](URL_da_sua_imagem)


3. **Nomeando e Configurando a Função Lambda:**
   - Preencha um nome descritivo para sua função Lambda, por exemplo, "Lambda_Ponderada2".
   - Selecione "Python 3.x" como o tempo de execução.
   - Escolha ou crie uma função de autor que tenha permissões para o que você precisa.
   - Clique em "Criar função" no canto inferior direito.

![Descrição da imagem](URL_da_sua_imagem)


4. **Exemplo de Criação de uma Função Lambda:**
   - No editor de código, cole o código Python fornecido para o Lambda_Ponderada2.

![Descrição da imagem](URL_da_sua_imagem)


5. **Visão Geral da Função:**
   - Clique em "Salvar" no canto superior direito para salvar a função Lambda.

![Descrição da imagem](URL_da_sua_imagem)


### Configuração do API Gateway

6. **Adição de Gatilho + Seleção de API Gateway:**
   - No painel de detalhes da função Lambda, role para baixo até a seção "Designer".
   - Clique em "Adicionar gatilho" e selecione "API Gateway" como o gatilho.

![Descrição da imagem](URL_da_sua_imagem)


7. **Criação da API:**
   - Selecione "Criar uma API nova" e escolha "REST API".
   - Clique em "Criar um novo API" e dê um nome à sua API, por exemplo, "API_Ponderada2".

![Descrição da imagem](URL_da_sua_imagem)


8. **API Gateway Criada:**
   - Clique em "Adicionar" para criar o gatilho da API Gateway.

![Descrição da imagem](URL_da_sua_imagem)


9. **Endpoint da API Gateway:**
   - Na seção "Designer" da função Lambda, você verá o gatilho da API Gateway listado. Clique no nome da API (por exemplo, "API_Ponderada2") para acessar as configurações da API.

![Descrição da imagem](URL_da_sua_imagem)


10. **Seleção de POST:**
    - No painel de navegação à esquerda da página da API, clique em "Recursos".
    - Selecione o recurso "POST" para configurar um endpoint de solicitação POST.

![Descrição da imagem](URL_da_sua_imagem)


### Configuração de Autorização

11. **Buscando o ARN da Função:**
    - Na página de configuração do método POST, role para baixo até a seção "Configurações de Integração".
    - No campo "Função de AWS Lambda", clique no botão de edição e selecione a função Lambda que você criou.

12. **Adicionando Permissão:**
    - Após selecionar a função, clique em "Salvar" e, em seguida, clique em "Salvar" novamente na página do método POST.
    - Clique em "Método de Atualização" para atualizar as configurações do método POST.

13. **Buscando o ARN da Função:**
    - No painel de navegação à esquerda da página da API, clique em "Autorização".
    - Clique em "Criar e associar permissões".

14. **Adicionando Permissão:**
    - Na seção "Definir permissões", defina o tipo de autorização para "Sigv4".
    - Clique em "Salvar" para criar as permissões.

### Endpoint REST

15. **Buscando o URL da API Gateway:**
    - Volte para a página principal da sua API.
    - No painel de navegação à esquerda, selecione "Stages".
    - Clique no nome do estágio (por exemplo, "Prod") para acessar as configurações do estágio.

16. **Depois do Deploy, Teste do POST no Thunder:**
    - No painel de configurações do estágio, você encontrará o URL de invocação do seu endpoint REST. Copie este URL para uso posterior.

## Teste do Lambda

17. **Criação do Script Python:**
    - Crie um script Python para testar o Lambda. O código Python deve incluir funções que simulam solicitações com diferentes cenários.

18. **No Auth, Verificando o Username e o Password:**
    - Crie uma função Python para testar autenticação bem-sucedida, onde você verifica o nome de usuário e senha.

19. **Username e Password Corretos:**
    - Crie uma função Python para testar autenticação malsucedida com nome de usuário e senha corretos.

20. **Username e Password Não Autorizado:**
    - Crie uma função Python para testar autenticação malsucedida com nome de usuário e senha não autorizados.

21. **Configuração do Teste:**
    - Configure o ambiente de teste Python, incluindo a criação de eventos de teste que correspondam aos cenários que você deseja testar.

22. **Criar Novo Evento de Teste:**
    - Crie novos eventos de teste que representem os cenários desejados. Certifique-se de passar os parâmetros corretos para simular diferentes tipos de solicitações.

23. **Passando os Parâmetros para Acionar um Acesso Não Autorizado:**
    - Execute seus testes Python e verifique se os resultados correspondem às expectativas.

Este guia deve ajudar você a criar e testar o Lambda integrado com o API Gateway, atendendo aos requisitos especificados. Certifique-se de personalizar o `readme.md` com informações adicionais e de licença, e você está pronto para compartilhar seu projeto.

<hr><hr>

## Código do Lambda

O código do Lambda é responsável por autenticar os usuários com base em credenciais fornecidas no cabeçalho de autorização. Ele utiliza um dicionário que mapeia usuários a senhas. Quando as credenciais são válidas, o Lambda retorna um status 200 e processa o corpo da solicitação JSON.

## Testes Python

Para testar o Lambda e garantir que ele atende aos requisitos, foram criadas funções Python separadas que simulam solicitações com diferentes cenários. Estes cenários incluem autenticação bem-sucedida, autenticação malsucedida, evento sem autenticação e verificação do formato JSON.

### Autenticação Bem-sucedida

O primeiro teste simula uma solicitação com credenciais válidas, incluindo um corpo JSON bem formatado.

### Autenticação Malsucedida

O segundo teste simula uma solicitação com credenciais inválidas, incluindo um corpo JSON.

### Evento Sem Autenticação

O terceiro teste simula uma solicitação sem credenciais, incluindo um corpo JSON.

### Verificação do Formato JSON

O quarto teste simula uma solicitação com credenciais válidas, mas um corpo JSON mal formatado.

### Autenticação e Verificação do Formato JSON

O quinto teste simula uma solicitação com credenciais válidas e um corpo JSON formatado corretamente.

## Endpoint REST

O Lambda foi integrado com o API Gateway para criar um endpoint REST. Você pode acessar o endpoint REST no seguinte URL:

https://xxfox8dz2e.execute-api.us-east-1.amazonaws.com/default/Lambda_Ponderada2

## Uso

Você pode usar o endpoint REST para autenticar e processar solicitações com credenciais válidas. Certifique-se de incluir o cabeçalho de autorização com o formato 'Basic usuario:senha'.

## Autor

[Seu Nome]

## Licença

Este projeto está licenciado sob a [Sua Licença].
