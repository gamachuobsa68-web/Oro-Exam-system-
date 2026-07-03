[app]
title = OroExamSystem
package.name = oroexamsystem
package.domain = org.oro

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1