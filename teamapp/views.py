from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from .models import Flashcard, Folder
from .forms import FlashcardForm, FolderForm
import random

# Create your views here.
def index(request):
    return render(request, 'teamapp/index.html')

def create_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list') # 登録後のリダイレクト先
    else:
        form = FlashcardForm()
    return render(request, 'teamapp/create_flashcard.html', {'form': form})

# def create_flashcard(request):
#     if request.method == 'POST':
#         form = FlashcardForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('flashcard_list') # 登録後のリダイレクト先
#     else:
#         form = {
#             "form": FlashcardForm()
#         }
#         return render(request, 'teamapp/create_flashcard.html', form)

def flashcard_list(request):
    folders = Folder.objects.all()
    flashcards = Flashcard.objects.filter(folder=None) # フォルダに属さないカード
    return render(request, 'teamapp/flashcard_list.html', {'folders': folders, 'flashcards': flashcards})

# def flashcard_list(request):
#     Flashcards = {
#         "flashcards": Flashcard.objects.all()
#     }
#     return render(request, 'teamapp/flashcard_list.html', Flashcards)

def flashcard_quiz(request, index_id):
    list = Flashcard.objects.values_list("id", flat=True)
    if index_id >= len(list):
        return redirect('index')
    context = {
        "flashcard": Flashcard.objects.get(pk=list[index_id]),
        "next": 1 + index_id
    }
    return render(request, 'teamapp/flashcard_quiz.html', context)

def update(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
    except Flashcard.DoesNotExist:
        raise Http404("Flashcard does not exist")
    if request.method == 'POST':
        flashcard.front = request.POST['front']
        flashcard.back = request.POST['back']
        flashcard.memo = request.POST['memo']
        flashcard.save()
        return redirect(detail, flashcard_id)
    context = {
        'flashcard': flashcard
    }
    return render(request, "teamapp/edit.html", context)

def detail(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
    except Flashcard.DoesNotExist:
        raise Http404("Flashcard does not exist")
    context = {
        'flashcard': flashcard
    }
    return render(request, "teamapp/detail.html", context)

def delete(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
    except Flashcard.DoesNotExist:
        raise Http404("Flashcard does not exist")
    flashcard.delete()
    return redirect(index)

def folder_cards(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    flashcards = folder.flashcards.all()
    return render(request, 'teamapp/folder_cards.html', {'folder': folder, 'flashcards': flashcards})

def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('flashcard_list')
    else:
        form = FolderForm()
    return render(request, 'teamapp/create_folder.html', {'form': form})
