from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.



# Function Base View Show a Template
'''
def indexView(request):
    name = "ali"
    context = {"name":name}
    return render(request,"index.html",context)
'''

class IndexView(TemplateView):
    template_name = 'index.html'
    '''
    a class based view to show index page 
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


