from django.urls import path

from cars.views import (
    index,
    about,
    services,
    contact_form_handler, 
    search_car_handler
)

app_name = "cars"

urlpatterns = [
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("contactmessage/", contact_form_handler, name="contactmessage"),
    path("search/", search_car_handler, name="search-car")
]
