from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

def admin_login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to your desired page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'admin/admin_login.html', {'form': form})



def dashboard_view(request):
    return render(request, 'admin/dashboard.html')