from django import forms
from .models import Flashcard, Folder

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'memo', 'folder']
        widgets = {
            'front': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '表面のテキスト'}),
            'back': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '裏面のテキスト'}),
            'memo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'メモを記入'}),
            'folder': forms.Select(attrs={'class': 'form-control'}),
        }

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'フォルダ名'})
        }