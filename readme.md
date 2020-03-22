[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=brunoraphaeldutra_cashback_back&metric=alert_status)](https://sonarcloud.io/dashboard?id=brunoraphaeldutra_cashback_back)
[![Build Status](https://github.com/brunoraphaeldutra/cashback_back/workflows/Python%20application/badge.svg)](https://github.com/brunoraphaeldutra/cashback_back)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=brunoraphaeldutra_cashback_back&metric=coverage)](https://sonarcloud.io/dashboard?id=brunoraphaeldutra_cashback_back)

# Migrations
Para realizar a migration do banco de dados
```
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
```
Hoje o sistema está configurado para SQLite, mas pode ser migrado para outras bases realcionais. 
```
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
```

# Tests
```
python -m unittest test.TestCashback
python -m unittest test.RepositoryTest
```

# Coverage
Para validar o coverage
```
coverage run  -m unittest test.TestRepository
coverage run -m unittest discover 
coverage report
```

# Login
Primeiro usuário é criado de acordo com a configuração
```
CPF_ADM = "15350946056"
DEFAULT_PASSWORD = "senha"
```
Para conseguir o token é necessesário realizar um post
```
POST: http://127.0.0.1:5000/auth
{ "username": "usuario", "password": "senha" }
```

# Rotas autenticadas 
Para todas as rotas é necessário envio do token
```
header: {Authorization: JWT TOKEN}
```
