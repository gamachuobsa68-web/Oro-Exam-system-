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
# Ensure useful libraries are listed here
requirements = python3,kivy==2.3.0,sqlite3,cython

# (str) Application versioning
version = 1.0.0

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android API to use (Match with GitHub Workflow)
android.api = 33

# (str) Android build-tools version to use
android.build_tools_version = 33.0.2

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid automatic updates
android.skip_update = False

# (bool) Auto-accept Android license (CRITICAL FOR PHONES/ACTIONS)
android.accept_licenses = True

# (str) The Android architecturalis to build for
android.archs = armeabi-v7a, arm64-v8a

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Use fullscreen mode or not
fullscreen = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1