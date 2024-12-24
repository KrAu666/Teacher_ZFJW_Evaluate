# 📷 教师信息处理脚本说明

本脚本主要用于与学校教务系统交互，实现教师信息获取与相关表单的自动化处理，方便对教师数据进行管理与操作。

---

## 🛠️ 功能概述

### 📄 教师信息获取
- 从指定的教务系统网址抓取教师的详细信息，包括教师工号（`jgh_id`）、课程号（`kch_id`）等多类数据。
- 支持多页数据获取，可自动遍历所有页面，确保完整收集教师信息。

### 📝 表单自动填写
- 依据获取的教师信息，自动填充并提交相关表单。
- 表单数据填写精准，涵盖各类评价指标与状态信息的设置。

### 🔍 智能数据处理
- 对获取的数据进行有效筛选与整理，仅提取脚本运行所需的关键信息，提高数据处理效率。
- 具备数据校验功能，能够识别已填写完毕的教师记录并跳过，避免重复操作。

---

## 📚 使用指南

### 1️⃣ 环境配置

**安装依赖：**
```bash
pip install -r requirements.txt
```

### 2️⃣ Cookie 设置

**获取 Cookie：**
 - 参考浏览器抓包教程视频：https://www.bilibili.com/video/BV1G24y1o75g/，获取 `route` 和 `JSESSIONID` 的 Cookie 值。

**填写 Cookie：**
在代码中找到 `cookies` 变量部分，将获取到的 `route` 和 `JSESSIONID` 冒号后面的内容分别填写至对应冒号中间，如下所示：
```python
cookies = {
    'route': '你的 route cookie 值',
    'JSESSIONID': '你的 JSESSIONID cookie 值'
}
```

### 3️⃣ 运行脚本

直接运行脚本文件，它将自动执行教师信息获取与表单填写流程，完成后输出 `所有老师均已填写完毕`。

---

## ⚠ 使用免责声明
本脚本仅供学习和研究用途，请勿将其用于任何商业或非法目的。使用本脚本可能涉及违反相关平台的使用协议或法律法规的风险，用户需自行承担由此产生的后果。开发者不对因使用本脚本而导致的任何直接或间接损失承担责任。 
