from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import *


class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()

        # применение фильтров
        min_price = self.request.GET.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        max_price = self.request.GET.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        available = self.request.GET.get('available')
        if available:
            queryset = queryset.filter(stock_quantity__gt=0)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        application_area = self.request.GET.get('application_area')
        if application_area:
            queryset = queryset.filter(application_area=application_area)

        rating = self.request.GET.get('rating')
        if rating:
            queryset = queryset.filter(rating__gte=rating)

        # поиск по названию товара
        search_query = self.request.GET.get('search_query')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'
    context_object_name = 'product'
