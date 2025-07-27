[app]

# 其他设置保持不变
title = 工时表格生成器
package.name = WorkTimeExporter
package.domain = org.example.worktime
source.include_exts = py,kv,json,png,ttf
version = 1.0
requirements = python3,kivy,kivymd,openpyxl
orientation = portrait
fullscreen = 0
source.dir = .

# 签名设置
android.release_keystore = my-release-key.keystore
android.release_keyalias = WorkTimeKey
android.release_keystore_password = @KEYSTORE_PASSWORD@
android.release_keyalias_password = @KEY_PASSWORD@

# 构建设置
android.api = 33
android.ndk = 25b
android.minapi = 29
android.enable_legacy_storage = 1
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True

# 路径：GitHub Actions 中设置 SDK/NDK 路径
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk

log_level = 2
