
from django.contrib import admin
from django.urls import path, include

#alt uygulamaların urllerini tanımlıyoruz

urlpatterns = [
    path('', include('pages.urls')),
    path('kurslar/', include('courses.urls')),
    path('admin/', admin.site.urls),   #tüm alt endpointleri /client endpoint altına toplamış oluruz
]
