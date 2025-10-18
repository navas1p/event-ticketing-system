from django.shortcuts import render

# Vendors views

def dashboard(request):
    return render(request, 'vendors/dashboard.html')
