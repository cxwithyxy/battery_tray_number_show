# 电池电量在系统托盘显示

battery_tray_number_show 指在解决 windows 系统版的平板电脑查看电量不方便的问题（需要点一下右下角电池图标，这真的是蠢，你看 Android 、IOS、MacOS，哪个是需要点一下看电量的）

---

## 使用

1. 去[发布页](https://github.com/cxwithyxy/battery_tray_number_show/releases)下载程序，程序已经被打包成7z压缩包
2. 用解压工具（winrar、7z、bandizip等）解压
3. 双击运行 **battery_tray_number_show.exe** 即可

---

## 开发

#### 安装依赖

```bat
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

#### 运行

```bat
python index.py
```

#### 打包

```bat
pyinstaller index.spec
```

