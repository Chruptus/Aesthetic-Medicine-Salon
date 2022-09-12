from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Visit, Employee

times =(
    ("9:00", "9:00"),
    ("9:15", "9:15"),
    ("9:30", "9:30"),
    ("9:45", "9:45"),
    ("10:00", "10:00"),
    ("10:15", "10:15"),
    ("10:30", "10:30"),
    ("10:45", "10:45"),
    ("11:00", "11:00"),
    ("11:15", "11:15"),
    ("11:30", "11:30"),
    ("11:45", "11:45"),
    ("12:00", "12:00"),
    ("12:15", "12:15"),
    ("12:30", "12:30"),
    ("12:45", "12:45"),
    ("13:00", "13:00"),
    ("13:15", "13:15"),
    ("13:30", "13:30"),
    ("13:45", "13:45"),
    ("14:00", "14:00"),
    ("14:15", "14:15"),
    ("14:30", "14:30"),
    ("14:45", "14:45"),
    ("15:00", "15:00"),
    ("15:15", "15:15"),
    ("15:30", "15:30"),
    ("15:45", "15:45"),
    ("16:00", "16:00"),
    ("16:15", "16:15"),
    ("16:30", "16:30"),
    ("16:45", "16:45"),
    ("17:00", "17:00"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class VisitForm(forms.ModelForm): 
    visit_time = forms.ChoiceField(choices = times)
    employee = forms.ModelChoiceField(queryset=Employee.objects.values_list('user__last_name', flat=True))
    
    class Meta:
        model = Visit
        fields = ['visit_date', 'visit_time', 'employee']
        widgets = {'visit_date': DateInput()}