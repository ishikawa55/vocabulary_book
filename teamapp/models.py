from django.db import models
from django.utils import timezone

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True) # フォルダ名
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    front = models.CharField(max_length=255) # 表面のテキスト
    back = models.CharField(max_length=255) # 裏面のテキスト
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    updated_at = models.DateTimeField(auto_now=True) # 更新日時
    memo = models.TextField(blank=True, null=True) # メモのフィールド
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='flashcards', null=True, blank=True) # フォルダとの関連
    
    def __str__(self):
        return f"{self.front} - {self.back} (Folder: {self.folder})"
        # return self.front


