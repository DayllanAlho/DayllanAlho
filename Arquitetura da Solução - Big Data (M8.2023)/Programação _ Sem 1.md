
# Introdução

Essa é uma entrega de atividade de Arquitetura de Solução, na qual foram abordados diversos tópicos relacionados à criação de um pipeline de dados. Entre eles, destacam-se a demonstração dos requisitos do pipeline, a identificação dos dados de entrada e saída, a análise das necessidades e objetivos do pipeline, a escolha de serviços adequados para cada etapa do pipeline, a justificativa para a escolha dos serviços, a representação visual do pipeline, a consideração de boas práticas para garantir resiliência e escalabilidade, a implementação de medidas básicas de segurança, a utilização de recursos de segurança da AWS e a descrição clara dos serviços utilizados e sua finalidade.

A seguir, serão apresentados detalhes sobre a implementação de medidas básicas de segurança e a utilização de recursos de segurança da AWS, que são fundamentais para garantir a proteção dos dados processados pelo pipeline.


# 1. Demonstração dos requisitos do pipeline de dados

O primeiro passo para a criação de um pipeline de dados é identificar seus requisitos, ou seja, o que é necessário para que ele funcione corretamente. Isso pode incluir a frequência de atualização dos dados, o volume de dados a ser processado, a necessidade de integração com outros sistemas, entre outros fatores.<br><br>
Neste caso específico, o pipeline é projetado para coletar dados de múltiplas fontes, consolidando informações de diferentes origens em uma única solução. Além disso, a arquitetura foi desenvolvida para garantir que os dados sejam armazenados em um formato agnóstico à nuvem, permitindo que a solução seja migrada para qualquer provedor de serviços em nuvem, sem ficar restrita a uma única plataforma. Por fim, a segurança desempenha um papel fundamental, e a arquitetura utiliza o AWS Identity and Access Management (IAM) para gerenciar o controle de acesso com base em funções de usuário, garantindo que apenas os usuários autorizados tenham acesso aos dados e recursos da aplicação.
- <b>Coleta de Dados de Múltiplas Fontes</b>: O pipeline é projetado para coletar dados de três fontes distintas:
    - <i>Dados governamentais</i> (disponíveis via site e arquivos),
    - <i>Dados de CNPJ</i> (disponibilizados em arquivos); e
    - <i>Dados de parceiros externos</i>, acessados por meio de uma API de consulta.

O objetivo é consolidar informações de diferentes origens em uma única solução.

- <b>Armazenamento em Formato Agnóstico à Nuvem</b>: A arquitetura foi desenvolvida para garantir que os dados sejam armazenados em um formato agnóstico à nuvem, permitindo que a solução seja migrada para qualquer provedor de serviços em nuvem, sem ficar restrita a uma única plataforma.

- <b>Requisitos de Segurança com Controle de Acesso Baseado em Funções de Usuário</b>: A segurança desempenha um papel fundamental. Para isso, a arquitetura utiliza o AWS Identity and Access Management (IAM) para gerenciar o controle de acesso com base em funções de usuário. Os analistas de marketing e vendas têm permissão para acessar o infográfico no Grafana, enquanto o usuário root (Engenheiro de Dados) tem acesso a toda a aplicação.

# Identificação dos dados de entrada e saída

Em seguida, é preciso identificar quais são os dados de entrada e saída do pipeline. Isso pode incluir dados de diferentes fontes, como bancos de dados, arquivos CSV, APIs, entre outros.
- <b>Dados de Entrada</b>: O pipeline recebe dados brutos de várias fontes, incluindo arquivos CSV de fontes governamentais, dados de CNPJ e informações de parceiros externos via API de consulta.

- <b>Dados de Saída</b>: Após o processamento, os dados são direcionados para várias saídas. Isso inclui o armazenamento em bancos de dados relacionais (PostgreSQL), bancos de dados OLAP e a plataforma Grafana para visualização de dados. A implementação de filas de mensagens e eventos em várias etapas do processo permite a transferência eficiente de dados entre os módulos.

Uma visão completa de como os dados fluem por todo o pipeline, desde a coleta até a análise e a visualização final. Cada módulo desempenha um papel importante na preparação e transformação dos dados para alcançar os objetivos de negócios.

- ## Módulo Fonte

<b>Entrada</b>: Dados brutos de fontes governamentais (disponíveis via site e arquivos), dados de CNPJ (arquivos CSV) e informações dos parceiros externos via API de consulta.<br>
<b> Saída</b>: Os dados são preparados e estruturados para serem transmitidos aos módulos subsequentes.

- ## Módulo Automação e Ingestão:

<b>Entrada</b>: Dados estruturados da etapa anterior, incluindo informações governamentais, dados de CNPJ e dados dos parceiros. Além disso, recebe constantemente novos dados conforme eles se tornam disponíveis nas fontes.<br>
<b>Saída</b>: Os dados processados são enviados para filas de eventos e filas de mensagens (Kafka) para transferência eficiente entre módulos, garantindo que as informações estejam prontas para serem consumidas e processadas na próxima etapa.

- ## Módulo Preparação e Armazenamento:

<b>Entrada</b>: Recebe os dados das filas de eventos e mensagens, que incluem informações governamentais, dados de CNPJ e dados dos parceiros. Integra informações recém-coletadas com os dados já existentes no DataLake AWS S3.<br>
<b>Saída</b>: Os dados são processados, limpos e transformados por meio de operações ETL (Extração, Transformação, Carregamento) usando o Apache Spark. Em seguida, os dados são armazenados em um DataLake no AWS S3, garantindo escalabilidade e armazenamento confiável. Os dados processados são inseridos em um Banco de Dados Relacional (PostgreSQL) e em um Banco de Dados OLAP otimizado para consultas analíticas.

- ## Módulo Análise:

<b>Entrada</b>: Recebe os dados processados armazenados no Banco de Dados Relacional (PostgreSQL) e no Banco de Dados OLAP. Além disso, recebe informações de eventos da fila.<br>
<b>Saída</b>: Executa um processo chamado Ensemble no AWS Lambda, que combina os dados e gera análises estatísticas e tendências. Os resultados são enviados para a plataforma de Infográficos (Grafana) para a criação de dashboards interativos e relatórios.

- ## Módulo Infográfico:

<b>Entrada</b>: Recebe os resultados do processo Ensemble e os dados armazenados no Banco de Dados OLAP.<br>
<bSaída</b>: Cria e exibe infográficos interativos usando a plataforma de Infográficos (Grafana), permitindo aos analistas de marketing e vendas visualizar os insights e tendências de negócios de forma clara e concisa.

# Análise das necessidades e objetivos do pipeline

- <b>Necessidade de Coleta e Processamento de Dados</b>: A necessidade de coletar dados de várias fontes deriva do desejo de obter insights de negócios sólidos. A análise de dados é fundamental para a tomada de decisões informadas e a identificação de oportunidades de negócios. O processamento dos dados é essencial para torná-los prontos para análise, incluindo limpeza, transformação e estruturação.

- <b>Objetivos de Eficiência</b>: A eficiência é alcançada por meio da automação de processos de coleta e ETL. Isso elimina a necessidade de trabalho manual repetitivo, economizando tempo e recursos. A eficiência também é alcançada com a capacidade de dimensionar a solução, permitindo o processamento de grandes volumes de dados de forma rápida e escalável.

- <b>Objetivos de Escalabilidade</b>: A arquitetura do pipeline é projetada para ser altamente escalável. A capacidade de processar grandes volumes de dados, adicionar fontes de dados adicionais e a capacidade de migração para diferentes plataformas de nuvem oferece escalabilidade e flexibilidade.

- <b>Objetivos de Segurança</b>: O controle de acesso baseado em funções de usuário, implementado através do AWS IAM, garante que apenas pessoal autorizado tenha acesso a partes específicas da aplicação. Isso protege a integridade e confidencialidade dos dados.

# Escolha de serviços adequados para cada etapa do pipeline

A escolha dos serviços para cada etapa do pipeline foi cuidadosamente ponderada para atender às necessidades específicas de coleta, processamento, armazenamento, análise e visualização de dados. Elas podem ser observadas abaixo:

- ## Módulo Fonte:

<b>Coleta de Dados Governamentais</b>: Nessa etapa, a coleta de dados governamentais será realizada por meio de Web Scraping com Python, permitindo a extração eficiente de informações de fontes governamentais na web.<br><br>
<b>Coleta de Dados de CNPJ</b>: Os dados de CNPJ são obtidos a partir de arquivos CSV, que são facilmente manuseados por scripts Python.<br><br>
<b>API do Parceiro</b>: A API de consulta do parceiro é consumida diretamente, permitindo a recuperação de informações de parceiros externos de forma automatizada.

- ## Módulo Automação e Ingestão:

<b>Web Scraping</b>: A técnica de Web Scraping é suportada por scripts Python, que possibilitam a coleta de dados da web de forma programática e o envio para as filas de mensagens.<br><br>
<b>AWS EC2</b>: O AWS EC2 é utilizada para consultar a API do parceiro, oferecendo um ambiente controlado para coletar informações dos parceiros externos, sem compromenter a segurança dos dados dos mesmo.<br><br>
<b>Kafka</b>: O uso de Kafka para filas de eventos e mensagens permite a transferência eficiente e confiável de dados entre módulos, garantindo a integridade dos dados.<br><br>
<b>Gerenciamento de Docker e Docker Compose</b>: A arquitetura inclui a gestão de contêineres Docker e Docker Compose para facilitar a escalabilidade e o gerenciamento de componentes do pipeline, garantindo a flexibilidade e a portabilidade do sistema em diferentes ambientes de nuvem.

- ## Módulo Preparação e Armazenamento:

<b>AWS S3</b>: O AWS S3 oferece armazenamento escalável e confiável para dados brutos e processados. Os dados brutos de fontes governamentais serão armazenados aqui para posterior processamento.<br><br>
<b>Apache Spark</b>: O Apache Spark é empregado para operações ETL, permitindo a extração, transformação e carga de dados, bem como o processamento de grandes volumes de informações.<br><br>

<b>Cloud Scheduler</b>: Para agendar e executar tarefas de rotina de forma automática. O Cloud Scheduler foi implementado como um módulo separado no pipeline para lidar com a automação de tarefas programadas. Ele desempenha um papel crucial na execução de ações com base em eventos ou em horários específicos. O Cloud Scheduler se conecta com a API construída e verifica os dados que nossa API construída pegou da API do parceiro. Ele verifica se precisa executar alguma ação e, caso necessário, encaminha os dados para o processo ETL. Se a ação não for necessária, o Cloud Scheduler encaminha os dados para a fila de mensagens, que os enviará para o PostgreSQL, onde serão armazenados. Esta adição permite que o pipeline execute tarefas em horários programados, o que é essencial para a integração eficaz dos dados e a automação das operações. A inclusão do Cloud Scheduler no pipeline melhora ainda mais a eficiência e a precisão do processamento de dados.<br><br>
<b>Banco de Dados Relacional (PostgreSQL)</b>: O PostgreSQL é escolhido para armazenar os dados processados de forma relacional, adequado para consultas e operações transacionais.<br><br>
<b>Banco de Dados OLAP</b>: O Banco de Dados OLAP (Online Analytical Processing) é uma parte essencial do pipeline, otimizado para consultas analíticas complexas. Ele armazena dados pré-processados após a etapa de preparação, melhorando o tempo de resposta das consultas e a entrega de visualizações no infográfico, uma vez que o processamento pesado já foi realizado no estágio anterior com o Apache Spark. Isso garante um desempenho eficiente e respostas rápidas para consultas analíticas da etapa seguinte.

- ## Módulo Análise:

<b>AWS Lambda</b>: O AWS Lambda é empregado para executar o processo Ensemble, que combina e analisa os dados, produzindo insights estatísticos e tendências de negócios.

- ## Módulo Infográfico:

<b>Plataforma de Infográficos (Grafana)</b>: A plataforma de Infográficos (Grafana) é utilizada para criar dashboards interativos e relatórios que apresentam as informações de maneira clara e concisa, permitindo que os analistas de marketing e vendas visualizem os insights de negócios.


- # Segurança:
A segurança é abordada em várias camadas do pipeline. As autenticações baseadas em AWS IAM garantem controle de acesso, permitindo que apenas usuários autorizados visualizem e manipulem os dados. Além disso, a estrutura de contêineres Docker e Docker Compose é configurada para fornecer isolamento e segurança em todo o sistema, permitindo que os recursos sejam facilmente gerenciados em ambientes agnósticos à nuvem.

# Justificativa para a escolha dos serviços

A escolha dos serviços baseou-se nas necessidades específicas do pipeline e nas características de cada etapa exigidas pelo cliente. Eis as justificativas para a escolha de cada serviço:

<b>Web Scraping com Python</b>: Escolhido para coleta eficiente de dados governamentais de fontes na web.<br><br>
<b>AWS EC2</b>: Utilizado para hospedar a API do parceiro, permitindo a consulta automatizada de informações de parceiros externos.<br><br>
<b>Kafka</b>: Selecionado para gerenciamento de filas de eventos e mensagens, garantindo a transferência eficiente de dados entre módulos.<br><br>
<b>AWS S3</b>: Oferece escalabilidade e confiabilidade no armazenamento de dados brutos e processados, tornando-os acessíveis a todos os módulos.<br><br>
<b>Apache Spark</b>: Capacita as operações ETL para limpeza, transformação e preparação de dados.<br><br>
<b>Banco de Dados Relacional (PostgreSQL)</b>: Adequado para armazenar dados processados de forma relacional e transacional.<br><br>
<b>Banco de Dados OLAP</b>: Escolhido para suportar análises analíticas avançadas.<br><br>
<b>AWS Lambda</b>: Utilizado para executar o processo Ensemble, produzindo análises estatísticas e tendências de negócios.<br><br>
<b>Plataforma de Infográficos (Grafana)</b>: Selecionada para criar dashboards e relatórios interativos, proporcionando uma visualização eficaz dos dados para os analistas de marketing e vendas.

# Representação visual do pipeline

![Arquitetura](https://github.com/DayllanAlho/DayllanAlho/blob/main/Arquitetura%20da%20Solu%C3%A7%C3%A3o%20-%20Big%20Data%20(M8.2023)/Arquitetura.png)
# Consideração de boas práticas para garantir resiliência e escalabilidade e uso de serviços ou recursos da AWS que suportem resiliência e escalabilidade

Para garantir que o pipeline seja resiliente e escalável, é fundamental adotar boas práticas, incluindo a redundância, o balanceamento de carga e a capacidade de escalabilidade. A arquitetura abraça essas práticas para assegurar a robustez e o desempenho necessários:<br><br>

- <b>Redundância</b>
    - <b>Fonte de Dados Diversificada</b>: No módulo de Fonte, dados são coletados a partir de três fontes distintas, promovendo a diversificação e evitando viés na construção do dado. Essa abordagem garante uma ampla gama de dados para análises e maior resiliência no caso de problemas com uma das fontes.
    - <b>Uso do Apache Kafka</b>: O emprego do Apache Kafka para filas de eventos e mensagens entre várias etapas do pipeline estabelece uma redundância vital. Em caso de falha em um dos módulos, os dados podem ser recuperados a partir do Kafka, assegurando a integridade do fluxo de dados.

- <b>Balanceamento de Carga</b>
    - <b>Containers Docker para Serviços Específicos</b>: Como parte das boas práticas, adotamos a abordagem de criar contêineres Docker para serviços individuais ou para serviços e seus complementos, como filas de mensagens. Isso não apenas distribui a carga uniformemente, mas também melhora o isolamento de serviços, o que contribui para a escalabilidade de partes específicas do pipeline.
- <b>Capacidade de Escalabilidade</b>
    - <b>Elasticidade do Apache Spark</b>: A arquitetura incorpora a capacidade de escalabilidade do Apache Spark, que é usado para processamento e transformação de dados (ETL). O Apache Spark pode ser escalado horizontalmente para lidar com volumes crescentes de informações, ajustando-se às demandas variáveis de dados em tempo real.

    - <b>AWS Lambda Adaptável</b>: O módulo de Análise utiliza o AWS Lambda, um serviço adaptável que provisiona automaticamente recursos com base na carga de trabalho. Isso assegura que o pipeline seja capaz de se adaptar com agilidade a cargas de trabalho em constante evolução.

Essas práticas de redundância, balanceamento de carga e escalabilidade, combinadas com a estratégia de contêineres Docker, resultam em um pipeline de dados resiliente e dimensionável que é capaz de enfrentar desafios em tempo real e evoluir de acordo com as necessidades da empresa.

# Implementação de medidas básicas de segurança e utilização de recursos de segurança da AWS

A segurança dos dados é uma prioridade central em nosso pipeline. Para garantir a integridade e confidencialidade dos dados, implementamos o controle de acesso para perfis diferentes, no caso o analista de marketing vendas e o consultor de dados:

- <b>Controle de Acesso com AWS IAM</b>: Utilizamos o AWS Identity and Access Management (IAM) para gerenciar com precisão quem tem acesso a quais partes do pipeline. Isso garante que apenas usuários autorizados possam acessar os recursos e realizar ações específicas, mantendo os dados seguros.

# Conclusão da Descrição clara dos serviços utilizados na arquitetura e sua finalidade.

Esta análise detalhada da arquitetura do pipeline de dados destaca a importância de compreender as necessidades, objetivos e requisitos específicos do projeto. A escolha de serviços, a implementação de medidas de segurança e a adoção de boas práticas refletem um planejamento cuidadoso e a busca por soluções escaláveis e resilientes.<br><br>
A descrição clara dos serviços utilizados e suas finalidades fornece um guia preciso para todas as partes envolvidas no projeto, desde analistas de marketing e vendas até engenheiros de dados. Isso garante uma compreensão compartilhada de como os dados são coletados, processados e disponibilizados para análise e tomada de decisões.
<br><br>
A segurança foi abordada em várias camadas do pipeline, com um controle de acesso rigoroso com base no AWS IAM, garantindo que apenas usuários autorizados tenham acesso aos dados. Além disso, a estrutura de contêineres Docker e Docker Compose proporciona isolamento e segurança em todo o sistema, tornando-o adaptável a diferentes ambientes de nuvem.
<br><br>
As boas práticas de redundância, balanceamento de carga e escalabilidade, combinadas com a estratégia de contêineres Docker, resultam em um pipeline de dados resiliente e dimensionável, capaz de enfrentar desafios em tempo real e evoluir conforme as necessidades da empresa.
<br><br>
# Referências
 - https://medium.com/itautech/boas-pr%C3%A1ticas-para-testar-a-resili%C3%AAncia-de-suas-aplica%C3%A7%C3%B5es-d189088b6e8f
 - https://cleancloud.io/pilares-de-seguranca-aws/
 - https://docs.aws.amazon.com/pt_br/wellarchitected/latest/reliability-pillar/resiliency-and-the-components-of-reliability.html
 - https://aws.amazon.com/pt/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc
 - https://aws.amazon.com/pt/autoscaling/


# Agradecimentos

A criação desta arquitetura de solução foi possível graças ao valioso auxílio e colaboração dos seguintes professores:

- Afonso Lelis
- Cristiano
- Vitor Hayashi
- José Romualdo
- Renato Penha

Além disso, gostaria de agradecer aos discentes que colaboraram com meu ânimo ao longo deste árduo trabalho e com as contribuições de entendimento da arquitetura:

- Giovanna Furlan
- Vitória Rodrigues
- Pedro Rezende
- Lucas Brito

### Lembrando que esta arquitetura foi desenvolvida com a ajuda de todas essas pessoas.