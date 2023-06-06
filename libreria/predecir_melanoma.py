
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# import lib.constants as C
IMG_SIZE = (160,160)
NUM_CLASSES = 2

def predict_image_array(img_arr, model, plot=True):
    input_arr = tf.convert_to_tensor(img_arr)# Convierte en un array 
    input_arr = input_arr[tf.newaxis, ...] # aniade ejee para bach
    input_arr = tf.image.resize(input_arr, IMG_SIZE) # re compone a tamano
    input_arr = input_arr.numpy() 
    # input_arr = np.array([input_arr])  # Convert single image to a batch.

    predictions = model.predict(input_arr) #predice los logist
    # Apply a sigmoid since our model returns logits
    predictions_prob = tf.nn.softmax(predictions, axis=1)
    predictions_values = tf.argmax(predictions,axis=1)
    # created values for output 
    prediction_value = int(predictions_values[0])
    print('===========>>>> predicion value: ', prediction_value)
    prediction_prob = predictions_prob.numpy()[0][prediction_value]
    print('------>>>   probs: ', predictions_prob) 
    # prediction_prob = 0

    class_names = ['Melanoma', 'NotMelanoma']
    prediction_name = class_names[prediction_value] 
    
    return prediction_name,prediction_value



def load_entire_model(path_to_model):
    model = tf.keras.models.load_model(path_to_model)
    return model 




if __name__ == '__main__':
    # model = create_model(None)
    model = load_entire_model('./saved_model/my_model')
    image_path = 'imagen_limon_verde.jpg'
    pred_value, pred_prob, pred_name = predict_image(image_path, model)

