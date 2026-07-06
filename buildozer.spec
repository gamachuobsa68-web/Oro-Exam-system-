[app]
title = Oro Exam System
package.name = oroexam
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 1.0

requirements = python3,kivy,cython

orientation = portrait

# ANDROID FIXES
android.api = 33
android.minapi = 21
android.build_tools_version = 34.0.0
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

# stability
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2