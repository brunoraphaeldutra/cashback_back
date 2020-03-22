[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=brunoraphaeldutra_cashback_back&metric=alert_status)](https://sonarcloud.io/dashboard?id=brunoraphaeldutra_cashback_back)
[![Build Status](https://github.com/brunoraphaeldutra/cashback_back/workflows/Python%20application/badge.svg)](https://github.com/brunoraphaeldutra/cashback_back)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=brunoraphaeldutra_cashback_back&metric=coverage)](https://sonarcloud.io/dashboard?id=brunoraphaeldutra_cashback_back)

# Migrations
```
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
```

# Tests
```
python -m unittest test.TestCashback
python -m unittest test.RepositoryTest
```

# Coverage
```
coverage run  -m unittest test.TestRepository
coverage run -m unittest discover 
coverage report
```

# Login
```
POST: http://127.0.0.1:5000/auth
{ "username": "usuario", "password": "senha" }
```

# Rotas autenticadas 
```
header: {Authorization: JWT }
```
