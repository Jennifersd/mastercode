from django.shortcuts import render, get_object_or_404

from .models import TutorialSeries

def tutorial_series_detail(request, slug):
    object = get_object_or_404(TutorialSeries, slug=slug)
    template = "tutorials/tutorialseries_detail.html"
    context = {
        'object': object,
    }
    return render(request, template, context)
    
    