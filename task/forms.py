from django import forms
from .models import Task
import datetime
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'Task_Category':forms.CheckboxSelectMultiple(),
            'Task_Assign_Date': forms.DateInput(attrs={'type':'date'}),
            'Task_Description':forms.Textarea(attrs={'rows':4})
        }