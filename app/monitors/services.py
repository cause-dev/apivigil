import requests
from django.utils import timezone
from .models import EndpointLog


class MonitorService:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.expected_code = endpoint.expected_status_code
        self.url = endpoint.url
        self.timeout = 10
        self.headers = {
            "User-Agent": "ApiVigil/1.0 (https://apivigil.com)",
        }
        # Variables
        self.is_online = False
        self.status_code = None
        self.response_time = None
        self.error_message = None

    def run_check(self):
        """
        The main entry point. Pings the site, creates a log, and updates the model.
        """
        try:
            response = self._perform_request("HEAD")
            if response.status_code in [404, 405]:
                response = self._perform_request("GET")

            self.status_code = response.status_code
            self.response_time = response.elapsed.total_seconds()
            self.is_online = self.status_code == self.expected_code

        except Exception as e:
            self.is_online = False
            self.error_message = str(e)[:1000]

        self._create_log_entry()

        return self._update_endpoint_model()

    def _perform_request(self, method):
        """Internal helper to execute the HTTP call."""
        if method == "HEAD":
            return requests.head(
                self.url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True,
            )
        return requests.get(
            self.url, headers=self.headers, timeout=self.timeout, stream=True
        )

    def _update_endpoint_model(self):
        """Updates the Django model instance with the check results."""
        self.endpoint.is_online = self.is_online
        self.endpoint.last_checked = timezone.now()
        self.endpoint.save()
        return self.endpoint

    def _create_log_entry(self):
        """Saves a snapshot of this check to the EndpointLog table."""
        EndpointLog.objects.create(
            endpoint=self.endpoint,
            status_code=self.status_code,
            latency=self.response_time,
            is_online=self.is_online,
            error_message=self.error_message,
        )
