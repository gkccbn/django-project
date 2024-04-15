from django.urls import path
from django.http import HttpResponse
from . import views  #nokta bulunduğum dizini işaret eder
#bulunduğum dizinden viewsdeki dosyaşara ulaşmak için import ettik

# http://127.0.0.1:8000//client
# http://127.0.0.1:8000/client/home
# http://127.0.0.1:8000/client/kurslar



urlpatterns = [
    path('', views.home), #route
    path('anasayfa',views.home),
    path('kurslar',views.kurslar)
]
