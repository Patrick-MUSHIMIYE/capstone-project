from django.shortcuts import render, redirect, HttpResponse,  get_object_or_404
from .forms import UploadImageForm
from lostfound_app.models import upload_image
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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
    return HttpResponse('No document was uploaded')
   

def board_images(request):
    image_list = upload_image.objects.all()
    return render(request, 'board.html', {'image_list': image_list})

def search_document(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        results = upload_image.objects.filter(
            Q(first_name__icontains=search_query) | Q(second_name__icontains=search_query)
        )

        context = {'results': results, 'search_query': search_query}
        return render(request, 'board.html', context)

    # Handle GET requests or other cases
    return render(request, 'board.html')

@login_required
def image_details(request, id):
    image = get_object_or_404(upload_image, pk=id)
    return render(request, 'claim.html', {'image': image})
    