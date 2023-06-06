# Sistema-inteligente-para-monitoreo-e-identificación-temprana-de-melanoma
En el presente repositorio se presenta la realización de un modelo inteligente para la detección temprana de melanoma, cancer de la piel. Para la realización de este proyecto se hace uso de un dataset desde la platafroma Kaggle para el entrenamiento del modelo. 
Sobre el modelo, se realiza un modelo convolucional, CNN, esto a causa del uso de las imagenes para su mejor procesamiento y rendimiento del modelo, ademas de utilizar pooling en las capas del modelo para la extracción características más importantes de una imagene mediante la reducción de su tamaño. Finalmente dentro de los parametros utilizados, se hace uso de activaciones Relu, para la mayoria de las capas y para la última una activación sigmoidal, ya que como estamos trabajando con un sistema binario este nos entrega valores entre 0 y 1, de salidas "melanoma"=1, "no melanoma"=0. 
Por otro lado se realiza otro modelo haciendo uso de un modelo pre entrenado como base, con la finalidad de comparar los resultados de accuracy y loss para tener una idea más amplia de como podria mejorar nuestro modelo.
Ya con el modelo entrenado se cuenta con el sensor, que en este caso es una cámara web, y el actuador, que sera un bot de mensajes para que el resultado del modelo sea enviado directamente al doctor encargado o al paciente.

## Dentro del proyecto puede encontrar:
* Carpeta: libreria: Se encuentran las librerias necesarias para correr el .py
* Carpeta: saved_model: Se encuentra el modelo entrenado ya descargado
* ImplementaciónDetectorMelanoma: código en GoogleColab, en el que se realiza la predicción con la cámara web.
* MelanomaModelo1: Modelo CNN del proyecto con algunas pruebas de funcionamiento.
* Pasos para el uso: pdf, con el instructivo para correr el archivo "main con mensaje.py" desde una nueva computadora
* Preview.txt: comandos para la descarga de librerias
* finalSIS: pdf con el reporte final del proyecto
* main con mensaje: archivo .py completo del proyecto con el uso del sensor y del actuador.
* main: archivo .py con el cargado y prueba del modelo con solo la cámara
* melanoma_a_s_a_p: modelo CNN usando un modelo base pre entrenado
## Contribución por miembro de equipo ASAP
| Documento | Integrantes involucrados|
| ----- | -------- |
|Carpetas| Sebastián Castro|
|ImplementaciónDetectorMelanoma| Andres Hinojosa|
|MelanomaModelo1| Ariel Clemente, Pamela Patzi|
|Pasos para el uso|Sebastián Castro, Ariel Clemente, Pamela Patzi |
|Preview.txt| Ariel Clemente|
|finalSIS| Sebastián Castro, Ariel Clemente, Andres Hinojosa, Pamela Patzi|
|main con mensaje| Sebastián Castro, Ariel Clemente,Pamela Patzi|
|main| Sebastián Castro|
|melanoma_a_s_a_p| Sebastián Castro,Ariel Clemente,Pamela Patzi|
|Edición Github y readme|Pamela Patzi|
