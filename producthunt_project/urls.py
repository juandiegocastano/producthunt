from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls'), name='profiles'),
    path('', include('products.urls'), name='products'),
    # path('', views.home, name='home')
]
