from django.contrib import admin

# Register your models here.
from .models import upload_image

admin.site.site_title = "lost and found document"
admin.site.site_header = "Lost_Found"
admin.site.register(upload_image)