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

# Version mínima compatible
android.minapi = 23

# NDK recomendado
android.ndk = 28c


# NO usar sdk_path personalizado
# Buildozer lo manejará desde ANDROID_HOME


android.accept_sdk_license = True


# Herramientas Android
android.build_tools_version = 35.0.0


# Arquitecturas
archs = arm64-v8a,armeabi-v7a
