# Image build
`docker build -t int .`

# Run container

`docker run -it --name int`

# Upload to a Dockerhub
`docker login`
`docker tag int:latest dockerhub-username/int:latest`
`docker push dockerhub-username/int:latest`


