M_DIR = "monitors"
U_DIR = "user"


class MONITORS:
    DASHBOARD = "monitors/dashboard.html"
    DETAILS = "monitors/endpoint.html"
    LOGS = "monitors/logs.html"

    class PARTIALS:
        STATS = "partials/dashboard/stats.html"
        HTMX_RESPONSE = "partials/dashboard/htmx-response.html"
        ROW = f"{M_DIR}/partials/monitor_row.html"
        LIST = f"{M_DIR}/partials/monitor_list.html"
        CONTENT = f"{M_DIR}/partials/dashboard_content.html"
        HEADER = "partials/dashboard/header.html"
        POLL = "partials/dashboard/poll.html"

        class ENDPOINTS:
            LIST = "partials/endpoints/list.html"
            ROW = "partials/endpoints/endpoint.html"
            FORM = "partials/endpoints/form.html"
            MODAL = "partials/endpoints/modal.html"


class USERS:
    LOGIN = f"{U_DIR}/login.html"
    PROFILE = f"{U_DIR}/profile.html"


class LAYOUT:
    BASE = "base.html"
    HTMX_BASE = "partials/htmx_base.html"

    class PARTIALS:
        BREADCRUMBS = "partials/breadcrumbs.html"
        MESSAGES = "partials/messages.html"


class T:
    MONITORS = MONITORS
    USERS = USERS
    LAYOUT = LAYOUT
