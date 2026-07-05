[app]

title = Oro Exam System

package.name = oroexam

package.domain = org.gamachuobsa

source.dir = .

source.include_exts = py,png,jpg,jpeg,gif,kv,atlas,json,txt,db,ttf,otf

version = 1.0.0

requirements = python3,kivy==2.3.0,pillow,requests,urllib3,certifi,reportlab

orientation = portrait

fullscreen = 0

icon.filename = assets/icon.png

presplash.filename = assets/presplash.png

log_level = 2

warn_on_root = 0

android.api = 34

android.minapi = 24

android.sdk = 34

android.ndk = 27b

android.accept_sdk_license = True

android.archs = arm64-v8a

android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE

android.allow_backup = True

android.release_artifact = apk

android.enable_androidx = True

p4a.bootstrap = sdl2

android.gradle_dependencies =

android.add_packaging_options =

android.entrypoint = org.kivy.android.PythonActivity

android.numeric_version = 100

android.manifest.intent_filters =

android.copy_libs = 1

android.logcat_filters = python:D *:S

android.wakelock = False

android.skip_update = False

android.accept_sdk_license = True

[buildozer]

log_level = 2

warn_on_root = 0