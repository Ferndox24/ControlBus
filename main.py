from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import platform

from buscar import buscar_trabajador
from asistencia import registrar_asistencia
from qr import extraer_rut


# Selección automática de cámara
if platform.system() == "Android":
    from camara_android import abrir_camara
else:
    from camara import abrir_camara



class ControlBusApp(App):


    ruta_excel = None



    def build(self):

        ventana = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        titulo = Label(
            text="🚌 CONTROL SUBIDA BUS",
            font_size=25
        )

        ventana.add_widget(titulo)



        self.archivo = Label(
            text="Excel no seleccionado"
        )

        ventana.add_widget(
            self.archivo
        )



        boton_excel = Button(
            text="📂 Seleccionar Excel",
            size_hint_y=None,
            height=50
        )

        boton_excel.bind(
            on_press=self.seleccionar_excel
        )

        ventana.add_widget(
            boton_excel
        )



        boton_qr = Button(
            text="📷 Escanear QR",
            size_hint_y=None,
            height=50
        )

        boton_qr.bind(
            on_press=self.abrir_qr
        )

        ventana.add_widget(
            boton_qr
        )



        self.rut = TextInput(
            hint_text="Ingresar RUT",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        ventana.add_widget(
            self.rut
        )



        boton_buscar = Button(
            text="🔎 Buscar trabajador",
            size_hint_y=None,
            height=50
        )


        boton_buscar.bind(
            on_press=self.buscar_rut
        )


        ventana.add_widget(
            boton_buscar
        )



        self.resultado = Label(
            text="Esperando..."
        )


        ventana.add_widget(
            self.resultado
        )


        return ventana






    def seleccionar_excel(self, boton):


        from tkinter import filedialog
        import tkinter as tk


        root = tk.Tk()
        root.withdraw()


        archivo = filedialog.askopenfilename(

            title="Seleccionar Excel",

            filetypes=[
                ("Excel", "*.xlsx")
            ]

        )



        if archivo:


            self.ruta_excel = archivo


            nombre = archivo.split("/")[-1]


            self.archivo.text = (

                "Excel seleccionado:\n"
                + nombre

            )


            self.resultado.text = (

                "✅ Excel cargado"

            )


        else:


            self.resultado.text = (

                "❌ No se seleccionó Excel"

            )







    def abrir_qr(self, boton):


        abrir_camara(

            self.qr_detectado

        )







    def qr_detectado(self, texto):


        print(
            "QR COMPLETO:",
            texto
        )



        rut = extraer_rut(
            texto
        )


        print(
            "RUT EXTRAÍDO:",
            rut
        )



        if rut:


            self.procesar_trabajador(
                rut
            )


        else:


            self.resultado.text = (

                "❌ QR sin RUT"

            )








    def buscar_rut(self, boton):


        rut = self.rut.text.strip()



        if rut == "":


            self.resultado.text = (

                "❌ Ingrese RUT"

            )

            return



        self.procesar_trabajador(
            rut
        )








    def procesar_trabajador(self, rut):


        if not self.ruta_excel:


            self.resultado.text = (

                "❌ Seleccione Excel primero"

            )

            return




        trabajador = buscar_trabajador(

            rut,

            self.ruta_excel

        )



        if trabajador:


            registrado = registrar_asistencia(

                trabajador,

                self.ruta_excel

            )



            if registrado:


                self.resultado.text = (

                    "✅ ASISTENCIA REGISTRADA\n\n"

                    f"Nombre:\n"
                    f"{trabajador['NOMBRE']}\n\n"

                    f"RUT:\n"
                    f"{trabajador['RUT']}"

                )



            else:


                self.resultado.text = (

                    "⚠️ YA REGISTRADO\n\n"

                    f"{trabajador['NOMBRE']}"

                )



        else:


            self.resultado.text = (

                "❌ TRABAJADOR NO ENCONTRADO"

            )







ControlBusApp().run()