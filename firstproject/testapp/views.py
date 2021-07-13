from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.
def greeting(request):
    s='<title>Landing Page</title>'
    s+='<h1>Hello and Welcome to first view of testapp</h1>'
    s+='<h3>This is landing page</h3>'
    return HttpResponse(s)
def showContact(request):
    s='<h2>Contact Page</h2>'
    s+='<p>website: harsh.com</p>'
    s+='<p>Mob: 9009009001</p>'
    return HttpResponse(s)
def about(request):
    return render(request,'testapp/about.html')
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employee.html',data)
    return res
