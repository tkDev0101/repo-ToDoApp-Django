from django.shortcuts import render, redirect
from .models import MytodoModel #Mytodo
from .forms import TodoForm


def alltodos(request):
    tasks = MytodoModel.objects.all() #Model.objetcs.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'alltodo.html',  {'task': tasks, 'form': form} )


def updateItem(request, pk):
    todo = MytodoModel.objects.get( id=pk )
    updateForm = TodoForm(instance= todo)
    
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = todo ) #edit current item, not create a new one

        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')

    return render(request, 'updateItem.html', {'todo': todo, 'updateForm': updateForm} )


def deleteItem(request, pk):
    task = MytodoModel.objects.get( id=pk )
    task.delete()
    return redirect('alltodos')
