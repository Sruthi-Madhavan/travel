from django.http import HttpResponse
from django.shortcuts import render
from.models import place
# Create your views here.
def demo(request):
    obj = place.objects.all()
    return render(request,"index.html",{'result':obj})
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #a=x-y
    #b=x*y
    #c=x/y
    #return render(request,"result.html",{'result':res,'sub':a,'mult':b,'div':c})
#def sample(request):
    #return HttpResponse("hello world")
