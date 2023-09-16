from django.shortcuts import render
from django.http import HttpResponse
from . models import student

# Create your views here.

def data(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        da=student.objects.create(name=name,email=email,mobile=mobile)
        da.save()
        return HttpResponse("good")
    else:
        return render(request, 'data.html')

