[app]

title = ControlBus

package.name = controlbus

package.domain = org.controlbus


source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,json,txt,atlas


version = 1.0


requirements = python3,kivy


orientation = portrait



[buildozer]

log_level = 2



[android]

# Version Android
android.api = 35

android.minapi = 23


# Dejamos la recomendada por python-for-android
android.ndk = 28c


# Licencias
android.accept_sdk_license = True


# Build tools instalada en el workflow
android.build_tools_version = 35.0.0


# IMPORTANTE:
# Ruta del SDK de GitHub Actions
android.sdk_path = /home/runner/android-sdk


# Arquitecturas
archs = arm64-v8a,armeabi-v7a
