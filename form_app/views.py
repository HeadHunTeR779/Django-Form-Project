from django.shortcuts import render
from .forms import MyFirstForm   #this is MY ofrms.py file other one is from django import forms

# Create your views here.

def index(request):
    return render(request, 'form_app/index.html')


#Here MyFirstForm() is the form I made and form is the form object I made here
def form_view(request):
    form = MyFirstForm()    #I made an object/instance to my Form class here

    if request.method=='POST':          #If the guy filled out the form and hit submit
        form = MyFirstForm(request.POST)       #taking in the data

        if form.is_valid():      #if the data conforms with the fields
            print("FORM IS VALID!")
            print("NAME: {}".format(form.cleaned_data["name"]))
            print("EMAIL: {}".format(form.cleaned_data["email"]))
            print("TEXT: {}".format(form.cleaned_data["text"]))


        else:
            print("NOT VALID!")

    return render(request, 'form_app/form_app.html', context={'form':form})
