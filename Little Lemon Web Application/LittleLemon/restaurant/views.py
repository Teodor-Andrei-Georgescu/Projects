from django.shortcuts import render

def index(reuqest):
    return render(reuqest,'index.html', {})
