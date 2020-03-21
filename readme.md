[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=brunoraphaeldutra_cashback_back&metric=alert_status)](https://sonarcloud.io/dashboard?id=brunoraphaeldutra_cashback_back)

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
coverage run  -m unittest test.RepositoryTest
coverage report
```