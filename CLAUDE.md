# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

单文件 Python 工具（`checkin.py`），用于 ikuuu 服务的自动每日签到。通过 HTTP POST 登录后，利用同一会话执行签到请求。

## 运行方式

```bash
python3 checkin.py --email <邮箱> --passwd <密码> [--url <站点地址>]
```

默认站点地址为 `https://ikuuu.nl`，可通过 `--url` 参数覆盖。

## 依赖

- Python 3
- `requests` 库（`pip install requests`）

## 架构

单文件脚本，无测试，无构建步骤。使用 `requests.Session` 保持 Cookie，依次调用两个接口：

1. `POST /auth/login` — 登录认证，建立会话
2. `POST /user/checkin` — 执行每日签到

两个接口均返回 JSON，包含 `ret`（1 表示成功）和 `msg` 字段。
