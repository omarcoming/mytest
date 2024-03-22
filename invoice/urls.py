from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('product', ProductEditView.as_view(extra_context={'add': True}), name='product-add'),
    path('product/<int:pk>/', ProductEditView.as_view(extra_context={'add': False}), name='product-edit'),
    path('product/list/', ProductListView.as_view(extra_context={'add': False}), name='product-list'),
    ]
