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

from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=200)          # 论文名称
    authors = models.CharField(max_length=300)        # 作者
    link = models.URLField(max_length=500)            # 链接
    published_date = models.DateTimeField(null=True)   # 允许为 NULL

    def __str__(self):
        return self.title



class ResearchDirection(models.Model):
    direction_name = models.TextField()  # 使用 TextField 代替 CharField，移除最大长度限制

    def __str__(self):
        return self.direction_name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')  # 图片字段，存储上传的图片
    weight = models.IntegerField()  # 权重字段，用来决定图片的展示优先级
    created_at = models.DateTimeField(auto_now_add=True)  # 自动记录添加时间
    description = models.TextField(blank=True, null=True)  # 图片介绍，允许为空
    def __str__(self):
        return f"Gallery Image {self.id} - Weight: {self.weight}"



class ResultImage(models.Model):
    image = models.ImageField(upload_to='result_images/')  # 图片字段，存储上传的图片
    weight = models.IntegerField()  # 权重字段，用来决定图片的展示优先级
    created_at = models.DateTimeField(auto_now_add=True)  # 自动记录添加时间
    description = models.TextField(blank=True, null=True)  # 图片介绍，允许为空
    def __str__(self):
        return f"Gallery Image {self.id} - Weight: {self.weight}"

from django.db import models

from django.db import models


class Member(models.Model):
    POSITION_CHOICES = [
        ('Professor', 'Professor'),
        ('Member', 'Member'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='Member')  # 设置默认值为学生
    degree = models.CharField(max_length=100, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatar.jpg')
    weight = models.IntegerField(default=0)  # 新增字段，用于权重排序

    def __str__(self):
        return self.name


from django.db import models


class BackgroundImage(models.Model):
    avatar = models.ImageField(upload_to='bg/', blank=True, null=True, default='logo.jpg')
    weight = models.IntegerField(default=0)  # 新增字段，用于权重排序
    quote = models.TextField(blank=True, null=True, default='If I have seen further it is by standing on the shoulders of giants.')
    author = models.CharField(blank=True, null=True, max_length=100, default='Isaac Newton')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Quote by {self.author}"

import os
from django.db import models

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    return f'files/{ext}/{filename}'  # 存储路径：media/pdf/example.pdf

class UploadedFile(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # ✅ 显示文件名而不是 "UploadedFile object (2)"

    def filename(self):
        return os.path.basename(self.file.name)

    def file_ext(self):
        return os.path.splitext(self.file.name)[1][1:].lower()


