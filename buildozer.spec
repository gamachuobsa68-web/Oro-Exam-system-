[app]

title = Oro Exam System
package.name = oroexam
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

# Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# Remove all broken packages like "android", "kivy==version", etc.
