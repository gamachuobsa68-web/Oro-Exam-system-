[app]
title = Oro Exam System
package.name = oroexam
package.domain = org.gamachu

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,db,txt,ttf

version = 1.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

android.api = 34
android.build_tools = 34.0.0
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

log_level = 2
warn_on_root = 0

# IMPORTANT (fix build crashes)
p4a.branch = master