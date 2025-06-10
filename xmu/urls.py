from django.urls import path
from . import views

urlpatterns = [
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('members/', views.members, name='members'),
    path("", views.login, name="login"),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]

