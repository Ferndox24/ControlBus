[app]

# (str) Nombre de la aplicación
title = ControlBus

# (str) Nombre del paquete
package.name = controlbus

# (str) Dominio del paquete
package.domain = org.controlbus

# (str) Carpeta donde está main.py
source.dir = .

# (list) Extensiones
source.include_exts = py,png,jpg,jpeg,kv,xlsx,json

# (str) Versión obligatoria
version = 1.0.0


# (list) Dependencias Python
requirements = python3,kivy,openpyxl,pillow


# (str) Orientación
orientation = portrait


# (bool) Pantalla completa
fullscreen = 0



# Android

android.api = 35
android.minapi = 23

# IMPORTANTE: evita build-tools 37
android.build_tools_version = 35.0.0


# NDK recomendado
android.ndk = 28c


# Arquitecturas
android.archs = arm64-v8a,armeabi-v7a


# Permisos cámara
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# Activar cámara Android
android.enable_androidx = True


# Copiar archivos
android.add_src = .


# Nombre del icono (si existe)
# icon.filename = %(source.dir)s/icon.png



[buildozer]

# Log
log_level = 2

# Avisos
warn_on_root = 1
