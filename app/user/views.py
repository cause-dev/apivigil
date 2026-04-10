from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)
from django.views.generic import CreateView

from .forms import SignUpForm, LoginForm
from .mixins import HtmxMixin, HtmxFormMixin, AuthContextMixin

# Create your views here.


class RegisterView(AuthContextMixin, HtmxFormMixin, CreateView):
    form_class = SignUpForm
    template_name = "user/register.html"
    success_url = reverse_lazy("login")

    url_name = "register"
    btn_label = "Create Account"
    is_register = True
    error_message = "Please correct the errors below."
    success_message = "Account has been created! You can now log in."


class LoginView(AuthContextMixin, HtmxFormMixin, DjangoLoginView):
    template_name = "user/login.html"
    authentication_form = LoginForm
    success_url = reverse_lazy("dashboard")

    url_name = "login"
    btn_label = "Login"
    is_register = False
    error_message = "Invalid username or password. Please try again."
    success_message = "Welcome back! You have successfully logged in."


class LogoutView(HtmxMixin, DjangoLogoutView):
    next_page = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You have been logged out.")
        if request.htmx:
            return self.get_htmx_redirect_response(self.next_page)
        return response
