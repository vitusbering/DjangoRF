from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Men(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name