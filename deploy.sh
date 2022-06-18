echo "Starting to deploy docker image.."
DOCKER_IMAGE=asbind/photogalleryflaskapp:latest
docker pull $DOCKER_IMAGE
docker rm -f $(docker ps -aq)
docker run -d -p 5000:5000 $DOCKER_IMAGE
