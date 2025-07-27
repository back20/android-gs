
[app]
title = 工时表格生成器
package.name = WorkTimeExporter
package.domain = org.example.worktime
source.dir = .
source.include_exts = py,kv,json,png,ttf
version = 1.0
requirements = python3,kivy,kivymd,openpyxl
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 29
android.sdk = 33
android.ndk = 25b
android.api = 33
android.enable_legacy_storage = 1
log_level = 2
android.sdk_path = $HOME/android-sdk
android.ndk_path = $HOME/android-sdk/ndk
android.accept_sdk_license = True
