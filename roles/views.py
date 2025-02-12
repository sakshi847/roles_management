from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Role
from .forms import RoleForm, SignupForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import views as auth_views


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home_message.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect('home')  
    else:
        form = SignupForm()
    return render(request, 'roles/signup.html', {'form': form})  

def is_admin(user):
    if user.is_superuser:
        return True
    return HttpResponseRedirect('/') 

@login_required
@user_passes_test(is_admin)
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'roles/role_list.html', {'roles': roles})

@login_required
@user_passes_test(is_admin)
def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Role created successfully!')
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'roles/role_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def role_update(request, role_id):
    role = get_object_or_404(Role, role_id=role_id, status=True)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, 'Role updated successfully!')
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/role_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def role_delete(request, role_id):
    role = get_object_or_404(Role, role_id=role_id, status=True)
    if request.method == 'POST':
        role.status = False  
        role.save()
        messages.success(request, 'Role has been deactivated successfully!')
        return redirect('role_list')  

    return render(request, 'roles/role_confirm_delete.html', {'role': role})



class CustomLoginView(auth_views.LoginView):
    def get_redirect_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url  
        return super().get_redirect_url()  


