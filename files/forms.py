from django import forms
from .models import File, Comment

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'description', 'file',  'uploaded_by'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']