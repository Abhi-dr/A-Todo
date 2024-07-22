from django.shortcuts import render

from .models import Todo

def home(request):    
    return render(request, "home.html")











def todo(request):
    
    todos = Todo.objects.all()
    
    parameters = {
        "todos": todos,
        "name": "This is DK"
    }
    
    return render(request, "todo.html", parameters)















def add_todo(request):
    return render(request, "add_todo.html")



'''
Django models m hr ek class k kuch methods mujhe phle s milue hue hn

jse ki?

1. objects.all()

Todo.objects.all()

'''




'''
Todo ek class h
Todo m m objects create kr pa rha hu
Todo m objects ko modify bhi kia ja skta h

Todo ek Mutable data rkh rkha h?

Todo.objects.all() ka return data type kya hoga


MOST IMPORTANT:
Dictionary m key or value kse likhte hn ye pta hona chaiye

data = {
    key: value
}

'''