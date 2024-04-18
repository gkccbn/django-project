from django.urls import path
from . import views  #nokta bulunduğum dizini işaret eder
#bulunduğum dizinden viewsdeki dosyaşara ulaşmak için import ettik

urlpatterns = [
    path('',views.kurslar),
    path('list',views.kurslar),
    path('details',views.details),
    path('programlama',views.programlama),
    path('mobil',views.mobil),
    path('<category>', views.getCoursesByCategory) #kategori bilgisine göre dinamik olarak kurs bilgilerini ekliyoruz

]
#courseapp -> ana proje klasoru
#courses  -> uygulama dosyası
#pages  -> uygulama dosyası