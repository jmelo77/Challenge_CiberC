#Challenge CiberC

[![CiberC](https://i0.wp.com/portalgeek.co/wp-content/uploads/2018/11/CiberC.jpg?resize=715%2C400&ssl=1)](https://www.ciberc.com)

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/bin/python3.7
or
pyvenv-3.7 env
```

```bash
source env/bin/activate
```
# Install dependencies:

```bash
pip install -r requirements.txt
```

# Initialize the git repository(DEPRECATED)

```bash
git init
git remote add origin https://github.com/jmelo77/Challenge_CiberC.git
```

# Migrate, create a superuser, and run the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Start project with custom settings

```bash
python manage.py runserver 127.0.0.1:8000
```
