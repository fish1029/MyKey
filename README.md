# 安装与使用方法
## 前置要求
    
    Windows 操作系统
windows11 windows10
    
    AutoHotkey v1.1+（必需）
(从官网下载并安装 AutoHotkey)

    Python 3.10.8 (配置管理)
 
# 获取 MyKey 项目 
直接下载全部文件

# 首次配置
编辑配置文件（推荐使用记事本或 VS Code）
config.txt，修改应用路径为你的实际安装路径
```
示例：将 Firefox 路径改为你的实际路径

修改前：firefox"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"#f

修改后：firefox"D:\Browser\Firefox\firefox.exe"#f

```
# 启动运行
## 方法1：直接运行
双击 mykeys.ahk 文件

## 方法2：使用 script\mykey.py 脚本
### 初次使用将 mykey.py中的
第45行: 
exe_path = r"C:\Program Files\AutoHotkey\v1.1.37.02\AutoHotkeyU64.exe"
替换为实际的路径, 使用v1版本.
### 启动指令
cd script
python mykey.py --start


# 核心快捷键功能

🖥️ 窗口管理

    Win + D - 渐进最小化（逐个隐藏窗口）

    Win + E - 文件管理器循环切换

    Alt + Tab - 按住 Alt 后使用 WASD 精确定位窗口

🚀 应用快速启动/切换

    Win + A - Windows Terminal

    Win + F - Firefox 浏览器

    Win + C - VS Code

    Win + Q - Reader

    ...

🖱️ 鼠标增强

    鼠标侧键前 - 粘贴（Ctrl+V）

    鼠标侧键后 - 复制（Ctrl+C）

    Ctrl + 鼠标侧键 - Home/End 键

    Ctrl + 右键 - 回车键

# 编辑配置
## 使用 script\mykey.py 脚本

### 进入脚本目录
cd script

### 查看当前配置
python mykey.py -l

### 添加/修改应用配置
```
#修改路径和键, 如果之前没有定义过firefox则添加这个定义到配置文件.
python mykey.py -c firefox "C:\new\path\firefox.exe" #f

#仅修改热键
python mykey.py -c vscode #c                

#仅修改路径    
python mykey.py -c chrome -p "C:\Chrome\chrome.exe"

```
### 删除应用配置
```
python mykey.py -c -r firefox
```
### 应用配置更改
```
python mykey.py --change
```
### 选择预设（输入对应数字）
```
python mykey.py -pp 0 4 7

想要更改预设需要修改脚本代码, 这需要自己修改.
```
# 局限
因为每个应用对窗口的管理并不是完全一致的, 所以对于一个没有实际适配的应用, 不能确定默认方式是否有效. 所以这需要你自己去适配. 

## fast_start目录就是适配的文件, 每一个文件对应一个应用程序
最简单的适配方式就是添加一个文件, 写入适配的代码
```
python mykey.py -add NAME PATH
这里的PATH 是适配的文件. 这将会自动在 fast_start目录下创建一个对应的txt文件.

```
## 最简单的适配代码
```
适配代码:
    SwitchOrActivateWordWindows("Chrome_WidgetWin_1", "Code.exe", code_path, Last_code)
    return

这两行都需要开头4个空格进行缩进, 使用autohotkey自带的 WindowSpy.ahk获取ahk_class, ahk_exe, code_path是固定写法, NAME + "_path", Last_code只要不重复即可

```
# 故障排除
...
