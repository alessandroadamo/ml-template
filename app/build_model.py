# Script to build and serialize the classifier

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, hash
import datetime
import shutil
import os


def dump_model(model):

    path = os.path.abspath('../lib/models/')

    # dump model to file
    date = str(datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S'))
    src = path + os.sep + 'model-' + date + '.joblib'
    dst = path + os.sep + 'model-latest.joblib'
    dst_md5 = path + os.sep + 'model-latest.md5'
    dst_sha1 = path + os.sep + 'model-latest.sha1'

    dump(model, src)
    if os.path.islink(dst):
        os.remove(dst)
    shutil.copy(src, dst)

    md5 = hash(model, 'md5')
    md5_path = path + os.sep + 'model-' + date + '.md5'
    with open(md5_path, 'w') as f:
        f.write(md5)
    shutil.copy(md5_path, dst_md5)

    sha1 = hash(model, 'sha1')
    sha1_path = path + os.sep + 'model-' + date + '.sha1'
    with open(sha1_path, 'w') as f:
        f.write(sha1)
    shutil.copy(sha1_path, dst_sha1)


###################
# BUILD THE MODEL #
###################

iris = datasets.load_iris()

model = RandomForestClassifier()
model.fit(iris.data, iris.target)

#######################
# SERIALIZE THE MODEL #
#######################

dump_model(model)
