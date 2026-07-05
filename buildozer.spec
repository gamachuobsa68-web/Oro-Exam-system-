[app]

title = Oro Exam System
package.name = oroexamsystem
package.domain = org.gamachu

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,ttf,atlas

version = 1.0

requirements = python3,kivy,pillow,sqlite3

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

presplash.filename = assets/presplash.png
icon.filename = assets/icon.png

log_level = 2

warn_on_root = 0

# Do NOT set:
# p4a.branch
# p4a.commit
# p4a.url
# p4a.fork
