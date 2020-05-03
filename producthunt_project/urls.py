from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls'), name='profiles'),
    path('products/', include('products.urls'), name='products'),
    # path('', views.home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
