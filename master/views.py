from django.shortcuts import render

from tutorials.models import TutorialSeries

#View home Page
def home(request):
    # series = TutorialSeries.objects.all() Show all   y [:2] indica la cantidad de item a mostrar
    series = TutorialSeries.objects.filter(archived=False).order_by('-id')[:3]
    template = 'home.html'
    context = {'series': series}
    return render(request, template, context)