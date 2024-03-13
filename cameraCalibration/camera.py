import cv2

# Dirección IP y puerto de la cámara DroidCam
direccion_ip = '192.168.1.152'
puerto = 4747

# Inicia la captura de video desde la cámara DroidCam
direccion_captura = f'http://{direccion_ip}:{puerto}/video'
cap = cv2.VideoCapture(direccion_captura)
num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == ord('q'):
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(r'D:\Usuario\Escritorio\cameraCalibration\trainingImages' + '\\img' + str(num) + '.png', img)
        print("image saved!")
        num += 1

    cv2.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()