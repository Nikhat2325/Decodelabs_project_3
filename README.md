# Database Integration REST API

## Project Overview

This project demonstrates Database Integration using Django REST Framework (DRF).
<img width="671" height="524" alt="Screenshot 2026-06-04 014237" src="https://github.com/user-attachments/assets/4a5f61e0-cd1e-4fe5-a350-c5f09a5f117b" />

The application connects a backend API with a SQLite database and implements complete CRUD (Create, Read, Update, Delete) operations using Django ORM.

The project also demonstrates database relationships, validations, constraints, and secure database access through ORM queries.

---

## Objective

Build a database-driven REST API capable of:

* Storing data permanently in SQLite database
* Performing CRUD operations
* Applying validations and constraints
* Managing relationships between tables
* Protecting against SQL Injection using Django ORM

---

## Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* SQLite Database
* Django ORM
* Thunder Client / Postman

---

## Database Models

### Teacher

```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
```

### Student

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
```

### Student Profile

```python
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
```

### Course

```python
class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    course_code = models.CharField(max_length=20, unique=True)
    duration = models.IntegerField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(Student)
```

---

## Database Relationships

### One-to-One Relationship

Student ↔ StudentProfile

```text
Student
   |
   | One-To-One
   |
StudentProfile
```

### One-to-Many Relationship

Teacher ↔ Course

```text
Teacher
   |
   | One Teacher can teach many Courses
   |
Course
```

### Many-to-Many Relationship

Student ↔ Course

```text
Student
   |
   | Many Students
   |
Course
   |
   | Many Courses
```

---

## CRUD Operations Implemented

### Create Student

```http
POST /students/
```

Request:

```json
{
    "name": "Mithra",
    "roll_number": "CS101",
    "email": "mithra@gmail.com",
    "age": 20
}
```

Response:

```json
{
    "id": 1,
    "name": "Mithra",
    "roll_number": "CS101",
    "email": "mithra@gmail.com",
    "age": 20
}
```

Status Code:

```http
201 Created
```

---

### Get All Students

```http
GET /students/
```

Response:

```json
[
    {
        "id": 1,
        "name": "Mithra",
        "roll_number": "CS101",
        "email": "mithra@gmail.com",
        "age": 20
    }
]
```

Status Code:

```http
200 OK
```

---

### Get Single Student

```http
GET /students/1/
```

---

### Update Student

```http
PUT /students/1/
```

Request:

```json
{
    "name": "Mithra Tarvin",
    "roll_number": "CS101",
    "email": "mithra@gmail.com",
    "age": 21
}
```

Response:

```json
{
    "id": 1,
    "name": "Mithra Tarvin",
    "roll_number": "CS101",
    "email": "mithra@gmail.com",
    "age": 21
}
```

Status Code:

```http
200 OK
```

---

### Delete Student

```http
DELETE /students/1/
```

Response:

```json
{
    "message": "Student Deleted Successfully"
}

<img width="639" height="447" alt="Screenshot 2026-06-04 014306" src="https://github.com/user-attachments/assets/2b1067d7-c0a8-43b8-9017-98ed6185d5ba" />


Status Code:

```http
200 OK
```

---

## Validation & Constraints

The project implements database-level and application-level validations.

### Unique Constraints

```python
email = models.EmailField(unique=True)
roll_number = models.CharField(unique=True)
phone = models.CharField(unique=True)
course_code = models.CharField(unique=True)
```

### Required Fields

```python
name = models.CharField(max_length=100)
```

### Relationship Constraints

* One Student can have only one Profile.
* One Teacher can teach multiple Courses.
* Multiple Students can enroll in multiple Courses.

---

## Security Features

This project uses Django ORM for all database operations.

Example:

```python
Student.objects.get(pk=pk)
Student.objects.all()
```

Benefits:

* SQL Injection Protection
* Parameterized Queries
* Secure Data Access
* Easy Database Management

No raw SQL queries are used.

---

## API Endpoints

### Student APIs

```http
GET      /students/
POST     /students/
GET      /students/<id>/
PUT      /students/<id>/
DELETE   /students/<id>/
```

### Future APIs

```http
GET      /teachers/
POST     /teachers/

GET      /courses/
POST     /courses/

GET      /profiles/
POST     /profiles/
```

---

## Project Structure

```text
database_integration/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Testing

The APIs were tested using:

* Django REST Framework Browser API
* Thunder Client
* Postman

---

## Learning Outcomes

Through this project, I learned:

* Database Integration
* SQLite Database
* Django ORM
* REST API Development
* CRUD Operations
* Serializer Usage
* Database Relationships
* One-to-One Relationships
* One-to-Many Relationships
* Many-to-Many Relationships
* Validation and Constraints
* Secure Database Access
* HTTP Status Codes

---

## Future Enhancements

* JWT Authentication
* User Authorization
* Search & Filtering
* Pagination
* Course Enrollment APIs
* Teacher Management APIs
* Student Profile APIs
* Deployment on Cloud

