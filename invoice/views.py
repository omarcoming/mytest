import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView
from django.utils.encoding import force_str
from django.http.response import JsonResponse
from django.urls import reverse_lazy, reverse

from formset.views import EditCollectionView, FormCollectionView, FormView, FileUploadMixin, FormViewMixin

from .forms import *
from .models import *


class EditView(UpdateView, FormViewMixin):
    def get_object(self, queryset=None):
        if self.extra_context['add'] is False:
            return super().get_object(queryset)

    def form_valid(self, form):
        if extra_data := self.get_extra_data():
            if extra_data.get('delete') is True:
                self.object.delete()
                success_url = self.get_success_url()
                response_data = {'success_url': force_str(success_url)} if success_url else {}
                return JsonResponse(response_data)
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'invoice/product-list.html'

class ProductEditView(EditView):
    model = Product
    template_name = 'invoice/product-add.html'
    form_class = ProductForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('product-edit', kwargs={'pk': pk})
        else:
            return reverse('product-list')
