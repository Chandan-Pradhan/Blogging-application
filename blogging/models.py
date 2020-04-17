from django.db import models


class ToDo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=400)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.text


class Info(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    phone_no = models.CharField(max_length=20)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
