<div align="center">
  <h1> Docker Networks </h1>
</div>

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

Docker Compose simplifies the management of Docker containers, including networking. When you define services in a `docker-compose.yml` file, Docker Compose automatically creates a network for those services to communicate with each other.

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

The key point here is that `"HOST": os.environ.get("SQL_HOST")` will be pointing to `db`. The `HOST` value should be an IP Address. Docker Compose, service names (like `db`) **are automatically mapped to container IP addresses within the Docker network**. Docker Compose creates a default network for your services, and each service is accessible by its service name.

Hence, when I specify `"HOST": os.environ.get("SQL_HOST")` as `db`, Docker Compose understands that you're referring to the service named `db` in your `docker-compose.yml` file. Docker Compose sets up DNS resolution so that other services within the same Docker network can reach each other by their service names. DNS will be responsible for translating the service name to the IP address of the container.

# How a Container IP Address is Assigned

Containers in Docker can be thought of as a seperate virtual machines or computers within a network, each container can be assigned an IP address just like physical computers on a traditional network. 

When a container is started, it is assigned an IP address from the subnet of the network it is connected to.

- **Dynamic Subnetting** - Docker dynamically allocates IP addresses from a pool defined by the network's subnet. For example, the default bridge network uses the `172.17.0.0/16` subnet.

- **Multiple Networks** - A container can be connected to multiple networks, and it will receive an IP address for each network it is connected to.

- **User-Defined Networks** - You can create custom networks and specify subnets, gateways, and other options. Containers connected to these networks can communicate using their IP addresses or container names.

Containers on the same network can communicate with each other using their IP addresses or container names. This makes it easy to set up complex applications with multiple interconnected services.

The most common Docker network types are,

- Bridge Network (default)
- Host Network
- Overlay Network
- Macvlan Network
- None Network

When you run a new container in Docker without specifying a network, it is automatically connected to the default `bridge` network. This network is created by Docker when you first install it and it's called `bridge`. They will be assigned IP addresses from the bridge network's IP range (e.g., `172.17.0.2` and `172.17.0.3`). They can communicate with each other using these IP addresses or their container names.

# Network Types

## Bridge Network (default)

The `bridge network` is the default network type in Docker. When you run a container without specifying a network, Docker connects it to a bridge called `bridge` by default.

The bridge network creates a virtual Ethernet bridge on the Docker host. Each container connected to this network is assigned an IP address from the bridge network's IP range. Containers on the same bridge network can communicate with each other using their IP addresses. By default, containers on different networks cannot communicate directly.

Docker uses a private IP address range (e.g., `172.17.0.0/16`) for the bridge network. Each container gets an IP address from this range, similar to how devices on a local network get IP addresses from a router.

If you have two containers running on the default bridge network, they might get IP addresses like `172.17.0.2` and `172.17.0.3`. They can communicate with each other using these IP addresses or their container names. Docker automatically sets up DNS resolution.

For example,

If we start two containers from,

```cmd
docker run -d --name webserver nginx
```

```
 docker run -d --name database mysql
```

These two containers can communicate using their assigned IPs or by their names `webserver` and `database`.

## Host Network

The `host network` allows a container to share the host system's network stack. This means the container doesn't get its own IP address, instead, it shares the host's IP address.

The container runs directly on the hosts network, without any network isolation. This is useful for cases where you want to avoid network overhead or need the container to bind to specific ports on the host.

The container uses the host machines IP address, no seperate IP address is assigned to the container. Any service running inside the container will be accessible on the hosts IP address.

## Overlay Network

The `overlay network` is used in Docker Swarm and Kubernetes environments to enable communication between containers running on different Docker hosts.

Overlay networks span multiple Docker hosts, creating a distributed network. Containers on different hosts can communicate as if they were on the same local network. Each container gets an IP address from the overlay network’s IP range. Docker manages the routing and ensures that traffic is correctly forwarded between hosts.

If you have a Swarm cluster with three nodes, containers on any of the nodes can communicate with each other over the overlay network.

## Macvlan Network

The `macvlan network` allows you to assign a MAC address to each container, making it appear as a physical device on the network.

The container gets its own IP and MAC address, and it’s treated as a physical device on the host's network. This network type is useful when you need containers to appear as physical devices to the outside world or when integrating with legacy applications that require MAC addresses.


## None Network

The `none network` disables networking for the container. This means the container has no network access at all.

The container is isolated with no external network connectivity. You might use this network type if your container doesn’t need to communicate with other containers or the host. No IP address is assigned, as there’s no network interface.