from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password

from speedrun_app.models import CustomUser
from speedrun_app.forms import CustomUserLoginForm, CustomUserRegisterForm, CustomUserForm, CustomUserUpdateForm


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'speedrun_app/user/custom_user_list.html'
    context_object_name = 'users'

class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'speedrun_app/user/custom_user_detail.html'
    context_object_name = 'user'

class CustomUserRegisterView(CreateView):
    template_name = 'speedrun_app/user/custom_user_register.html'
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class CustomUserLoginView(FormView):
    template_name = 'speedrun_app/user/custom_user_login.html'
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Neplatné přihlašovací údaje')
            return self.form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('user_login')