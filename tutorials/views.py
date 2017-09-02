from django.shortcuts import render, get_object_or_404
#from django.views.generic import DetailView   no es necesario
#from django.views.generic import ListView
from django.db.models import Count
from .models import TutorialSeries, Lesson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

#class TutorialSeriesListView(ListView):
#    model = TutorialSeries

def tutorial_series_list(request):
    tutorials = TutorialSeries.objects.all().prefetch_related(
        'tutorials'
    ).annotate(
        lesson=Count('tutorials')
    )               # Con esto podemos ver e numero de lecciones que tiene un tutorial 
    
    paginator = Paginator(tutorials, 2)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
        
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index 
    page_range = paginator.page_range[start_index:end_index]
    
    template = "tutorials/tutorialseries_list.html"
    context = {
        'tutorials': tutorials,
        'items': items,
        'page_range': page_range,
    }
    return render(request, template, context)
    

def tutorial_series_detail(request, slug):
    series = get_object_or_404(TutorialSeries, slug=slug)
    lessons = series.tutorials.filter(tutorial_series=series)
    
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



