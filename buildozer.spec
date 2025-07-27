[app]
# 应用名称（中文）
title = 工时表格生成器

# 包名
package.name = WorkTimeExporter
package.domain = org.example.worktime

# 源码目录和包含文件类型
source.dir = .
source.include_exts = py,kv,json,png,ttf

# 应用版本
version = 1.0

# 项目依赖
requirements = python3,kivy,kivymd,openpyxl

# 应用方向和显示设置
orientation = portrait
fullscreen = 0

# Android 权限
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android 构建设置
android.minapi = 29
android.api = 33
android.ndk = 25b
android.enable_legacy_storage = 1

# SDK/NDK 安装路径（适用于 GitHub Actions 的环境）
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# 自动接受 SDK 许可协议
android.accept_sdk_license = True

# 日志等级（2 = debug）
log_level = 2

# 设置编码为 UTF-8，以支持中文
android.extra_args = --encoding=UTF-8
