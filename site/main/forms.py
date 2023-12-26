from django import forms
from .models import Product, AdvUser, App


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ("username", "password", "photo")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image")

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = "__all__"
        widgets = {'user': forms.HiddenInput, 'product': forms.HiddenInput}