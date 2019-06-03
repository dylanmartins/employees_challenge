import logging
import json
from django.http import Http404, HttpResponse
from .models import Employee
from .serializers import EmployeeSerialiser
from .helpers import normalize_objects, validate_email
from .forms import CreateEmployeeForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


# Create your views here.
class EmployeeApi(APIView):
    """
    List all employees, get a employee, delete a employee or create a new employee.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            employee = self.get_object(pk)
            serializer = EmployeeSerialiser(employee)
            data = serializer.data
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerialiser(employees, many=True)
            data = normalize_objects(serializer.data)
        return HttpResponse(
            json.dumps(data),
            content_type="application/json")

    def post(self, request):
        employees = request.data
        data = {'success': []}
        for obj in employees:
            serializer = EmployeeSerialiser(data=obj)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                if validate_email(email):
                    employee = Employee.objects.filter(email=email).all()
                    if not employee:
                        serializer.save()
                        data['success'].append(email)
        return HttpResponse(
            json.dumps(data),
            content_type="application/json")

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    html_data = {
        'employees': Employee.objects.all()
    }
    return render(request, 'index.html', html_data)


def create_employee(request):
    html_data = {
    }
    if request.method == 'GET':
        form = CreateEmployeeForm()
        html_data['form'] = form
        return render(request, 'create_employee.html', html_data)
    
    form = CreateEmployeeForm(request.POST)
    if form.is_valid():
        employee = Employee.objects.filter(email=form.cleaned_data['email'])
        if not employee:
            employee = Employee(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                department=form.cleaned_data['department']
            )
            employee.save()
    return redirect('home')


def delete_employee(request, pk):
    html_data = {}
    if not pk:
        return Response(status=status.HTTP_204_NO_CONTENT)

    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return redirect('home')
    except Employee.DoesNotExist as e:
        raise Http404