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

#Coverage
```
coverage run  -m unittest test.RepositoryTest
coverage report
```