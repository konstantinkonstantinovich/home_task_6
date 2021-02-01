# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from connection.models import City, Country, Name  # noqa: I100


def index(request):
    return HttpResponse("Hello, world. You're at the connection index.")


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for country in Country.objects.annotate():
            result = country.city
        context['city'] = result
        return context
