from django.shortcuts import render, redirect, HttpResponse,  get_object_or_404
from .forms import UploadImageForm
from lostfound_app.models import upload_image
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.core.mail import send_mail

# detect images
from .utils import is_nude
from PIL import Image


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
        
        
        # Save the uploaded image temporarily
        with open('temp_image.jpg', 'wb') as f:
            f.write(image_upload.read())

        # Check if the uploaded image is nude
        if is_nude('temp_image.jpg'):
            return HttpResponse('<script>alert("Image contains nudity and cannot be uploaded."); window.history.back();</script>')
        
        upload_image.objects.create(
            first_name=first_name,
            second_name=second_name,
            name=name,
            location=location,
            tel=tel,
            upload_images=image_upload
        )
        # Retrieve all images from the database
        image_list = upload_image.objects.all()
        return render(request, 'board.html', {'image_list': image_list})
    else:
        return HttpResponse('No document was detected! Please upload a different image.')

   
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


def send_password_reset_email(user_email, protocol, domain, uid, token):
    email_template = 'password_reset_email.html'
    context = {
        'email': user_email,
        'protocol': protocol,
        'domain': domain,
        'uid': uid,
        'token': token,
    }
    subject = "Password Request Reset"
    message = render_to_string(email_template, context)
    sender = "techteam@lostfound.com"
    send_mail(subject, message, sender,[user_email], fail_silently=False,)
    
    
@login_required
def delete_image(request, id):
    image = get_object_or_404(upload_image, pk=id)  # Retrieve the image object from the database
    current_user = request.user
    if current_user.first_name in image.name or current_user.last_name in image.name:
        image.delete()
        return HttpResponse('<script>alert("Image deleted successfully."); window.location.href = window.history.back();</script>')
    else:
        return HttpResponse('<script>alert("You are not authorized to delete this image."); window.location.href = window.history.back();</script>')
            
    
@login_required
def update_image(request, id):
    # Retrieve the image object from the database
    image = get_object_or_404(upload_image, pk=id)
    current_user = request.user
    
    if current_user.first_name in image.name or current_user.last_name in image.name:
        if request.method == 'POST':
            form = UploadImageForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                # Check if the uploaded image is nude
                if 'upload_images' in request.FILES:
                    with open('temp_image.jpg', 'wb') as f:
                        f.write(request.FILES['upload_images'].read())
                    if is_nude('temp_image.jpg'):  
                        return HttpResponse('<script>alert("Image contains nudity and cannot be uploaded."); window.history.back();</script>')
                    else:
                        form.save()
                        return redirect('board_images')
        else:
            # If it's not a POST request, instantiate the form with the image data
            form = UploadImageForm(instance=image)
            
        # Render the template with the form
        return render(request, 'update.html', {'form': form, 'image': image})
    else:
        return HttpResponse('<script>alert("You are not authorized to update this image."); window.location.href = window.history.back();</script>')
