name: Android Build

on:
  workflow_dispatch:  # 手动触发

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: ✅ 检出代码
        uses: actions/checkout@v4

      - name: 🧰 更新 APT 并安装依赖
        run: |
          sudo apt update && sudo apt upgrade -y
          sudo apt install -y zip unzip openjdk-17-jdk python3-pip git

      - name: 🐍 安装 Python 依赖
        run: |
          pip install --upgrade pip
          pip install buildozer cython

      - name: 📦 设置 Android SDK 路径
        env:
          ANDROID_SDK_ROOT: /home/runner/android-sdk
        run: |
          mkdir -p $ANDROID_SDK_ROOT
          echo "ANDROID_SDK_ROOT=$ANDROID_SDK_ROOT" >> $GITHUB_ENV

      - name: 📥 下载并安装 Android cmdline-tools
        run: |
          cd /home/runner/android-sdk
          curl -o cmdline-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
          unzip cmdline-tools.zip -d cmdline-tools-temp
          mkdir -p cmdline-tools/latest
          mv cmdline-tools-temp/cmdline-tools/* cmdline-tools/latest/
          rm -rf cmdline-tools-temp

      - name: 🛠️ 设置环境变量
        run: |
          echo "ANDROID_HOME=$ANDROID_SDK_ROOT" >> $GITHUB_ENV
          echo "ANDROID_NDK_HOME=$ANDROID_SDK_ROOT/ndk/25.2.9519653" >> $GITHUB_ENV
          echo "$ANDROID_SDK_ROOT/cmdline-tools/latest/bin" >> $GITHUB_PATH
          echo "$ANDROID_SDK_ROOT/platform-tools" >> $GITHUB_PATH

      - name: 📦 安装 SDK 必需组件
        run: |
          yes | sdkmanager --licenses
          sdk
