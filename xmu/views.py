from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import HttpResponse

def login(request):
    papers = Paper.objects.all()
    directions = ResearchDirection.objects.all()
    galleryimages = GalleryImage.objects.order_by('-weight')[:3]  # 取 weight 最大的 3 张图
    resultimages = ResultImage.objects.order_by('-weight')[:4]
    conf = BackgroundImage.objects.order_by('-weight').first()
    return render(request, 'login.html', {'papers': papers, 'directions': directions, 'galleryimages': galleryimages, 'resultimages': resultimages, 'conf': conf})

from django.shortcuts import render, redirect
from .models import ContactMessage, Paper, ResearchDirection, GalleryImage, ResultImage, Member, BackgroundImage


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

def members(request):
    # 按照 position 排序，导师 (Professor) 排在前，成员 (Member) 排在后
    # 然后根据 weight 排序，权重大的排在前
    members = Member.objects.all().order_by('-position', '-weight')
    return render(request, 'members.html', {'members': members})
