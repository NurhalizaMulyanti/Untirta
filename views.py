from django.shortcuts import render

# Create your views here.
def index(request):
    judul = "Fakultas Kedokteran"

    konteks = {
        'judul': judul
    }
    return render(request, 'index.html', konteks)