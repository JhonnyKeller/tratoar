from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from . import models
from categories.models import Categories,SubCategories
from django.shortcuts import get_object_or_404




# Create your views here.



def AcSearch(request):
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    go_next_istrue = 'False'
    go_back_istrue = 'False'
    saved_page_numbers = 0
    page_started = 0
    page_ended = 15
    hide_go_back = 'True'
    count_pages = 0
    count_objects = 0
    pages = ['0']


    if request.method == 'POST':
        searched_ac = request.POST['searched_ac']
        searched_brand = request.POST['ac_brand']
        searched_categorie = request.POST['sc_categorie']
        searched_subcategorie = request.POST['sc_subcategorie']
        searched_potency = request.POST['sc_potency']
        saved_page_number = request.POST.get('saved_page_number', '0')
        go_next_istrue = request.POST.get('go_next_istrue', 'False')
        go_back_istrue = request.POST.get('go_back_istrue', 'False')
        go_to_page_istrue = request.POST.get('go_to_page_istrue', 'False')


        if searched_brand != 'Todos':
            airconditioner = models.AirConditioner.objects.filter(brand__title__contains=searched_brand)
        else:
            airconditioner = models.AirConditioner.objects.all()

        if searched_categorie != 'Todos':
            airconditioner = airconditioner.filter(categorie__title__contains=searched_categorie)
            subcategories = SubCategories.objects.filter(Categorie__title__contains=searched_categorie)

        if searched_subcategorie != '':
            airconditioner = airconditioner.filter(sub_categorie__title__contains=searched_subcategorie)

        if searched_potency != '':
            airconditioner = airconditioner.filter(btu__gte=searched_potency)

        if searched_ac != '':
            airconditioner = airconditioner.filter(title__contains=searched_ac)

        if go_next_istrue == 'True':
            page_start = request.POST.get('page_start', '0')
            page_end = request.POST.get('page_end', '15')
            saved_page_numbers = int(saved_page_number) + 1
            page_started = int(page_start)
            page_ended = int(page_end)
            page_started +=15;
            page_ended +=15;

        if go_back_istrue == 'True':
            page_start = request.POST.get('page_start', '0')
            page_end = request.POST.get('page_end', '15')
            saved_page_numbers = int(saved_page_number) - 1
            page_started = int(page_start)
            page_ended = int(page_end)
            page_started -=15;
            page_ended -=15;

        if go_to_page_istrue == 'True':
            go_to_page = request.POST.get('go_to_page', '0')
            go_to_page_int = int(go_to_page)
            print(go_to_page)
            saved_page_numbers = go_to_page_int
            page_started = go_to_page_int * 15
            page_ended = (go_to_page_int+1) * 15
            print(page_ended)
            print(page_started)


        if saved_page_numbers == 0:
            hide_go_back = 'True'
        else:
            hide_go_back = 'False'

        for x in airconditioner:
            count_objects += 1

        count_pages = count_objects / 15

        for x in range(int(count_pages)):
            pages.append(x+1)



    return render(request,
    'air_conditioners/ac_search.html',
    {'searched_ac':searched_ac,'airconditioner':airconditioner[page_started:page_ended],'searched_brand':searched_brand,
    'searched_categorie':searched_categorie,'searched_subcategorie':searched_subcategorie,
    'searched_potency':searched_potency,'categories':categories,'subcategories':subcategories,
    'page_start':page_started,'page_end':page_ended,'saved_page_number':saved_page_numbers,
    'hide_go_back':hide_go_back,'pages':pages})



class AcCreateView(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields = ('brand','title','categorie','sub_categorie','energy_efficiency','btu','description','ac_img')
    model = models.AirConditioner
    template_name = 'air_conditioners/ac_createview.html'
    redirect_field_name = 'air_conditioners/ac_createview.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)



def AcDetailView(request):

    if request.method == 'POST':
        product_pk = request.POST['product_pk']
        product = models.AirConditioner.objects.get(pk=product_pk)

    return render(request,'air_conditioners/ac_detailview.html',{'product':product})




class AcUpdateView(LoginRequiredMixin,UpdateView):
    model = models.AirConditioner
    fields = ('__all__')
    template_name = 'air_conditioners/ac_createview.html'
    redirect_field_name = 'air_conditioners/ac_detailview.html'



class AcListView(LoginRequiredMixin, generic.ListView):
    model = models.AirConditioner
    template_name = 'air_conditioners/ac_listview.html'



class AcDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = models.AirConditioner
    template_name = 'air_conditioners/ac_deleteview.html'

    # success_url = ("/basic_app/user_budget_list.html")
    # redirect_field_name = 'basic_app/user_budget_list.html'
    # ("basic_app:budgetview", kwargs={'username':'mayu'})("home")
    success_url = reverse_lazy('air_conditioners:ac_listview')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Ac Deleted")

        return super().delete(*args, **kwargs)
