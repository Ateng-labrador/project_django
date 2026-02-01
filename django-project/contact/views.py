from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kelas Terbuka | Kontak',
        'subjudul' : 'Kontak',
    }
    return render(request, 'contact/index.html', context)
