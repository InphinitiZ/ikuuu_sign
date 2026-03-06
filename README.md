# ikuuu 自动签到工具

自动完成 ikuuu 每日签到的 Python 脚本。

## 依赖

- Python 3
- requests

```bash
pip install requests
```

## 使用方法

```bash
python3 checkin.py --email <邮箱> --passwd <密码>
```

可选参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--url` | 站点地址 | `https://ikuuu.nl` |

## 示例

```bash
python3 checkin.py --email user@example.com --passwd mypassword
```

自定义站点地址：

```bash
python3 checkin.py --email user@example.com --passwd mypassword --url https://example.com
```

## 定时执行

可配合 cron 实现每日自动签到：

```bash
# 每天早上 8 点执行签到
0 8 * * * cd /path/to/ikuuu_sign && python3 checkin.py --email user@example.com --passwd mypassword
```
