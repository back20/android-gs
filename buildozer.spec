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

# 权限
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android 构建配置
android.minapi = 29
android.api = 33
android.ndk = 25b
android.enable_legacy_storage = 1

# 路径：请使用绝对路径（在 GitHub Actions 中通过环境变量设置）
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk

# 自动接受许可
android.accept_sdk_license = True

# 日志等级
log_level = 2
