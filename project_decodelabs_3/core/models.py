from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique =True)
    department=models.CharField(max_length=100)
    created_At=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name=models.CharField(max_length=100,null=False)
    roll_number=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique =True)
    age=models.IntegerField()

    created_At=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class StudentProfile(models.Model):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.student.name


class Course(models.Model):

    title = models.CharField(
        max_length=200,
        unique=True
    )

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    duration = models.IntegerField()

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    students = models.ManyToManyField(
        Student,
        related_name='courses'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
