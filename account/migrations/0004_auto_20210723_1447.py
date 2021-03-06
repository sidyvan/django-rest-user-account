# Generated by Django 3.2.5 on 2021-07-23 17:47

import account.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210723_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(validators=[account.models.validate_age], verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Entre com o formato correto do telefone Ex: (99) 99999-9999', regex='^(\\(?\\d{2}\\)?\\s)?(\\d{4,5}\\-\\d{4})$')], verbose_name='Telefone'),
        ),
    ]
