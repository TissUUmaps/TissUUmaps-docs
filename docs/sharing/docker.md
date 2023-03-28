# Docker container

## Start a TissUUmaps docker instance

1. Start the docker container `cavenel/tissuumaps:latest` from Docker Hub:
```bash
docker run -it -p 56733:80 --name=tissuumaps -v /path/to/local/images:/mnt/data cavenel/tissuumaps:latest
```
1. Place your images in the local folder `/path/to/local/images/share`.
1. Open [http://127.0.0.1:56733/](http://127.0.0.1:56733/) in your favorite browser.

## Define TissUUmaps service in a Compose file

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

**If you use compose, you don't need to start the docker container from the previous section.**

1. Install [docker-compose](https://docs.docker.com/compose/install/).

1. Create a file called `docker-compose.yml` in your project directory and paste the following:

    ```
    version: "3.9"
    services:
      backend:
        image: docker.io/cavenel/tissuumaps:latest
        volumes:
          - type: bind
            source: /jail
            target: /mnt/data
        restart: on-failure
        ports:
          - 127.0.0.1:8050:80
    ```

    This `Compose` file defines TissUUmaps backend service on port 8050.
    The web service uses an image that’s built from docker.io hub. It then binds the container and the host machine to the exposed port, 8050.

1. Put your data in the source folder (here `/jail/shared/`). You can change the source path in the `docker-compose.yml` file.

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

## Configure sftp multi-user access (Optional)

Add the following lines to `/etc/ssh/sshd_config`:
```
Subsystem sftp internal-sftp
Match Group sftpusers
    ChrootDirectory /jail/shared/%u
    X11Forwarding no
    AllowTcpForwarding no
    ForceCommand internal-sftp
    PasswordAuthentication yes
```

Use the following bash script to create new sftp users **(as root)**:
```bash
#! /bin/bash

read -p 'Username: ' uservar
# Use the path mounted in docker:
MOUNT_TMAP='/jail'

# Create sftpusers group and $uservar user
groupadd sftpusers
adduser --gecos "" --home $MOUNT_TMAP/shared/$uservar $uservar
usermod -G sftpusers $uservar 

# Create home for user in $MOUNT_TMAP/shared/ with correct permissions
mkdir -p $MOUNT_TMAP/shared/$uservar/files
chmod 755 $MOUNT_TMAP/shared/$uservar/
chown root:root $MOUNT_TMAP/shared/$uservar/
chmod 750 $MOUNT_TMAP/shared/$uservar/files/
chown $uservar:$uservar $MOUNT_TMAP/shared/$uservar/files

# Make sure all files created in the files folder are writable by $uservar
setfacl -m d:u:$uservar:rwx $MOUNT_TMAP/shared/$uservar/files/

echo 'To access files placed in the /files sftp folder, use:'
echo '    http://TMAP_URL/FILENAME?path='$uservar'/files'
```

The new users will be able to connect through sftp, and only see the files in `/jail/shared/USER_NAME/files`. Files will be available on the web using `http://localhost:8050/MYFILE.tmap?path=/USER_NAME/files`

Restart the ssh daemon with `sudo service ssh restart`.

## Password protection of files hosted on TissUUmaps docker

You can add login and password for any folder hosted on the TissUUmaps server by adding a `auth` file containing your login and password in the format:
```
login:password
```