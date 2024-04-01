# Docker Networks

Docker networks are a fundamental feature of Docker that enable communication between containers. They provide isolation, security, and efficient communication between Docker containers. Docker networks allow containers to communicate with each other regardless of which host they are running on.

## Without Docker Compose

Without Docker Compose, you typically create Docker networks manually using the `docker network` command. Here's how you might create and use a network without Docker Compose,

1. **Create a Network:** You create a network using the `docker network create` command. For example,

```sh
docker network create my-network
```

2. **Run Containers in the Network:** When you run containers, you specify which network they should be attached to using the `--network` flag. For example:

```sh
docker run --name my-container --network my-network my-image
```

3. **Communicate Between Containers:** Containers within the same network can communicate with each other using their container names or container IP addresses.

## With Docker Compose

Docker Compose simplifies the management of Docker containers, including networking. When you define services in a docker-compose.yml file, Docker Compose automatically creates a network for those services to communicate with each other.

1. **Network Creation:** When you run `docker compose up`, Docker Compose creates a default network for your services. You can also define custom networks in your `docker-compose.yml` file if needed.

2. **Service Communication:** Services defined in the `docker-compose.yml` file can communicate with each other using their service names. Docker Compose sets up DNS resolution so that service names are resolved to the IP addresses of the containers running those services.

3. **Network Isolation:** Each Docker Compose project gets its own isolated network, preventing interference from other Docker containers running on the same host.

By handling networking automatically, Docker Compose simplifies the process of managing Docker containers, especially when you have multiple interconnected services. It abstracts away the complexities of manual network configuration, allowing you to focus on defining your services and their relationships.

Viewing the `docker-compose.yaml` in order to create my backend which includes the interaction of my Django application connecting to a postgres database,

```YAML
services:

  db:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
      - POSTGRES_DB=radix_fitness_postgresql_db

  web:
    build: .
    command: gunicorn backend.wsgi:application --bind 0.0.0.0:8000
    expose:
      - 8000
    env_file:
      - .dev.env
    depends_on:
      - db

  nginx:
    build: ./nginx
    ports:
      - 1337:80
    depends_on:
      - web

volumes:
  postgres_data:
```

Docker compose will create three containers here, but I will be focusing on the communcation between the container `web` and `db`. The `web` container will start up `gunicorn` to pass requests to my Django application. Within my Django application `setting.py` I would have set the appropiate environment variables.

Within `.env` I will have set,

```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=radix_fitness_postgresql_db
SQL_USER=admin
SQL_PASSWORD=admin
SQL_HOST=db
SQL_PORT=5432
```

which would be used from,

```Python
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}
```

The key point here is that `"HOST": os.environ.get("SQL_HOST")` will be pointing to `db`. The `HOST` value should be an IP Address. Docker Compose, service names (like `db`) are automatically mapped to container IP addresses within the Docker network. Docker Compose creates a default network for your services, and each service is accessible by its service name.

Hence, when I specify `"HOST": os.environ.get("SQL_HOST")` as `db`, Docker Compose understands that you're referring to the service named `db` in your `docker-compose.yml` file. Docker Compose sets up DNS resolution so that other services within the same Docker network can reach each other by their service names. DNS will be responsible for translating the service name to the IP address of the container.
