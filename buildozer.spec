[app]
title = Mi Aplicacion
package.name = miapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.arch = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 33
android.accept_sdk_license = True
android.gradle_dependencies = 'androidx.webkit:webkit:1.4.0'
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 0
