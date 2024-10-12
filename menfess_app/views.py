from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "menfess_app/index.html")

def create(request):
    return render(request, "menfess_app/create_menfess.html")

def reply(request):
    return render(request, "menfess_app/reply.html")