from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kelas Terbuka | Blog',
        'subjudul' : 'Selamat datang',
        'banner' : 'blog/img/banner_blog.png',
        'logo' : 'blog/img/logo.png',
        'app_css' : 'blog/css/style.css',
    }
    return render(request, 'blog/index.html', context)
