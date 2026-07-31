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

android.minapi = 23

android.ndk = 28c

android.sdk_path = /home/runner/android-sdk

android.build_tools_version = 35.0.0

android.accept_sdk_license = True

archs = arm64-v8a,armeabi-v7a
