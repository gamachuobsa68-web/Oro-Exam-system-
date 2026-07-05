[app]

title = Oro Exam System
package.name = oroexam
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# ✅ ONLY SAFE REQUIREMENTS (this fixes your build error)
requirements = python3,kivy,pyjnius

orientation = portrait

# =========================
# ANDROID SETTINGS (STABLE)
# =========================
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# =========================
# REMOVE ANY OLD BAD LINES:
# ❌ DO NOT ADD:
# pyjnius==1.7.0
# kivy==2.3.1
# android
# =========================
