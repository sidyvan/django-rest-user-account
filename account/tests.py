from django.test import TestCase
from account.models import User
from datetime import date


class UserTestCase(TestCase):
    def setUp(self):
        self.user =  User.objects.create(email="teste@teste.com", fullName="Teste", birthDate="2001-02-02", phone="(31) 986097668", document="099.556.430-21")

    def test_check_count_user(self):

        assert User.objects.all().count() == 1

