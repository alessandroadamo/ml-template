# README

This project contain a template useful for the deployment of machine learning algorithms based on [scikit-learn](http://scikit-learn.org/stable).

Using [Flask](http://palletsprojects.com/p/flask) it implements REST apis for query the *machine learning* model.

The file [build_model.py](https://github.com/alessandroadamo/ml-template/blob/master/app/build_model.py) is dedicated to the implementation and serialization and storage of the model in binary form.

The file [app.py](https://github.com/alessandroadamo/ml-template/blob/master/app/app.py) contain the [Flask](http://palletsprojects.com/p/flask) main app in which is loaded the machine learning model, defined the REST apis and initialized the service.

In the file [model.py](https://github.com/alessandroadamo/ml-template/blob/master/app/model.py) is implemented a simple classifier that extends the classes *BaseEstimator* and *ClassifierMixin* of [scikit-learn](http://scikit-learn.org/stable) 


## Build the Docker image

To build the docker image run the following code in the shell.

```console
foo@bar:~$ docker build --no-cache -t ml-template -f Dockerfile . 
```

## Run the Docker service

To run the contained is required to pass the volume containing the binary (*model-latest.joblib*) and the checksum files (*model-latest.md5* and *model-latest.sha1*).

```console
foo@bar:~$ docker run --rm -i -t -p 5000:5000 -v /home/user/lib/models/:/home/user/lib/models/ ml-template
```
