[app]

title = ControlBus

package.name = controlbus

package.domain = org.ferndox

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,xlsx,txt

requirements = python3,kivy,openpyxl,plyer

orientation = portrait

fullscreen = 0


[android]

android.archs = arm64-v8a

android.minapi = 23

android.api = 35

android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


[buildozer]

log_level = 2
