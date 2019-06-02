from model_mommy import mommy
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from management.models import Employee

class EmployeeIndexView(TestCase):
    
    def setUp(self):
        self.url = reverse('home')
        self.client = Client()
        mommy.make('management.Employee', _quantity=10)

    def tearDown(self):
        Employee.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('employees' in response.context)
        employees = response.context.get('employees')
        self.assertEquals(employees.count(), 10)