from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request=request, template_name="baseapp/base.html")


def adminPanel(request):
    return render(request=request, template_name="baseapp/admin-panel.html")
