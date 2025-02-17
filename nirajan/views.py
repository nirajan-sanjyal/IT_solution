from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
from django.contrib import messages


def admin_login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('nirajan:dashboard')  # Redirect to your desired page after registration
        else:
            print(form.errors)
            return render(request, 'admin_pannel/admin_login.html', {'form': form.errors})
    else:
        form = UserCreationForm()
    
    return render(request, 'admin_pannel/admin_login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            print("successful")
            return redirect('it_solution:admin-page')  
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'admin_pannel/login.html')




def dashboard_view(request):
    return render(request, 'admin_pannel/dashboard.html')





def logout_view(request):
    logout(request)  # Logs out the 
    return redirect('/')  # Redirect to a desired page