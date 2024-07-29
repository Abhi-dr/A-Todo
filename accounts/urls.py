from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    
]

# 127.0.0.1:8000/accounts/login/

# url concatination/add/join/plus/judaav/ekta/sambandh
