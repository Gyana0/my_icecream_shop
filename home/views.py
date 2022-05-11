from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page..")
def about(request): 
    return render(request, 'about.html')
    # return HttpResponse("This is a about page..")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is our service page..")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message') 
        contact = Contact(name=name, phone=phone, email = email, message=message, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    # return HttpResponse("This is our contact page..")
def payment(request):
    return render(request, 'payment_form.html')