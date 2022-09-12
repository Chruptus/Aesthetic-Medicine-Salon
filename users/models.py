from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="client_user")
    phone_number = models.IntegerField()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="employee_user")
    phone_number = models.IntegerField()
    home_adress = models.TextField()
    workplace = models.TextField()
    
class Procedure(models.Model):
    name = models.TextField()
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name="employee_procedure")
    price = models.FloatField()
    length_minutes = models.IntegerField()

class Visit(models.Model):
    visit_date = models.DateField()
    visit_time = models.TextField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name="client_visit")
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name="employee_visit")
    procedure = models.ForeignKey(Procedure, on_delete = models.CASCADE, related_name="procedure_visit")
    STATUS_CHOICE = (
        ('C', 'Cancelled'),
        ('D', 'Done'),
        ('P', 'Pending'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)