from django.shortcuts import render

# Create your views here.

def unknown(request):
    return render(request,'unknown.html')