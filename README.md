# Tivix School System ( Django Rest Framework & Vue.js)


## Setup:
- Run `docker-compose build`
- Run `docker-compose run web python manage.py migrate`
- Run `docker-compose up`
- go to `localhost:8000`


## API Endpoints
- Create/List Teachers : /api/teachers/ 
- Retrieve/Update/Delete Teacher : /api/teachers/<PK\>
- Create/List Student : /api/students/ 
- Retrieve/Update/Delete Student : /api/students/<PK\>
- Create/List Stars : /api/star/ 
- Retrieve/Update/Delete Star : /api/star/<PK\>

## TODO
- GraphQL endpoint

## Testing
- Run python manage.py test api.tests tivix.tests # Run test


## Coverage (so far) (No front-end tests completed)

```

Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
__init__.py                           0      0   100%
api/__init__.py                       0      0   100%
api/admin.py                          5      0   100%
api/models.py                        21      0   100%
api/serializers.py                   57      5    91%   32-36
api/star/__init__.py                  0      0   100%
api/star/urls.py                      3      0   100%
api/students/__init__.py              0      0   100%
api/students/urls.py                  3      0   100%
api/teachers/__init__.py              0      0   100%
api/teachers/urls.py                  3      0   100%
api/tests/__init__.py                 0      0   100%
api/tests/h_data.py                   7      0   100%
api/tests/test_models.py             58      0   100%
api/tests/test_star_views.py         79      0   100%
api/tests/test_student_views.py      59      0   100%
api/tests/test_teacher_views.py      59      0   100%
api/views.py                         39      1    97%   68
tivix/__init__.py                     0      0   100%
tivix/settings.py                    34      0   100%
tivix/tests.py                       90      0   100%
tivix/urls.py                         4      0   100%
tivix/views.py                       64      2    97%   82-83
---------------------------------------------------------------
TOTAL                               585      8    99%

```
