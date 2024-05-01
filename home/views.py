from django.shortcuts import render


def home(request):
    context = {"title": "Home"}
    return render(request, "home/home.html", context=context)


def about(request):
    context = {"title": "About"}
    return render(request, "home/about.html", context=context)


def contact(request):
    context = {"title": "Contact"}
    return render(request, "home/contact.html", context=context)


def gallery(request):
    context = {"title": "Gallery"}
    return render(request, "home/gallery.html", context=context)

def detail(request, video_id):
    context = { "title": video.title }
    return render(request, "home/detail.html", context=context)
