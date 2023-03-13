# python.django

- comandos para executar:
1. Instalar a biblioteca de ambiente virtual
```
pip install virtualenv
```

2. Criar o ambiente virtual
```
virtualenv venv
```

3. Ativar o ambiente virtual
```
venv\Scripts\Activate
```

        3.1. Desativar o ambiente virtual:
        ```
        deactivate
        ```

4. Instalar as dependências do projeto (no ambiente virtual)
```
pip install -m requirements.txt
```

5. Acionar o serviço do django
```
python manage.py runserver
```

        5.1. Desativar o servidor django: CTRL+C no terminal



>Para criar um app chamado 'galeria':
>```
>python manage.py startapp galeria
>```

