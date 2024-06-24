from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
import json


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})


@csrf_exempt
def add_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo = Todo.objects.create(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
        )
        return JsonResponse(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "due_date": todo.due_date.isoformat() if todo.due_date else None,
                "completed": todo.completed,
            }
        )


@csrf_exempt
def update_todo(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        data = json.loads(request.body)
        todo.completed = data["completed"]
        todo.save()
        return JsonResponse({"success": True})
