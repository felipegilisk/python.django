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

4. Instalar as dependências do projeto (no ambiente virtual)
```
pip install -m requirements.txt
```

5. Acionar o serviço do django
```
python manage.py runserver
```


- Desativar o ambiente virtual:
    ```
    deactivate
    ```
- Desativar o servidor django: CTRL+C no terminal

- Para criar um app chamado 'galeria':
    ```
    python manage.py startapp galeria
    ```

6. Para utilizar ORM:
- Criar classes para ORM em models
- (venv) Rodar o comando ```python manage.py makemigrations```
- (venv) Em seguida o comando ```python manage.py migrate```

7. Criar dados na tabela do SQLite:
- (venv) Executar o comando ```python manage.py shell```
- A seguir ```from galeria.models import <Classe criada no models>```
- próximo passo: ```objeto = Classe(atr1="algumacoisa", atr2="outracoisa"...)```

8. Remover dados na tabela do SQLite
- (venv) Classe.objects.filter(id=<id>).delete()
- Fechar e abrir o db.sqlite3 para confirmar

9. Criar admin
- (venv) python manage.py createsuperuser
- Fornecer nome de usuario, email e senha

10. Criar nova página
- Criar função no galeria > views.py
- Criar path no galeria > urls.py
- Criar página html no templates > galeria > nova_pagina.html
- Adequar os menus e elementos universais, como usado no index.html por exemplo
