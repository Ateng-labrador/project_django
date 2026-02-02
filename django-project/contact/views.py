from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Selamat Datang',
        'subjudul' : 'Kontak',
    }
    return render(request, 'contact/index.html', context)
