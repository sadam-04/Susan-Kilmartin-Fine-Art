from django.shortcuts import render, get_object_or_404, redirect

def homepage(request):
    return render(request, "templates/homepage.html")