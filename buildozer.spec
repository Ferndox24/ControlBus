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

# Archivos incluidos
source.include_exts = py,png,jpg,jpeg,kv,json,xlsx,txt

# Dependencias
requirements = python3,kivy,numpy,opencv,openpyxl,plyer

# Orientación
orientation = portrait

# Pantalla completa
fullscreen = 0



[android]

# Arquitectura Android
android.archs = arm64-v8a

# Android mínimo compatible
android.minapi = 23

# Android objetivo
android.api = 35

# Permisos necesarios
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



[buildozer]

# Nivel de logs
log_level = 2
