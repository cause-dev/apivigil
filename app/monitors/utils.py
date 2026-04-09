from .models import Endpoint


def get_endpoint_stats(user):
    """Utility to calculate stats for a specific user."""
    qs = Endpoint.objects.filter(user=user)
    return {
        "total_count": qs.count(),
        "online_count": qs.filter(is_online=True, is_active=True).count(),
        "offline_count": qs.filter(is_online=False, is_active=True).count(),
    }
