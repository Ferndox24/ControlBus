[app]

# Nombre de la aplicación
title = ControlBus

# Nombre interno del paquete (sin espacios)
package.name = controlbus

# Dominio inverso
package.domain = org.ferndox

# Archivo principal
source.main = main.py

# Extensiones que incluirá
source.include_exts = py,png,jpg,jpeg,kv,json,txt

# Dependencias
requirements = python3,kivy

# Orientación de pantalla
orientation = portrait

# Permitir pantalla completa
fullscreen = 0


[buildozer]

# Advertencias
log_level = 2


[android]

# Arquitecturas compatibles
android.archs = arm64-v8a, armeabi-v7a

# Versión mínima Android
android.minapi = 21

# Versión objetivo
android.api = 35

# Permisos (ajustaremos según use tu app)
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
