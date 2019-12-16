# README

This project contain a template useful for the deployment of machine learning algorithms based on [scikit-learn](http://scikit-learn.org/stable).

Using [Flask](http://palletsprojects.com/p/flask) it implements REST apis for query the *machine learning* model.

The file [build_model.py](https://github.com/alessandroadamo/ml-template/blob/master/app/build_model.py) is dedicated to the implementation and serialization and storage of the model in binary form.

The file [app.py](https://github.com/alessandroadamo/ml-template/blob/master/app/app.py) contain the Flask main app in which is loaded the machine learning model, defined the REST apis and initialized the service.




## Build the Docker image

To build the docker image run the following code in the shell

```console
foo@bar:~$ docker build --no-cache -t ml-template -f Dockerfile . 
```

## Run the Docker service

```console
foo@bar:~$ docker run --rm -i -t -p 6000:5000 -v /home/user/PycharmProjects/ml-template/lib/models/:/home/user/lib/models/ ml-template
```