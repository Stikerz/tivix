STUDENTS = [
    {"first_name": "James", "last_name": "Brown", "age": "2019-02-04", "year": 1},
    {"first_name": "Lala", "last_name": "Land", "age": "2019-12-01", "year": 4},
    {"first_name": "Duol", "last_name": "Cod", "age": "2019-12-01", "year": 2},
]

TEACHERS = [
    {
        "username": "teacher1",
        "first_name": "one",
        "last_name": "one",
        "email": "one@tivix.com",
    },
    {
        "username": "teacher2",
        "password": "lolll",
        "first_name": "two",
        "last_name": "two",
        "email": "two@tivix.com",
        "students": [],
    },
    {
        "username": "teacher3",
        "password": "lolll",
        "first_name": "three",
        "last_name": "three",
        "email": "three@tivix.com",
        "students": [],
    },
]

INVALID_STUDENT = {"first_name": "", "last_name": "", "age": "", "year": None}
INVALID_TEACHER = {
    "username": "",
    "password": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "students": [],
}

STARS = [
    {"teacher": 1, "student": 1, "star": True},
    {"teacher": 1, "student": 2, "star": True},
    {"teacher": 1, "student": 3, "star": False},
]

INVALID_STAR = {"teacher": None, "student": None, "star": None}

UPDATED_STAR = {"teacher": 1, "student": 1, "star": False}
