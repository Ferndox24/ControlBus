[app]

# Nombre de la aplicación
title = ControlBus

# Versión de la aplicación
version = 1.0

# Nombre interno del paquete (sin espacios)
package.name = controlbus

# Dominio del paquete
package.domain = org.ferndox

# Carpeta donde está main.py
source.dir = .

# Archivos que se incluirán en la APK
source.include_exts = py,png,jpg,jpeg,kv,json,xlsx,txt

# Dependencias de Python/Kivy
requirements = python3,kivy,numpy,opencv,openpyxl,plyer

# Orientación de pantalla
orientation = portrait

# Pantalla completa desactivada
fullscreen = 0



[android]

# Arquitectura compatible
android.archs = arm64-v8a

# Android mínimo soportado
android.minapi = 23

# Android objetivo
android.api = 35

# Permisos necesarios
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



[buildozer]

# Nivel de información del proceso
log_level = 2
