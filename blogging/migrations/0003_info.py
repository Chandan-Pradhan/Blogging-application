# Generated by Django 3.0 on 2020-04-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_todo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('phone_no', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
