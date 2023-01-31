import tensorflow as tf
from tensorflow.keras import models
import tensorflow_hub as hub
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np

# Our custom Activation Functions
# pflu activation function
def pflu_activation(x):
    """ A non-montonic activation function """
    return x*0.5*(1+(x/(1+x**2)**0.5))

#fpflu actiavtion function
def fpflu_activation(x):
    """ A non-montonic activation function ( faster form of pflu ) """
    return tf.math.maximum(x,x/(1+x**2))


# Loading Model
from tensorflow.keras.models import load_model
model1 = load_model("ml_model/model.h5", custom_objects={'KerasLayer': hub.KerasLayer , 'fpflu_activation' :fpflu_activation , 'pflu_activation' : pflu_activation  })


def actual_class(pred) :
    """Determination of class of image"""
    if pred == 0 :
        return 'confirmed'
    if pred == 1 :
        return 'crossed-out'
    if pred == 2 :
        return 'empty'


def ImageClass(path) :
    """ Gives back the model's prediction with confidence score"""
    img = tf.keras.preprocessing.image.load_img(
    path, color_mode='rgb', interpolation='bilinear', target_size=(224,224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = tf.keras.applications.mobilenet.preprocess_input(
    x[tf.newaxis,...])
    pred = model1.predict(x)
    pred_class = np.argmax( pred , axis = -1 )[0]
    pred = pred.reshape(3)
    print(pred_class)
    confidence_score = pred[pred_class]

    ac_class = actual_class(pred_class)

    return confidence_score, ac_class