from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
 img = ""
 if request.method=="POST":
  form=ImageForm(request.POST,request.FILES)
  if form.is_valid():
   form.save()
   img=Image.objects.all()
 form= ImageForm()
 return render(request, 'myapp/index.html', {'img': img, 'form': form})
