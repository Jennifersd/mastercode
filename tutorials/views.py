from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import TutorialSeries, Lesson

#def tutorial_series_detail(request, slug):
#    object = get_object_or_404(TutorialSeries, slug=slug)
#    template = "tutorials/tutorialseries_detail.html"
#    context = {
#        'object': object,
#    }
#    return render(request, template, context)
    
    
class TutorialSeriesDetailView(DetailView):
    model = TutorialSeries
    
    def get_context_data(self, **kwargs):
        context = super(TutorialSeriesDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(tutorial_series=self.object)
        return context