from django.shortcuts import render

def admin_homepage(request):
    return render(request, 'Admin_Home.html')
