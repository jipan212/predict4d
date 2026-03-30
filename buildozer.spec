[app]
title = 4DPredictor
package.name = predict4d
package.domain = org.irvan

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,atlas,db

version = 1.0

requirements = python3,kivy
p4a.branch = develop

orientation = portrait
fullscreen = 0
icon.filename = logo.png

android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

android.ndk = 25b
android.sdk = 31

[buildozer]
log_level = 2
android.accept_sdk_license = True
warn_on_root = 1
