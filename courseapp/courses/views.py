from django.http import HttpResponse
from django.shortcuts import render

#creating views


# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurs listesi')
