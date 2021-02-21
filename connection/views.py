# Create your views here.
from connection.forms import ContactForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from connection.models import City, Country, Name  # noqa: I100

from .tasks import send_mail_task


def index(request):
    num_names = Name.objects.count()
    num_country = Country.objects.count()
    num_city = City.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={
            'num_names': num_names,
            'num_visits': num_visits,
            'num_country': num_country,
            'num_city': num_city,
        },
    )


def success(request):
    return HttpResponse("SUCCESS!!!")


class NameCreate(LoginRequiredMixin, CreateView):
    model = Name
    fields = ['name']
    success_url = '/connection/name/create'
    login_url = '/admin/login/'
    redirect_field_name = 'admin'

    def form_valid(self, form):
        Name.objects.create(**form.cleaned_data)
        return redirect(self.success_url)


class NameUpdate(LoginRequiredMixin, UpdateView):
    model = Name
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = '/connection/success/'
    login_url = '/admin/login/'
    redirect_field_name = 'admin'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class NameDelete(LoginRequiredMixin, DeleteView):
    model = Name
    success_url = '/connection/success/'
    login_url = '/admin/login/'
    redirect_field_name = 'admin'

    def form_valid(self, form):
        form.delete()
        return redirect(self.success_url)


class NameDetailView(DetailView):

    model = Name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class NameListView(ListView):

    model = Name
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CountryCityList(ListView):
    model = City
    template_name = 'connection/country_list.html'
    paginate_by = 100

    def get_queryset(self):
        return super(CountryCityList, self).get_queryset().select_related('country')  # noqa:E501


def contact_form(request):
    data = dict()
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            send_mail_task.delay(subject, message, from_email)
            return redirect('connection:index')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name='includes/contact.html',
        context=context,
        request=request
    )
    return JsonResponse(data)
