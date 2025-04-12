from django.contrib import admin
from .models import ContactMessage, Paper, ResearchDirection, GalleryImage, ResultImage, Member

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Paper)
admin.site.register(ResearchDirection)
admin.site.register(GalleryImage)
admin.site.register(ResultImage)
admin.site.register(Member)