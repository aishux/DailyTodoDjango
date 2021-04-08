from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_todo_items': all_todo_items})

def addTodo(request):
    if(request.method=="POST"):
        c = request.POST.get('content')
        new_item = TodoItem(content=c)
        new_item.save()
        print(new_item)
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    del_item = TodoItem.objects.get(id=todo_id)
    del_item.delete()
    return HttpResponseRedirect('/todo/')

 