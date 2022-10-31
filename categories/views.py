from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from . import models



# Create your views here.

# ________________Categories__________________________
class CatCreateView(LoginRequiredMixin,CreateView):
    fields = ('title',)
    model = models.Categories
    template_name = 'categories/cat_createview.html'
    success_url = reverse_lazy('categories:cat_listview')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)



class CatDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Categories
    template_name = "categories/cat_detailview.html"


class CatListView(LoginRequiredMixin, generic.ListView):
    model = models.Categories
    template_name = "categories/cat_listview.html"



class CatUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = models.Categories
    fields = ('__all__')
    template_name = 'categories/cat_updateview.html'
    redirect_field_name = 'categories/cat_detailview.html'



class CatDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = models.Categories
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Categorie Deleted")

        return super().delete(*args, **kwargs)



# _________________SubCategories____________________
class SubCreateView(LoginRequiredMixin,CreateView):
    fields = ('title','Categorie',)
    model = models.Categories
    template_name = 'categories/sub_createview.html'
    success_url = reverse_lazy('categories:cat_listview')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)



class SubDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Categories
    template_name = "categories/sub_detailview.html"


class SubListView(LoginRequiredMixin, generic.ListView):
    model = models.Categories
    template_name = "categories/sub_listview.html"



class SubUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = models.Categories
    fields = ('__all__')
    template_name = 'categories/sub_updateview.html'
    redirect_field_name = 'categories/sub_detailview.html'



class SubDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = models.Categories
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "sub categorie Deleted")

        return super().delete(*args, **kwargs)
