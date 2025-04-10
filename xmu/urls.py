from django.urls import path
from . import views

urlpatterns = [
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path("", views.login)
]
