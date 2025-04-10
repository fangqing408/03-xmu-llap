from django.db import models

# Create your models here.

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Paper(models.Model):
    title = models.CharField(max_length=200)          # 论文名称
    authors = models.CharField(max_length=300)        # 作者
    link = models.URLField(max_length=500)            # 链接

    def __str__(self):
        return self.title


