[app]

# Nombre de la aplicación
title = ControlBus

# Versión de la aplicación
version = 1.0

# Nombre interno del paquete
package.name = controlbus

# Dominio del paquete
package.domain = org.ferndox

# Carpeta del proyecto
source.dir = .

# Archivos incluidos en la APK
source.include_exts = py,png,jpg,jpeg,kv,json,xlsx,txt

# Dependencias necesarias
requirements = python3,kivy,numpy,opencv,openpyxl,plyer

# Orientación de pantalla
orientation = portrait

# Pantalla completa
fullscreen = 0



[android]

# Arquitectura
android.archs = arm64-v8a

# Android mínimo
android.minapi = 23

# Android objetivo
android.api = 35

# Versión de Build Tools para evitar problemas con la 37
android.build_tools_version = 35.0.0

# Permisos necesarios
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



[buildozer]

# Nivel de información
log_level = 2
