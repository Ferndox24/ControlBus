[app]

# (str) Title of your application
title = ControlBus


# (str) Package name
package.name = controlbus


# (str) Package domain
package.domain = org.controlbus


# (str) Source code directory
source.dir = .


# (list) Source files to include
source.include_exts = py,kv,png,jpg,jpeg,json,txt,atlas


# (str) Application version
version = 1.0


# (list) Requirements
requirements = python3,kivy


# (str) Orientation
orientation = portrait



[buildozer]

# (int) Log level
log_level = 2



[android]

# Android API
android.api = 35


# Minimum Android version
android.minapi = 23


# NDK version
android.ndk = 28c


# Architecture
archs = arm64-v8a,armeabi-v7a


# Accept SDK licenses
android.accept_sdk_license = True


# Use build tools
android.build_tools_version = 35.0.0


# Disable old SDK path
# NO poner android.sdk_path aquí


# Permissions (agrega solo si las necesitas)
# android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE



# (str) Python for android branch
p4a.branch = master
