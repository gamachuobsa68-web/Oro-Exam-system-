[app]

title = Oro Exam System
package.name = oroexamsystem
package.domain = org.oroexam
source.dir = .
source.include_exts = py,png,jpg,kv,db
requirements = python3,kivy==2.3.0,sqlite3
version = 1.0.0
orientation = portrait
fullscreen = 1

# ==============================================================================
# Android specific configuration
# ==============================================================================

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Path dhuunfaa keenya irra deebinee asittis mirkaneessuu
android.sdk_path = /home/runner/local-android-sdk
android.ndk_path = /home/runner/local-android-ndk/android-ndk

android.accept_licenses = True
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1