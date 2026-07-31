import cv2
from pyzbar.pyzbar import decode


def abrir_camara(callback):

    # Cámara principal
    camara = cv2.VideoCapture(0)

    if not camara.isOpened():
        print("❌ No se pudo abrir la cámara")
        return


    print("📷 Cámara iniciada")


    while True:

        ret, frame = camara.read()


        if not ret:
            print("❌ Error leyendo cámara")
            break



        # Buscar códigos QR

        codigos = decode(frame)



        for codigo in codigos:


            texto = codigo.data.decode(
                "utf-8"
            )


            print(
                "QR DETECTADO:",
                texto
            )


            # Cerrar cámara

            camara.release()
            cv2.destroyAllWindows()


            # Enviar resultado al main

            callback(texto)


            return



        # Mostrar cámara

        cv2.imshow(
            "Escanear QR - Presione ESC para salir",
            frame
        )



        # ESC para cerrar

        tecla = cv2.waitKey(1)

        if tecla == 27:

            break



    camara.release()

    cv2.destroyAllWindows()