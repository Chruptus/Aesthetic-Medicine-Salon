from http import client
from re import T
from this import d
from tkinter import E
from django.shortcuts import redirect, render
from django.shortcuts import render
from users import models as user_models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import VisitForm
from datetime import datetime
from users.models import Visit

picked_procedure = ''

# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'website/contact.html')

def login(request):
    return render(request, 'website/login.html')

def pricing(request):
    return render(request, 'pricing.html')

def index(request):
    return render(request, 'index.html', {})

@login_required
def profile(request):
    try:
        user_req = request.user
        all_visits = user_models.Visit.objects.filter(client = user_req.client_user).order_by('-visit_date')
        visits_list=[]
        for visit in all_visits:
            visit_status_dict = {'P':'pending', 'C':'cancelled', 'D':'done'}
            visit_status = visit_status_dict[visit.status]
            one_visit = {'visit_date':visit.visit_date.strftime("%d/%m/%y"), 'visit_time':visit.visit_time, 'status':visit_status, 'procedure':visit.procedure.name, 'employee_first_name':visit.procedure.employee.user.first_name,'employee_last_name': visit.procedure.employee.user.last_name, 'price':visit.procedure.price}
            visits_list.append(one_visit)
        return render(request, 'website/profile.html', context={'visits':visits_list})
    except:
        user_req = request.user
        all_visits = user_models.Visit.objects.filter(employee = user_req.employee_user).order_by('-visit_date')
        visits_list=[]
        for visit in all_visits:
            visit_status_dict = {'P':'pending', 'C':'cancelled', 'D':'done'}
            visit_status = visit_status_dict[visit.status]
            one_visit = {'visit_date':visit.visit_date.strftime("%d/%m/%y"), 'visit_time':visit.visit_time, 'status':visit_status, 'procedure':visit.procedure.name, 'employee_first_name':visit.client.user.first_name,'employee_last_name': visit.client.user.last_name, 'price':visit.procedure.price}
            visits_list.append(one_visit)
        return render(request, 'website/profile.html', context={'visits':visits_list})

@login_required
def choose_procedure(request):
    if request.method == 'POST':
        global picked_procedure
        picked_procedure = request.POST['button']
        return redirect('add_visit')

    all_procedures= user_models.Procedure.objects.all()

    procedures_names = []
    procedures_times = []
    procedures_employees = []
    procedures_prices = []

    for procedure in all_procedures:
        if procedure.name not in procedures_names:
            procedures_names.append(procedure.name)
            procedures_times.append(procedure.length_minutes)
            employee = procedure.employee.user.first_name + " " + procedure.employee.user.last_name
            procedures_employees.append(employee)
            procedures_prices.append(procedure.price)
        else:
            for i in range(len(procedures_names)):
                if procedure.name == procedures_names[i]:
                    if procedures_prices[i] == procedure.price:
                        employee_old = procedures_employees[i]
                        new_employee = employee_old + ", " + procedure.employee.user.first_name + " " + procedure.employee.user.last_name
                        procedures_employees[i] = new_employee
                    else:
                        procedures_names.append(procedure.name)
                        procedures_times.append(procedure.length_minutes)
                        procedures_employees.append(procedure.employee)
                        procedures_prices.append(procedure.price)

    num_list = [i for i in range(len(procedures_names))]
    html_list = zip(procedures_names, procedures_times, procedures_employees, procedures_prices, num_list)

    return render(request, 'website/choose_procedure.html', context={'procedures':html_list})

@login_required
def add_visit(request):
    if request.method == 'POST': 
        visit_form = VisitForm(request.POST)
        #if visit_form.is_valid():
        procedure_picked = get_procedure()

        x = user_models.Procedure.objects.filter(name=procedure_picked)
        c = user_models.Client.objects.filter(user__username=request.user)
        d = request.POST['visit_date']
        d = datetime.strptime(d, '%Y-%m-%d').date()
        t = request.POST['visit_time']
        e = 'Pol'
        e2 = user_models.Employee.objects.filter(user__last_name=e)

        b = Visit(status='P', procedure=x[0], client = c[0], visit_date = d, visit_time = t, employee = e2[0])
        b.save()
        return redirect('profile')

    visit_form = VisitForm()

    procedure_picked = get_procedure()

    return render(request, 'website/add_visit.html', context={'procedure':procedure_picked, 'visit_form':visit_form})

def get_procedure():
    all_procedures= user_models.Procedure.objects.all()

    procedures_names = []
    for procedure in all_procedures:
        if procedure.name not in procedures_names:
            procedures_names.append(procedure.name)

    procedure_picked = str(procedures_names[int(picked_procedure)])
    return procedure_picked