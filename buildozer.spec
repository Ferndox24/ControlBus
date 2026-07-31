[app]

# Nombre de la aplicación
title = ControlBus

# Nombre interno del paquete (sin espacios)
package.name = controlbus

# Dominio del paquete
package.domain = org.ferndox

# Carpeta donde está main.py
source.dir = .

# Archivos que se incluirán
source.include_exts = py,png,jpg,jpeg,kv,json,xlsx,txt

# Librerías necesarias
requirements = python3,kivy,numpy,opencv,openpyxl,plyer

# Orientación de pantalla
orientation = portrait

# No usar pantalla completa
fullscreen = 0



[android]

# Arquitectura recomendada actualmente
android.archs = arm64-v8a

# Android mínimo compatible
android.minapi = 23

# Versión objetivo
android.api = 35

# Permisos necesarios
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



[buildozer]

# Nivel de información del compilador
log_level = 2
