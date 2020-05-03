from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from . import models
from django.utils import timezone

# Create your views here.

def home(request):
    products = models.Product.objects
    return render(request, 'products/home.html', {"products": products } )

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
            #print(redirect('detail/' + str(product.id)))
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'faltan campos'})  
            
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

def upvote(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    product.votes_total +=1
    product.save()
    return render(request, 'products/detail.html', {'product': product})