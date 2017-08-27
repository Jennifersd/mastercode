from django.shortcuts import render

#View home Page
def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)