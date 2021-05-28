from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import validate_slug, validate_email
from .models import Image
class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}  

def email(self):
        email=self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        print (user_count)
        if user_count > 0:
          raise forms.validationError("tttttttttt")
        return email    
