from django.urls import path
from . import views  #nokta bulunduğum dizini işaret eder
#bulunduğum dizinden viewsdeki dosyaşara ulaşmak için import ettik

urlpatterns = [
    path('',views.index),
    path('list',views.kurslar),
    path('<kurs_adi>',views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategory, name ='courses_by_category'),
      #kategori bilgisine göre dinamik olarak kurs bilgilerini ekliyoruz

]
#courseapp -> ana proje klasoru
#courses  -> uygulama dosyası
#pages  -> uygulama dosyası