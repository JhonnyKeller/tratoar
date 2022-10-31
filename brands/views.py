from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from . import models



# Create your views here.
class BrandCreateView(LoginRequiredMixin,CreateView):
    # form_class = forms.PostForm
    fields = ('title','brand_url','brand_img')
    model = models.AcBrands
    template_name = 'brands/brand_createview.html'
    success_url = reverse_lazy('home')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)



class BrandDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AcBrands
    template_name = "brands/brand_detailview.html"


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = models.AcBrands
    template_name = "brands/brand_listview.html"



class BrandUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = models.AcBrands
    fields = ('__all__')
    template_name = 'brands/brand_updateview.html'
    redirect_field_name = 'brands/brand_detailview.html'



class BrandDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = models.AcBrands

    # success_url = ("/basic_app/user_budget_list.html")
    # redirect_field_name = 'basic_app/user_budget_list.html'
    # ("basic_app:budgetview", kwargs={'username':'mayu'})("home")
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Brand Deleted")

        return super().delete(*args, **kwargs)
