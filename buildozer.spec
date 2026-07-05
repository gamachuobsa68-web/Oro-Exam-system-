[app]

# (str) Title of your application
title = Oro Exam System

# (str) Package name
package.name = oroexamsystem

# (str) Package domain (needed for android packaging)
package.domain = org.oroexam

# (str) Application version
version = 1.0.0

# (str) Source code directory (where main.py is located)
source.dir = .

# (list) Source files to include (leave empty to include all)
source.include_exts = py,png,jpg,kv,atlas,json,txt,db,sqlite

# (list) Application requirements
# SQLite3, Kivy, and other essential modules for Oro Exam System
requirements = python3,kivy==2.2.0,pillow,sqlite3,urllib3,certifi,openssl

# (str) App orientation (portrait, landscape or all)
orientation = portrait

# (bool) Use fullscreen mode
fullscreen = 1

# ==========================================
# Android Specific Configurations
# ==========================================

# (int) Android API to use (API 33 is highly recommended for modern Play Store requirements)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version (blank allows Buildozer to select compatible version)
# android.ndk = 25b

# (bool) Use private storage for your app (True or False)
android.private_storage = True

# (bool) Accept SDK license without prompting (CRITICAL FOR GITHUB ACTIONS AND AUTOMATED BUILDS!)
android.accept_sdk_license = True

# (str) Android entry point, default is main.py
android.entrypoint = main.py

# (list) Supported architectures (both are required for modern 64-bit Android devices)
android.archs = armeabi-v7a, arm64-v8a

# (bool) Allow backup of app data
android.allow_backup = True

# (list) Permissions your app requires (uncomment and add if you need internet or storage)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1