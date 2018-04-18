# Backend


## Steps to setup:


#### Create Virtual Environment
```sh
$ sudo pip install virtualenv
$ virtualenv backend
```
#### Start virtualenv
```sh
$ source backend/bin/activate
```

#### Clone git repo
```sh
(backend)$ git clone https://github.com/avishek4redacid/Backend 
```

#### Setup the dependencies
```sh 
(backend)$ pip install requirements.txt
```

```

#### Setup the database
```sh
(backend)$ python manage.py makemigrations
(backend)$ python manage.py migrate
```

#### Start the server 
```sh
(backend)$ python manage.py runserver
```

#### Create Superuser 
```sh
(backend)$ python manage.py createsuperuser
```
