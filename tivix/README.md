# Tivix School System ( Django Rest Framework & Vue.js)


## Setup:

- Create virtualenv(Optional) using python 3.6+
- Run pip install -r requirements.txt
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py createsuperuser
- Run python manage.py runserver 
- go to localhost:8000/admin #Login with superuser due to no login or register page completed as noted below.
- go to localhost:8000/mystudents


## API Endpoints
- Create/List Teachers : /api/teachers/ 
- Retrieve/Update/Delete Teacher : /api/teachers/<PK\>
- Create/List Student : /api/students/ 
- Retrieve/Update/Delete Student : /api/students/<PK\>
- Create/List Stars : /api/star/ 
- Retrieve/Update/Delete Star : /api/star/<PK\>


## Template Endpoints
- List Teachers : /teachers/ 
- Create Student : /student/ 
- List Teachers Student : /mystudents/ 
- Retrieve/Update/Delete Student : /api/students/<PK\>
- List Stars : /star/ 

## TODO
- Register/ Login Teacher Template
- GraphQL endpoint
- Update Star FE implementation
- Dockerization


## Testing
- Run python manage.py test api.tests # Run test


## Coverage (so far) (No front-end tests completed)

```

Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
__init__.py                                     0      0   100%
api/__init__.py                                 0      0   100%
api/admin.py                                    5      0   100%
api/apps.py                                     3      3     0%
api/migrations/0001_initial.py                  8      0   100%
api/migrations/0002_auto_20191201_0303.py       4      0   100%
api/migrations/0003_auto_20191201_0304.py       4      0   100%
api/migrations/0004_auto_20191201_0409.py       6      0   100%
api/migrations/0005_auto_20191201_0828.py       4      0   100%
api/migrations/__init__.py                      0      0   100%
api/models.py                                  23      2    91%
api/serializers.py                             41      0   100%
api/star/urls.py                                3      0   100%
api/students/__init__.py                        0      0   100%
api/students/urls.py                            3      0   100%
api/teachers/urls.py                            3      0   100%
api/tests/__init__.py                           0      0   100%
api/tests/h_data.py                             7      0   100%
api/tests/test_star_views.py                   79      0   100%
api/tests/test_student_views.py                59      0   100%
api/tests/test_teacher_views.py                59      0   100%
api/views.py                                   36      0   100%
manage.py                                      12      2    83%
tivix/__init__.py                               0      0   100%
tivix/settings.py                              21      0   100%
tivix/urls.py                                   4      0   100%
tivix/views.py                                 22     16    27%
tivix/wsgi.py                                   4      4     0%
---------------------------------------------------------------
TOTAL                                         410     27    93%
```
