------ Calibración de la camara en OpenCV ------

* Primero abrimos el archivo camera.py que al ejecutarlo iniciara la camara (en este caso utilizando droidcam) y recopilará imagenes que irá almacenando en la carpeta trainingImages
	* Cada que se presione la tecla 's' almacenaremos una imagen. Al presionar 'q' terminaremos el proceso.
* Una vez recopiladas todas las imagenes ejecutamos el archivo cameraCalibration que se encargará de analizar todas las imagenes recopiladas para realizar la calibración.
	* Una vez termina el proceso almacena las imagenes calibradas en la carpeta trainingResults

!!!!!! IMPORTANTE !!!!!!!!
Eliminar las imagenes que contienen las carpetas antes de comenzar a utilizar los programas