from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


# Create your views here.