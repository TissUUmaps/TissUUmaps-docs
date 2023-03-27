# Docker container

1. Start the docker container `cavenel/tissuumaps:latest` from Docker Hub:
```bash
docker run -it -p 56733:80 --name=tissuumaps -v /path/to/local/images:/mnt/data cavenel/tissuumaps:latest
```
1. Place your images in the local folder `/path/to/local/images/share`.
1. Open [http://127.0.0.1:56733/](http://127.0.0.1:56733/) in your favorite browser.

# Define TissUUmaps service in a Compose file

1. Install [docker-compose](https://docs.docker.com/compose/install/).

1. Create a file called `docker-compose.yml` in your project directory and paste the following:

    ```
    version: "3.9"
    services:
      backend:
        image: docker.io/cavenel/tissuumaps:latest
        volumes:
          - type: bind
            source: ./data
            target: /mnt/data
        restart: on-failure
        ports:
          - 127.0.0.1:8050:80
    ```

    This `Compose` file defines TissUUmaps backend service on port 8050.
    The web service uses an image that’s built from docker.io hub. It then binds the container and the host machine to the exposed port, 8050.

1. Put your data in the source folder (here `./data`). You can change the source path in the `docker-compose.yml` file.

1. From your project directory, start up your application by running `docker compose up`.

    ```bash
    $ docker-compose up
    Creating network "tmap_compose_default" with the default driver
    Creating tmap_compose_backend_1 ... done
    Attaching to tmap_compose_backend_1
    backend_1  | [2023-03-27 11:23:57 +0000] [1] [INFO] Starting gunicorn 20.1.0
    backend_1  | [2023-03-27 11:23:57 +0000] [1] [INFO] Listening at: http://0.0.0.0:80 (1)
    backend_1  | [2023-03-27 11:23:57 +0000] [1] [INFO] Using worker: gevent
    backend_1  | [2023-03-27 11:23:57 +0000] [7] [INFO] Booting worker with pid: 7
    backend_1  | [2023-03-27 11:23:57 +0000] [8] [INFO] Booting worker with pid: 8
    backend_1  | [2023-03-27 11:23:57 +0000] [9] [INFO] Booting worker with pid: 9
    backend_1  | [2023-03-27 11:23:57 +0000] [10] [INFO] Booting worker with pid: 10
    backend_1  | [2023-03-27 11:23:57 +0000] [11] [INFO] Booting worker with pid: 11
    backend_1  | [2023-03-27 11:23:57 +0000] [12] [INFO] Booting worker with pid: 12
    backend_1  | [2023-03-27 11:23:57 +0000] [13] [INFO] Booting worker with pid: 13
    backend_1  | [2023-03-27 11:23:57 +0000] [14] [INFO] Booting worker with pid: 14
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    backend_1  | INFO:root: * TissUUmaps version: 3.1.0.1
    ```

1. Enter http://localhost:8050 in a browser to see TissUUmaps application running.