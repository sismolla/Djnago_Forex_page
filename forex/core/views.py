from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView
from .models import Forex
from django.db.models import F


class Home(ListView):
    template_name = 'home.html'
    model = Forex
    paginate_by = 4    

    def get_queryset(self):
        Query = self.request.GET.get('q')       
        file_t = self.request.GET.get('type')
        star = self.request.GET.get('stars')
        price = self.request.GET.get('price')
    
        if Query:
            return Forex.objects.filter(title__icontains=Query)       
        if file_t:
            return Forex.objects.filter(file_type__icontains=file_t)
        if star:
            if star.lower() == '3':
                return Forex.objects.filter(stars__icontains=3)
            elif star.lower() == '4':
                return Forex.objects.filter(stars__icontains=4)
            elif star.lower() == '5':
                return Forex.objects.filter(stars__icontains = 5)
        if price:
            if price.lower() == 'low':
                return Forex.objects.filter(price__lt=100)
            elif price.lower() == 'mid':
                return Forex.objects.filter(price__gte=300)
            elif price.lower() == 'high':
                return Forex.objects.filter(price__gte=500)
        return Forex.objects.all()
    
# class RelatedView(ListView):
#     template_name = 'related.html'
#     model = Forex
#     queryset = Forex.objects.filter(file_type__icontains='book')
    
    
    
class DetailView(DetailView):
    model = Forex
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = Forex.objects.filter(slug = self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        return context
    
    def get_object(self):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Forex,slug=slug_)





