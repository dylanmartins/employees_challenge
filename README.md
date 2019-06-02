# EMPLOYEES CHALLENGE

Pequeno CRUD para controle de funcionários feito em Django 1.11.20.

## Getting Started

Para executar a aplicação, além de clonar o projeto você precisa também ter instalado [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) em sua maquina.

Com isso, você deve executar o comando de build do docker-compose
```
$ docker-compose build
```

Após o build você deve levantar os containeres com o seguinte comando
```
$ docker-compose up
```

Então você deve acessar o container do Django para executar as migrations necessárias para o banco de dados.
Acessando o container
```
$ docker exec -it employees_challenge_web_1 bash
```
Executando as primeiras migrações
```
$ python manage.py migrate
```

Após isso você ja consegue acessar o painel de gestão de funcionários pelo link http://localhost:8000/

## API

Este painel possui também uma API em que você pode Listar, Adicionar e Remover funcionários.

Você pode listar pela URL http://localhost:8000/employee/ com um método GET, ou caso queira listar um funcionário especifico você também pode enviar o ID do banco por exemplo http://localhost:8000/employee/1/ eu estaria buscando o funcionário do ID 1.

Você pode adicionar funcionários com um método POST na URL http://localhost:8000/employee/ enviando um json junto com a requisição.
Exemplo:
> {'name': 'Dylan', 'email': 'dylan@dylan.com', 'department': 'department'}

E se você enviar uma request como método DELETE e um ID de funcionário, você irá deletar este funcionário.
Exemplo:
> curl -X DELETE "http://localhost:8000/employee/1/"

## Author

* **Dylan Martins Janine de Andrade** - [github](https://github.com/dylanmartins) [linkedin](https://www.linkedin.com/in/dylan-m-j-andrade/)


