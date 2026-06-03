from rest_framework import serializers
from .models import *


# =========================
# TEACHER SERIALIZER
# =========================

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


# =========================
# STUDENT SERIALIZER
# =========================

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


# =========================
# STUDENT PROFILE SERIALIZER
# =========================

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = '__all__'


# =========================
# COURSE SERIALIZER
# =========================

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'