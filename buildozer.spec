[app]
title = Oro Exam System
package.name = oroexam
package.domain = org.gamachuobsa

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,db,ttf

version = 1.0.0

requirements = python3,kivy==2.3.0,pillow,requests,urllib3,certifi,reportlab

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 27b
android.archs = arm64-v8a

android.accept_sdk_license = True
p4a.bootstrap = sdl2

log_level = 2
warn_on_root = 0


[buildozer]
log_level = 2
warn_on_root = 0