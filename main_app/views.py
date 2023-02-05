from django.shortcuts import render

from .models import Appointment, Article


def home(request):
    articles = Article.objects.all()
    context = {
        "title": "Z&S Clinic",
        "articles": articles,
    }
    return render(request, "main_app/home.html", context)


def about(request):
    context = {"title": "Z&S Clinic"}

    return render(request, "main_app/about.html", context)
