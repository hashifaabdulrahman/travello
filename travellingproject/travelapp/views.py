from django.http import HttpResponse
from django.shortcuts import render
from  .models import Places
from  .models import Team
# Create your views here.

def index(request):
    obj=Places.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'leader':obj1})


# Create your views here.
