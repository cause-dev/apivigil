# 🚀 ApiVigil

**ApiVigil** is a professional-grade API and website monitoring tool designed for speed, reliability, and ease of use. It provides real-time health checks, latency visualization, and detailed event logging through a seamless Single Page Application (SPA) experience.

![Dashboard Preview](https://via.placeholder.com/800x400?text=ApiVigil+Dashboard+Preview) <!-- Optional: Add a screenshot later -->

## ✨ Features

-   **Real-time Monitoring:** Automated background pings via Celery and Redis.
-   **SPA Experience:** Powered by HTMX 2.0 for high-speed navigation without page reloads.
-   **Visual Latency Tracking:** Beautiful line charts powered by Chart.js showing response time trends over 24 hours.
-   **Uptime Analytics:** Detailed uptime percentages and history logs for every endpoint.
-   **Modern UI:** Clean, dark-mode first design using Tailwind CSS 4.0 and DaisyUI 5.0.
-   **Manual Health Checks:** Trigger instant pings directly from the dashboard with live UI updates.

## 🛠 Tech Stack

-   **Backend:** [Django 6.0](https://www.djangoproject.com/) (Python 3.14)
-   **Task Queue:** [Celery](https://docs.celeryq.dev/) with [Redis](https://redis.io/)
-   **Frontend:** [HTMX 2.0](https://htmx.org/), [Tailwind CSS 4.0](https://tailwindcss.com/), [DaisyUI 5.0](https://daisyui.com/)
-   **Database:** [PostgreSQL 18](https://www.postgresql.org/)
-   **Charts:** [Chart.js](https://www.chartjs.org/)
-   **Environment:** [Podman](https://podman.io/) / [Docker Compose](https://docs.docker.com/compose/)

## 🚀 Getting Started

### Prerequisites

-   Podman or Docker installed.
-   `uv` (Python package manager) installed locally (optional, for linting).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/apivigil.git
    cd apivigil
    ```

2.  **Spin up the containers:**
    ```bash
    podman compose up --build
    ```

3.  **Run Migrations:**
    ```bash
    podman exec -it backend uv run python manage.py migrate
    ```

4.  **Create a Superuser:**
    ```bash
    podman exec -it backend uv run python manage.py createsuperuser
    ```

5.  **Access the app:**
    Open [http://localhost:8000](http://localhost:8000) in your browser.

## ⚙️ Configuration

The project uses a **Template Registry** (`config/template_registry.py`) to manage HTML paths centrally. This allows for easy renaming of apps or folders without breaking the views.

Core environment variables (set in `docker-compose.yml`):
-   `DATABASE_URL`: PostgreSQL connection string.
-   `CELERY_BROKER_URL`: Redis connection string.