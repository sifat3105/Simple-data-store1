from django.shortcuts import render, redirect
from .models import Human
from django.db.models import Q
import os

# Create your views here.
def home_func(request):
    if request.method == 'POST':
        message = 'Enter Name and Age'
        print(message)
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES.get('image')
        if Human.objects.filter(name=name).exists():
            message = 'data already exist'
        else:
            Human.objects.create(name=name, age=age, image=image)
            # data.save()
            message = 'data added'
          
    search_query = request.GET.get('search')
    if search_query:
        all_data = Human.objects.filter(name__icontains = search_query)
        message = 'Search result...'       
    else:
        all_data = Human.objects.all()
    return render(request,'home.html', locals())

def delete_data(request,id):
    data = Human.objects.get(id=id)
    image_path = data.image.path
    data.delete()
    os.remove(image_path)
    return redirect('/')

def update_data(request,id):
    data = Human.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES.get('image')
        if Human.objects.filter(Q(name=name) & Q(age=age)).exists():
            message = 'data already exist'
        else:

            data.name = name
            data.age = age
            data.image = image
            data.save()
            message = 'data added'
            return redirect('/')
    
    return render(request,'update.html', locals())