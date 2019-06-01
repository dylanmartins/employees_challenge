import logging
import json
from django.http import Http404, HttpResponse
from .models import Employee
from .serializers import EmployeeSerialiser
from .helpers import normalize_employees
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class EmployeeApi(APIView):
    """
    List all employees, delete a employee or create a new employee.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerialiser(employees, many=True)
        data = normalize_employees(serializer.data)
        return HttpResponse(
            json.dumps(data),
            content_type="application/json")

    def post(self, request):
        serializer = EmployeeSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)