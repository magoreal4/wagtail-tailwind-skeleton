# Generated by Django 4.0.4 on 2022-05-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Correo Electronico', max_length=254)),
                ('full_name', models.CharField(help_text='Nombre y Apellido', max_length=40)),
            ],
        ),
    ]