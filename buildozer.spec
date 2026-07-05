[app]

title = Oro Exam System
package.name = oroexam
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# ✅ FIXED REQUIREMENTS (THIS IS THE KEY)
requirements = python3,kivy==2.2.1

orientation = portrait

# Android config
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 🔥 IMPORTANT STABILITY FIX
p4a.branch = stable
