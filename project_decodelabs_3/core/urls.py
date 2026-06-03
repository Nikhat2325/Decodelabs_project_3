# from django.urls import path
# from . import views

# urlpatterns = [

#     path(
#         'students/create/',
#         views.create_student
#     ),

#     path(
#         'stu/',
#         views.get_students
#     ),

#     path(
#         'students/update/<int:id>/',
#         views.update_student
#     ),

#     path(
#         'students/delete/<int:id>/',
#         views.delete_student
#     ),
# ]

from django.urls import path
from .views import *


urlpatterns = [

    path(
        'students/',
        StudentListCreateAPIView.as_view()
    ),

    path(
        'students/<int:pk>/',
        StudentDetailAPIView.as_view()
    ),
]