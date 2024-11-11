# Descrição do Projeto

Este é o repositório para disciplina de FCCPD que tem como objetivo o desenvolvimento de uma aplicação CRUD básica, incluindo configuração de banco de dados e integração com Docker e Docker Compose.

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## Estrutura do Projeto

### I. Definição do Contexto
1. **Contexto do CRUD**: O CRUD está inserido em um contexto específico e exclusivo, evitando duplicação de atividades semelhantes em outros projetos.

### II. Aplicação
1. **Desenvolvimento da Aplicação**:
   - Implementar uma aplicação simples conectada ao banco de dados.
   - Apresentar um menu para as operações do CRUD, com as seguintes funcionalidades:
     - **Inserir dados**
     - **Atualizar dados**
     - **Recuperar dados**: incluir pelo menos 2 consultas com junção entre tabelas.
     - **Excluir dados**

2. **Dockerfile da Aplicação**:
   - Configuração do Dockerfile para definir as dependências e ambiente da aplicação.

### III. Banco de Dados
1. **Escolha do Serviço de Banco de Dados**:
   - Seleção do banco de dados que melhor se adapta ao projeto.

2. **Scripts Iniciais do Banco de Dados**:
   - Criação das tabelas e inserção de dados iniciais:
     - Criar ao menos 3 tabelas (entidades) relacionadas, com ao menos 6 inserções em cada tabela.

3. **Dockerfile do Banco de Dados**:
   - Definição do Dockerfile para configurar o banco de dados no ambiente Docker.

4. **Credenciais de Acesso ao Banco de Dados**:
   - Definição de credenciais (usuário, senha, nome do banco) a serem utilizadas pela aplicação e no Docker Compose.

### IV. Docker Compose
1. **Configuração do docker-compose.yml**:
   - Definir o arquivo `docker-compose.yml` para descrever e orquestrar os serviços necessários:
     - Serviço da aplicação.
     - Serviço do banco de dados.


# Tecnologias utilizadas
* Java
* MySQL
* Streamlit
* FastAPI
* Uvicorn
* SQLAlchemy
* Mysqlclient
* Python-dotenv
* FastCRUD 

## Cenário de execução isolado para o container do banco de dados                
1. Instalar a imagem do mysql no Docker : docker pull mysql
2. Criar um volume no docker: docker volume create amor_em_pote
3. Criar o conteiner do mysql: docker run -d --name amor_em_pote_db -e MYSQL_ROOT_PASSWORD=root -v amor_em_pote_data:/var/lib/mysql mysql:latest
4. Executar o conteiner do mysql: docker exec -it amor_em_pote_db mysql -u root -p
                


# Equipe
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/108764670?v=4" width=115><br><sub>Adriana Lúcia</sub>](https://github.com/Dricalucia) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/107653834?v=4" width=115><br><sub>Bruna Carvalho</sub>](https://github.com/brunacarvalho202)  |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/47667167?v=4" width=115><br><sub>Guilherme Oliveira</sub>](https://github.com/Guilherme) |  
| :---: | :---: | :---: |
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/47667167?v=4" width=115><br><sub>Pedro Villas Boas</sub>](https://github.com/PedroVillasBoas)  | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/112591325?v=4" width=115><br><sub>Thiago de Araújo</sub>](https://github.com/tharaujo17)  |   |  

