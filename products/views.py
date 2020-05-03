from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'products/home.html' )

@login_required
def create(request):
    if request.method == 'POST':

        #Checks that no field is missing
        if request.POST['title'] and request.POST['body'] and \
            request.POST['url'] and request.FILES['image'] and \
            request.FILES['icon']:

            #Instantiate Product()
            product = models.Product()

            product.title = request.POST['title']
            product.pub_date = timezone.now()
            product.body = request.POST['body']

            #Checks if starts with http or https for url field
            if request.POST['url'].startswith('http://') or \
               request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+request.POST['url']

            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.hunter = request.user

            #Save
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.html', {'error': 'faltan campos'})  
            
    else:
        return render(request, 'products/create.html')
            
