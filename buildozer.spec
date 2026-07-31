[app]

# Nombre de la aplicación
title = ControlBus

# Nombre interno del paquete
package.name = controlbus

# Dominio del paquete
package.domain = org.controlbus

# Carpeta donde está main.py
source.dir = .

# Archivos que se incluirán
source.include_exts = py,kv,png,jpg,jpeg,json,txt,atlas

# Versión
version = 1.0


# Dependencias
requirements = python3,kivy


# Orientación
orientation = portrait



[buildozer]

# Nivel de logs
log_level = 2



[android]

# Versión Android usada para compilar
android.api = 35

# Android mínimo compatible
android.minapi = 23

# NDK recomendado por python-for-android
android.ndk = 28c


# Aceptar licencias automáticamente
android.accept_sdk_license = True


# Arquitecturas soportadas
archs = arm64-v8a,armeabi-v7a
