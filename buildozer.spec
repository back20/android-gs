[app]

# 应用信息
title = 工时表格生成器
package.name = worktimeexporter
package.domain = org.example.worktime
version = 1.0

# 项目源代码和资源
source.dir = .
source.include_exts = py,kv,json,png,ttf

# 依赖项
requirements = python3,kivy,kivymd,openpyxl

# 屏幕设置
orientation = portrait
fullscreen = 0

# Android 权限
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android 构建配置
android.api = 33
android.minapi = 29
android.ndk = 21b
android.enable_legacy_storage = 1

# SDK/NDK 路径（GitHub Actions 使用）
//android.sdk_path = /home/runner/android-sdk
//android.ndk_path = /home/runner/android-sdk/ndk/21.4.7075529

# 日志等级（0-2，2为详细）
log_level = 2

# 自动接受 SDK 许可协议
android.accept_sdk_license = True

# 签名配置（通过 GitHub Actions 环境变量替换）
android.release_keystore = my-release-key.keystore
android.release_keyalias = WorkTimeKey
android.release_keystore_password = @KEYSTORE_PASSWORD@
android.release_keyalias_password = @KEY_PASSWORD@
