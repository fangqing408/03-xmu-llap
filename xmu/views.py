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

from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from .models import UploadedFile
from .forms import UploadForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.title = request.FILES['file'].name
            uploaded_file.save()
            return redirect('upload_file')
    else:
        form = UploadForm()

    show_all = request.GET.get("all") == "1"
    if show_all:
        files = UploadedFile.objects.order_by('-uploaded_at')
    else:
        files = UploadedFile.objects.order_by('-uploaded_at')[:10]

    return render(request, 'upload.html', {
        'form': form,
        'files': files,
        'show_all': show_all
    })

def download_file(request, file_id):
    try:
        file = UploadedFile.objects.get(id=file_id)
        return FileResponse(file.file.open(), as_attachment=True, filename=file.filename())
    except UploadedFile.DoesNotExist:
        raise Http404

