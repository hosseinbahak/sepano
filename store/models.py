from django.db import models
from django.contrib.auth.models import User
import os


CATEGORY_CHOICES = ((0, 'تعریف نشده'), (1, 'خوراکی'), (2, 'الکترونیکی'), (3, 'پوشاک'), (4, 'آرایشی و بهداشتی'))


def user_directory_path_img(instance, filename):    
    return os.path.join(
        "products/" , filename)

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=64)
    category = models.IntegerField(choices = CATEGORY_CHOICES, null=True, blank=True, default=0)
    description = models.TextField(max_length=256, null=True, blank=True)
    count = models.IntegerField(default=0)
    image = models.ImageField(
        'product image',
        upload_to = user_directory_path_img,
        null=True, 
        blank=True,
    )
    
    def __str__(self):
        return str(self.id)

    def counter(self):
        self.count = self.count + 1
        self.save()
        return self.count

