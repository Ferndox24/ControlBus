[app]

# Nombre de la aplicación
title = ControlBus

# Nombre interno del paquete (sin espacios)
package.name = controlbus

# Dominio inverso
package.domain = org.controlbus


# Carpeta donde está tu main.py
source.dir = .

# Extensiones que incluirá la aplicación
source.include_exts = py,kv,png,jpg,jpeg,json,txt,atlas


# Versión de la aplicación
version = 1.0


# Dependencias
requirements = python3,kivy


# Orientación
orientation = portrait


# Ocultar barra de estado
fullscreen = 0



[buildozer]

# Nivel de información del proceso
log_level = 2


# Limpiar compilaciones anteriores si es necesario
warn_on_root = 1



[android]

# Versión Android usada para compilar
android.api = 35

# Versión mínima compatible
android.minapi = 23


# NDK recomendado para versiones actuales
android.ndk = 28c


# Arquitecturas compatibles
archs = arm64-v8a,armeabi-v7a


# Aceptar licencias automáticamente
android.accept_sdk_license = True


# Usar build tools estable
android.build_tools_version = 35.0.0


# Nombre del archivo final
android.entrypoint = org.kivy.android.PythonActivity



[python]

# No usar Python debug
python.debug = 0

# No usar warnings como errores
warn_on_root = 1
