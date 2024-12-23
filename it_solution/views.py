from django.shortcuts import render
from django.views.generic import ListView 

# Create your views here.




def homeview(request):

    return render(request, "home/index.html")


