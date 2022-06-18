echo "Starting to deploy docker image.."
DOCKER_IMAGE=asbind/photogalleryflaskapp:latest
docker pull $DOCKER_IMAGE
docker ps -q --filter ancestor=$DOCKER_IMAGE | xargs docker rm -f
docker run -d -p 5000:5000 $DOCKER_IMAGE
