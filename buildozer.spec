[app]

# 应用信息
title = 工时表格生成器
package.name = worktimeexporter
package.domain = org.example.worktime
version = 1.0

# 源码与资源
source.dir = .
source.include_exts = py,kv,json,png,ttf

# Python依赖
requirements = python3,kivy,kivymd,openpyxl

# 屏幕设置
orientation = portrait
fullscreen = 0

# Android 权限
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android 构建配置
android.api = 33
android.minapi = 29
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.enable_legacy_storage = 1

# 日志等级
log_level = 2

# 自动接受 SDK 协议
android.accept_sdk_license = True

# APK 签名配置（GitHub Actions 自动注入）
android.release_keystore = my-release-key.keystore
android.release_keyalias = WorkTimeKey
android.release_keystore_password = @KEYSTORE_PASSWORD@
android.release_keyalias_password = @KEY_PASSWORD@
