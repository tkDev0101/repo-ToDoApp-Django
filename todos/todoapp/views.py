from django.shortcuts import render, redirect
from .models import MytodoModel #Mytodo
from .forms import TodoForm


def alltodos(request):
    tasks = MytodoModel.objects.all() #Model.objetcs.all() # Fetch all tasks from the database
    form = TodoForm() # Create an empty form instance

    if request.method == 'POST': # Check if the request method is POST (form submission)
        form = TodoForm(request.POST) # Bind form data from the request

        if form.is_valid(): # Validate the form data
            form.save() # Save the new task to the database

    return render(request, 'alltodo.html',  {'task': tasks, 'form': form} ) 
        # Render the template with the list of tasks and the form


def updateItem(request, pk):
    todo = MytodoModel.objects.get( id=pk ) # Retrieve the specific task using its primary key (pk)
    updateForm = TodoForm(instance= todo)  # Pre-fill the form with the existing task data
    
    if request.method == 'POST': # Check if the request method is POST (form submission)
        updateForm = TodoForm(request.POST, instance = todo ) #edit current item, not create a new one # Update the specific task instance

        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos') # Redirect to the list of all tasks

    return render(request, 'updateItem.html', {'todo': todo, 'updateForm': updateForm} )
                # Render the template with the specific task and the update form


def deleteItem(request, pk):
    task = MytodoModel.objects.get( id=pk )
    task.delete()
    return redirect('alltodos') # Redirect to the list of all tasks
