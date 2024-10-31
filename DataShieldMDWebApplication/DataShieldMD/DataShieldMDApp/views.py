from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def how_we_do_it(request):
    return render(request, 'how_we_do_it.html')