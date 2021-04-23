# swen356-containerization-lab
A lab exercise to try out Docker. The Dockerfile is incomplete and needs a few commands put in, and you'll need to figure out the correct commands to create your image and start the application.

## Application Overview
The application is a simple web server with two routes.

* GET /hello
* GET /data?key={key}

`/hello` is a simple GET route that returns a hello world line.

`/data?key={key}` is a GET route that accesses the local file `data.json` and returns the value stored at the provided key.

## Files
In addition to `server.py`, there are two files required for the server to operate properly. Both `config.json` and `data.json` must be in the same directory as `server.py`. `config.json` is accessed at startup to properly configure the server. `data.json` is accessed during runtime to provide data when the `/data` route is called.

## Your Task
The Dockerfile in this repo needs some tender, loving care. Read up on the [Docker reference](https://docs.docker.com/engine/reference/builder/), then put back the missing commands in the Dockerfile. After that, build a new Docker image and run a container from it. When running the container you'll need to forward your host machine's port 80 to the container's port 80. Once your container is running, you can check the web server by accessing `127.0.0.1:80/hello` in a browser, with `wget`, or through an HTTP Client like Postman, assuming you've published the ports successfully. We'll be around to check in, so be sure to ask if you need help. Note that the server configuration specifies the IP 0.0.0.0; rest assured that this is correct. It allows the server to bind to its exterior IP address instead of just its loopback address, which then lets Docker connect your networking to it when the container is run with the correct flags.

Once you've got that done, play around with some of the management commands that Docker provides. You can stop, start, and remove containers and images as you see fit. Use `docker container help` or `docker image help` to see all the ways you can mess around with images and containers. If that gets boring maybe give some of the other commands you can try!

### Goals
* Make sure the container builds successfully.
* After running the container, you can access the `/hello` route.
* If you added any extra keys to the `data.json` file, make sure those are available through the `/data` route.
* Try out the image and container management commands.

### Hints
* Using the `-y` flag on `apt-get` commands will make the program automatically say yes to any prompts.
* When initially creating your Docker image, use the `-t <NAME>:<VERSION>` flag to set a tag on your image, instead of a SHA256 hash.
* When initially starting the Docker container, use the `--name <ANY NAME>` flag to set a convenient name for your container, instead of a SHA256 hash.
* Make sure to forward port 80 on your machine to port 80 on your container when you initially start it. This is done with the `-p` flag.
