import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('COM5',9600,timeout=1)
time.sleep(2)

cap = cv2.VideoCapture(0)

# rangos HSV

red_lower1 = np.array([0,100,100])
red_upper1 = np.array([10,255,255])

red_lower2 = np.array([170,100,100])
red_upper2 = np.array([180,255,255])

green_lower = np.array([40,70,70])
green_upper = np.array([80,255,255])

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red = cv2.inRange(hsv, red_lower1, red_upper1) + cv2.inRange(hsv, red_lower2, red_upper2)
    mask_green = cv2.inRange(hsv, green_lower, green_upper)

    rojo_detectado = False
    verde_detectado = False

    # ROJO
    contours_red,_ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours_red:

        if cv2.contourArea(cnt) > 800:

            cv2.drawContours(frame,[cnt],-1,(0,0,255),3)

            x,y,w,h = cv2.boundingRect(cnt)

            cv2.putText(frame,"Rojo",(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,(0,0,255),2)

            rojo_detectado = True

    # VERDE
    contours_green,_ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours_green:

        if cv2.contourArea(cnt) > 800:

            cv2.drawContours(frame,[cnt],-1,(0,255,0),3)

            x,y,w,h = cv2.boundingRect(cnt)

            cv2.putText(frame,"Verde",(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,(0,255,0),2)

            verde_detectado = True


    # =====================
    # ENVIAR A ARDUINO
    # =====================

    if rojo_detectado:
        arduino.write(b'ROJO_ON\n')
    else:
        arduino.write(b'ROJO_OFF\n')

    if verde_detectado:
        arduino.write(b'VERDE_ON\n')
    else:
        arduino.write(b'VERDE_OFF\n')


    cv2.imshow("Vision Artificial",frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()