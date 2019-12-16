from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort
import configparser
import logging
import sys
from joblib import load, hash
import datetime


MODEL_NAME='iris'


# create the logger
logger = logging.Logger('app')
logger.setLevel(logging.DEBUG)

# read the configuration file
config = configparser.ConfigParser()
config.read('./config.ini')

if 'MODEL' not in config.sections():
    logger.error('[ ' + str(datetime.datetime.utcnow()) + ' ] ' +'MODEL section is not present')
    sys.exit(2)

if 'model_path' not in config['MODEL']:
    logger.error('[ ' + str(datetime.datetime.utcnow()) + ' ] ' +'model_path key is not present in MODEL section')
    sys.exit(2)

if 'model_md5_path' not in config['MODEL']:
    logger.error('[ ' + str(datetime.datetime.utcnow()) + ' ] ' +'model_md5_path key is not present in MODEL section')
    sys.exit(2)

if 'model_sha1_path' not in config['MODEL']:
    logger.error('[ ' + str(datetime.datetime.utcnow()) + ' ] ' +'model_sha1_path key is not present in MODEL section')
    sys.exit(2)


# load the model from the model path
logger.info('[ ' + str(datetime.datetime.utcnow()) + ' ] ' + 'Loading the model')
model = load(config['MODEL']['model_path'])

logger.info('[ ' + str(datetime.datetime.utcnow()) + ' ] ' + 'Cheching model checksums')
md5 = hash(model, 'md5')
sha1 = hash(model, 'sha1')

with open(config['MODEL']['model_md5_path'], 'r') as f:
    md5_orig = f.read()

with open(config['MODEL']['model_sha1_path'], 'r') as f:
    sha1_orig = f.read()

if md5 != md5_orig or sha1 != sha1_orig:
    logger.error('[ ' + str(datetime.datetime.utcnow()) + ' ] ' + 'Model checksums does not match')
    sys.exit(2)

logger.info('[ ' + str(datetime.datetime.utcnow()) + ' ] ' + 'Model checksums OK!')

# Model Class Definition
class Model(Resource):

    @staticmethod
    def post():
        posted_data = request.get_json()
        sepal_length = posted_data['sepal_length']
        sepal_width = posted_data['sepal_width']
        petal_length = posted_data['petal_length']
        petal_width = posted_data['petal_width']

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        if prediction == 0:
            predicted_class = 'Iris-setosa'
        elif prediction == 1:
            predicted_class = 'Iris-versicolor'
        else:
            predicted_class = 'Iris-virginica'

        return jsonify(
            prediction = predicted_class,
            confidence = None
        )


app = Flask(__name__)
api = Api(app)


api.add_resource(Model, '/' + MODEL_NAME + '/predict')


if __name__ == '__main__':

    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5000)
