from django.shortcuts import render, redirect, HttpResponse
from .forms import UploadImageForm
from lostfound_app.models import upload_image


def home(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')



def upload_image_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        name = request.POST.get('name')
        location = request.POST.get('location')
        tel = request.POST.get('tel')
        image_upload = request.FILES.get('upload_images')
        
        upload_image.objects.create(
            first_name=first_name,
            second_name=second_name,
            name=name,
            location=location,
            tel=tel,
            upload_images=image_upload
        )
        image_list = upload_image.objects.all()
        return render(request, 'board.html', {'image_list': image_list})
        # return HttpResponse('Document successfully uploaded')
    return HttpResponse('No document was uploaded')
    # else:
    #     form = UploadImageForm()
    # return render(request, 'post.html', {'form': form})

def board_images(request):
    image_list = upload_image.objects.all()
    return render(request, 'board.html', {'image_list': image_list})