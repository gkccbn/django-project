from django.http import HttpResponse
from django.shortcuts import render

#creating views

# Create your views here.


def kurslar(request):
    return HttpResponse('kurs listesi')

def programlama(request):
    return HttpResponse('programlama kurs listesi')

def mobil(request):
    return HttpResponse('mobil uygulama kurs listesi')

def details(request):
    return HttpResponse('detaylar')
#http://127.0.0.1:8000/kurs/.. bu urlden sonra ne yazarsak üsttekiler dısında
#üsttekilerle eşleşmeyeceği için getCOurses by category return olcak
def getCoursesByCategory(request,category):
    return HttpResponse('kategoriye göre kurs listesi')

 

 