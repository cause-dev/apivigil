from typing import TYPE_CHECKING, Any

from django.contrib import messages
from django.forms import BaseForm
from django.http import HttpResponse
from django.views.generic.base import ContextMixin

if TYPE_CHECKING:
    from django_htmx.http import HttpRequest


class HtmxMixin:
    if TYPE_CHECKING:
        request: HttpRequest

        def get_success_url(self) -> str: ...

    def get_htmx_redirect_response(self, url: str) -> HttpResponse:
        response = HttpResponse()
        response["HX-Redirect"] = url
        return response

    def htmx_redirect_or_response(self, normal_response: HttpResponse) -> HttpResponse:
        if getattr(self.request, "htmx", False):
            return self.get_htmx_redirect_response(self.get_success_url())
        else:
            return normal_response


class HtmxFormMixin(HtmxMixin):
    """Handles HTMX redirects and error responses for form views."""

    error_message = "Please correct the errors below."
    success_message = ""

    def form_valid(self, form: BaseForm) -> HttpResponse:
        response = super().form_valid(form)  # ty: ignore[missing-attribute]
        if self.success_message:
            messages.success(self.request, self.success_message)
        return self.htmx_redirect_or_response(response)

    def form_invalid(self, form: BaseForm) -> HttpResponse:
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)  # ty: ignore[missing-attribute]


class AuthContextMixin(ContextMixin):
    """Provides common context variables for auth views."""

    url_name: str
    btn_label: str
    is_register: bool

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "url_name": self.url_name,
                "btn_label": self.btn_label,
                "is_register": self.is_register,
            }
        )
        return context
