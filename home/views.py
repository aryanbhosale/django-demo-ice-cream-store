from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    context={
        'variable':"this message is sent.",
        'variable1':"Aryan is great!",
    }
    return render(request, 'index.html', context)

def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')


def contact(request):
    #return HttpResponse("this is contact page")
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,phone=phone,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def services(request):
    #return HttpResponse("this is services page")
    return render(request, 'services.html')

