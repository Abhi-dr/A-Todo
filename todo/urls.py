from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("myapp.urls")),
    path("accounts/", include("accounts.urls"))
]

# 127.0.0.1:8000/accounts/