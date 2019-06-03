import json
from model_mommy import mommy
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from management.models import Employee

class EmployeeIndexViewTest(TestCase):

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


class EmployeeApiTest(TestCase):

    def setUp(self):
        self.url = '/employee/'
        self.client = Client()
        mommy.make('management.Employee', _quantity=10)

    def tearDown(self):
        Employee.objects.all().delete()

    def test_get_without_pk(self):
        response = self.client.get(self.url)
        content = eval(response.content)
        self.assertEquals(len(content), 10)

    def test_get_with_pk(self):
        response = self.client.get(self.url + '1/')
        content = eval(response.content)
        self.assertNotEquals(type(content), list)

    def test_post(self):
        response = self.client.get(self.url)
        content = eval(response.content)
        self.assertEquals(len(content), 10)

        test_data = [{
            'name' : 'mock_employee',
            'email': 'mock_email@mail.com',
            'department': 'mock_department',
        }]
        response = self.client.post(
            self.url, json.dumps(test_data),
            format='json', content_type='application/json')

        response = self.client.get(self.url)
        content = eval(response.content)
        self.assertEquals(len(content), 11)

    def test_post_invalid(self):
        response = self.client.get(self.url)
        content = eval(response.content)
        self.assertEquals(len(content), 10)

        test_data = [{
            'name' : 'mock_employee',
            'department': 'mock_department',
        }]
        response = self.client.post(
            self.url, json.dumps(test_data),
            format='json', content_type='application/json')

        response = self.client.get(self.url)
        content = eval(response.content)
        self.assertEquals(len(content), 10)

    def test_delete(self):
        response = self.client.get(self.url)
        content = eval(response.content)
        before_qty = len(content)

        response = self.client.delete(self.url + '1/')
        self.assertEquals(response.status_code, 204)

        response = self.client.get(self.url)
        content = eval(response.content)
        after_qty = len(content)

        self.assertNotEquals(before_qty, after_qty)

    def test_delete_invalid(self):
        response = self.client.get(self.url)
        content = eval(response.content)
        before_qty = len(content)

        response = self.client.delete(self.url + '9999/')
        self.assertEquals(response.status_code, 404)

        response = self.client.get(self.url)
        content = eval(response.content)
        after_qty = len(content)

        self.assertEquals(before_qty, after_qty)