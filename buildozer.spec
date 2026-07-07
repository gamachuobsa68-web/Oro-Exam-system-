[app]

title = Oro Exam System

package.name = oroexam

package.domain = org.gamachuobsa


source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,txt


version = 1.0


# IMPORTANT:
# Do not add pyjnius or android here.
requirements = python3,kivy==2.3.0,requests


orientation = portrait


fullscreen = 0


# Android configuration

android.api = 34

android.minapi = 21

android.ndk = 25b

android.build_tools_version = 34.0.0


android.archs = arm64-v8a,armeabi-v7a


android.permissions = INTERNET


# Kivy Android bootstrap

p4a.bootstrap = sdl2


# Accept SDK license

android.accept_sdk_license = True


# Debug information

log_level = 2

warn_on_root = 1
