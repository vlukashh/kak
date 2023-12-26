from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

class IndexList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/index.html'

    def get_queryset(self):
        return Product.objects.all()[:5]

class ServiceList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/service_list.html'

    def get_queryset(self):
        return Product.objects.all()

def service(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product_id = id
            instance.save()
    else:
        form = AppForm(initial={'user': request.user.pk, 'product': id})

    return render(request, "main/service.html", {'product': product, 'form': form})

def profile(request):
    order = App.objects.filter(user=request.user)

    context = {
        "orders": order,
    }

    return render(request, 'main/profile.html', context)

class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('index')

class Logout(LogoutView):
    template_name = 'main/logout.html'
    success_url = reverse_lazy('index')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
