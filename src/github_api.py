import requests
import base64


GITHUB_TOKEN = ""
GITHUB_API_BASE = ""


def get_readme_content():
    """README.md の現在の内容を取得"""
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(GITHUB_API_BASE, headers=headers)

    if response.status_code == 200:
        data = response.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        sha = data["sha"]
        return content, sha
    else:
        return None, None


def update_readme(new_content, sha):
    """README.md を更新"""
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "message": "Update README.md with new LINE message",
        "content": base64.b64encode(new_content.encode("utf-8")).decode("utf-8"),
        "sha": sha
    }

    response = requests.put(GITHUB_API_BASE, headers=headers, json=data)
    return response.status_code == 200
