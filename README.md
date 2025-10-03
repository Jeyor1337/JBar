# JBar - Python 多功能进度条库

JBar 是一个功能丰富、灵活易用的 Python 进度条库，支持多种显示样式和彩色输出，特别适合复杂任务进度的精确控制。

## 目录
- [功能特性](#功能特性)
- [安装要求](#安装要求)
- [快速开始](#快速开始)
- [使用方法](#使用方法)
- [API 参考](#api-参考)
- [示例演示](#示例演示)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 功能特性

- **多种进度条模式**：支持 6 种不同的显示样式（基础、彩色、方块、箭头、旋转动画、简洁百分比）。
- **彩色输出支持**：基于 `colorama` 库实现跨平台的彩色进度条显示[4](@ref)。
- **直接进度设置**：允许直接传入 0-100 的整数值来更新进度，控制灵活。
- **时间估算功能**：实时显示已用时间和预估剩余时间。
- **多进度条管理**：支持通过 `ProgressManager` 同时管理多个进度条实例。

## 安装要求

JBar 需要以下依赖库：
- **`colorama >= 0.4.4`**（用于彩色输出支持）

使用 pip 安装依赖：

```
pip install colorama
```

将 JBar 的 Python 文件（如 `jbar.py`）保存到您的项目目录中即可导入使用。

## 快速开始

### 基础用法
以下示例展示了如何快速创建并使用一个基础进度条。

```
import time

from jbar import create_progress_bar 

创建一个基础样式的进度条

bar = create_progress_bar(style="basic", desc="处理任务")

bar.start()

模拟任务进展，直接更新进度值

for progress in [0, 25, 50, 75, 100]:

bar.update(progress)

time.sleep(0.5)

bar.finish()
```

### 彩色进度条
使用彩色样式能让进度显示更醒目。

```
bar = create_progress_bar(style="colorful", desc="下载文件")

bar.start()

bar.update(100) # 直接设置为完成

bar.finish()
```

## API 参考

### `ProgressBar` 类
主要参数：
- `total` (int)：总进度值，默认为100。
- `style` (str)：进度条样式，如 `"basic"`, `"colorful"` 等。
- `desc` (str)：进度条前方的描述文字。
- `length` (int)：进度条的长度（字符数）。

主要方法：
- `start()`: 开始显示进度条。
- `update(value)`: 将进度设置到指定的值（0-100）。
- `increment(value=1)`: 以增量方式增加进度。
- `finish()`: 完成进度条并清理显示。

### `create_progress_bar` 函数
快速创建进度条的工厂函数，参数与 `ProgressBar` 构造函数一致。

### `ProgressManager` 类
用于集中管理多个进度条，提供 `add_bar`, `update`, `finish_all` 等方法。

## 示例演示

### 文件处理流程
此示例模拟了一个包含读取、处理、写入三个步骤的文件处理流程。


## 贡献指南
我们欢迎社区贡献！如果您有兴趣为 JBar 贡献力量，请遵循以下步骤：
1. Fork 本项目的仓库。
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 开启一个 Pull Request。

## 许可证
本项目采用 MIT 许可证分发。详情请参阅项目中的 LICENSE 文件。

---

*JBar - 让进度显示直观而优雅！*
