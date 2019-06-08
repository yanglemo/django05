from django.shortcuts import render
from django.http import HttpResponse
from books.models import BookInfo
from django.views.generic import View
from datetime import datetime

# Create your views here.
def index(request):
    books=BookInfo.objects.all()
    for book in books:
        print(book)
    context ={
        'books':books
    }
    reslut=10/10

    return render(request,'index.html',context)
    return HttpResponse('----------------')
class HomeView(View):
    def get(self,request):
        username=request.GET.get('username')
        context ={
            'username':username,
            'age':14,
            'birthday':datetime.now(),
            'firends':['tom','jack','rose'],
            'moeny':{
                '2019':12000,
                '2020':18000,
                '2021':25000,
            },
            'desc':'<script>alert("hot")</script>'
        }

        return render(request,'home.html',context)
def detail(request):
    return render(request,'detail.html')
