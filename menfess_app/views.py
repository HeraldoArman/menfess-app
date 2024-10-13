from django.shortcuts import render, redirect
from menfess_app import forms
# Create your views here.
def index(request):
    return render(request, "menfess_app/index.html")

def create(request):
    form = forms.CreateMenfess()
    if request.method == 'POST':
        form = forms.CreateMenfess(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('index')
    
    return render(request, "menfess_app/create_menfess.html", context={'form': form})

def reply(request):
    return render(request, "menfess_app/reply.html")