from django.shortcuts import render
from .models import Savol

def savollar_view(request):
    savollar = None
    parcha = ""

    if request.method == "POST":
        parcha = request.POST.get("parcha", "").strip()

        if parcha:
            savollar = Savol.objects.filter(savol__icontains=parcha)

    context = {
        "savollar": savollar,
        "parcha": parcha
    }

    return render(request, "index.html", context)
