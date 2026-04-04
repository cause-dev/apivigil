from celery import shared_task
from .models import Monitor
from .services import MonitorService


@shared_task
def check_api_task(api_id):
    """
    Background task to ping a specific monitor.
    """
    try:
        monitor = Monitor.objects.get(id=api_id)
        service = MonitorService(monitor)
        service.run_check()
        return f"Successfully checked {monitor.name}"
    except Monitor.DoesNotExist:
        return f"Monitor with id {api_id} no longer exists."
