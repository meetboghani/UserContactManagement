# Generated by Django 3.0.8 on 2021-06-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('middle', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
