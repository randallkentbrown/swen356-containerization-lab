# Some Docker commands have been removed!
# They've been replaced with their descriptions, in brackets [Like this].
# Look through the documentation and figure out how to do what this command needs!

# Copy from base Ubuntu image and copy files
FROM ubuntu:18.04
RUN mkdir /app
# [A command to copy everything in this local repo to the /app directory in the image.]
WORKDIR /app

# Install dependencies
RUN apt-get -y update
# [A command to install the aiohttp module using apt-get.]

# Networking and running
# [A command to expose the container's port 80.]
CMD [ "python3", "/app/server.py" ]
