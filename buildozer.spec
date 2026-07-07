[app]

title = Oro Exam System
package.name = oroexam
package.domain = org.gamachuobsa

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy

orientation = portrait
git rm -r --cached .buildozer
git commit -m "Remove buildozer cache"
git push
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Leave empty so Buildozer downloads/uses the SDK automatically.
android.sdk_path =
android.ndk_path =

android.permissions = INTERNET

android.allow_backup = True

android.accept_sdk_license = True

# Build tools
android.build_tools_version = 34.0.0

# Logging
log_level = 2
warn_on_root = 1

# Package formats
# android.release_artifact = apk

# Presplash/icon (uncomment if you have them)
# presplash.filename = assets/presplash.png
# icon.filename = assets/icon.png

# Services
# services =

# Python-for-Android
p4a.branch = develop

[buildozer]

bin_dir = ./bin
build_dir = ./.buildozer