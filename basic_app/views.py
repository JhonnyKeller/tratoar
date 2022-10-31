from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy,reverse
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.loader import render_to_string
from . import models
from air_conditioners.models import AirConditioner
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import BudgetForm, contactForm
from django.core.mail import send_mail


User = get_user_model()

@login_required
def UserBudgetView(request):
    detail_view = 'False'
    search_budget_view_istrue = 'False'
    searched_date = ''
    searched_useremail = ''
    searched_status = 'Todos'
    ac_sugestions = ''


    if request.method == 'POST':
        detail_view = request.POST.get('detail_view_istrue', 'False')
        search_budget_view = request.POST['search_budget_view_istrue']
        user_pk = request.POST.get('user_pk', '0')
        user_pk_pk = request.user.pk
        print(user_pk_pk)


        if search_budget_view == 'True' and int(user_pk) == int(user_pk_pk):
            budget = models.Budget.objects.filter(user__pk__contains=user_pk).order_by('-pk')
            searched_date = request.POST.get('sc_date', '')
            searched_status = request.POST.get('sc_status', 'Todos')
            searched_useremail = request.POST.get('sc_useremail', '')


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


        if detail_view == 'True' and int(user_pk) == int(user_pk_pk):
            clicked_budget = request.POST['clicked_budget']
            potency_search = request.POST['potency']
            budget = models.Budget.objects.filter(pk__contains=clicked_budget)
            ac_sugestions = AirConditioner.objects.filter(btu__gte=potency_search)


    return render(request,'basic_app/user_budget_view.html',{'budget':budget,'detail_view':detail_view,
                                                               'potency_search':ac_sugestions,'searched_useremail':searched_useremail,
                                                               'searched_date':searched_date,'searched_status':searched_status})


class index(TemplateView):
    template_name = 'index.html'


class about(TemplateView):
    template_name = 'about.html'

def contactSend(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            get_name = request.POST.get('name','no')
            phone_number = request.POST.get('phone_number','no')
            get_subject = request.POST.get('subject','no')
            get_message = request.POST.get('message','no')
            get_email = request.POST.get('Email','no')

            reply_to_owner = ('Nome de cliente: ' + get_name +
                               '. \n Email: ' + get_email +
                               '. \n Telemovel: ' + phone_number +
                               '. \n Mensagem: ' + get_message + '.')

            send_mail(get_subject,
                      reply_to_owner,
                      'jhonnykellerdev@gmail.com',
                      [get_email],
                      fail_silently=False)

    return render(request, 'thankYouForContactingPage.html', {'email':get_email})


def budgetCreateView(request):
    budget = models.Budget.objects.all()
    form = BudgetForm()
    sended = 'False'
    get_email = 'no'

    if request.method == "POST":
        form = BudgetForm(request.POST,request.FILES)
        get_email = request.POST.get('email','null')
        get_name = request.POST.get('name','null')
        get_phone = request.POST.get('phone_number', 'null')
        get_message = request.POST.get('budget_text','no text')
        get_zip_code = request.POST.get('zip_code','no text')
        get_adress = request.POST.get('address','null')
        get_instalation = request.POST.get('Instalation','null')
        get_message = request.POST.get('budget_text','null')
        get_division_1 = request.POST.get('Division_1','null')
        get_division_2 = request.POST.get('Division_2','/n')
        get_division_3 = request.POST.get('Division_3','/n')
        get_division_4 = request.POST.get('Division_4','/n')
        get_division_5 = request.POST.get('Division_5','/n')
        get_division_6 = request.POST.get('Division_6','/n')
        get_area_1 = request.POST.get('Area_1','null')
        get_area_2 = request.POST.get('Area_2','/n')
        get_area_3 = request.POST.get('Area_3','/n')
        get_area_4 = request.POST.get('Area_4','/n')
        get_area_5 = request.POST.get('Area_5','/n')
        get_area_6 = request.POST.get('Area_6','/n')

        reply_to_owner = ('Nome de cliente: ' + get_name +
                           '. \n Email: ' + get_email +
                           '. \n Telemovel: ' + get_phone +
                           '. \n Codigo Postal: ' + get_zip_code +
                           '. \n Morada: ' + get_adress +
                           '. \n Tipo de Instalação: ' + get_instalation +
                           '. \n Descrição pelo cliente: ' + get_message +
                           '. \n Divisão 1: ' + get_division_1 + ' ' + 'Area: ' + get_area_1 +
                           '. \n Divisão 1: ' + get_division_2 + ' ' + 'Area: ' + get_area_2 +
                           '. \n Divisão 1: ' + get_division_3 + ' ' + 'Area: ' + get_area_3 +
                           '. \n Divisão 1: ' + get_division_4 + ' ' + 'Area: ' + get_area_4 +
                           '. \n Divisão 1: ' + get_division_5 + ' ' + 'Area: ' + get_area_5 +
                           '. \n Divisão 1: ' + get_division_6 + ' ' + 'Area: ' + get_area_6 + '.')
        reply = ("Agradecemos o seu contacto  Sr\\h." + get_name + ". \n \n Vamos analisar o seu pedido e entraremos em contacto consigo o mais breve possível."
                 "\n \n Com os melhores cumprimentos, Tratoar.")
        title = "Orçamento, " + get_instalation + " com a Tratoar."
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            send_mail(title,
            reply,
            'jhonnykellerdev@gmail.com',
            [get_email],
            fail_silently=False)
            send_mail(get_email,
            reply_to_owner,
            'jhonnykellerdev@gmail.com',
            ['jhonnykellerdev@gmail.com'],
            fail_silently=False)
            sended = 'True'

    return render(request, 'basic_app/budget_form.html', {'budget':budget,'form':form,'sended':sended,'get_email':get_email})

class BudgetDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Budget

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class UserBudgets(LoginRequiredMixin,generic.ListView):
    model = models.Budget
    template_name = "basic_app/user_budget_list.html"


    def get_queryset(self):
        try:
            self.budget_user = User.objects.prefetch_related("user_budget").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.budget_user.user_budget.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["budget_user"] = self.budget_user
        return context



class BudgetUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = models.Budget
    redirect_field_name = 'basic_app/budget_detail.html'



class DeleteBudget(LoginRequiredMixin,generic.DeleteView):
    model = models.Budget

    # success_url = ("/basic_app/user_budget_list.html")
    # redirect_field_name = 'basic_app/user_budget_list.html'
    # ("basic_app:budgetview", kwargs={'username':'mayu'})("home")
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Budget Deleted")

        return super().delete(*args, **kwargs)

#__________________budget_views_End_______________________
