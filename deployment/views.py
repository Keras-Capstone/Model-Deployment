from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        mean_radius = request.POST.get('mean_radius')
        mean_texture = request.POST.get('mean_texture')
        mean_perimeter = request.POST.get('mean_perimeter')
        mean_area = request.POST.get('mean_area')
        pass
    return render(request, 'index.html')