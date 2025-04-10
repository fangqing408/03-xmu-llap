from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import HttpResponse

def login(request):
    papers = Paper.objects.all()
    return render(request, 'login.html', {'papers': papers})

from django.shortcuts import render, redirect
from .models import ContactMessage, Paper


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        referer = request.META.get('HTTP_REFERER', '/')
        return render(request, 'contact_success.html', {'referer': referer})  # 提交后跳转
    return redirect('/')
def contact_success(request):
    return render(request, 'contact_success.html')  # 自己创建这个模板
