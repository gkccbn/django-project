from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
#creating views

# Create your views here.

data = {
    "programlama": "progmalama kategorisine ait kurslar",
    "web":"web kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

def index(request):
    return render(request,'courses/index.html')

def kurslar(request):
    list_items =""
    category_list = list(data.keys())
    

    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} kurs detay sayfası')

def getCoursesByCategory(request,category_name):
    try:
        category_text = data[category_name];
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")
#altta direkt response yapılıyor
#def getCoursesByCategoryId(request, category_id):
#    return HttpResponse(category_id) 

#altta ise redirect yapıp sayfaya yönlendiriyor. inspect network inceleyebilirsin
#def getCoursesByCategoryId(request, category_id):
#   return HttpResponseRedirect('/kurs/kategori/programlama')

#path('kategori/<str:category_name>', ->>> url  kısmında yazılan bu path kategoriye göre yönlendirmesidr 
#biz reverse ile dinamk olarak gerçekleştirdik. yani path ismi coursesapp altında url de değişse bile elle heryerde değiştirmemize gerek yok
def getCoursesByCategoryId(request, category_id):
   category_list = list(data.keys())

   if(category_id > len(category_list)):
       return HttpResponseNotFound("yanlış kategori seçimi")
   category_name =category_list[category_id-1]
   redirect_url = reverse('courses_by_category', args=[category_name])
   return redirect(redirect_url)
#dinamik url oluşturuyoruz reverse ile return kısmında
#return redirect('/kurs/kategori' + category_name) şeklinde de yazabilirdik ama dinamik olmaz kurs ismi değişirse burdada değiştirmemiz lazım


 

 