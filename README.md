# README

## Build the Docker image

To build the docker image run the following code in the shell

```console
foo@bar:~$ docker build --no-cache -t ml-template -f Dockerfile . 
```

## Run the Docker service

```console
foo@bar:~$ docker run --rm -i -t -p 6000:5000 -v /home/user/PycharmProjects/ml-template/lib/models/:/home/user/lib/models/ ml-template
```