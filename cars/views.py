from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from cars.models import Car, Brand
from common.models import ContactMessage
from cars.forms import ContactMessageForm, SearchBrandForm
from users.models import CustomUser


def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
        is_superuser=False,
        is_staff=True
    )
    brands = Brand.objects.all()
    return render(
        request=request, 
        template_name='index.html',
        context={
            "cars": cars,
            "users": users,
            "brands": brands
        }
    )

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'service.html')


def contact_form_handler(request):
    if request.method == "POST":
        print(request.POST)
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            return render(request, 'index.html')
    
    return HttpResponse("Invalid Form")


def search_car_handler(request):
    if request.method == "POST":
        print(request.POST)

        form = SearchBrandForm(request.POST)

        if form.is_valid():
            brand = form.cleaned_data["brand"]
            print(">>>", brand)

            cars = Car.objects.filter(brand=brand)
            users = CustomUser.objects.filter(
                is_active=True,
                is_superuser=False,
                is_staff=True
            )
            brands = Brand.objects.all()

            return render(
                request=request, 
                template_name='index.html',
                context={
                    "cars": cars,
                    "users": users,
                    "brands": brands
                }
            )
    
    return HttpResponse("Invalid Form")