from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Product


class ProductList(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = ['name','price']
    success_url = reverse_lazy('product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name','price']
    success_url = reverse_lazy('product_list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
