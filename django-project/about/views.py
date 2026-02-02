from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kelas Terbuka',
        'subjudul' : 'Selamat Datang',
        'banner' : 'about/img/banner_about.png',
        'app_css' : 'about/css/style.css'
    }

    return render(request, 'about/index.html', context)
