<div align="center">
  <h1> Compose </h1>
</div>

Docker compose is a tool that allows you to define and run multiple services and applications that belong together in one isolated environment. It's common to have a frontend container, a backend container, an authentication container, etc...Docker compose allows us to group and execute these together. Simply put, if we want to deploy multiple docker containers where each container may have its different  configuration options, we can use docker compose to accomplish this.

# Without Docker compose

Let us take an example where we run two containers,

1. Create a Docker Network (To allow containers to communicate)
2. Start MongoDB Container
3. Start Mongo Express Container (A UI tool for MongoDB)

Would appear as,

1. Create the Docker Network

```sh
docker network create mongo-network
```
2. Start the MongoDB Container. The following command will pull the latest mongo image from dockerhub repository and run it in a detached mode.

```sh
docker run -d  \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=supersecret \
--network mongo-network \
--name mongodb \
mongo
```

3. Start the Mongo Express container.

Here, we are connecting our Mongo Express container to our MongoDB container.


```sh
docker run -d  \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=supersecret \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--network mongo-network \
--name mongo-express \
mongo-express
```

- The port for Mongo Express is 8081
- The Environment variables are [retrieved from their documentation](https://hub.docker.com/_/mongo-express)
- The image `mongo-express` is pulled from [docker hub](https://hub.docker.com/_/mongo-express)

To test that this is working, we can access it by visiting `localhost:8081`. In this example their is only two containers, but we can envision this becoming significantly larger with more than 10 containers interacting with each other. Starting, stopping and configuring these containers will require a lot of tedious manual work. This is where docker compose is used.

With docker compose, we have a single YAML file to configure and maintain our application services (containers) that we want to start together with all of their configuration in one central location that we can easily modify and use to start and stop those containers.

With a docker compose file, we start off by specifying the `services`. Here, our two main services are `mongodb` and `mongo-express`. This is mapped from the container name. Here, we can map the `mongodb` service to the following structure inside the docker compose file,

```YAML
services:
    mongodb:
        image: mongo
        ports:
            - 27017:27017
        environment:
            MONGO_INITDB_ROOT_USERNAME: admin
            MONGO_INITDB_ROOT_PASSWORD: supersecret
```

Combining both services, the end result will become,

```YAML
services:
    mongodb:
        image: mongo
        ports:
            - 27017:27017
        environment:
            MONGO_INITDB_ROOT_USERNAME: admin
            MONGO_INITDB_ROOT_PASSWORD: supersecret
    
    mongo-express:
        image: mongo-express
        ports:
            - 8081:8081
        environment:
            ME_CONFIG_MONGODB_ADMINUSERNAME: admin
            ME_CONFIG_MONGODB_ADMINPASSWORD: pass
            ME_CONFIG_MONGODB_SERVER: mongodb
```

`--network mongo-network` is intentionally not included. By default, compose sets up a single network for the application. Now, we have created an easily modifiable and shareable file can be also be versioned.

The compose file can be ran by executing `docker compose -f docker-compose.yaml up`. Execution of this file will result in both services starting at the same time, this can be seen by the mixed output in the terminal.

```
mongo-express-1  |
mongo-express-1  |
mongo-db-1       |
mongo-express-1  |
mongo-db-1       |
...
```

Now, this is causing a problem for us because we need the `mongo-db` container to have completely started before we begin the `mongo-express` service, as this tries to connect to the database. This can be achieved by adding the `depends_on` tag, hence modifying the `mongo-express` container to,

```YAML
    mongo-express:
        image: mongo-express
        ports:
            - 8081:8081
        environment:
            ME_CONFIG_MONGODB_ADMINUSERNAME: admin
            ME_CONFIG_MONGODB_ADMINPASSWORD: pass
            ME_CONFIG_MONGODB_SERVER: mongodb
        depends_on:
            - "mongodb"
```

Without running in detached mode (`-d`), the container can be stopped by stopping the shell using `ctrl + c`. When it began in detached mode, we will need to stop it by using `docker compose -f docker-compose.yaml down`. This will stop and then remove the containers, network, volumes and image created from `up`. Alternatively replace `up` and `down` with `start` and `stop` to stop and re-start them the container, which in this case will make the data persistent as the container has not restarted.