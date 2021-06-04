from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    return render(request, 'index.html')
def index2(request):
    obj=Item.objects.all()
    
    return render(request, 'index2.html',{"video":obj})
