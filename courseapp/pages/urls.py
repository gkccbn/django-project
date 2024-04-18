from django.urls import path
from . import views


urlpatterns = [
    path('', views.home), #route
    path('anasayfa',views.home),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda),

]
