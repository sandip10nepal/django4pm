from .views import *
from django.urls import path, include

urlpatterns = [
    path("", home, name = "home"),
    path("about", about, name = "about"),
    path("portfolio", portfolio, name = "portfolio"),
    path("contact", contact, name = "contact"),
    path("price", price, name = "price"),
    path("services", services, name = "services"),
]