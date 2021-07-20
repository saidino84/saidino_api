# flask_bot_with_flutter

heroku access --app:saidinosecondapp

# Configuaraco do banco de dados postgrel

heroku addons:create heroku-postgrel:hobby-dev --app:saidinosecondapp

```sh
Creating heroku-postgresql:hobby-dev on ⬢ saidinosecondapp... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-cubic-58455 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation

```

# para verificar as infos do Database do postgresql

heroku pg:info

# como acessar as credenciais do banco o url e tudo sobre o banco
para se connectar

```sh
heroku pg:credentials:url --app=saidinosecondapp


Connection information for default credential.
Connection info string:
   "dbname=d5t6ibvkjcp7gq host=ec2-34-194-14-176.compute-1.amazonaws.com port=5432 user=rlvawhxyajskth password=1ae752d1119605d1d6d12e8724461d7eea12a5d9bae4d8c5ad8a77a6e32aa33a sslmode=require"
Connection URL:
   postgres://rlvawhxyajskth:1ae752d1119605d1d6d12e8724461d7eea12a5d9bae4d8c5ad8a77a6e32aa33a@ec2-34-194-14-176.compute-1.amazonaws.com:5432/d5t6ibvkjcp7gq

``
