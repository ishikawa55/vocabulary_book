from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.flashcard_list, name='flashcard_list'),
    path('create/', views.create_flashcard, name='create_flashcard'),
    path('<int:flashcard_id>', views.detail, name='detail'),
    path('<int:flashcard_id>/delete', views.delete, name='delete'),
    path('<int:flashcard_id>/update', views.update, name='update'),
    path('quiz/<int:index_id>', views.flashcard_quiz, name='flashcard_quiz'),
    path('create-folder/', views.create_folder, name='create_folder'),
    path('folder/<int:folder_id>/', views.folder_cards, name='folder_cards'),
]