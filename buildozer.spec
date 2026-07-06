[app]

# (str) Title of your application
title = Oro Exam System

# (str) Package name
package.name = oroexamsystem

# (str) Package domain (needed for android packaging)
package.domain = org.oroexam

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,db

# (list) Application requirements
requirements = python3,kivy==2.3.0,sqlite3

# (str) Application versioning
version = 1.0.0

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Use fullscreen mode or not
fullscreen = 1

# ==============================================================================
# Android specific configuration
# ==============================================================================

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android build-tools version to use (Fixes Build-tools 37 missing)
android.build_tools_version = 37.0.0

# (str) Android NDK directory to use (Fixes NDK r28c path)
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk

# (str) python-for-android directory to use (Fixes FileNotFoundError)
p4a.dir = .buildozer/android/platform/python-for-android

# (bool) Auto-accept Android license
android.accept_licenses = True

# (str) The Android architecturalis to build for
android.archs = armeabi-v7a, arm64-v8a

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1