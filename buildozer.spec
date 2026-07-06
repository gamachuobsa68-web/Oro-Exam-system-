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

# 🔥 IMPORTANT FIX (DO NOT USE 37)
android.build_tools_version = 34.0.0
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

log_level = 2
warn_on_root = 1