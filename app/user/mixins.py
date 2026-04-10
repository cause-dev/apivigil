from django.http import HttpResponse
from django.forms import Form
from django.contrib import messages


class HtmxMixin:
    def get_htmx_redirect_response(self, url: str) -> HttpResponse:
        response = HttpResponse()
        response["HX-Redirect"] = url
        return response

    def htmx_redirect_or_response(self, normal_response: HttpResponse) -> HttpResponse:
        if self.request.htmx:
            return self.get_htmx_redirect_response(self.get_success_url())
        else:
            return normal_response


class HtmxFormMixin(HtmxMixin):
    """Handles HTMX redirects and error responses for form views."""

    error_message = "Please correct the errors below."
    success_message = ""

    def form_valid(self, form: Form) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return self.htmx_redirect_or_response(response)

    def form_invalid(self, form: Form) -> HttpResponse:
        response = super().form_invalid(form)
        messages.error(self.request, self.error_message)
        if self.request.htmx:
            return self.render_to_response(self.get_context_data(form=form))
        return response


class AuthContextMixin:
    """Provides common context variables for auth views."""

    def get_context_data(self, **kwargs: str):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "url_name": self.url_name,
                "btn_label": self.btn_label,
                "is_register": self.is_register,
            }
        )
        return context
