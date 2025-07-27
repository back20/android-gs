[app]
title = 工时表格生成器
package.name = WorkTimeExporter
package.domain = org.example.worktime
source.include_exts = py,kv,json,png,ttf
requirements = python3,kivy,kivymd,openpyxl
orientation = portrait
fullscreen = 0

# 权限
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android 构建配置
android.minapi = 29
android.api = 33
android.ndk = 25b
android.enable_legacy_storage = 1

# 使用 GitHub Actions 的路径（已在上方定义）
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

android.accept_sdk_license = True
log_level = 2
