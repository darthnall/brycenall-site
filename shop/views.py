from django.shortcuts import render

def shop_all(request):
    context = { "title": "Shop All" }
    return render(request, "shop/home.html", context=context)
