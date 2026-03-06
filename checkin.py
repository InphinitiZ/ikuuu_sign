#!/usr/bin/env python3
import argparse
import requests

DEFAULT_URL = "https://ikuuu.nl"


def login(session, email, passwd, base_url):
    resp = session.post(f"{base_url}/auth/login", data={"email": email, "passwd": passwd})
    data = resp.json()
    print(f"登录: {data.get('msg', '未知响应')}")
    return data.get("ret", 0) == 1


def checkin(session, base_url):
    resp = session.post(f"{base_url}/user/checkin")
    data = resp.json()
    print(f"签到: {data.get('msg', '未知响应')}")
    return data.get("ret", 0) == 1


def main():
    parser = argparse.ArgumentParser(description="ikuuu 自动签到工具")
    parser.add_argument("--email", required=True, help="登录邮箱")
    parser.add_argument("--passwd", required=True, help="登录密码")
    parser.add_argument("--url", default=DEFAULT_URL, help=f"站点地址 (默认: {DEFAULT_URL})")
    args = parser.parse_args()

    base_url = args.url.rstrip("/")
    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": f"{base_url}/auth/login",
        "Origin": base_url,
    }
    session = requests.Session()
    session.headers.update(headers)
    if login(session, args.email, args.passwd, base_url):
        checkin(session, base_url)
    else:
        exit(1)


if __name__ == "__main__":
    main()
