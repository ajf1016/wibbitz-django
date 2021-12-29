from django.urls import path
from web.views import *


app_name = "web"
urlpatterns = [    
    path("",index,name="index"),
    path("subscribe/",subscribe,name="subscribe"),
    path("contact/",contact,name="contact"),
    path("product/<int:pk>/",product,name="product")
]
