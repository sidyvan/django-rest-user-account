from django.db import models
from cpf_field.models import CPFField
# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, email, birthDate, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            birthDate=birthDate,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birthDate, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            birthDate=birthDate,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user





def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    
def validate_age(born):
    age = calculate_age(born)
    if age < 18:  
        raise ValidationError(_(' Com apenas %(age) s anos não é possível cadastrar.Aguarde até completar 18 anos'), 
        params= {'age':age},) 
    
class User(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name='Endereço de Email',
        max_length=255,
        unique=True,
    )
    fullName = models.CharField('Nome Completo', max_length=255)
    birthDate = models.DateField('Data de Nascimento', validators=[validate_age])

    phone_regex = RegexValidator(regex=r'^(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})$', message="Entre com o formato correto do telefone Ex: (99) 99999-9999")
    phone = models.CharField('Telefone', validators=[phone_regex], max_length=50)
    document = CPFField('CPF', unique=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthDate']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin