[app]
title = 4DPredictor
package.name = predict4d
package.domain = org.irvan

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,atlas,db

version = 1.0

# Requirement minimal & stabil
requirements = python3,kivy
p4a.branch = develop

# Tampilan
orientation = portrait
fullscreen = 0
icon.filename = logo.png

# Android config (DIKUNCI biar stabil)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.build_tools = 30.0.3

# Arsitektur
android.archs = arm64-v8a, armeabi-v7a

# Permission
android.permissions = INTERNET

# (Opsional tapi aman)
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
