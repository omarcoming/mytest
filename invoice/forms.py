from datetime import datetime

from django.forms import fields, ModelForm, fields, forms, widgets
from django import forms
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.forms.models import construct_instance, model_to_dict
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

from formset.collection import FormCollection
from formset.renderers.bootstrap import FormRenderer
from formset.fieldset import Fieldset, FieldsetMixin
from formset.utils import FormMixin
from formset.widgets import Selectize
from .models import *




class ProductForm(ModelForm):
    # id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={
            'unit': 'm-1 col-1',
            'prod_name': 'm-1 col-3',
            '*': 'm-1 col-2',
        }
    )

    class Meta:
        model = Product
        fields = [
            'unit',
            'prod_name',
            'material',
            'vendor',
            # 'id',
        ]
        widgets = {
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'unit',
            }),
            'prod_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'prod_name',
            }),
            'material': forms.Select(attrs={
                'class': 'form-control',
                'id': 'material',
            }),
            'vendor': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'vendor',

            }),
        }
