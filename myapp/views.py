from django.shortcuts import render, redirect
from .models import Todo

# =================================== VIEWS HERE =========================

def home(request):    
    return render(request, "home.html")

# ====================================== TODO =========================================

def todo(request):
    
    todos = Todo.objects.all()
    
    parameters = {
        "todos": todos,
    }
    
    return render(request, "todo.html", parameters)

# ===================================== ADD TODO =======================================

def add_todo(request):
    
    if request.method == "POST":
        
        # Template s view m data la rha hu
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        # View vala data model m save kr rha hu
        new_todo = Todo(task=user_task, created_at=user_created_at)
        new_todo.save()
        
        return redirect("todo")
        
    return render(request, "add_todo.html")

# ================================== DELETE TODO ===================================

def delete_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    todo.delete()

    return redirect("todo")
