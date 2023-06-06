# import the opencv library
import cv2
import numpy as np
from libreria.predecir_melanoma import load_entire_model, predict_image_array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
import datetime
TOKEN = "5858768507:AAFL8yBpPmfZAeJK826YxIfLtFZXzThpKJA"
CHAT_ID = "5514441598"

def bot_send_text(bot_message):
    
    bot_token = TOKEN
    bot_chatID = CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

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
pred_name,value_pred = predict_image_array(frame, model)
print("==========>>>>>>>",pred_name)

plt.imshow(frame)
plt.title(pred_name)
plt.axis('off')  # Opcional: Desactiva los ejes
plt.show()

fecha_actual = datetime.date.today().strftime("%d-%m-%Y")

no_orden = input("Ingrese el número de orden: ")
nombre_paciente = input("Ingrese el nombre del paciente: ")
edad_paciente = input("Ingrese la edad del paciente: ")
telefono = input("Ingrese el número de teléfono: ")
ci = input("Ingrese el número de cédula de identidad: ")
texto = f'''\
\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPagina No. 01 \
\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFecha: {fecha_actual}\
\n================================================\
\nNo Orden : {no_orden}\t\t\t\t\t\t\t\t\t\t\t\tNo. ingreso : 010\
\nPaciente : {nombre_paciente}\tEdad\t\t\t\t\t\t\t : {edad_paciente}\
\nC.I.\t\t\t\t : {ci}\t\t\t\t\t\t\tTelefono\t\t\t : {telefono}\
\nEl tiene el siguiente diagnóstico: {pred_name}
'''

test_bot = bot_send_text(texto)







