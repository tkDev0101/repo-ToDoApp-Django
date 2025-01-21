from django.shortcuts import render
from .models import Mytodo
from .forms import TodoForm

# Create your views here.
def alltodos(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()


    return render(request, 'alltodo.html',  {'task': tasks, 'form': form} )