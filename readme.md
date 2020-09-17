# API Python

* Desenvolvimento de uma api em python utilizando flask, sqlalchemy e sqlite para o desafio de uma entrevista

* Desafio

- Construção de uma API que comporte a inclusão de voluntários e ações sociais.

- Para cada voluntário, nós gostaríamos de recolher:


    * Nome

    * Sobrenome

    * Bairro

    * Cidade


Já para as ações:


    * Nome da ação

    * Instituição que está organizando

    * Local (cidade, bairro e endereço)

    * Descrição


# Guia da API
    - Instalação

    * Para esta aplicação funcionar você deve ter instalado o python 3.x juntamente com o pip
    * A virtualenv deve estar na mesma pasta que a pasta app
    * Caso a virtualenv não funcione, há um arquivo requirements.md com todas as dependencias da aplicação

    - Utilização
    * Para testar a aplicação primeiro deve-se cadastrar um voluntário e uma ação social para testar os demais métodos
    * Como cadastrar um voluntário: A api só aceita este formato JSON:
    ```
    {
        "nome":"nome do voluntário",
        "sobrenome":"sobrenome do voluntário",
        "bairro":"bairro onde reside o voluntário",
        "cidade":"cidade onde reside o voluntário"
    }
    ```
    * Como cadastrar uma ação social: A api só aceita este formato JSON:
    ```
    {
    "nome": "nome da ação social",
    "instituição": "instituição que está fazendo esta ação",
    "bairro": "bairro onde será a ação",
    "cidade": "cidade onde será a ação",
    "endereço": "endereço onde será a ação",
    "descrição": "Uma pequena descrição de no máximo 100 caracteres da ação"
    }
    ```
    * Rota para cadastro/consulta do voluntário - "/voluntarios/"
    * Rota para cadastro/consulta da ação social - "/acoessociais/"
    
