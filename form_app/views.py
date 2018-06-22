from django.shortcuts import render
from .forms import MyFirstForm

# Create your views here.


def index(request):
    return render(request, 'form_app/index.html')



def form_view(request):
    form = MyFirstForm()    #I made an object/instance to my Form class here
    return render(request, 'form_app/form_app.html', context={'form':form})
