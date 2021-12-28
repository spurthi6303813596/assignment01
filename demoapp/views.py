from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
# Create your views here.
class HomePage(View):
    def get(self,request):
        return render(request,'home.html')
class InsertView(View):
    def post(self,request):
        fno=int(request.POST["t1"])
        sno=int(request.POST["t2"])
        c=fno+sno
        return render(request,'insert.html',{"c_data":c})
