from django.shortcuts import render, redirect
from .forms import UserForm, ClientForm, UserUpdateForm, ClientUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': 
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user_form.instance.username = user_form.instance.email
            user = user_form.save()
            client = client_form.save(commit = False)
            client.user = user
            client.save()
            return redirect('login')
    else:
        user_form = UserForm()
        client_form = ClientForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'client_form': client_form})

@login_required
def update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        client_form = ClientUpdateForm(request.POST, instance=request.user.client_user)
        if user_form.is_valid() and client_form.is_valid():
            user_form.instance.username = user_form.instance.email
            user_form.save()
            client_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        client_form = ClientUpdateForm(instance=request.user.client_user)
   
    context = {
        'user_form': user_form,
        'client_form': client_form
    }
    
    return render(request, 'users/update.html', context)
