from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerialiser

# Create your views here.
class EmployeeList(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialiser