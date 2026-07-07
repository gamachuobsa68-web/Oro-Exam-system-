[app]

title = Oro Exam System

package.name = oroexam

package.domain = org.gamachuobsa


source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,txt


version = 1.0


# IMPORTANT:
# Do NOT add pyjnius or android here.
requirements = python3,kivy==2.2.1,requests


orientation = portrait

fullscreen = 0


# Android

android.api = 34

android.minapi = 21

android.ndk = 25b

android.build_tools_version = 34.0.0


android.archs = arm64-v8a,armeabi-v7a


android.permissions = INTERNET


p4a.bootstrap = sdl2


android.accept_sdk_license = True


log_level = 2

warn_on_root = 1
