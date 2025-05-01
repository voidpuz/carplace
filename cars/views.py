from django.shortcuts import render

from cars.models import Car
from users.models import CustomUser


def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
        is_superuser=False,
        is_staff=True
    )
    print(">>>", users)
    return render(
        request=request, 
        template_name='index.html',
        context={
            "cars": cars,
            "users": users
        }
    )