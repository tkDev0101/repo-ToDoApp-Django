from django import forms
from .models import MytodoModel


# Form class for task input, based on the MytodoModel
class TodoForm(forms.ModelForm):

    # Define a custom field for the 'task' attribute with additional properties
    
    task = forms.CharField(max_length=50, widget=forms.TextInput( attrs= { 
        'id': 'todoField', 'placeholder': 'Enter Task' } ))

    class Meta:
        model = MytodoModel # Link the form to the MytodoModel
        fields = [ 'task', ] # Specify which model fields to include in the form