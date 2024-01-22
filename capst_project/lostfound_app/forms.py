from django import forms
from .models import upload_image

class UploadImageForm(forms.ModelForm):
    first_name = forms.CharField(max_length=254, required=True)
    second_name = forms.CharField(max_length=254, required=True)
    name = forms.CharField(max_length=254, required=True)
    location = forms.CharField(max_length=254, required=True)
    tel = forms.IntegerField(required=True)
    upload_images = forms.ImageField(max_length=254, required=True)
    
    class Meta:
        model = upload_image
        fields = ['first_name', 'second_name', 'name', 'location', 'tel', 'upload_images', 'created_at']
        
    def clean_tel(self):
        tel = self.cleaned_data['tel']
        if not tel.isdigit():
            raise forms.ValidationError("Please enter a valid integer for the tel field.")
        return tel