# Development environment setup

```sh
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt

python3 manage.py runserver
```

### To check Members app functionality you should open [link](http://localhost:8000/members_app/)

### To check Courses app functionality you should reproduce next steps

1. Create createsuperuser.

```sh
python manage.py createsuperuser
```

Follow the instructions in the console. You will be prompted to enter a Username, Email, and Password for the new administrator.

2. Log in the Django administrative interface [admin](http://localhost:8000/admin/).

3. Open [link](http://localhost:8000/courses_app/)
