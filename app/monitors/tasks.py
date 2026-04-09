from celery import shared_task
from .models import Endpoint
from .services import MonitorService


@shared_task
def check_api_task(api_id):
    """
    Background task to ping a specific monitor.
    """
    try:
        endpoint = Endpoint.objects.get(id=api_id)
        service = MonitorService(endpoint)
        service.run_check()
        return f"Successfully checked {endpoint.name}"
    except Endpoint.DoesNotExist:
        return f"Endpoint with id {api_id} no longer exists."


@shared_task
def check_all_apis_task():
    """
    Background task to ping all endpoints.
    """
    active_endpoints = Endpoint.objects.filter(is_active=True)
    for endpoint in active_endpoints:
        check_api_task.delay(endpoint.id)

    return f"Scheduled checks for {active_endpoints.count()} endpoints."
