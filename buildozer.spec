[app]

# (str) Nombre de la aplicación
title = ControlBus

# (str) Nombre del paquete (sin espacios)
package.name = controlbus

# (str) Dominio inverso
package.domain = org.example


# (str) Carpeta donde está main.py
source.dir = .

# (list) Extensiones de archivos que se incluirán
source.include_exts = py,png,jpg,jpeg,kv,json,txt


# (str) Versión de la aplicación
version = 1.0


# (list) Dependencias de Python
requirements = python3,kivy


# (str) Orientación de pantalla
orientation = portrait


# (bool) Permitir pantalla completa
fullscreen = 0



# -------------------------
# ANDROID
# -------------------------

# Versión de Android usada para compilar
android.api = 35

# Versión mínima compatible
android.minapi = 23

# NDK recomendado por python-for-android
android.ndk = 28c


# Arquitecturas soportadas
android.archs = arm64-v8a, armeabi-v7a


# Aceptar licencias automáticamente
android.accept_sdk_license = True


# Evita que busque build-tools 37
android.build_tools_version = 35.0.0


# Permisos (agrega solo los que uses)
# INTERNET si usas conexión
android.permissions = INTERNET



# -------------------------
# BUILD
# -------------------------

# Nombre del archivo generado
android.release_artifact = apk

# Usar gradle moderno
android.gradle_dependencies =


# -------------------------
# KIVY
# -------------------------

[buildozer]

# Log más detallado
log_level = 2

# No usar warnings como errores
warn_on_root = 1
