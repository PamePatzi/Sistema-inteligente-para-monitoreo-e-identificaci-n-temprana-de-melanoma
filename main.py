# import the opencv library
import cv2
import numpy as np
from libreria.predecir_melanoma import load_entire_model, predict_image_array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

a = 0 
# define a video capture object
vid = cv2.VideoCapture(0)
model = load_entire_model('./saved_model/my_model')
while True:
    ret, frame = vid.read() 
    if a == 1:
        print("foto tomada")
        break
    a = int(input("apreta 1 para sacar la foto:"))
cv2.waitKey(1)
 # After the loop release the cap object
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
pred_name = predict_image_array(frame, model)
print("==========>>>>>>>",pred_name)

plt.imshow(frame)
plt.title(pred_name)
plt.axis('off')  # Opcional: Desactiva los ejes
plt.show()











