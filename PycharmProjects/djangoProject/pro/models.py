from django.db import models

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=500, verbose_name="Название", help_text="Название документа")
    text = models.TextField(verbose_name="Текст")
