from django.shortcuts import render

# Create your views here.
def home(request):
    return render(render, 'app/home.html')