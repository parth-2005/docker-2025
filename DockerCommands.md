# Docker Commands Cheat Sheet

## Table of Contents
1. [Building Images](#building-images)
2. [Managing Images](#managing-images)
3. [Working with Containers](#working-with-containers)
4. [Networking](#networking)
5. [Docker Hub](#docker-hub)
6. [General Commands](#general-commands)
7. [Installation & Resources](#installation--resources)

---

## Building Images

- **Build an Image from a Dockerfile**  
  ```sh
  docker build -t <image_name> .
  ```
- **Build an Image without cache**  
  ```sh
  docker build -t <image_name> . --no-cache
  ```

## Managing Images

- **List local images**  
  ```sh
  docker images
  ```
- **Delete an Image**  
  ```sh
  docker rmi <image_name>
  ```
- **Remove all unused images**  
  ```sh
  docker image prune
  ```

## Working with Containers

- **Create and run a container from an image**  
  ```sh
  docker run --name <container_name> <image_name>
  ```
- **Run a container and publish ports**  
  ```sh
  docker run -p <host_port>:<container_port> <image_name>
  ```
- **Run a container in the background**  
  ```sh
  docker run -d <image_name>
  ```
- **Start or stop an existing container**  
  ```sh
  docker start <container_name>
  docker stop <container_name>
  ```
- **Remove a stopped container**  
  ```sh
  docker rm <container_name>
  ```
- **Open a shell inside a running container**  
  ```sh
  docker exec -it <container_name> sh
  ```
- **View logs of a container**  
  ```sh
  docker logs -f <container_name>
  ```
- **Inspect a running container**  
  ```sh
  docker inspect <container_name>
  ```
- **List running containers**  
  ```sh
  docker ps
  ```
- **List all containers (including stopped ones)**  
  ```sh
  docker ps --all
  ```
- **View resource usage stats**  
  ```sh
  docker container stats
  ```

## Networking

- **List available networks**  
  ```sh
  docker network ls
  ```
- **Inspect a network**  
  ```sh
  docker network inspect <network_name>
  ```
- **Create a network**  
  ```sh
  docker network create <network_name>
  ```
- **Connect a running container to a network**  
  ```sh
  docker network connect <network_name> <container_name>
  ```
- **Disconnect a running container from a network**  
  ```sh
  docker network disconnect <network_name> <container_name>
  ```

## Docker Hub

- **Login to Docker Hub**  
  ```sh
  docker login -u <username>
  ```
- **Publish an image to Docker Hub**  
  ```sh
  docker push <username>/<image_name>
  ```
- **Search for an image on Docker Hub**  
  ```sh
  docker search <image_name>
  ```
- **Pull an image from Docker Hub**  
  ```sh
  docker pull <image_name>
  ```

## General Commands

- **Start the Docker daemon**  
  ```sh
  docker -d
  ```
- **Get help with Docker commands**  
  ```sh
  docker --help
  ```
- **Display system-wide information**  
  ```sh
  docker info
  ```

## Installation & Resources

- **Docker Desktop (Mac, Linux, Windows)**  
  [https://docs.docker.com/desktop](https://docs.docker.com/desktop)
- **Example projects using Docker**  
  [https://github.com/docker/awesome-compose](https://github.com/docker/awesome-compose)
- **Official Docker documentation**  
  [https://docs.docker.com](https://docs.docker.com)