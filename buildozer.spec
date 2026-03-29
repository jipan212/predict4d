[app]
title = 4DPredictor
package.name = predict4d
package.domain = org.irvan

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,atlas,db

version = 1.0

requirements = python3,kivy,sqlite3

orientation = portrait
fullscreen = 0
icon.filename = logo.png

android.api = 30
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1






