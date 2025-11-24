安装与使用方法
📥 安装步骤
前置要求

    Windows 操作系统

    AutoHotkey v1.1+（必需）

    Python 3.x（可选，用于高级配置管理）

快速安装

    安装 AutoHotkey
    bash

# 从官网下载并安装 AutoHotkey
# 或使用 winget（Windows 11 推荐）
winget install AutoHotkey.AutoHotkey

获取 MyKey 项目
bash

# 方法1：下载 ZIP 压缩包
# 点击 GitHub 页面的 "Code" → "Download ZIP"
# 解压到任意目录，如 D:\MyKey\

# 方法2：Git 克隆
git clone https://github.com/yourusername/MyKey.git
cd MyKey

首次配置
bash

# 编辑配置文件（推荐使用记事本或 VS Code）
# 打开 config.txt，修改应用路径为你的实际安装路径

# 示例：将 Firefox 路径改为你的实际路径
# 修改前：firefox "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" #f
# 修改后：firefox "D:\Browser\Firefox\firefox.exe" #f

启动 MyKey
bash

# 方法1：直接运行
双击 mykeys.ahk 文件

# 方法2：命令行启动
AutoHotkeyU64.exe mykeys.ahk

# 方法3：使用 Python 管理工具（推荐）
cd script
python mykey.py --start

开机自启动（可选）

方法1：快捷方式到启动文件夹
bash

# 按 Win + R，输入 shell:startup
# 将 mykeys.ahk 的快捷方式拖入此文件夹

方法2：使用任务计划程序
bash

# 创建基本任务，触发器设为"计算机启动时"
# 程序选择 AutoHotkey.exe，参数填写 mykeys.ahk 的完整路径

🚀 基础使用方法
核心快捷键功能

🖥️ 窗口管理

    Win + D - 渐进最小化（逐个隐藏窗口）

    Win + E - 文件管理器循环切换

    Alt + Tab - 按住 Alt 后使用 WASD 精确定位窗口

🚀 应用快速启动/切换

    Win + A - Windows Terminal（默认）

    Win + F - Firefox 浏览器（默认）

    Win + C - VS Code（默认）

    Win + Q - Reader（默认）

🖱️ 鼠标增强

    鼠标侧键前 - 粘贴（Ctrl+V）

    鼠标侧键后 - 复制（Ctrl+C）

    Ctrl + 鼠标侧键 - Home/End 键

    Ctrl + 右键 - 回车键

验证安装成功

    检查系统托盘

        启动后，右下角系统托盘应出现 MyKey 图标

        右键图标可查看菜单选项

    测试基本功能
    bash

# 测试 Win + E
# 应该能打开或在文件管理器窗口间切换

# 测试 Win + D  
# 应该逐个最小化窗口，而非直接显示桌面

⚙️ 自定义配置
方法1：手动编辑配置文件

编辑 config.txt 文件：
ini

# 格式：应用名 "应用路径" 热键
# 示例：
firefox "C:\Program Files\Mozilla Firefox\firefox.exe" #f
code "D:\Microsoft VS Code\Code.exe" #c
terminal "C:\Program Files\WindowsTerminal\wt.exe" #a

# 特殊值：
# - #a = Win + A
# - #f = Win + F  
# - - = 无热键（不绑定）

方法2：使用 Python 管理工具（推荐）
bash

# 进入脚本目录
cd script

# 查看当前配置
python mykey.py -l

# 添加/修改应用配置
python mykey.py -c firefox "C:\new\path\firefox.exe" #f
python mykey.py -c vscode #c                    # 仅修改热键
python mykey.py -c chrome -p "C:\Chrome\chrome.exe" # 仅修改路径

# 删除应用配置
python mykey.py -c -r chrome

# 应用配置更改
python mykey.py --change

方法3：快速预设配置
bash

# 查看预设分组
python mykey.py -pp

# 输出示例：
# [#g]   0    android_stdio64
#         1    java_idea64  
#         2    pycharm64
#         3    visual_stdio
# [#q]   4    winword
#         5    telegram
#         6    powerpnt
#         7    reader

# 选择预设（输入对应数字）
python mykey.py -pp 0 4 7
# 这将为 android_stdio64、winword、reader 分配预设热键

🔧 高级功能
添加对新应用的支持

    获取窗口信息
    bash

# 运行 WindowSpy（AutoHotkey 安装目录中）
# 或右键系统托盘 MyKey 图标 → "Window Spy"

创建应用配置文件
bash

# 在 fast_start 目录创建 应用名.txt
# 参考现有模板编写窗口切换逻辑

注册应用到系统
bash

python mykey.py --add 应用名 "应用路径"
python mykey.py -c 应用名 #热键

故障排除

问题：热键无响应
bash

# 检查 AutoHotkey 是否正常运行
# 查看系统托盘是否有 MyKey 图标

# 检查热键冲突
# 尝试修改 config.txt 中的热键组合

问题：应用无法启动
bash

# 验证应用路径是否正确
# 检查路径是否包含空格（需要用引号包围）

# 使用绝对路径
# 相对路径可能因工作目录变化而失效

问题：窗口切换不正常
bash

# 使用 WindowSpy 确认窗口类名和进程名
# 检查 fast_start/应用名.txt 中的匹配逻辑
## 项目名称

**MyKey - Windows 快捷键重定义工具**

## 项目描述

MyKey 是一个基于 AutoHotkey 开发的效率工具，它重新定义了 Windows 系统的原生 Win 快捷键，提供更智能、更高效的窗口管理和应用启动体验。

### 重新设计的 Win 快捷键

使用 MyKey 后，系统原生的 Win 快捷键将被更实用的功能替代：

**🔄 增强的窗口管理**

- `Win + E` - 智能资源管理器：启动或激活文件管理器，在多个资源管理器窗口间循环切换
    
- `Win + D` - 渐进式最小化：逐个最小化窗口（而非直接返回桌面）
    
- `Alt + Tab` - 精准窗口选择：按住 Alt 时使用 WASD 进行上下左右精确定位
    

**🚀 可定制的应用启动器**  
支持为以下组合键绑定应用程序：

text

Win + Q, W, A, S, Z, X, C, B, N, M, T, F, G

每个绑定都支持：

- **快速启动** - 应用未运行时立即启动
    
- **智能切换** - 应用已运行时在多个窗口间循环切换
    
### 技术特色

**🔧 高度可定制**

- 不同应用需要不同的窗口处理逻辑，MyKey 为每个应用提供独立适配
    
- 使用 AutoHotkey 自带的 WindowSpy 工具，轻松获取窗口的 `ahk_exe` 和 `ahk_class`
    
- 模块化设计，便于添加新应用的支持
    

**⚡ 轻量高效**

- 纯脚本实现，零依赖，不占用系统资源
    
- 配置即代码，所有设置透明可控    

### 核心价值

🔸 **告别盲目切换** - 从杂乱的 Alt+Tab 轮播中解脱，精准定位目标窗口  
🔸 **工作流优化** - 快捷键行为符合实际工作习惯，减少操作步骤  
🔸 **个性化定制** - 完全按照你的使用场景定制快捷键行为  
🔸 **持续可扩展** - 随着使用需求变化，轻松调整和新增功能

### 适合谁使用？

- **效率追求者** - 对系统原生快捷键不满，希望更高效的工作流
    
- **多任务工作者** - 频繁在多个应用和窗口间切换的用户
    
- **开发者/技术用户** - 理解技术概念，愿意进行个性化配置
    
- **Windows 高级用户** - 希望完全掌控自己的操作环境
    

---

_"我厌倦了在杂乱的窗口堆叠中寻找目标，于是重新设计了 Windows 的快捷键逻辑。现在，我把这个更高效的工作方式分享给你。"_

---
