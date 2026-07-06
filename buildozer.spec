[app]
title = Oro Exam System
package.name = oroexam
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 1.0

requirements = python3,kivy,cython

orientation = portrait

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

# important fix
android.allow_backup = True
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2