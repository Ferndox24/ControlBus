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

[android]

android.api = 35
android.minapi = 23
android.ndk = 28c
android.accept_sdk_license = True
android.build_tools_version = 35.0.0

archs = arm64-v8a,armeabi-v7a

