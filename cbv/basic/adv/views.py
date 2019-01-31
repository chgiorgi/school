from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
								  CreateView, UpdateView, DeleteView)

from . import models


# Create your views here.


class IndexView(TemplateView):
	template_name = 'index.html'


class SchoolListView(ListView):
	context_object_name = 'schools'
	model = models.School


class SchoolDetailView(DetailView):
	model = models.School
	context_object_name = 'school_detail'


class SchoolCreateView(CreateView):
	model = models.School
	fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
	model = models.School
	fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy('adv:list')

# def index(request):
# 	return render(request,'index.html')
