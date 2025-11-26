# stunning-dollop

A **collaborative learning platform** aimed at developers and software enthusiasts who want to exchange skills in a free and personalized way. Unlike traditional course platforms or one-directional mentorship systems, the project focuses on reciprocity: each user can **teach what they know and learn what they need**, within an intelligent matching dynamic based on the supply and demand of technical skills.

The system manages the full interaction cycle between users —from OAuth2 authentication to matchmaking, real-time messaging, and post-session feedback— integrating asynchronous notification mechanisms and a data model optimized for skill-to-skill relationships.

The solution aims to foster communities of practice that narrow the gap between self-taught learners and professionals, offering a smooth and secure experience powered by a robust backend.

Built with a modular architecture on a modern stack (**FastAPI, PostgreSQL, Redis, Celery, WebSockets**), Stunning Dollop showcases a real application of professional software design focused on scalability, asynchronicity, and peer-to-peer collaboration.

## Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/doc/)[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)[![REST API](https://img.shields.io/badge/REST_API-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://restfulapi.net/)[![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=for-the-badge&logo=websocket&logoColor=white)](https://developer.mozilla.org/docs/Web/API/WebSockets_API)[![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)[![SQLModel](https://img.shields.io/badge/SQLModel-1C3C3C?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlmodel.tiangolo.com/)[![Alembic](https://img.shields.io/badge/Alembic-3D3D3D?style=for-the-badge&logo=alembic&logoColor=white)](https://alembic.sqlalchemy.org/)[![PyJWT](https://img.shields.io/badge/PyJWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://pyjwt.readthedocs.io/)[![OAuth2 Google](https://img.shields.io/badge/OAuth2_Google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://developers.google.com/identity/protocols/oauth2)[![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/)[![Pub/Sub](https://img.shields.io/badge/Pub%2FSub-000000?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://cloud.google.com/pubsub/docs)[![Ruff](https://img.shields.io/badge/Ruff-000000?style=for-the-badge&logo=ruff&logoColor=white)](https://docs.astral.sh/ruff/)[![mypy](https://img.shields.io/badge/mypy-233564?style=for-the-badge&logo=mypy&logoColor=white)](https://mypy.readthedocs.io/)[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/)[![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=for-the-badge&logo=traefikmesh&logoColor=white)](https://doc.traefik.io/)[![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/docs/)[![Logs](https://img.shields.io/badge/Logs-000000?style=for-the-badge&logo=logstash&logoColor=white)](https://www.elastic.co/guide/en/logstash/current/index.html)[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)](https://prometheus.io/docs/)[![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/docs/)[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://docs.github.com/actions)[![CI/CD](https://img.shields.io/badge/CI%2FCD-000000?style=for-the-badge&logo=github&logoColor=white)](https://about.gitlab.com/topics/ci-cd/)[![PyTest](https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)[![Locust](https://img.shields.io/badge/Locust-000000?style=for-the-badge&logo=locust&logoColor=white)](https://docs.locust.io/)[![ELK Stack](https://img.shields.io/badge/ELK-Stack-5A5A5A?style=for-the-badge&logo=elkstack&logoColor=white)](https://stackshare.io/)[![Monolith](https://img.shields.io/badge/Monolith-6C63FF?style=for-the-badge)](https://en.wikipedia.org/wiki/Monolithic_application)[![Event-Driven](https://img.shields.io/badge/Event-Driven-E91E63?style=for-the-badge)](https://en.wikipedia.org/wiki/Event-driven_architecture)[![Clean Architecture](https://img.shields.io/badge/Clean_Architecture-00A86B?style=for-the-badge)](https://en.wikipedia.org/wiki/Clean_architecture)[![Hexagonal](https://img.shields.io/badge/Hexagonal-FFB300?style=for-the-badge)](https://en.wikipedia.org/wiki/Hexagonal_architecture)

---

## Quickstart

### Clone the repository

```bash
git clone https://github.com/JohannGaviria/stunning-dollop
cd stunning-dollop
```

### Copy environment variables

Copy `.env.example` to `.env` and edit as needed, or set the variables directly in your environment. See the table below for required variables.

```bash
cp .env.example .env
```

| Category    | Key                      | Description                                                       | Example                                                                                                                                                   |
|-------------|--------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application | `APP_NAME`               | Name of the application                                           | `Stunning Dollop`                                                                                                                                         |
|             | `APP_SUMMARY`            | Brief description of the application's purpose                    | `Skill Exchange Platform for Programmers`                                                                                                                 |
|             | `APP_DESCRIPTION`        | Detailed description of the application                           | `A web platform that allows users to offer and learn programming skills through an interest-based matching system and a real-time communication channel.` |
|             | `APP_VERSION`            | Current version of the application                                | `0.1.0`                                                                                                                                                   |
| Backend     | `DEBUG`                  | Enable/disable debug mode (use `TRUE`/`FALSE`)                    | `TRUE`                                                                                                                                                    |
|             | `BACKEND_PORT`           | Port where the backend server runs                                | `8000`                                                                                                                                                    |
|             | `BACKEND_HOST`           | Host address for the backend server                               | `miapu.com`                                                                                                                                               |
|             | `BACKEND_WORKERS`        | Number of worker processes for handling requests                  | `4`                                                                                                                                                       |
|             | `ACME_EMAIL`             | Email for Let's Encrypt SSL certificate notifications             | `email@miapi.com`                                                                                                                                         |
|             | `TRAEFIK_AUTH`           | Basic authentication for Traefik dashboard (user:hashed_password) | `your_secure_password_here`                                                                                                                               |
|             | `ENVIRONMENT`            | Current environment (development/production)                      | `development`                                                                                                                                             |
| Database    | `DB_PORT`                | Port where the PostgreSQL service runs                            | `5432`                                                                                                                                                    |
|             | `POSTGRES_USER`          | PostgreSQL database user                                          | `postgres`                                                                                                                                                |
|             | `POSTGRES_DB`            | PostgreSQL database name                                          | `stunning_dollop_db`                                                                                                                                      |
|             | `POSTGRES_PASSWORD`      | Password for the PostgreSQL database user                         | `your_secure_password_here`                                                                                                                               |
| Redis       | `REDIS_PORT`             | Port where Redis server runs                                      | `6379`                                                                                                                                                    |
|             | `REDIS_PASSWORD`         | Password for Redis authentication                                 | `your_secure_password_here`                                                                                                                               |
|             | `REDIS_HOST`             | Redis server host                                                 | `redis`                                                                                                                                                   |
|             | `REDIS_DB`               | Redis database number                                             | `0`                                                                                                                                                       |
| CORS        | `CORS_ALLOW_ORIGINS`     | Comma-separated list of allowed origins for cross-origin requests | `http://localhost,http://example.com`                                                                                                                     |
|             | `CORS_ALLOW_CREDENTIALS` | Allow credentials like cookies and authorization headers          | `True`                                                                                                                                                    |
|             | `CORS_ALLOW_METHODS`     | Comma-separated list of allowed HTTP methods                      | `GET,POST,PUT,DELETE`                                                                                                                                     |
|             | `CORS_ALLOW_HEADERS`     | Comma-separated list of allowed HTTP headers                      | `Authorization,Content-Type`                                                                                                                              |


### Run in a Docker environment

#### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

Claro, aquí tienes una versión más clara y profesional, con un poco más de contexto y estilo consistente:

---

#### Running the Service with Docker

You can start the backend and database easily using Docker Compose:

```bash
# Start services in development mode with environment variables from .env
docker compose --env-file .env -f docker/docker-compose.dev.yml up --build
```

Alternatively, if you prefer using the Makefile:

```bash
# Start all services defined in the Makefile
make up
```

Once the services are running, the API will be accessible at:

[http://localhost:8000/docs](http://localhost:8000/docs) – this provides the **interactive Swagger UI** for testing all endpoints.

---

## Features

* **Hexagonal Architecture** – Business logic isolated from infrastructure, enabling cleaner code evolution and long-term maintainability
* **Clean dependency flow** – Domain-driven modules, adapters, and ports aligned with extensibility goals
* **FastAPI** – Async-first framework with automatic docs and native WebSockets support
* **Real-time messaging** – Live sessions and chat powered by WebSockets and Redis pub/sub
* **Skill-based matchmaking** – Intelligent pairing system based on user abilities and learning interests
* **OAuth2 with Google** – Modern authentication flow with secure token exchange
* **JWT Authentication** – Short-lived access with refresh support for session persistence
* **SQLModel + PostgreSQL** – Type-safe models, relational integrity, and clean query patterns
* **Alembic** – Versioned migrations for predictable database evolution
* **Redis** – Cache, rate-limiting, pub/sub channels, and async task coordination
* **Celery Workers** – Background tasks for email notifications, delayed actions, and session reminders
* **Structured Logging** – Application-wide logs with context propagation and standard formats
* **Monitoring-ready** – Prometheus metrics exposure and Grafana dashboard compatibility
* **Full Docker Environment** – Reproducible development and deployable stack with Traefik-ready routing
* **Pytest Suite** – Unit, integration, and end-to-end testing boilerplate
* **Type Checking & Linting** – mypy, Ruff, and strict code-quality enforcement

---

## Further Reading

* **Architecture**
  * [Hexagonal Architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture)
  * [Clean Architecture](https://en.wikipedia.org/wiki/Clean_architecture)

* **Backend & APIs**
  * [FastAPI Documentation](https://fastapi.tiangolo.com/)
  * [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
  * [Alembic Documentation](https://alembic.sqlalchemy.org/)
  * [Pydantic Documentation](https://docs.pydantic.dev/)

* **Authentication & Security**
  * [Google OAuth2](https://developers.google.com/identity/protocols/oauth2)
  * [PyJWT Documentation](https://pyjwt.readthedocs.io/)

* **Async & Distributed Systems**
  * [Celery Documentation](https://docs.celeryq.dev/)
  * [Redis Pub/Sub](https://redis.io/docs/latest/develop/interact/pubsub/)
  * [WebSockets API](https://developer.mozilla.org/docs/Web/API/WebSockets_API)

* **DevOps & Observability**
  * [Docker Documentation](https://docs.docker.com/)
  * [Prometheus Documentation](https://prometheus.io/docs/)
  * [Grafana Documentation](https://grafana.com/docs/)
  * [Traefik Documentation](https://doc.traefik.io/)

* **Testing & Quality**
  * [Pytest Documentation](https://docs.pytest.org/)
  * [mypy Documentation](https://mypy.readthedocs.io/)
  * [Ruff Documentation](https://docs.astral.sh/ruff/)

## License

Distributed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

> Made with ❤️ by [JohannGaviria](https://github.com/JohannGaviria) – always happy to connect for feedback, collaboration, or job opportunities.
