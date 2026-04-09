from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from monitors.utils import get_endpoint_stats
from monitors.models import Endpoint


class DashboardView(LoginRequiredMixin, ListView):
    model = Endpoint
    template_name = "monitors/dashboard.html"
    context_object_name = "endpoints"

    def get_queryset(self):
        # Always filter by current user and newest first
        return Endpoint.objects.filter(user=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Merges our stats helper into the template context
        context.update(get_endpoint_stats(self.request.user))
        context["base_template"] = (
            "partials/content_base.html" if self.request.htmx else "base.html"
        )
        return context


class DashboardPollView(LoginRequiredMixin, TemplateView):
    template_name = "monitors/partials/dashboard_poll.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["endpoints"] = Endpoint.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )
        context.update(get_endpoint_stats(self.request.user))
        return context
