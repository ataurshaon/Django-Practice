from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls'))

    # path('index/', views.home, name='index'),    
    # path('home/', views.home, name='index'), # same index but url name is difference for index function views
    # path('', views.home, name='index'), # for default url
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about')
]
