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
    
    
#class TutorialSeriesDetailView(DetailView):
#    model = TutorialSeries
    
#    def get_context_data(self, **kwargs):
#        context = super(TutorialSeriesDetailView, self).get_context_data(**kwargs)
#        context['lessons'] = Lesson.objects.filter(tutorial_series=self.object)
#        return context
    
#class LessonDetailView(DetailView):
#    model = Lesson
     
#    def get_object(self, tutorial_series, slug):
#        tutorial_series = TutorialSeries.objects.filter(slug=tutorial_series).first()
#        object = get_object_or_404(Lesson, tutorial_series=tutorial_series, slug=slug)
#        return object
    
#    def get(self, request, tutorial_series, slug):
#        self.object = self.get_object(tutorial_series, slug)
#        context = self.get_context_data(object=self.object)
#        return self.render_to_response(context)

 

def tutorial_series_detail(request, slug):
    series = get_object_or_404(TutorialSeries, slug=slug)
    lessons = series.lesson_set.filter(tutorial_series=series)
    
    template = "tutorials/tutorialseries_detail.html"
    
    context = {
        'series': series,
        'lessons': lessons,
    }
    return render(request, template, context)


def lesson_detail(request, tutorial_series, slug):
    item = get_object_or_404(Lesson.objects.filter(tutorial_series__slug=tutorial_series, slug=slug))
    template = "tutorials/lesson_detail.html"
    context = {
        'item': item,
    }
    
    return render(request, template, context)
