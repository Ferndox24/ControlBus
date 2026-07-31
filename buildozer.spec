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

android.api = 35
android.minapi = 24
android.ndk = 28c

android.accept_sdk_license = True

archs = arm64-v8a,armeabi-v7a
