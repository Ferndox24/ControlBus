from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock

from pyzbar.pyzbar import decode
import cv2
import numpy as np


class CamaraQR(BoxLayout):

    def __init__(self, callback, popup, **kwargs):

        super().__init__(
            orientation="vertical",
            **kwargs
        )

        self.callback = callback
        self.popup = popup


        self.camera = Camera(
            index=0,
            resolution=(640,480),
            play=True
        )


        self.add_widget(
            self.camera
        )


        boton = Button(
            text="Cerrar cámara",
            size_hint_y=None,
            height=50
        )


        boton.bind(
            on_press=self.cerrar
        )


        self.add_widget(
            boton
        )


        Clock.schedule_interval(
            self.leer_qr,
            0.3
        )



    def leer_qr(self, dt):

        if not self.camera.texture:
            return


        try:

            textura = self.camera.texture


            imagen = np.frombuffer(
                textura.pixels,
                dtype=np.uint8
            )


            imagen = imagen.reshape(
                textura.height,
                textura.width,
                4
            )


            imagen = cv2.cvtColor(
                imagen,
                cv2.COLOR_RGBA2BGR
            )


            codigos = decode(imagen)


            for codigo in codigos:

                texto = codigo.data.decode(
                    "utf-8"
                )


                print(
                    "QR DETECTADO:",
                    texto
                )


                self.callback(
                    texto
                )


                self.cerrar(
                    None
                )


                return



        except Exception as e:

            print(
                "Error lectura QR:",
                e
            )



    def cerrar(self, boton):

        self.camera.play = False


        if self.popup:

            self.popup.dismiss()



def abrir_camara(callback):


    popup = Popup(
        title="Escanear QR",
        size_hint=(0.95,0.95)
    )


    camara = CamaraQR(
        callback,
        popup
    )


    popup.content = camara


    popup.open()