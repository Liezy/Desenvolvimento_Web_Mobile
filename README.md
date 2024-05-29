# Sistema de Anúncios de Veículos

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-5.0.4-green.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-4.5.2-purple.svg)

## Sobre o Projeto

Este é um projeto desenvolvido para a disciplina de Desenvolvimento Web Mobile da Universidade Federal do Tocantins. O objetivo é criar um sistema de anúncios de veículos, onde os usuários podem cadastrar, listar e visualizar anúncios de veículos.

## Universidade Federal do Tocantins

**Curso**: Bacharelado em Ciência da Computação  
**Professor**: Thiago Magalhães  
**Aluno**: Eliézer Alencar Moreira

## Funcionalidades

- Cadastro de veículos com informações detalhadas.
- Listagem de veículos cadastrados.
- Criação de anúncios para os veículos cadastrados.
- Visualização dos anúncios com fotos dos veículos.

## Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [Django 5.0.4](https://www.djangoproject.com/)
- [Bootstrap 4.5.2](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/)

## Como Executar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python 3.12](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Passo a Passo

1. **Clone o repositório**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. **Navegue até o diretório do projeto**
    ```bash
    cd sistema
    ```

3. **Crie e ative o ambiente virtual**
    ```bash
    pipenv install
    pipenv shell
    ```

4. **Instale as dependências**
    ```bash
    pipenv install django djangorestframework
    ```

5. **Realize as migrações do banco de dados**
    ```bash
    python manage.py migrate
    ```

6. **Inicie o servidor de desenvolvimento**
    ```bash
    python manage.py runserver
    ```

7. **Acesse o projeto no navegador**
    ```
    http://127.0.0.1:8000/
    ```


## Contato

**Eliézer Alencar Moreira**  
Email: [eliezer.alencar@uft.edu.br](mailto:alencar.eliezer@mail.uft.edu.br)

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
