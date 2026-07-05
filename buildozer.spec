[app]

title = Oro Exam System
package.name = oroexam
package.domain = org.gamachu

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,csv,ttf

version = 1.0

requirements = python3,kivy==2.3.0,pillow,sqlite3

orientation = portrait

fullscreen = 0

icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.enable_androidx = True

log_level = 2

warn_on_root = 0
