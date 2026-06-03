# from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Student
# import json


# # =========================
# # CREATE STUDENT
# # =========================

# @csrf_exempt
# def create_student(request):

#     if request.method == "POST":

#         data = json.loads(request.body)

#         student = Student.objects.create(
#             name=data['name'],
#             roll_number=data['roll_number'],
#             email=data['email'],
#             age=data['age']
#         )

#         return JsonResponse({
#             'message': 'Student Created',
#             'id': student.id
#         })


# # =========================
# # GET ALL STUDENTS
# # =========================

# def get_students(request):

#     if request.method == "GET":

#         students = list(
#             Student.objects.values()
#         )

#         return JsonResponse(
#             students,
#             safe=False
#         )


# # =========================
# # UPDATE STUDENT
# # =========================

# @csrf_exempt
# def update_student(request, id):

#     if request.method == "PUT":

#         student = Student.objects.get(id=id)

#         data = json.loads(request.body)

#         student.name = data.get(
#             'name',
#             student.name
#         )

#         student.email = data.get(
#             'email',
#             student.email
#         )

#         student.age = data.get(
#             'age',
#             student.age
#         )

#         student.save()

#         return JsonResponse({
#             'message': 'Student Updated'
#         })


# # =========================
# # DELETE STUDENT
# # =========================

# @csrf_exempt
# def delete_student(request, id):

#     if request.method == "DELETE":

#         student = Student.objects.get(id=id)

#         student.delete()

#         return JsonResponse({
#             'message': 'Student Deleted'
#         })
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


# ====================================
# STUDENT LIST + CREATE
# ====================================

class StudentListCreateAPIView(APIView):

    # GET ALL STUDENTS
    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)


    # CREATE STUDENT
    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ====================================
# STUDENT DETAIL API
# ====================================

class StudentDetailAPIView(APIView):


    # GET SINGLE STUDENT
    def get(self, request, pk):

        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)


    # UPDATE STUDENT
    def put(self, request, pk):

        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE STUDENT
    def delete(self, request, pk):

        student = Student.objects.get(pk=pk)

        student.delete()

        return Response({
            'message': 'Student Deleted Successfully'
        })