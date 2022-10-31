from django.shortcuts import render
from basic_app.models import Budget
from air_conditioners.models import AirConditioner
from categories.models import Categories,SubCategories
from django.db.models import F
from categories.forms import CategoriesForm,SubCategoriesForm
from brands.forms import AcBrandsForm
from brands.models import AcBrands
from django.core.exceptions import SuspiciousOperation
from air_conditioners.models import AirConditioner
from air_conditioners.forms import AirConditionerForm
from air_conditioners.views import AcSearch
from itertools import chain
# Create your views here.


def AdminBudgetView(request):
    detail_view = 'False'
    search_budget_view_istrue = 'False'
    budget = Budget.objects.all().order_by('-pk')
    searched_date = ''
    searched_useremail = ''
    searched_status = 'Todos'
    ac_sugestions = ''

    if request.method == 'POST':
        detail_view = request.POST['detail_view_istrue']
        search_budget_view = request.POST['search_budget_view_istrue']

        if search_budget_view == 'True':
            searched_date = request.POST['sc_date']
            searched_status = request.POST['sc_status']
            searched_useremail = request.POST['sc_useremail']

            if searched_date != '':
                budget = budget.filter(created_at__lte=searched_date).order_by('pk')
            if searched_status != 'Todos':
                budget = budget.filter(status__contains=searched_status)
            if searched_useremail != '':
                save_budget = budget
                budget = budget.filter(user__username__contains=searched_useremail)
                save_budget = save_budget.filter(email__contains=searched_useremail)
                budget = list(chain(save_budget,budget))
                budget = set(budget)


        if detail_view == 'True':
            clicked_budget = request.POST['clicked_budget']
            potency_search = request.POST['potency']
            budget = Budget.objects.filter(pk__contains=clicked_budget)
            ac_sugestions = AirConditioner.objects.filter(btu__gte=potency_search)


    return render(request,'admin_view/admin_budget_view.html',{'budget':budget,'detail_view':detail_view,
                                                               'potency_search':ac_sugestions,'searched_useremail':searched_useremail,
                                                               'searched_date':searched_date,'searched_status':searched_status})



def AdminCategorieView(request):
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    categories_form = CategoriesForm()
    subcategories_form = SubCategoriesForm()
    categorie_istrue = 'False'
    subcategorie_istrue = 'False'
    searched_cat = 'Todas'
    searched_categorie = 'Todas'
    searched_subcategories = SubCategories.objects.all()

    if request.method == 'POST':
        searched_cat = request.POST['searched_cat']
        categorie_istrue = request.POST['categorie_istrue']
        subcategorie_istrue = request.POST['subcategorie_istrue']
        searched_categorie = request.POST['searched_cat']

        if categorie_istrue == 'True':
            form = CategoriesForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()

        if subcategorie_istrue == 'True':
            form = SubCategoriesForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
        if searched_categorie != 'Todas':
            searched_subcategories = SubCategories.objects.filter(Categorie__title__contains=searched_categorie)


    return render(request, 'admin_view/admin_categories_view.html',{'categories':categories,'subcategories':subcategories,
                                                                    'categories_form':categories_form,'subcategories_form':subcategories_form,
                                                                    'searched_subcategories':searched_subcategories,'searched_cat':searched_cat,
                                                                    'searched_categorie':searched_categorie})


def AdminBrandView(request):
    acbrands_form = AcBrandsForm()
    brand_istrue = 'False'
    delete_brand_istrue = 'False'

    if request.method == 'POST':
        brand_istrue = request.POST.get('brand_istrue', 'False')
        delete_brand_istrue = request.POST.get('delete_brand_istrue', 'False')

        if delete_brand_istrue == 'True':
            brand_pk = request.POST['brand_pk']
            instance = AcBrands.objects.get(pk=brand_pk)
            instance.delete()


        if brand_istrue == 'True':
            form = AcBrandsForm(request.POST, request.FILES)
            if form.is_valid():
                brand = form.save(commit=False)
                brand.save()
                return render(request, 'admin_view/admin_brands_view.html',{'acbrands_form':acbrands_form,})
            else:
                raise SuspiciousOperation("can't create")


    return render(request, 'admin_view/admin_brands_view.html',{'acbrands_form':acbrands_form,})



def AdminProductsView(request):
    product_form = AirConditionerForm()
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    # products = AirConditioner.objects.all()
    product_istrue = 'False'
    delete_object_istrue = 'False'
    search_istrue = 'True'
    error_message = 'False'
    searched_ac = ''
    searched_brand = 'Todos'
    searched_categorie = 'Todos'
    searched_subcategorie = ''
    searched_potency = ''
    airconditioner = AirConditioner.objects.all()
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
        delete_object_istrue = request.POST['delete_object_istrue']
        searched_ac = request.POST['searched_ac']
        searched_brand = request.POST['ac_brand']
        searched_categorie = request.POST['sc_categorie']
        searched_subcategorie = request.POST['sc_subcategorie']
        searched_potency = request.POST['sc_potency']
        product_istrue = request.POST['product_istrue']
        saved_page_number = request.POST.get('saved_page_number', '0')
        go_next_istrue = request.POST.get('go_next_istrue', 'False')
        go_back_istrue = request.POST.get('go_back_istrue', 'False')
        go_to_page_istrue = request.POST.get('go_to_page_istrue', 'False')


        if delete_object_istrue == 'True':
            object_pk = request.POST['object_pk']
            isinstance = AirConditioner.objects.get(pk=object_pk)
            isinstance.delete()

        if product_istrue == 'True':
            form = AirConditionerForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                # return render(request, 'admin_view/admin_products_view.html',{'product_form':product_form,'error_message':error_message,'products':products,})
            else:
                error_message = 'True'
                # return render(request, 'admin_view/admin_products_view.html',{'product_form':product_form,'error_message':error_message,'products':products,})

        if search_istrue == 'True':
                if searched_brand != 'Todos':
                    airconditioner = AirConditioner.objects.filter(brand__title__contains=searched_brand)
                else:
                    airconditioner = AirConditioner.objects.all()

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
            saved_page_numbers = go_to_page_int
            page_started = go_to_page_int * 15
            page_ended = (go_to_page_int+1) * 15


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
    'admin_view/admin_products_view.html',
    {'searched_ac':searched_ac,'airconditioner':airconditioner[page_started:page_ended],'searched_brand':searched_brand,
    'searched_categorie':searched_categorie,'searched_subcategorie':searched_subcategorie,
    'searched_potency':searched_potency,'categories':categories,'subcategories':subcategories,
    'product_form':product_form,'error_message':error_message,'error_message':error_message,
    'page_start':page_started,'page_end':page_ended,'saved_page_number':saved_page_numbers,
    'hide_go_back':hide_go_back,'pages':pages})


    # 'airconditioner':products,
